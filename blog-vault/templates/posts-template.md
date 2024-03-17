<%*
const title = await tp.system
	.prompt("Enter File Title", tp.file.title.replaceAll("-", " "));
const fileName = title.replace(/\s/g, "-").toLowerCase();
await tp.file.rename(fileName);

const filterWords = ["and"];

const words = title.split(" ");
const titleCaseTitle = words
    .map(word => {
        if (filterWords.includes(word.toLowerCase())) {
            return word;
        } else {
            return word.charAt(0).toUpperCase() + word.slice(1).toLowerCase();
        }
    }) 
    .join(" ");
-%>
---
title: <% tp.file.title %>
description:
date: <% tp.file.creation_date('YYYY-MM-DD HH:mm:ss ZZ') %>
categories:
tags:
published: false
img_path: /assets/
---

<% tp.file.cursor() %>
