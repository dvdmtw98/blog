<%*
const title = await tp.system.prompt("Enter File Title", tp.file.title);
await tp.file.rename(title);
-%>
---
title: "<% title %>"
description:
date: <% tp.file.creation_date('YYYY-MM-DD HH:mm:ss ZZ') %>
categories:
tags:
published: false
img_path: /assets/
---

<% tp.file.cursor() %>
