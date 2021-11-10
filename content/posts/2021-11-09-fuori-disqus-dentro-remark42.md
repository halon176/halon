---
title: "Fuori Disqus, Dentro remark42"
date: 2021-11-09T20:56:12+01:00
draft: false
cover:
    image: "../posts/img/remark42.jpg"
    alt: "<alt text>"
    caption: ""
    relative: false # To use relative path for cover image, used in hugo Page-bundles

categories: ["blog"]
---
Se c'è una cosa che ho sempre voluto avere sono i commenti sul blog. Pur andando contro la filosofia minimale, a parer mio è necessario per dare quel minimo di interazione fra chi crea i contenuti e chi legge, oltre a dare la possibilità agli utenti di interagire fra loro e fare domande.

### Staticman

La mia prima scelta è ricaduta su [staticman](https://staticman.net/), la più famosa delle soluzione nell'ambito. In sintesi il software crea un form sul sito e quando l'utente commenta, crea una pull request su una repository git per memorizzarlo, al che il sito viene rigenerato includendo il commento in questione. Questo sistema già astruso di per se mi creava non pochi problemi, in primis il blog è generato in locale da me e poi sincronizzato con rsync sul server, per far funzionare staticman avrei dovuto creare un processo che controlli periodicamente la presenza di nuovi commenti e rigeneri ogni volta ne sia presente uno, cosa che non mi faceva impazzire. Poi c'è il problema della modifica, pare che l'utente non sia in grado di modificare i commenti creati.

Ad ogni modo ho provato ad impostare tutta la macchina ma francamente era una montagna di problemi tecnici sopratutto per l'accesso del server al git, quindi ho dovuto trovare una soluzione alternativa.

### Disqus

Conoscevo disqus dai tempi di wordpress, già in principio non mi piaceva perché traccia molto gli utenti e la sua presenza in un sito minimale era come il dito nell'occhio, era però un compromesso necessario. Ho fatto pure una piccola [guida per integrare Disqus in Hugo](/posts/2021-09-10-impostare-disqus-su-hugo). Fatto pace con la mia coscienza lasciai Disqus ed andai avanti.

Diverso tempo dopo, quasi per caso ho scoperto ho che disqus, in browser senza adblocker (quindi per esempio tutti i browser interni ad app che aprono articoli, es. quello di instagram o facebook), crea un muro di ad incredibile, almeno 6 ad che fanno sembrare il blog una cialtronata incredibile. Articoli come "Dimagrire con la dieta ad aloe puro" e cose di questo tipo, quindi ne andava della reputazione del blog, cosi ho deciso di rimuovere il tutto in attesa di una soluzione.

### Habemus remark42

Quasi per caso mi sono imbattuto in [remark42](https://github.com/umputun/remark42), un progetto abbastanza nuovo ma molto attivo nello sviluppo. Il principio è molto semplice, il form di commenti viene creato direttamente dal server di remark42 (che gira sullo stesso server del blog), i commenti vengono memorizzati in una cartella presso /var/www in maniera criptata ed è molto semplice eseguire backup e ripristino di tutto il baraccone. Fra i grandi vantaggi troviamo la possibilità di commenti anonimi, login tramite varie piattaforme fra cui google/facebook/github ecc, possibilità di impostare gli amministratori che possano con facilità moderare il tutto. Inoltre ci sono alcune piccole chicche come la possibilità di impostare un bot telegram che mandi una notifica ogni volta che ricevi un commento-

Il setup non è banale ma molto ben documentato e qualche madonna di troppo più tardi sono riuscito ad impostare tutta la struttura. Non spiegherò il procedimento nel dettaglio ma nel caso qualcuno avesse bisogno mi contatti.

### Il risultato

Finalmente ho un blog statico con commenti che pur non essendo statici sono comunque custoditi e gestiti localmente, senza bisogno di piattaforme terze che inondino tutto di ad.