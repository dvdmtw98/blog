---
title: "Sofia Santos: OSINT Exercise #002"
description: Test your OSINT skills with this challenge, uncover hidden details through investigative techniques
date: 2024-11-16 09:50:00 -0600
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

![[sofia-osint-002-banner.png|640]]

Background by  <a href="https://www.freepik.com/free-photo/modern-background-with-lines_19314522.htm">BiZkettE1</a> on Freepik

In this write-up I will be going over OSINT Exercise #002 by [Sofia Santos](https://www.linkedin.com/in/sofia-santos-).

[OSINT Exercise #002 – Sofia Santos \| OSINT Analysis & Exercises](https://gralhix.com/list-of-osint-exercises/osint-exercise-002/)

## Task

We are given a image of a train station. We have 2 questions to answer:  
a) What is the name of the train station seen in the photo?  
b) What is the name and height of the tallest structure seen in the photo?

![[osint-exercise-002-picture.png|640]]

## Solution

### Task 1

For the 1st question we are given the solution directly. There are multiple sign boards in the image that tell us this photo was taken at “**Flinders Street**”.

![[flinders-street-1.png|640]]

We can perform a Google search to find where this train station is located.

![[flinders-street-2.png|400]]

Looks like Flinders Street Station is located in **Melbourne, Australia**.

There can be multiple train stations that have the same name. To confirm this is the correct station we can use Google Maps and look at photo sphere’s around the train station to see if any landmarks from the photo is visible.

![[flinders-street-3.png|640]]

In the photo that we are given we can see that there are 6 buildings in the background. We can see that the 3rd building is named “**HWT**” and the 4th building has the logo for the IT company “**IBM**”.

[Flinders Street Railway Station - Google Maps](https://www.google.com/maps/@-37.8184246,144.9652116,360m/data=!3m1!1e3?entry=ttu&g_ep=EgoyMDI0MTExMy4xIKXMDSoASAFQAw%3D%3D)

![[flinders-street-4.jpg|640]]

Use photo sphere’s that face **Yarra River** to see the buildings from the photo.

> [!IMPORTANT] Google Photo Sphere
> When you drag the yellow person (pegman) located at bottom left onto the map all the photo sphere’s that are available in the location will be shown. Drop pegman onto a sphere to view the image captured from that location.

![[flinders-street-5.jpg|640]]

[Yarra River Walk Path - Photo Sphere - Google Maps](https://www.google.com/maps/@-37.818175,144.9649698,3a,75y,106.45h,96.99t/data=!3m8!1e1!3m6!1sAF1QipOzElhVVhzvUNWnBkbh2oJlDVXu1nu7k3VbRXeX!2e10!3e11!6s%2F%2Flh5.ggpht.com%2Fp%2FAF1QipOzElhVVhzvUNWnBkbh2oJlDVXu1nu7k3VbRXeX%3Dw900-h600-k-no-pi-6.992928877791371-ya0.45323326200886527-ro0-fo100!7i7168!8i3584?entry=ttu&g_ep=EgoyMDI0MTExMy4xIKXMDSoASAFQAw%3D%3D)

As the same buildings are visible in the background we can be confident we have the correct train station. So, **Flinders Street** is located in **Melbourne, Australia**. From this view we can see that the 6th building in the photo is called “**Langhom**”.

### Task 2

We cannot guess the height by just looking at the photo. The angle at which the photo was taken could warp the real heights. Google Map has a 3D view option that can help us get a better look.

![[google-maps-1.png|400]]

![[google-maps-2.png|200]]

Hover mouse over the Layers button, choose “More” and then select “Global view”. This should help us gauge the heights of the buildings more accurately. 

![[google-maps-3.jpg|640]]

We can easily identify the first 5 buildings but the 6th (blue) building is a little challenging as there are multiple blue buildings in the same location. If we look closely at the photo that is provided we see that there are 2 red banners on the top floor of the blue building.

![[google-maps-4.jpg|600]]

This building matches the description of the building we need. It is blue, tall and has red signs on the top floor. The signs have “**Central Equity**” written on them.

![[google-maps-5.jpg|640]]

![[google-maps-6.jpg|640]]

If we look at the buildings from different directions it becomes clear only buildings 1 “**Arts Centre**”, 4 “**IBM Building**” and 6 “**Central Equity**” have to be considered. The other 3 buildings are shorter than the IBM building.

![[arts-centre-1.png|500]]

When we search for “Melbourne Arts Centre Height” Google AI overview tells us that the Arts Centre is **162 meters**. We can confirm the same information using the official website of the Arts Centre.

![[arts-centre-2.png|500]]

[Arts Centre Melbourne - About Us - Our History](https://www.artscentremelbourne.com.au/about-us/our-history)

[Arts Centre Melbourne - Wikipedia](https://en.wikipedia.org/wiki/Arts_Centre_Melbourne)

![[ibm-1.png|600]]

When we search for “Melbourne IBM Building Height” we get a link to a website that contains information on tall buildings. According to the site the building is **131 meters**.

[IBM Australia - The Skyscraper Center](https://www.skyscrapercenter.com/building/ibm-australia/13493)

![[ibm-2.png|500]]

We can confirm this is the correct building by looking at the building in 3D view.

When we search for “Melbourne Central Equity” we see that Central Equity is the name of a Real Estate Agency not the building. On there website we see that this agency has worked on 4 construction projects.

[Central Equity, Melbourne Property](https://centralequity.com.au/)

![[focus-1.png|600]]

If we look at the address of the Arts Centre and IBM Building we will notice that they are located in **Southbank**. Central Equity only has 1 project in Southbank. This should be the building we need. The apartment is called **Focus**.

![[focus-2.png|500]]

On Google Maps in 2D view if we zoom onto the building we can see that the building is indeed called Focus.

![[focus-3.jpg|640]]

We can also use Pegman and drop into Street View in front of the building. You will see that the entrance states the name of the apartment as Focus.

On searching for “Melbourne Focus Apartment” you will find a link to the same website that had information about the IBM building. The site states that Focus Apartments is **166 meters**.

![[focus-4.png|600]]

[Focus Melbourne - The Skyscraper Center](https://www.skyscrapercenter.com/building/focus-melbourne/38852)

Based on the information we have gathered we can conclude that the tallest building visible in the photo is **Focus Apartment**.

[OSINT Exercises – Challenge Yourself! – Sofia Santos \| OSINT Analysis & Exercises](https://gralhix.com/list-of-osint-exercises/)
