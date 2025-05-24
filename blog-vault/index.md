---
title: Post Index
tags:
  - posts
  - index
cssclasses:
  - table-wide
---

```dataviewjs
const groupedArticles = dv.pages('"articles"').groupBy(p => p.published);
// console.log(groupedArticles);
// Key -> false: Unpublished, true: Published

const tableHeaders = ["No.", "Title", "Publish Date", "Category", "Tags"];

let article_count = 1;

for (let group of groupedArticles) {
	let headerName = group.key ? "Published Articles" : "Draft Articles";
	let articleCount = group.rows.length;
    dv.header(3, `${headerName} (${articleCount})`);

	article_count = 1

	dv.table(
	    tableHeaders,
        group.rows
            .sort(k => k.date, 'desc')
            .map(k => [
		            article_count++,
					dv.func.link(k.file.link, k.title),
					dv.func.dateformat(dv.func.date(
						dv.func.replace(
							dv.func.substring(k.date, 0, 19), " ", "T")
						), "MM/dd/yyyy hh:mm a"
					),
					(k.categories || []).map((category) => `• ${category}`), 
					(k.tags || []).map((tag) => `• ${tag}`), 
				])
	);
}
```
