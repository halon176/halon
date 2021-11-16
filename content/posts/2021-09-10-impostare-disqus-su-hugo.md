---
title: "Impostare Disqus su Hugo"
date: 2021-09-10
draft: false
cover:
    alt: "<alt text>"
    caption: "Impostare Disqus su Hugo"
    relative: false # To use relative path for cover image, used in hugo Page-bundles
params:
    ShowShareButtons: true


categories: ["tutorial","tech"]
---

## Dio perdonami perché ho peccato.

Sognavo un blog interamente statico, veloce, scattante, senza neanche l'ombra di PHP. Invece sono costretto a piegarmi alla dura realtà per non discendere nella follia.

Purtroppo impostare [staticman](https://staticman.net/) si sta rivelando più complesso e rognoso del previsto, con mille incognite e difficoltà, pertanto ho deciso di ripiegare sul vecchio caro [disqus](https://disqus.com/).

Ecco una breve guida del come un'operazione tanto semplice puo diventare ostica.

## Introduzione

La guida in questione è relativa al template [hugo-papermode](https://github.com/adityatelange/hugo-PaperMod), con qualche variazione può essere adattata ad altri template (es. anzi che comments.html il file potrebbe chiamarsi disqus.html).

### Creare il file di commenti

Creare il file di comments nei layouts

> layouts/partials/comments.html

per ora lasciamolo vuoto.

### Creare il nuovo dominio su Disqus

Andiamo su [disqus](https://disqus.com/admin/) e creiamo un nuovo sito seguendo la procedura guidata, l'unica accortezza è di leggere scrivere bene il link della root (nel mio caso blog.halon.cc).

Fatto questo: Installing disqus -> In fondo all'elenco c'è il tasto se la piattaforma non è presente nella lista.

Nella pagina seguente, al punto 1 troveremo il codice html personalizzato con i dati del nostro sito, una cosa del genere:

>    (function() { // DON'T EDIT BELOW THIS LINE
>    var d = document, s = d.createElement('script');
>    s.src = 'https://EXAMPLE.disqus.com/embed.js';
>    s.setAttribute('data-timestamp', +new Date());
>    (d.head || d.body).appendChild(s);


nella prima parte ci sono commentate delle righe per la personalizzazione, se non sapete metterci le mani usatelo integralmente cosi come lo trovate.

Prendete tutto questo malloppo e lo schiaffate in _layouts/partials/comments.html_

### Abilitare i commenti

I commenti vanno abilitati in _config.yaml_ aggiungendo il seguente parametro

>params:
>  comments: true


### Finito

Il gioco è fatto. A differenza di altri template qui non c'è da aggiungere nulla nel header degli articoli. In automatico verrà abilitato su ogni articolo.

### Qualche riferimento utile

[Guida ufficiale ai commenti Disqus in Hugo](https://gohugo.io/content-management/comments/)

[Guida ai commenti in hugo-papermode](https://adityatelange.github.io/hugo-PaperMod/posts/papermod/papermod-features/#comments)

[Articolo di un santo che mi ha fatto capire qualcosa di tutto questo](https://al3xis.xyz/posts/setting-up-disqus-comments-in-hugo/)