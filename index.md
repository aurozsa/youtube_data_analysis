---
layout: default
title: "Home"
---
Welcome to my blog! Check out the latest posts below:

{% for post in site.posts %}
- [{{ post.title }}]({{ post.url }})
{% endfor %}
