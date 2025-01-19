---
title: "Sofia Santos: OSINT Exercise #004"
description: Test your OSINT skills with this challenge, uncover hidden details through your investigative skills
date: 2025-01-18 18:45:00 -0600
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

![[sofia-santis-osint-004-banner.png|640]]

Background Image by <a href="https://www.freepik.com/free-photo/modern-background-with-lines_19314522.htm">BiZkettE1</a> on Freepik

In this write-up I will be going over OSINT Exercise #004 by [Sofia Santos](https://www.linkedin.com/in/sofia-santos-).

[OSINT Exercise #004 – Sofia Santos \| OSINT Analysis & Exercises](https://gralhix.com/list-of-osint-exercises/osint-exercise-004/)

## Task

We have a photo of a resort located on an island. We have 3 questions to answer:  
a) What is the name of the resort?  
b) What are the coordinates of the island?  
c) In which cardinal direction was the camera facing when the photo was taken?

![[osint-exercise-004-image.png|640]]

## Solution

### Task 1

We can use a image reverse search service (Tiny Eye, Google Image) to find other articles/images that contain the photo we are given.

![[004-google-image-search-1.png|640]]

The search result shows us that the resort in the image is called “**Oan Resort**”.

![[004-google-maps-3.png|500]]

The resort is located on Oan Island, Wonip, Micronesia.

### Task 2

Searching for “Oan Resort” on Google Maps will bring up the listing for the resort. We can get the co-ordinate for the resort by right clicking on the pin icon on the map.

![[004-google-maps-1.png|600]]

[Oan Resort - Google Maps](https://www.google.com/maps/place/Oan+Resort/@7.3625898,151.7537439,1005m/data=!3m2!1e3!4b1!4m6!3m5!1s0x6667a510cf78a285:0x675c6874bba0f42!8m2!3d7.3625845!4d151.7563188!16s%2Fg%2F11g10qwz9t?entry=ttu&g_ep=EgoyMDI1MDExNS4wIKXMDSoASAFQAw%3D%3D)

The resort is located at “**7.3625207, 151.7561042**”.

### Task 3

For 3rd question we can utilize the 3D view feature provided by Google Maps. This feature can be enabled by clicking on Layers → More → Global View.

We need to position the 3D view camera in such a way that it resembles the angle from which the photo was taken. Once we have the correct view we can use the campus on the map to figure could the direction of the camera.

![[004-image-background.png|640]]

 If we look closely at the image we can see that behind Oan island towards the left side some islands are present visible.

![[004-google-maps-2.png|640]]

The compass on Google Maps uses uses the red arrow to represent North, the grey arrow represents South. The position represented by the **top of the compass** shows the **direction the virtual camera is facing**. 

![[004-compass.png|200]]

If we look at a compass with the cardinal directions and set it such that North is slightly towards the right we will see that we are facing North West.  From this we can conclude that the camera what was used to take the image was facing “**North West**”.

[OSINT Exercises – Challenge Yourself! – Sofia Santos \| OSINT Analysis & Exercises](https://gralhix.com/list-of-osint-exercises/)
