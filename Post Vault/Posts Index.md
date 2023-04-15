---
cssClasses: wide-page
---

### Draft Posts

```dataview
TABLE WITHOUT ID
	link(file.link, title) AS "Title",
	dateformat(
		date(replace(substring(date, 0, 19), " ", "T")), 
		"MM/dd/yyyy hh:mm a"
	) AS "Created Time",
	categories AS Categories,
	tags AS Tags
FROM "articles"
WHERE published = false
SORT date DESC
```

### Published Posts

```dataview
TABLE WITHOUT ID
	link(file.link, title) AS "Title",
	dateformat(
		date(replace(substring(date, 0, 19), " ", "T")), 
		"MM/dd/yyyy hh:mm a"
	) AS "Published Time",
	categories AS Categories,
	tags AS Tags
FROM "articles"
WHERE published = true
SORT date DESC
```