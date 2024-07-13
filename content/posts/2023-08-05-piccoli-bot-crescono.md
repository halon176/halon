+++
title = "Piccoli bot crescono: HCryptoPrice raggiunge la versione v1.0.0!"
date = 2023-08-05 21:46:12
images = ["/covers/hcryptoprice-first-stable.webp"]
categories = ["tech"]
+++

È trascorso parecchio tempo dall'attivazione del nostro bot, e tutte le funzionalità di base che avevo in mente durante
la fase di progettazione sono state implementate. Pertanto, ritengo sia giunto il momento di annunciare con orgoglio la
prima versione stabile di HCryptoPrice!

## Caratteristiche

Nel [precedente articolo](/posts/2023-04-21-introduzione-hcryptoprice/) ho già descritto dettagliatamente le principali
caratteristiche del bot, quindi sarò breve:

- Interrogazione delle API di CoinMarketCap e CoinGecko per ottenere il prezzo in tempo reale e le variazioni storiche
  di una criptovaluta, presentate in un formato fico.
- Generazione di grafici relativi a diverse scale temporali per una specifica criptovaluta elencata su CoinGecko.
- Ricezione di informazioni in tempo reale riguardanti il GAS su Ethereum.
- Aggiornamenti sulle ultime notizie legate al mondo delle criptovalute, prese da CoinTelegraph.
- Possibilità di utilizzare una chiave API di CoinMarketCap per accedere alle loro API e un comando dedicato per
  visualizzare informazioni relative alla chiave API utilizzata (ad esempio, chiamate effettuate, chiamate rimanenti,
  ecc.).
- Gestione delle collisioni tra simboli di token: nel caso in cui diversi token condividano lo stesso simbolo (come ACS
  che sta sia per AccessProtocol che per Acryptos), il bot richiederà di specificare il token desiderato attraverso un
  menu.

## Alcuni screenshot

![Grafico Bitcoin](../img/grafico-bitcoin.webp#center)
Grafico del prezzo di Bitcoin in un intervallo temporale di 1 giorno, accessibile con il comando `/c btc`.

![Selezione multipla di token](../img/selezione-multipla-token.webp#center)
Selezione multipla di token con lo stesso simbolo, utilizzando il comando `/p acs` (lo stesso vale per le collisioni nei
grafici).

## Piani per il futuro

L'obiettivo è di implementare il supporto a un database, consentendo il salvataggio delle preferenze degli utenti e la
gestione delle statistiche relative alle interazioni con il bot. Sto considerando l'uso di SQLite, tuttavia al momento
della rigenerazione dell'immagine Docker, il database verrebbe perso. Pertanto, sto valutando l'opzione di utilizzare un
database esterno, molto probabilmente PostgreSQL.

Questa implementazione rappresenterebbe un valore aggiunto rispetto all'utilizzo standard. Tuttavia, ho l'intenzione di
mantenere la funzionalità del bot anche senza l'obbligo di un database, anche se alcune funzioni potrebbero risultarne
influenzate.

Non sono ancora completamente convinto di questa scelta, poiché essa limita la possibilità di aggiungere numerose
caratteristiche interessanti. Ad esempio, al momento non è possibile memorizzare il colore dei grafici, che rimane
invariato finché l'applicazione non viene riavviata.

## Conclusione

Sono estremamente soddisfatto del risultato ottenuto. Il bot si è dimostrato stabile e performante, non ho mai
riscontrato problemi di crash o simili. Ho deciso di disabilitare il logging delle informazioni a causa di un problema
legato alla libreria httpx, che dopo un aggiornamento riempie il log con le chiamate di pooling all'API di Telegram,
rendendo i log praticamente inutilizzabili. Tuttavia, poiché questa dipendenza è legata a python-telegram-bot, le mie
possibilità di intervento sono limitate. Confido che questo problema venga risolto in futuro.

Per il resto, il codice sorgente è disponibile su [GitHub](https://github.com/halon176/h-crypto-price-bot) e il bot è
accessibile su Telegram cercando `@h_crypto_price_bot` o cliccando [qui](https://t.me/h_crypto_price_bot).

Pace e bene! :heart:

