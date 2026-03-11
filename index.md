---
layout: default
title: "Home"
---

Welcome to the **self_reporting** portal. 

### Latest Reports
<ul>
  {% for post in site.posts %}
    <li>
      <a href="{{ post.url }}">{{ post.date | date: "%b %d, %Y" }} - {{ post.title }}</a>
    </li>
  {% endfor %}
</ul>
