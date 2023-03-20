---
title: "Bye Disqus, Welcome remark42!"
date: 2021-11-09T20:56:12+01:00
draft: false
cover:
    image: "../posts/img/remark42.jpg"
    alt: "<alt text>"
    caption: ""
    relative: false # To use relative path for cover image, used in hugo Page-bundles

translationKey: fromdisqustoremark
categories: ["blog","tech"]
---
There's one thing I've always wanted to have: blog comments. Even if it goes against minimalism, in my opinion it is necessary to give that minimum of interaction between those who create the contents and the reader, as well as give users the possibility to interact with each other and ask questions.

### Staticman

My first choice was [staticman](https://staticman.net/), the most common of the solutions. Briefly, the software creates a form on the site and when the user comments, it creates a pull request on a git repository to store it, whereupon the site is regenerated including the comment just written. This system created many problems for me, first of all the blog is generated locally by me and then synchronized with rsync on the server, to make staticman work I would have to create a process that periodically checks for new comments and regenerates each time. Then there is the problem of editing, it seems that the user is not able to edit the comments created.

Anyway I tried to set up the whole machine but frankly it was a mountain of technical problems especially for the access of the server to the git, so I had to find an alternative solution.

### Disqus

I had known disqus since the days of wordpress, in the premises I did not like it because it tracks users a lot and its presence in a minimal site was like a finger in the eye, but it was a necessary compromise. I have done a [little tutorial to integrate Disqus in Hugo](/posts/2021-09-10-impostare-disqus-su-hugo). After I fixed my heart, I left Disqus and moved on.

Several time later, almost by chance I discovered that disqus, in browsers without adblocker (so for example all browsers inside apps that open articles, e.g. instagram or facebook), creates an incredible ad wall, at least 6 ad that do seem the blog an incredible slob. Articles like "Weight Loss on the Pure Aloe Diet" and stuff like that, so the reputation of the blog depended on it, so I decided to remove it all, continuing to look for a solution.

### Habemus remark42

Almost by accident I came across [remark42](https://github.com/umputun/remark42), a quite young project but very active in development. The principle is very simple, the comment form is created directly by the remark42 server (which runs on the same server as the blog), the comments are stored in /var/www in an encrypted way and it is very easy to backup and restore. Among the great advantages we find the possibility of anonymous comments, login through various platforms including google / facebook / github etc., the possibility of setting administrators who can easily moderate everything. Also there are some little goodies like the ability to set up a telegram bot that sends a notification every time you receive a comment.

The setup is not simple but very well documented and after solving some problems, I was able to set up the whole structure. I will not explain the procedure in detail but if anyone needs to contact me (or leave a comment 😏).

### The result

Finally I have a static blog with comments which, although not static, are still kept and managed locally, without the need for third-party platforms that flood everything with ad.