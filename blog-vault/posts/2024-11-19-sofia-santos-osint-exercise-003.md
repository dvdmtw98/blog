---
title: "Sofia Santos: OSINT Exercise #003"
description: Test your OSINT skills with this challenge, uncover hidden details through your investigative skills
date: 2024-11-19 21:40:00 -0600
categories:
  - Security
  - OSINT
tags:
  - security
  - osint
  - walkthrough
  - forensics
  - geolocation
published: true
media_subpath: /assets/
---

![[sofia-santos-osint-003-banner.png|640]]

Background Image by <a href="https://www.freepik.com/free-photo/modern-background-with-lines_19314522.htm">BiZkettE1</a> on Freepik

In this write-up I will be going over OSINT Exercise #003 by [Sofia Santos](https://www.linkedin.com/in/sofia-santos-).

[OSINT Exercise #003 – Sofia Santos \| OSINT Analysis & Exercises](https://gralhix.com/list-of-osint-exercises/osint-exercise-003/)

## Task

In April 2017 Mohamed Abdullahi Farmaajo, the then president of Somalia, visited Turkey. A news agency published a photo where he was seen shaking hands with Recep Tayyip Erdoğan, the country’s president. The article did not disclose where the photo was taken. Our task is to find out the name and coordinates of the location seen below.

![[osint-exercise-003-picture.png|600]]

## Solution

We can use Google image search to find articles that the same photo.

[Google Images - Reverse Image Search](https://images.google.com/)

![[003-image-search-1.png|640]]

[Google Lens - Search Result](https://lens.google.com/search?ep=gisbubu&hl=en&re=df&p=AbrfA8oZPxhOpe96ibQ7eivbpQQOFLs25jJg_dPS6SGK1XcWyCwIDFep2bxX1pAMa5plHy8UgenGh_eYu1UUb95mr3_DnLlnXy34eOyK3zydlx80296wRHiGykU4Hsi5mCVVQR9wWWPpAG260hygS3S9t_lVCEAWRYMvM3_ZK6cmQ6CxGPkKZc2oIx-bf-RInB7ziwGZCrJe4z8Ajw%3D%3D#lns=W251bGwsbnVsbCxudWxsLG51bGwsbnVsbCxudWxsLG51bGwsIkVrY0tKRGxpTjJOallXTXlMV0ptT1RVdE5ETmtOeTA1WVRCaExURXpNekprTUdVeE5HRTNPQklmT0RjMlRGZDFRbE52WVVWaVVVVjFlRFl4WHpJd1dFRmpUWEZHWjA1Q2F3PT0iLG51bGwsbnVsbCxudWxsLG51bGwsbnVsbCxudWxsLG51bGwsWyJiMTJhZjQ4My0zYjRhLTRhMmMtOTVmMy1jNmQ3NmVlNTY4YTQiXV0=)

The first result is a article that contains the same image along with a description.

![[003-image-search-2.png|640]]

The description states that the image was taken at the Ankara **Presidential Palace**. On Google Maps lets search for “Presidential Palace Turkey”.

![[003-google-maps-1.png|640]]

[Presidential Complex of Turkey - Google Maps](https://www.google.com/maps/place/Presidential+Complex+of+Turkey/@39.9308873,32.7965016,699m/data=!3m2!1e3!4b1!4m6!3m5!1s0x14d34f8f6ccdb7df:0xa9ee717727a3fee!8m2!3d39.9308873!4d32.7990765!16s%2Fm%2F0123lr04?entry=ttu&g_ep=EgoyMDI0MTExMy4xIKXMDSoASAFQAw%3D%3D)

This location does not have Street View or 3D View data so we cannot take a closer look at the property. The original photo was taken in front of a door. The presidential complex has multiple buildings so its going to multiple doors. So the question becomes in front of which door was the photo taken.

![[003-picture-details.png|640]]

If we look closely at the original image we can see that behind the flags there are transparent containers with gold frames. Additionally at the top of the door there is a red emblem.

Searching for “Presidential Palace Turkey Entrance” will lead us to other images that was taken at the same entrance.

[Turkish President at Presidential Palace - Getty Images](http://www.gettyimages.com/detail/1245023174)

[Turkish President shakes hands with Russian President - Getty Images](http://www.gettyimages.com/detail/459829588)

[What's Up With Turkey's New Military Base in Qatar? - Sputnik International](https://sputnikglobe.com/20151218/turkey-qatar-military-base-analysis-1031967375.html)

The above images all appear to be been taken at the same entrance as they all contain the artifacts identified in the original image.

If we can get a video that shows the presidents walking all the way to the door in the original photo then we could use the landmarks in the background along with the path to find the exact location of the door.

<iframe width="560" height="315" src="https://www.youtube-nocookie.com/embed/E6xl9D-cCWU?si=23iOeNXsZL9RH1U1" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>

<iframe width="560" height="315" src="https://www.youtube-nocookie.com/embed/9CWALiEg2Mw?si=7hL7zZ-Dcs28Gimt" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>

[Turkish President welcomes Egyptian President - Getty Images](https://www.gettyimages.in/detail/video/turkish-president-recep-tayyip-erdogan-on-wednesday-news-footage/2170178572)

Searching for “Presidential Palace Ankara Turkey Visits” on YouTube will bring up videos that show various presidents being welcomed to the presidential complex.

From these videos we can see that the door in question is parallel to a gate and a road. On the opposite side of the road there is a monument/structure.

![[003-google-maps-2.png|640]]

Using the information from the video we can confidently say that the photo was taken at the **Front Entrance** of the **Presidential Palace**. In Google Map we can right-click at the location where the front entrance would be located. The co-ordinates of the photo is **39.93116826482835, 32.799616279024214**.

[Challenge Yourself! – Sofia Santos \| OSINT Analysis & Exercises](https://gralhix.com/list-of-osint-exercises/)
