---
layout: default
title: "Home"
---

Welcome to the **self_reporting** portal. 

### Latest Reports
<ul>
  <div class="report-list">
  {% for post in site.posts %}
    <a href="{{ post.url }}" class="report-card">
      <strong>{{ post.date | date: "%B %d, %Y" }}</strong> — {{ post.title }}
    </a>
  {% endfor %}
</div>

</ul>
