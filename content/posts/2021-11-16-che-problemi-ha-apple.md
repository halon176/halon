---
title: "Che problemi ha Apple?"
date: 2021-11-16T08:50:12+01:00
draft: false
cover:
    image: "../posts/img/applewtf.jpg"
    alt: "<alt text>"
    caption: ""
    relative: false # To use relative path for cover image, used in hugo Page-bundles

translationKey: cheproblemihaapple
categories: ["blog","tech"]
---

"Gli iPhone sono più semplici da usare, non riuscirei mai ad usare un android", frase che ho sentito fino alla nausea ma talmente diffusa da convincermi fosse veramente così. Qualche giorno fa sono diventato un fiero possessore di un iPhone 12 Pro, è stato un momento di giubilo destinato a durare poco, il tempo di cominciare la travagliata migrazione dal mio caro vecchio Samsung S10.

## iOS WTF

Mentre per alcune operazioni è stato tutto semplice ed immediato, per esempio l'importazione di calendari e rubrica da nextcloud ha richiesto pochi secondi con la piena integrazione con le app di sistema, gli altri aspetti sono stati un cancro davvero inaspettato. In particolare.

### Whatsapp

Pur essendo un assiduo utilizzatore di telegram in ogni aspetto delle mie comunicazioni, i quasi 10 anni di cronologia whatsapp rappresentano comunque un prezioso ricordo che ovviamente vorrei conservare. Nella mia testa questo tipo di migrazione dovrebbe essere resa semplice da whatsapp stesso, visto che non appartiene ne a google ne ad apple, ed invece...

Da un po' di tempo, il backup che whatsapp esegue su iOS e su android sono incompatibili fra loro, pare siano anche crittografati in maniera differente, pertanto è impossibile ogni tipo di portabilità (ad onore del vero pare che Samsung abbia sviluppato [una loro app per portare le chat da ios ad android](https://faq.whatsapp.com/general/chats/how-to-migrate-your-whatsapp-data-from-iphone-to-a-samsung-phone/) ma non in senso contrario).

Ho perso diverse ore a navigare fra i siti di dubbia attendibilità e video di indiani ma nessuno soluzione pare funzionare, cosi alla fine mi sono deciso di **pagare** un'app terza che esegua il trasbordo, in particolare 25€ per la licenza di 1 anno di [Dr. Fone](https://drfone.wondershare.it/whatsapp-transfer-backup-and-restore.html), un vero furto ma per questo ringrazio la mamma Apple.

### Le foto

Questa è stata forse l'esperienza piu sconvolgente. L'obiettivo era semplice: prendere le foto dal android, spostarle sul pc e poi caricarle su iOS. Le prime due fasi si fanno in maniera semplice e banale, android viene visto come periferica di archiviazione da windows, entri, copi e incolli. Ma poi...

Naturalmente, iPhone si collega a PC windows solo tramite iTunes, da li, sempre seguendo i tutorial di indiani ma anche le chiare indicazioni dell'interfaccia vai ad indicare la cartella sorgente con la foto, le quali verranno sincronizzate sul telefono.

![](../img/itunes.jpg#center)

Semplice no? Peccato che non funzioni, letteralmente non fa nulla e raccogliendo informazioni in giro pare non abbia mai funzionato, quanto meno su windows.

A questo punto ci sono 2 modi di procedere: il primo è di pagare altri 25 euro di programma terzo che faccia il tutto, il secondo è di utilizzare app terze sul telefono. Ho scelto di procedere con il secondo.

Esiste un'app su iOS che in teoria aiuto ad organizzare meglio i documenti e le foto, si chiama [Documents by Readdle](https://apps.apple.com/it/app/documents-di-readdle/id364901807). Una volta installata, su iTunes, in sezione app appare la suddetta e permette di caricare dal pc ogni genere di documento, quindi anche le foto. Una volta caricate, basta spostarle dalla cartella documents in "foto" ed il gioco è fatto.

#### problema risolto, no?

Neanche per idea. Le foto a questo punto sono si nella galleria MA non hai modo di gestirle, se tu volessi eliminare qualche vecchia foto, l'unico modo per farlo è di ricollegare il telefono ad iTunes e DESINCRONIZZARE la foto in questione. Assurdo. Mi sono scervellato per molto tempo della possibile ragione di tale misura ma continua a sembrare una cagata atomica.

L'unica soluzione che pare salvare capra e cavoli è quella di usare iCloud, soluzione che mi crea non pochi problemi in primis perché avendo 25GB di foto dovrei pagare perennemente lo spazio aggiuntivo, in secondo luogo avere le mie foto che vengono automaticamente sincronizzate e con l'eventualità che qualcuno ci acceda non è nulla.

## in conclusione

iOS sembra essere un sistema perfettamente semplice e funzionante per chiunque non faccia alcuna operazione fuori dal seminato e sopratutto chiunque abbia sempre e solo usato i prodotti apple, non è contemplato nulla che ti faccia agire all'infuori dal loro ecosistema. Capisco bene che portare le foto dal PC al telefono sia un'operazione non da tutto però non mi sembra nemmeno una caratteristica trascurabile. In generale tutto il porting da android è mal supportato mentre secondo me sarebbe proprio di incentivo facilitare tale compito.