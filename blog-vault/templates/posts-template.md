<%*
const title = await tp.system.prompt("Enter File Title", tp.file.title);
await tp.file.rename(title);
-%>
---
title: "<% title %>"
description:
date: <% tp.date.now('YYYY-MM-DD HH:mm:ss ZZ') %>
categories:
tags:
published: false
media_subpath: /assets/
---

<% tp.file.cursor() %>
