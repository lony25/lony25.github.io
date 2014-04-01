---
layout: page
title: Archive
---

# Blog Posts

{% for cat in site.categories %}
   * {{ cat }}
      {% for post in site.categories[cat] %}
      * {{ post.date | date_to_string }} &raquo; [ {{ post.title }} ]({{ post.url }})
      {% endfor %}
{% endfor %}