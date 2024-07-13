+++
title = "Configurazione di GoAccess con statistiche Nginx in tempo reale"
date = 2023-08-27 16:46:12
images = ["/covers/goaccess.webp"]
categories = ["tech"]
+++

Qualche giorno fa mi è arrivata la mail di Google che mi avvisava di dover migrare le mie proprità Universal Analytics a Google Analytics 4.
Il problema di base è banale, GA4 non sembra essere supportato dal mio tema usato per il blog e poi però sono subentrate tutte le altre considerazioni.

## Questione etica

Google Analytics è un servizio che permette di tracciare gli utenti che visitano un sito web, raccogliendo informazioni come il browser utilizzato, il sistema operativo, la posizione geografica, ecc. Questi dati mi sono certo utili per avece un'idea di chi visita il mio sito, ma allo stesso tempo mi rendo conto che non è etico raccogliere per Google questi dati senza il consenso degli utenti (e si, fin'ora non ho messo il banner, potete chiamare i caraabinieri). Per questo motivo ho deciso di rimuovere Google Analytics dal mio sito.

## GoAccess

Volendo comunque mantenere un'idea di quanta gente legga il blog e tutti i siti collegati, ho valutato alcune opzioni e la mia scelta è caduta su [GoAccess](https://goaccess.io/), un software open source che permette di analizzare i log di un server web e di generare statistiche in tempo reale. Nel mio caso il log in questione è quello di nginx.

Questo mi permette di analizzare e conservare i dati dell'accesso da un log che viene già generato per conto proprio, e senza dover inoltrare i dati a terzi.

## Il funzionamento

In particolare del nostro uso, GoAccess avviandosi, crea un servizio che genera una pagina html che si aggiorna in tempo reale grazie ai dati in arrivo via websocket che viene sempre sollevato da GoAccess. La guida si focalizza sulla configurazione di nginx e sulla configurazione di goaccess come servizio in systemd.

## Configurazione

Io utilizzo Debian 11 e ho installato la versione del software dalle repository, per altre opzioni vi rimando [alla guida ufficiale](https://goaccess.io/download#distro).

### Installazione

```shell
sudo apt install goaccess
```

Per prima cosa andiamo a modificare le configurazione goaccess, che si trovano in `/etc/goaccess/goaccess.conf`, andiamo a decommentare le righe relative
al formato di date, di ora e del formato dei log, la mia configurazione è relativa al mio setup quindi riguardatela, l'importante è che ci siano almeno
queste righe:

```shell
time-format %H:%M:%S
date-format %d/%b/%Y
log-format %h %^[%d:%t %^] "%r" %s %b "%R" "%u"
```

### Configurazione nginx

Ora vado subito al sodo, a noi ci interessa una pagina html che aggiorna nel tempo reale le statistiche lette nel `access.log`,
prima andiamo ad aggiungere la gestione di upgrade del websocket in nginx, quindi andiamo a modificare `/etc/nginx/nginx.conf` e aggiungiamo:

```shell
http {
    map $http_upgrade $connection_upgrade {
        default upgrade;
        ''      close;
    }
}
```
andiamo a creare la directory che conterrà i file html generati da goaccess:

```shell
sudo mkdir -p /var/www/html/goaccess
```

quindi andiamo a modificare `/etc/nginx/sites-available/mydomain`, io lo configuro su su mydomain/analytic e il websocket su mydomain/ws, quindi aggiungo:

```shell
upstream gwsocket {
     server 127.0.0.1:7890;
}

server {
    location /analytic/ {
        alias /var/www/html/goaccess;
        try_files $uri/report.html =404;

        location ~ ^/analytic/(.*)/(.*)\.html$ {
            alias /var/www/html/goaccess/goaccess_files/$1/$2.html;
        }
    }
    location /ws {
         proxy_http_version 1.1;
         proxy_set_header Upgrade $http_upgrade;
         proxy_set_header Connection $connection_upgrade;
         proxy_pass http://gwsocket;
         proxy_buffering off;
         proxy_read_timeout 7d;
     }
}
```
parte web fatta, ora testiamo le nostre configurazioni:

```shell
 sudo nginx -t
```

se va tutto bene riavviamo nginx:

```shell
sudo systemctl restart nginx
```

### Configurazione goaccess come servizio

Ora andiamo a creare il servizio che andrà a leggere il log e a generare i file html, creiamo il file `/etc/systemd/system/goaccess.service`:

```shell
[Unit]
Description=GoAccess

[Service]
Type=simple
ExecStart=/usr/bin/goaccess -f /var/log/nginx/access.log \
          --real-time-html --ws-url=wss://mysite:443/ws \
          -o /var/www/html/goaccess/report.html --port=7890 \
          --config-file=/etc/goaccess/goaccess.conf 
ExecStop=/bin/kill ${MAINPID}
PrivateTmp=false
RestartSec=1800
User=root
Group=root
Restart=always

[Install]
WantedBy=multi-user.target
```
> **_NOTE:_**  alcune guida includono l'opzione `-g` che mi da errore e che non trovo nemmeno nella guida ufficiale e
> `--origin` che restringe l'accesso al websocket, ma quando provo a impostarla non mi funziona, quindi l'ho esclusa.



mi raccomando di sostituire `mysite` con il vostro dominio, ora abilitiamo il servizio:

ora ricaricchiamo le configurazioni dei servizi
    
```shell
sudo systemctl daemon-reload
```

e avviamo il servizio:

```shell
sudo systemctl start goaccess
```

se tutto va a buon fine, abilitiamo il servizio in modo che possa partire all'avvio:

```shell
sudo systemctl enable goaccess
```

per sicurezza controlliamo che il servizio sia attivo:

```shell
sudo systemctl status goaccess
```

## Finito

tutto fatto, ora andando su `mysite/analytic/` dovreste vedere la pagina di goaccess che si aggiorna in tempo reale.
Come riferimento do la pagina della mia configurazione [https://halon.cc/analytic/](https://halon.cc/analytic/).

## Conclusioni

Posso dirmi per ora soddisfatto, rimangono ancora alcuni problemi da risolvece:

- `access.log` di nginx è impostato su una rotazione fissa, si può aumentare la rotazione ad un mese ma rimane comunque limitante, tenere un log troppo lungo può dare dei problemi, vorrei trovare un modo per mantenere i dati storici senza compromettere il sistema, in teoria dovrei salvare una qualche sintesi (che in effetti il software genera) ma sto ancora valutando come fare.

- Non è il massimo avere questa pagina esposta al web, dovrei lavorare su qualche sistema di sicurezza che non implichi l'uso di un login, magari un sistema di token.

Per il resto, non se avete dei problemi non esitate di chiedere sotto, vedo di integrare o correggere la guida.

saluti!
