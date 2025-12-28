---
title: "OSINT4Fun: Advent of OSINT 2025 (Day 1 - Day 4)"
description: Get started with OSINT in 24 Days - Learn the basics by solving beginner-friendly challenge every day leading up to Christmas.
date: 2025-12-28 04:00:00 +0530
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

![[osint4fun-aoo-day-1-4-banner.png|640]]
_Image Background by [vector_corp](https://www.freepik.com/free-vector/yellow-grunge-brush-ink-background_37589666.htm) on Freepik_

### Day 1

[Advent of OSINT 2025 - Day 1 \| OSINT4Fun](https://www.osint4fun.eu/advent2025/20251201133000)

**Q) Who was driving this car in this picture?**

![[aoo-2025-day1-image.jpg|460]]
_Formula 1 Car_

We are given a picture so we can use Google Image Search (Google Lens) to find images with similar characteristics.

![[aoo-2025-1.png|540]]
_Google Image Search_

The first image looks exactly like the image we are given.

![[aoo-2025-2.png|600]]
_Google Image Search Results_

The description tells us that the car in the image was driven by **Fernando Alonso**.

[Wikipedia - Minardi PS01](https://en.wikipedia.org/wiki/File:Minardi_Ps01.jpg)

![[aoo-2025-3.png|640]]
_Fernando Alonso driving the Minardi PS01_

> Fernando Alonso

**Q) That year, on which circuit did Alonso achieve his best result?**

The metadata of the image tells us that it was taken in 2001. I went to Alonso’s Wikipedia page, as I know it would have his career milestones listed. In the career section it's mentioned that his best finish in 2001 was tenth place at the German Grand Prix.

![[aoo-2025-4.png|640]]
_Fernando Alonso Career Page_

[Fernando Alonso - Wikipedia](https://en.wikipedia.org/wiki/Fernando_Alonso#Minardi_and_Renault_(2001%E2%80%932006))

In 2001 the German Grand Prix was held at **Hockenheim** at the Hockenheimring.

![[aoo-2025-5.png|350]]
_German Grand Prix 2001 Details_

[2001 German Grand Prix - Wikipedia](https://en.wikipedia.org/wiki/2001_German_Grand_Prix)

> Hockenheimring

There are multiple websites that specialize in collating records & statistics related to Formula 1. One such website is Stats F1. This site can also help in finding the answer.

![[aoo-2025-10.png|640]]
_Fernando Alonso 2001 Grand Prix Stats_

**Q) A few years later, on this same circuit, he took his revenge by winning the race. What was his average speed (in km/h) during that race?** 

To solve this question, we need to find the first German Grand Prix after 2001, where Alonso won the race. Using Stats F1, we can find the details of all the races held at Hockenheim.

![[aoo-2025-11.png|640]]
_Formula 1 Race Locations_

We can see that Alonso won the German Grand Prix for the 1st time in **2005**.

![[aoo-2025-6.png|640]]
_Nurburgring Race Details_

[Nürburgring \| STATS F1](https://www.statsf1.com/en/circuit-nurburgring.aspx)

To find his average speed, we need to do a few calculations. First we need to find the total distance he traveled in kilometers, and then we need to find the time taken to cover this distance in hours.

$$Speed = \frac{Distance}{Time}$$

The time listed on Stats F1 for Alonso is incorrect. In this case, Wikipedia has the correct values. The German Grand Prix in 2005 lasted for 67 laps with a total distance of **306.458** km.

![[aoo-2025-12.png|350]]
_German Grind Prix 2005 Details_

[2005 German Grand Prix - Wikipedia](https://en.wikipedia.org/wiki/2005_German_Grand_Prix)

On the same page under the classification section, we see that Alonso took 1 hour, 26 minutes, and 28.599 seconds to complete the race.

![[aoo-2025-7.png|560]]
_German Grand Prix 2005 Race Details_

To convert the time into hours, we divide the minutes component by 60 (1 hour = 60 minutes), and we divide the seconds component by 3600 (1 hour = 3600 seconds). This gives us the total time taken as **1.441** hours.

![[aoo-2025-8.png|320]]
_Converting Time to Hours_

When we divide the distance by time, we get the average speed as **212.629 km/h**. 

![[aoo-2025-9.png|400]]
_Calculating Average Speed_

> 212.629 km/h

Since this challenge heavily relies on statistics, we can also use AI to quickly get the answers.

![[aoo-2025-13.png|560]]
_ChatGPT Results_

### Day 2

[Advent of OSINT 2025 - Day 2 \| OSINT4Fun](https://www.osint4fun.eu/advent2025/20251202143000)

Christmas is approaching, and you’re feeling nostalgic for your **summer** holidays.  
You come across this photo of one of the iconic places from your trip.  
One of the members of your group, who particularly enjoyed the visit, shared **her** thoughts in **August 2025** as well as other photos online, including one picture showing the **chandelier under the entrance porch**.

![[aoo-2025-day2-image.jpg|400]]
_Location with Ceiling with Flags_

**Q) What is this person’s first name and what is the green and red object hanging from the chandelier?**

For me this challenge was quite difficult. It took me a long time and a few hints before I was finally able to solve it.

The description provided along with the image is pretty important. We learn that the trip in question took place during **Summer 2025**. We also learn that the person who posted the image is a **woman.** We also are told that the person **enjoyed** the location.

Since we have an image, let's use Google Lens to find images with similar features.

![[aoo-2025-14.png|500]]
_Image Reverse Search Results_

Since this image was taken during a trip, results that list flags for purchase can be ignored. I used the TripAdvisor links as a starting point, as they provide reviews for locations that are popular with tourists. I believed this was the site where the person in question had posted their review/images.

However, this is where I ran into a major hurdle. I looked at all the relevant results from the image search; however, none of them had images that matched the picture provided in the question. 

This challenge can only be solved when the image search is performed from France (might work for some other countries as well). This issue can, however, be easily mitigated by using a VPN.

After changing my location to France, I once again performed the image search. This time I found a cafe that had a ceiling that looked similar to the image in the question. I decided to investigate the images related to this cafe to identify if this was the correct location.

![[aoo-2025-15.png|600]]
_Image Reverse Search Results_

[BAGDAD CAFE, Newberry Springs - Restaurant Review - Tripadvisor](https://www.tripadvisor.in/Restaurant_Review-g32775-d1988674-Reviews-Bagdad_Cafe-Newberry_Springs_California.html)

I opened the reviews section and filtered them to only display the ones that match the criteria that were given in the question, which narrowed it down to a single comment.

![[aoo-2025-25.png|450]]
_TripAdvisor Rating Filter_

This review did not have an image with a chandelier.

![[aoo-2025-16.png|600]]
_Tripadvisor Review_

However, this review had an image that showed the same globe that was present in the image from the question.

![[aoo-2025-17.png|600]]
_Tripadvisor Review_

Next, I decided to browse through the images that were posted for this location, and sure enough, I found other images that contained posters and flags, which are also visible in the original image.

![[aoo-2025-18.png|600]]
_Tripadvisor Review_

![[aoo-2025-19.png|600]]
_Tripadvisor Review Image Zoom_

I was now confident that I had the correct place. The location visited during the summer trip was **Baghdad Cafe** in Newberry Springs, California.

![[aoo-2025-20.jpg|400]]
_Original Image with Highlighted Items of Interest_

I looked up Baghdad Cafe on Google. Google also has an option to review places. Clicking the Opinion/Review button will open a new page.

![[aoo-2025-21.png|600]]
_Baghdad Cafe Google Listing_

On this page clicking on “more” beside any of the review will open a new page. On this page the full review, along with images, can be viewed.

![[aoo-2025-24.png|500]]
_Baghdad Cafe Google Review_

The third review (at the time of writing this walkthrough) was by a **Denise** Deneuville from 3 months ago (Sept 2025), which falls in the Summer 2025 time range. The review had 5 stars and seems to be posted by a lady. All the attributes of this review match the conditions specified in the description. This review also had an image of a chandelier from the cafe entrance.

![[aoo-2025-22.png|600]]
_Baghdad Cafe Google Review_

The chandelier has a green and red **hat** stuck on it.

![[aoo-2025-23.png|400]]
_Baghdad Cafe Google Review Image_

> Denise Hat

### Day 3

[Advent of OSINT 2025 - Day 3 \| OSINT4Fun](https://www.osint4fun.eu/advent2025/20251203153000)

![[aoo-2025-day3-image.jpg|640]]
_The Street Image_

**Q) A little further down this street, on a day in November 2022, there stood a rather unusual character. Who was it?**

We can see that this image is taken on a street called **The Street**. On the left side of this street is a place called **The Leather Bottle**.

![[aoo-2025-26.png|350]]
_The Leather Bottle Signage_

A quick Google Search lead me to the official site for this place. The Leather Bottle is a pub. The address mentioned in the link confirms that this is the correct branch.

![[aoo-2025-27.png|600]]
_The Leather Bottle Google Search_

The site has a picture that looks similar to the image from the question.

![[aoo-2025-28.png|600]]
_The Leather Bottle Website_

[The Leather Bottle, Gravesend](https://www.theleatherbottle.pub/index)

On the same page towards the bottom there is a map. Click "view large map" to open the address on Google Maps.

![[aoo-2025-31.png|600]]
_The Leather Bottle Website_

Zoom in a little and then drag the yellow person from the bottom right of the screen to the location denoted by arrow 2. This will put us in street view right in front of the pub.

![[aoo-2025-29.png|640]]
_The Leather Bottle Coordinates_

[The Leather Bottle - Google Maps](https://www.google.com/maps/place/The+Leather+Bottle/@51.3904351,0.3956337,15.94z/data=!4m9!3m8!1s0x47d8ca607898021b:0xfe0eed3739aa8fd5!5m2!4m1!1i2!8m2!3d51.3906137!4d0.398493!16s%2Fg%2F1tjxdy3y?hl=en-US&entry=ttu&g_ep=EgoyMDI1MTIwOS4wIKXMDSoASAFQAw%3D%3D)

Now our view looks exactly like the view from the image from the question. We are told in November 2022 there was someone unusual down the street. Click on the “See Latest Data” button, which should open up the historical data selector. Select November 2022.

![[aoo-2025-30.png|640]]
_The Leather Bottle Street View_

Now move down the street, and you should find the **Grinch** standing on the left-hand side of the street.

![[aoo-2025-32.png|600]]
_Street View with Person of Interest_

[Unusual Person - November 2022 - Google Maps](https://www.google.com/maps/place/The+Leather+Bottle/@51.3903482,0.3994205,3a,75y,107.94h,63.9t/data=!3m8!1e1!3m6!1sZuQlXYnvbvrwa98hkA_iDw!2e0!5s20221101T000000!6shttps:%2F%2Fstreetviewpixels-pa.googleapis.com%2Fv1%2Fthumbnail%3Fcb_client%3Dmaps_sv.tactile%26w%3D900%26h%3D600%26pitch%3D26.1%26panoid%3DZuQlXYnvbvrwa98hkA_iDw%26yaw%3D107.94!7i16384!8i8192!4m10!3m9!1s0x47d8ca607898021b:0xfe0eed3739aa8fd5!5m2!4m1!1i2!8m2!3d51.3906137!4d0.398493!10e5!16s%2Fg%2F1tjxdy3y?hl=en-US&entry=ttu&g_ep=EgoyMDI1MTIwOS4wIKXMDSoASAFQAw%3D%3D)

> Grinch

### Day 4

[Advent of OSINT - Day 4 \| OSINT4Fun](https://www.osint4fun.eu/advent2025/20251204163000)

`79°44'8"N 10°59'21"E`

**Q) These coordinates point to the location of a settlement that no longer exists. Its former name inspired the fictional town featured in a Christmas film. What is the name of the film and when was it released?**

Using Google Maps, we can see what is located at the coordinates. The coordinates take us to the southern tip of the island of Amsterdamøya, Svalbard. Svalbard is a very remote location, so no historic or street view data is available for it.

![[aoo-2025-33.png|640]]
_Amsterdam Island Coordinates_

[79°44'08.0"N 10°59'21.0"E - Google Maps](https://www.google.com/maps/place/79%C2%B044'08.0%22N+10%C2%B059'21.0%22E/@79.7538791,10.773146,11.75z/data=!4m4!3m3!8m2!3d79.7355556!4d10.9891667?entry=ttu&g_ep=EgoyMDI1MTIwOS4wIKXMDSoASAFQAw%3D%3D)

![[aoo-2025-36.png|600]]
_Amsterdam Island Coordinates_

Next, I searched on Google for Amsterdamoya and noticed that there is a Wikipedia article for this island.

![[aoo-2025-34.png|640]]
_Amsterdamoya Google Search_

[Amsterdamoya - Google Search](www.google.com/search?q=amsterdamoya)

The article tells us that in the 1600s there was a town called **Smeerenburg** that was constructed for whaling on the southeastern side of this island. This could be our town.

![[aoo-2025-35.png|550]]
_Amsterdamoya Wikipedia_

The entry for Smeerenburg contains coordinates.

![[aoo-2025-37.png|640]]
_Smeerenburg Wikipedia_

[Smeerenburg - Wikipedia](https://en.wikipedia.org/wiki/Smeerenburg)

The coordinates at first seems to point to the ocean.

![[aoo-2025-38.png|560]]
_Smeerenburg Google Maps_

[79°43'54.0"N 10°59'42.0"E - Google Maps](https://www.google.com/maps/place/79%C2%B043'54.0%22N+10%C2%B059'42.0%22E/@79.7558503,10.8649098,11.65z/data=!4m4!3m3!8m2!3d79.7316667!4d10.995?entry=ttu&g_ep=EgoyMDI1MTIwOS4wIKXMDSoASAFQAw%3D%3D)

However, if we use satellite view, we see that the coordinate points to the beach, which is located beside the coordinate given in the question.

![[aoo-2025-40.png|600]]
_Smeerenburg Google Maps Satellite View_

From this I was 80% certain this was the correct town. I decided to scroll through the Smeerenburg article to see if I could find any other useful information. This led me to the following sentence, which pretty much guaranteed this was the right place.

![[aoo-2025-41.png|640]]
_Smeerenburg Wikipedia_

To verify this information I did a Google Search using the following Dork:

```
smeerenburg "christmas" "movie"
```

The same movie showed up in the results. So the Christmas movie that has a town with a similar name is **Klaus**.

![[aoo-2025-39.png|500]]
_Smeerenburg Movie Google Search_

[In Klaus (2019), the town of Smeerensburg is actually based on a real place, located on a remote island in Norway: r/MovieDetails](https://www.reddit.com/r/MovieDetails/comments/13nydi7/in_klaus_2019_the_town_of_smeerensburg_is/)

> Klaus 2019
