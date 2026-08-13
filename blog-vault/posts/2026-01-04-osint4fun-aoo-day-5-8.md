---
title: "OSINT4Fun: Advent of OSINT 2025 (Day 5 - Day 8)"
description: Get started with OSINT in 24 Days - Learn the basics by solving beginner-friendly challenge every day leading up to Christmas.
date: 2026-01-04 18:50:01 +0530
categories:
  - Security
  - OSINT
tags:
  - security
  - osint
  - walkthrough
  - geolocation
  - investigation
published: true
media_subpath: /assets/
---

![[osint4fun-aoo-day-5-8-banner.png|640]]
_Image Background by [vector_corp](https://www.freepik.com/free-vector/yellow-grunge-brush-ink-background_37589666.htm) on Freepik_

### Day 5

[Advent of OSINT 2025 - Day 5 \| OSINT4Fun](https://www.osint4fun.eu/advent2025/20251205173000)

**Q) In France, some municipal decrees (« arrêté » in French) are rather unusual, such as those forbidding the character encountered on [3rd December](https://www.osint4fun.eu/advent2025/20251203153000) from disrupting Santa’s work. In December 2024, such decrees can be found on the WordPress sites of two communes. What are the surnames of these two mayors?**

We need to locate the laws that were passed by municipal councils in France that forbid “Grinch” from disrupting Christmas. We are told that in December 2024 the decrees were uploaded to the city's official (WordPress) website.

Government orders are generally uploaded to government websites as PDF documents. WordPress stores documents in a folder called “wp-content.” If the decree was uploaded as a PDF, then the URL to the file would contain the word “wp-content.”

Using this assumption, I crafted the following Google Dork:

```
inurl:wp-content "arrêté" "grinch"
```

The `inurl:` operator makes Google look for the word in the URL. The `".."` (double quote) operator makes Google look for the exact word. So, this query will only return results that contain “wp-content” in the URL and “arrêté” and “grinch” in the body.

![[aoo-2025-2-1.png|600]]
_Grinch Decree Google Search_

The first 3 results are official websites of French cities. The 3rd result, however, has an upload date of December 2022 and can be eliminated. The first 2 results fall in the time frame mentioned in the question.

![[aoo-2025-2-5.png|500]]
_Ville translation_

![[aoo-2025-2-2.png|520]]
_City 1 Wikipedia Article_

![[aoo-2025-2-3.png|550]]
_City 2 Wikipedia Article_

![[aoo-2025-2-4.png|500]]
_Decree Title Translation_

Both PDFs had a decree that mentioned Grinch, but since I don’t read French, I was not sure what this law was talking about. I used Google Translate to translate the text into English.

> [!NOTE]
> The content in the PDF is not in text format, so you will not be able to select the text and translate it directly. I had to use Adobe’s document conversion service to first convert the PDF into an editable Word document.
> 
> [Convert PDF to Word \| Adobe Acrobat](https://www.adobe.com/in/acrobat/online/pdf-to-word.html)

[Special Christmas Order 2024 \| Ville Villers-Semeuse](https://www.villers-semeuse.fr/wp-content/uploads/2024/12/arrete-special-pere-noel-24-12-2024.pdf)

![[aoo-2025-2-6.png|640]]
_Decree 1 - Article 6_

![[aoo-2025-2-8.png|500]]
_Article 6 translation_

[Special Christmas Order 2024 \| Ville Andrezieux-Boutheon](https://www.andrezieux-boutheon.com/wp-content/uploads/2024/12/Arrete-Pere-Noel-2024.pdf)

![[aoo-2025-2-7.png|640]]
_Decree 2 - Article 4_

![[aoo-2025-2-9.png|500]]
_Article 4 translation_

For the translation, I understood this was the correct decree. Both documents contained the mayor's name at the end.

![[aoo-2025-2-10.png|380]]
_Mayor 1 name_

![[aoo-2025-2-11.png|550]]
_Mayor 2 name_

> Dupuy Driol

### Day 6

[Advent of OSINT 2025 - Day 6 \| OSINT4Fun](https://www.osint4fun.eu/advent2025/20251206183000)

You come across this [inspiring video](https://www.linkedin.com/posts/macha-b-626b78_en-ces-temps-incertains-ou-nous-nous-faisons-activity-6921350945398288385-rvhy/) on LinkedIn.

**Q) Which influencer was the first to make this video go viral?**

This question was a little weird for me, as I just stumbled into the correct answer. I am not sure if this was the intended way to solve the challenge.

First, I used a LinkedIn post date extractor to find out when the video was posted.

![[aoo-2025-2-19.png|600]]
_LinkedIn Post Date_

[LinkedIn Post Date Extractor: How to See the Exact Date of a LinkedIn Post](https://trevorfox.com/linkedin-post-date-extractor.html)

The post on LinkedIn was made on **April 17, 2022**. Since we know this is a reshare, the original post will have been made on a date before April 17, 2022.

A video is nothing but a collection of images. Which means we can use the same technique we have used with images to find videos. Using screenshots taken at different points in the video, we can find videos with similar content.

This works because most of the time frames from the video are used as the thumbnail. Luckily for us, social media sites only use frames from the first few seconds to decide the thumbnail. So using screenshots from the start of the video, we should be able to find all sites on which this video was posted.

![[aoo-2025-2-12.png|460]]
_Frame 1 from Video_

I took the 1st frame from the video and performed an image search. There were multiple results from LinkedIn, but none of these accounts had sufficient followers to be called an influencer. 

![[aoo-2025-2-20.png|500]]
_LinkedIn page with post_

![[aoo-2025-2-21.png|500]]
_LinkedIn page with post_

There was also a post by an account on Facebook that had thousands of followers; however, this video was posted after April 17, 2022, which disqualifies it.

![[aoo-2025-2-23.png|400]]
_Facebook Group_

![[aoo-2025-2-22.png|600]]
_Facebook Group Post_

The result also had a news article. This caught my attention because the title mentioned **Anand Mahindra,** who I know is the chairman of the Mahindra Group. Mahindra Group is a large multinational conglomerate from India.

![[aoo-2025-2-13.png|600]]
_Google Image Search result_

[Anand Mahindra Praises Young Boy's Incredible Fishing Technique \| Firstpost](https://www.firstpost.com/india/anand-mahindra-praises-young-boys-incredible-fishing-technique-watch-the-video-here-10509271.html)

![[aoo-2025-2-14.png|550]]
_News article with video_

The article has a direct link to Mahindra’s post on Twitter/X. The video was uploaded to Twitter on April 1, 2022, which is before the April 17, 2022 date. Clicking on Mahindra’s name will take us to his Twitter page.

![[aoo-2025-2-15.png|400]]
_Link from news article_

He has over 11M followers and can definitely be called an influencer. Anand Mahindra turned out to be the correct answer.

![[aoo-2025-2-16.png|500]]
_Original posters Twitter page_

> Anand Mahindra

I also performed an image search using a frame that is a few seconds into the video. With this frame I was able to get Mahindra’s post on Twitter/X as the first result.

![[aoo-2025-2-17.png|450]]
_Another frame from the video_

![[aoo-2025-2-18.png|600]]
_Google Image Search results_

### Day 7

[Advent of OSINT - Day 7 \| OSINT4Fun](https://www.osint4fun.eu/advent2025/20251207193000)

In 1963, the Beatles released the first edition of their Christmas “flexi disc.” These limited editions, both humorous and a symbol of the group’s musical and artistic creativity, were distributed to members of the band's British fan club.

![[aoo-2025-2-24.png|300]]
_Album Cover_

**Q) In the first flexi disc, one of the boys speaks at 4:05 and thanks three people. What are their surnames?** 

Since The Beatles are quite popular, I decided to just search Google to find the name of the Christmas album they had released in 1963.

> [!NOTE]
> The album name can also be found using the album cover provided in the question.

![[aoo-2025-2-25.png|600]]
_Google Search results_

Using the Wikipedia article, I learned that the album was called “The Beatles Christmas Record.”

![[aoo-2025-2-26.png|600]]
_Album Wikipedia entry_

From the article we also learn that they continued the practice of sending out recorded Christmas albums on flexi discs till 1969.

![[aoo-2025-2-27.png|600]]
_Album Wikipedia details_

[The Beatles' Christmas records - Wikipedia](https://en.wikipedia.org/wiki/The_Beatles%27_Christmas_records)

Next, I searched Google for an MP3 version of the album. I found a link to the Christmas album on Internet Archive. By listening to the audio at the time mentioned in the question, I heard George Harrison thank 3 people.

![[aoo-2025-2-28.png|640]]
_Album MP3 Google Search_

[The Beatles - Complete Christmas Collection](https://archive.org/details/BeatlesCompleteChristmasCollection19631969_201312/t02_The+Beatles+Christmas+Record+(1963).mp3)

You can also pull up the transcript/lyrics for the album and read through it to find the 3 people that are thanked.

![[aoo-2025-2-29.png|500]]
_Album transcript snippet_

[The Beatles' Christmas Record Lyrics \| Genius Lyrics](https://genius.com/The-beatles-the-beatles-christmas-record-lyrics)

> Collingham Rose Kelly

**Q) When Freda Kelly is mentioned, you can hear the group exclaim « Good ol' Freda! ». Several years later, this expression would be chosen as the title of a documentary about Freda’s life. In the trailer of this documentary, Freda explains that she had naively given her personal address for the fan club, and this is briefly illustrated by an envelope. From which city and which country does the mail come?** 

At the 0:45 mark the envelope in question can be seen.

<iframe width="560" height="315" src="https://www.youtube-nocookie.com/embed/LqO3DIaKTXM?si=VWEsVkvcXrPkV7L_" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>

The thing to understand here is that the address that is given at the bottom is the recipient's address. The sender's location can be found out from the text on the stamp. I searched online for “Galati” and found out that this is a town in Romania.

![[aoo-2025-2-30.png|600]]
_Image from Beatles Documentary Trailer_

![[aoo-2025-2-31.png|640]]
_City of Galati details_

> Galati Romania

**Q) Those Beatles' flexi discs are collectors items; for instance, a 1965 flexi disc is part of a museum’s permanent collection. What is its inventory number?**

Using the Wikipedia article, I find out that the Christmas album released in 1965 was called “The Beatles Third Christmas Record.”

![[aoo-2025-2-32.png|600]]
_Wikipedia page on album

[The Beatles' Christmas records - Wikipedia](https://en.wikipedia.org/wiki/The_Beatles%27_Christmas_records)

I searched for this album along with the word “museum” and found a link that took me to the site of the museum in Liverpool.  

![[aoo-2025-2-33.png|600]]
_Google Search for album museum listing_

On this page I could see the inventory number for the record.

![[aoo-2025-2-34.png|600]]
_Museum of Liverpool Album Listing_

[The Beatles Third Christmas Record, 1965 \| National Museums Liverpool](https://www.liverpoolmuseums.org.uk/artifact/beatles-third-christmas-record-1965)

> MLL.2005.41.28

### Day 8

[Advent of OSINT - Day 8 \| OSINT4Fun](https://www.osint4fun.eu/advent2025/20251208203000)

![[aoo-2025-2-35.png|350]]
_Department Store Image_

**Q) Near this department store, several shots for a classic French film were illegally filmed without permission at the end of the 20th century. What is the filming date of these stolen shots?**

Since we are given an image with no other clues, I performed a reverse image search on Google. From this I discovered that the department store in the picture is called “Galeries Lafayette” and is located in Paris.  

![[aoo-2025-2-36.png|600]]
_Department Store Google Search_

![[aoo-2025-2-37.png|640]]
_Department Store Name_

[Christmas display at Les Galeries Lafayette - Wikimedia Commons](https://commons.wikimedia.org/wiki/File:Christmas_display_under_the_dome_at_Les_Galeries_Lafayette_in_Paris.jpg)

Next, I decided to use Google dorking and look for articles that mention the store along with words like “illegal” and “movie.” 

```
Galeries Lafayette "illegal" "movie"
```

This led me to a post on IMDb for a French theater play.

![[aoo-2025-2-38.png|640]]
_Movie Name Google Search_

["Emmenez-moi au théâtre" - Trivia - IMDb](https://m.imdb.com/title/tt0416175/trivia/)

The post talks about a movie that has an illegal scene that was filmed at this location. The name listed on the poster is the name of the movie in question.

![[aoo-2025-2-39.png|600]]
_Movie IMDb Entry_

> [!NOTE]
> This post is listed under a TV show on IMDb since the movie is based on a theater play. 

The name of the movie is “Le père Noël est une ordure.”

![[aoo-2025-2-40.png|640]]
_Movie French Name_

[Santa Claus Is a Stinker (1982) - IMDb](https://www.imdb.com/title/tt0084555/)

Which translates to “Santa Claus Is a Stinker” in English.

![[aoo-2025-2-41.png|640]]
_Movie English Name_

[Santa Claus Is a Stinker - Google Search](https://www.google.com/search?channel=entpr&q=Le+p%C3%A8re+No%C3%ABl+est+une+ordure)

Finding the time at which this scene was filmed proved to be quite challenging. No matter how hard I looked, I could not find a single article that listed the date on which the illegal scene was shot. I could not even find it by setting my location to France using a VPN.

> [!NOTE]
> Contents
If anyone knows how this question can be solved using Google please let me know.

Defeated I turn to ChatGPT to see if it would find the date. The answer it provided was primarily based on an article from a French website.

![[aoo-2025-2-42.png|600]]
_ChatGPT Search Result_

I scanned through the article, and sure enough, it mentioned the date on which the illegal scene was filmed.

![[aoo-2025-2-43.png|640]]
_Website with Movie Details_

[Santa Claus is a Stinker: The crazy behind-the-scenes of a cult comedy \| Premiere.fr](https://www.premiere.fr/Cinema/News-Cinema/Le-Pere-Noel-est-une-ordure-a-40-ans-dans-les-coulisses-dingues-d-une-comedie-culte)
> December 1981
