---
title: Post Index
cssclasses:
  - numbered-rows
  - wide-dataview
---

```dataviewjs
const groupedArticles = dv.pages('"articles"').groupBy(p => p.published);
// console.log(groupedArticles);

const tableHeaders = ["No.", "Title", "Publish Date", "Category", "Tags"];

for (let group of groupedArticles) {
	let headerName = group.key ? "Published Articles" : "Draft Articles";
	let articleCount = group.rows.length;
    dv.header(3, `${headerName} (${articleCount})`);

	dv.table(
	    tableHeaders,
        group.rows
            .sort(k => k.date, 'desc')
            .map(k => [
		            "",
					dv.func.link(k.file.link, k.title),
					dv.func.dateformat(dv.func.date(
						dv.func.replace(
							dv.func.substring(k.date, 0, 19), " ", "T")
						), "MM/dd/yyyy hh:mm a"
					),
					k.categories.map((category) => `&thinsp;• ${category}`), 
					k.tags.map((tag) => `&thinsp;• ${tag}`), 
				]
			)
	);
}
```
