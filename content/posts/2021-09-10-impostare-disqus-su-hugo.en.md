---
title: "Setting Up Disqus on Hugo"
date: 2021-09-10
draft: false
cover:
    alt: "<alt text>"
    caption: "Setting Up Disqus on Hugo"
    relative: false
params:
    ShowShareButtons: true
categories: ["tutorial","tech"]
translationKey: "2021-09-10-disqus-hugo"
---

## God forgive me, for I have sinned.

I dreamed of a fully static blog — fast, snappy, without even a shadow of PHP. Instead, I'm forced to bow to harsh reality to avoid descending into madness.

Unfortunately, setting up [staticman](https://staticman.net/) is proving more complex and troublesome than expected, with a thousand unknowns and difficulties, so I've decided to fall back on the good old [Disqus](https://disqus.com/).

Here's a short guide on how such a simple operation can become a pain.

## Introduction

This guide is specific to the [hugo-papermode](https://github.com/adityatelange/hugo-PaperMod) template. With a few tweaks, it can be adapted to other templates (e.g., instead of comments.html, the file might be called disqus.html).

### Create the comments file

Create the comments file in your layouts:

> layouts/partials/comments.html

Leave it empty for now.

### Create a new domain on Disqus

Go to [Disqus](https://disqus.com/admin/) and create a new site following the guided procedure. The only thing to watch for is to carefully type the root link (in my case blog.halon.cc).

Once done: Installing Disqus -> At the bottom of the list there's a button if your platform isn't present in the list.

On the next page, at step 1, you'll find the custom HTML code with your site's data, something like:

>    (function() { // DON'T EDIT BELOW THIS LINE
>    var d = document, s = d.createElement('script');
>    s.src = 'https://EXAMPLE.disqus.com/embed.js';
>    s.setAttribute('data-timestamp', +new Date());
>    (d.head || d.body).appendChild(s);

In the first part, there are some commented lines for customization. If you don't know how to work with them, use it as-is.

Take all this stuff and dump it into _layouts/partials/comments.html_

### Enable comments

Comments need to be enabled in _config.yaml_ by adding the following parameter:

>params:
>  comments: true

### Done

That's it. Unlike other templates, here there's nothing to add in the article headers. It'll be automatically enabled on every article.

### Some useful references

[Official Disqus comments guide for Hugo](https://gohugo.io/content-management/comments/)

[Comments guide for hugo-papermode](https://adityatelange.github.io/hugo-PaperMod/posts/papermod/papermod-features/#comments)

[Article by a saint who helped me understand some of this](https://al3xis.xyz/posts/setting-up-disqus-comments-in-hugo/)
