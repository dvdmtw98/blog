---
cssclasses:
  - numbered-rows
  - wide-dataview
---
### Draft Posts

```dataview
TABLE WITHOUT ID
	"" AS "No.",
	link(file.link, title) AS "Title",
	dateformat(
		date(replace(substring(date, 0, 19), " ", "T")), 
		"MM/dd/yyyy hh:mm a"
	) AS "Published Date",
	categories AS Categories,
	tags AS Tags
FROM "articles"
WHERE published = false
SORT date DESC
```

### Published Posts

```dataview
TABLE WITHOUT ID
	"" AS "No.",
	link(file.link, title) AS "Title",
	dateformat(
		date(replace(substring(date, 0, 19), " ", "T")), 
		"MM/dd/yyyy hh:mm a"
	) AS "Published Date",
	categories AS Categories,
	tags AS Tags
FROM "articles"
WHERE published = true
SORT date DESC
```