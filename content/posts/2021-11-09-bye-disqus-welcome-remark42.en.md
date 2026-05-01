+++
title = "Bye Disqus, Welcome remark42!"
date = 2021-11-09 20:56:12
images = ["/covers/remark42.jpg"]
categories = ["blog","tech"]
translationKey = "2021-11-09-remark42"
+++

If there's one thing I've always wanted, it's comments on my blog. Even if it goes against the minimalist philosophy, in my opinion it's necessary to provide that minimum of interaction between content creators and readers, as well as giving users the ability to interact with each other and ask questions.

### Staticman

My first choice was [staticman](https://staticman.net/), the most well-known solution in this space. In short, the software creates a form on the site and when a user comments, it opens a pull request on a git repository to store it, after which the site is regenerated including the comment. This system, already convoluted on its own, caused me quite a few issues: first of all, the blog is generated locally by me and then synced to the server via rsync. To make staticman work, I would have had to create a process that periodically checks for new comments and regenerates the site each time one appears — something I wasn't thrilled about. Then there's the editing problem: apparently users can't modify the comments they've created.

Anyway, I tried to set the whole thing up, but frankly it was a mountain of technical problems, especially around server access to git, so I had to find an alternative solution.

### Disqus

I knew Disqus from my WordPress days. In principle, I didn't like it because it heavily tracks users and its presence on a minimal site stuck out like a sore thumb, but it was a necessary compromise. I even wrote a [short guide on integrating Disqus into Hugo](/posts/2021-09-10-impostare-disqus-su-hugo). Having made peace with my conscience, I left Disqus in place and moved on.

Some time later, almost by chance, I discovered that Disqus — in browsers without an adblocker (so, for example, all in-app browsers that open articles, like Instagram or Facebook's) — creates an unbelievable wall of ads, at least 6 of them, making the blog look incredibly trashy. Articles like "Lose weight with the pure aloe diet" and that kind of thing. The blog's reputation was at stake, so I decided to remove it entirely and wait for a solution.

### Habemus remark42

Almost by chance I stumbled upon [remark42](https://github.com/umputun/remark42), a fairly new project but very actively developed. The principle is very simple: the comment form is created directly by the remark42 server (which runs on the same server as the blog), comments are stored in a folder under /var/www in encrypted form, and backing up and restoring everything is very straightforward. Among the major advantages: anonymous comments, login via various platforms including Google/Facebook/GitHub etc., and the ability to set up administrators who can easily moderate everything. There are also some nice touches like the ability to set up a Telegram bot that sends a notification every time you receive a comment.

The setup isn't trivial but it's very well documented, and after a fair bit of swearing I managed to get the whole thing working. I won't explain the procedure in detail, but if anyone needs help, feel free to contact me.

### The result

Finally, I have a static blog with comments that, although not static themselves, are still stored and managed locally, without the need for third-party platforms flooding everything with ads.
