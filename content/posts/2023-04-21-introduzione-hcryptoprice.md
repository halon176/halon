+++
title = "Ho generato una creatura e si chiama HCryptoPrice"
date = 2023-04-21 12:56:12
images = ["/covers/telegram-bot-creation-cover.jpg"]
categories = ["tech"]
+++

Ho partorito una piccola creatura, un bot di telegram in grado fare richiesta alle API di GoinGecko e di restituisce in un messaggio i dati relativi al prezzo, capitalizzazione, ATH, ATL e altre sigle.

## Introduzione

Frequento i gruppi Telegram dove si parla di criptovalute da anni, ma più che un fanatismo è un hobby. Ogni gruppo aveva un bot diverso e spesso non mi piacevano affatto, tutti con caratteristiche simili ma con qualche dettaglio che non mi soddisfaceva. Quindi, non appena ho avuto la capacità di farlo, ho scritto il mio bot.

Il bot è a open sources e [potete trovare il suo codice completo su GitHub sotto la licenza MIT](https://github.com/halon176/h-crypto-price-bot).

Chiaramente c'è anche il bot in funzione, [che potete raggiungere da qui](https://t.me/h_crypto_price_bot).

## Caratteristiche

La caratteristica principale del bot al momento è quella di prendere informazioni riguardo al prezzo attuale e quello storico in una finestra massima di 1 anno del token richiesto tramite comando `/p`. Siccome la chiamata avviene per simbolo, ci si scontra facilmente con token dove essi coincidono, per esempio ACS sta sia per Access Protocol sia per acryptos; in quel caso il bot genera un menù con i pulsanti dove effettuare la scelta del token desiderato. Questo è un esempio di risposta alla richiesta `/p btc`:

![](../img/bot-price-response.jpg#center)

Analizziamo la risposta per parti:

1) ranking generale, nome e simbolo del token, dove il nome ed il simbolo sono dei link rispettivamente al sito del progetto e al loro account Twitter (i bravi ragazzi di CoinGecko in alcuni link ai siti mettono anche dei referral che il bot elimina con una funzione);

2) variazione storica rispetto al prezzo attuale;

3) dati generali dell'asset seguiti dai valori di all-time high e all-time low con i relativi riferimenti temporali;


Solo questa funzione ha richiesto giorni di lavoro per una sostanziale inconsistenza dell'API e la gestione di una miriade di eccezioni, oltre ad un complesso sistema di specchi e leve per tenere allineate le varie colonne e rendere il tutto presentabile.


Per ora le altre funzioni sono poche, abbiamo:

- `/dom` che restituisce la top 10 dominance con le relative percentuali di mercato
- `/news` che restituisce le top picks news da Cointelegraph


## Roadmap

L'idea è di aggiungere altre funzioni, anche non strettamente legate all'API perché essa è abbastanza limitante. Vorrei almeno:

- una funzione tipo `/contract` che dia la possibilità, selezionando la chain di riferimento, di restituire l'indirizzo del contratto, in modo da poterlo inserire in vari wallet o swap;
- utilizzare meglio la funzione news, tipo rendendo disponibile la selezione della lingua (Cointelegraph ne ha diverse) o di programmare il messaggio con le news in un particolare momento della giornata;
- chiamate ad altre API pubbliche, anche se devo ancora indagare su quali.

## Feedback super graditi

Chiaramente è tutto in fase molto sperimentale e ancora qualche token da problemi, problemi che cerco di gestire di volta in volta creando delle eccezioni nella lettura dei dati, perciò chiedo a chi è del settore di usarlo, magari aggiungerlo a qualche gruppo (non richiede permessi amministratore), e di farmi sapere qualsiasi problema abbia o qualsiasi idea vi venga in mente per migliorarlo.

cià!