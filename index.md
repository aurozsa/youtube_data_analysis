---
layout: default
title: "Home"
---

<h1>Recent Analysis Posts</h1>
<ul>
  {%- for post in paginator.posts -%}
  <li>
    <strong>{{ post.date | date: '%B %d, %Y' }}</strong>: 
    <a href="{{ post.url }}">{{ post.title }}</a>
    <p>
      {%- if post.description -%}
      {{ post.description }}
      {%- else -%}
      {{ post.excerpt | strip_html }}
      {%- endif -%}
    </p>
  </li>
  {%- endfor -%}
</ul>

<nav>
  <div>
    {%- if paginator.previous_page -%}
    <a href="{{ paginator.previous_page_path }}">Newer Posts</a>
    {%- endif -%}
  </div>
  <div>
    {%- if paginator.next_page -%}
    <a href="{{ paginator.next_page_path }}">Older Posts</a>
    {%- endif -%}
  </div>
</nav>
