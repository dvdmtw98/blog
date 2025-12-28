---
title: "OSINT4Fun: Advent of OSINT 2025 (Day 5 - Day 8)"
description: Get started with OSINT in 24 Days - Learn the basics by solving beginner-friendly challenge every day leading up to Christmas.
date: 2025-12-24 21:45:01 +0530
categories:
  - Security
  - OSINT
tags:
  - security
  - osint
  - walkthrough
  - geolocation
  - investigation
published: false
media_subpath: /assets/
---

![[osint4fun-aoo-day-5-8-banner.png|640]]
_Image Background by [vector_corp](https://www.freepik.com/free-vector/yellow-grunge-brush-ink-background_37589666.htm) on Freepik_

### Day 5

[Advent of OSINT 2025 - Day 5 \| OSINT4Fun](https://www.osint4fun.eu/advent2025/20251205173000)

**Q) In France, some municipal decrees (« arrêté » in French) are rather unusual, such as those forbidding the character encountered on [3rd December](https://www.osint4fun.eu/advent2025/20251203153000) from disrupting Santa’s work. In December 2024, such decrees can be found on the WordPress sites of two communes. What are the surnames of these two mayors?**

We need to locate the laws that was passed by municipal councils in France that forbids “Grinch” from disrupting Christmas. We are also told that in December 2024 the decrees were uploaded to the respective cities official (WordPress) website.

Content on government websites are generally uploaded as documents (Word/PDF). WordPress stores documents in a folder called “wp-content.” If the decree was uploaded as a PDF then the URL to the document would contain the word “wp-content.”  

Using this information I crafted the following Google Dork:

```
inurl:wp-content "arrêté" "grinch"
```

The `inurl:` operator makes Google look for the provided word in the URL. The `".."` (double quote) operator makes Google look for the exact word. So, this query will only return results that contain “wp-content” in the URL and “arrêté” and “grinch” in the body.

![[aoo-2025-2-1.png|600]]

The first 3 results are for websites dedicated to French cities. The 3rd result however has an upload date of December 2022. The first 2 results fall in the time frame mentioned in the question. 

![[aoo-2025-2-5.png|500]]

![[aoo-2025-2-2.png|520]]

![[aoo-2025-2-3.png|550]]

![[aoo-2025-2-4.png|500]]

Both the PDF had a decree that mentioned Grinch but since I don’t read French I was not sure if it was the correct law.

[Special Christmas Order 2024 \| Ville Villers-Semeuse](https://www.villers-semeuse.fr/wp-content/uploads/2024/12/arrete-special-pere-noel-24-12-2024.pdf)

![[aoo-2025-2-6.png|640]]

![[aoo-2025-2-8.png|500]]

[Special Christmas Order 2024 \| Ville Andrezieux-Boutheon](https://www.andrezieux-boutheon.com/wp-content/uploads/2024/12/Arrete-Pere-Noel-2024.pdf)

![[aoo-2025-2-7.png|640]]

![[aoo-2025-2-9.png|500]]

After looking at the translation I was confident that this was the correct decrees. Both the document contained the respective mayors name at the end. 

![[aoo-2025-2-10.png|380]]

![[aoo-2025-2-11.png|550]]

> Dupuy Driol

> [!NOTE]
> The content in the PDF is not in text format so you will not be able to select the text and translate it directly. I had to use Adobe’s document conversion service to first convert the PDF into an editable Word document.
> 
> [Convert PDF to Word \| Adobe Acrobat](https://www.adobe.com/in/acrobat/online/pdf-to-word.html)

### Day 6

### Day 7

### Day 8
