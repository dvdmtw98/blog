---
title: "Character Set, ASCII, Unicode, UTF-8 & More: Simply Explained"
description: Character Encoding concepts explained in a simple easy to understand manner
date: 2024-02-28 21:56:01 -0600
categories:
  - Operating System
  - Programming
tags:
  - operating-system
  - programming
  - encoding
  - windows
  - linux
published: false
img_path: /assets/
---

In this article, you will learn about character encoding, its different types and how data is represented in Unicode the most widely used character encoding. I will try my best to explain these topics in an approachable manner. I will assume that the reader has a basic understanding of programming.

### Data Storage

First, we need to understand how data is stored. All data on a computer is stored as 0s and 1s either in the RAM (Memory) or on the Disk (Hard Drive, SSD). Whether it's a number like 42 or a character like the letter d it is transformed into bits (the most basic unit of data on computers) for storage. For numbers, it makes sense to transform them into their equivalent in the Base-2 number system which gives us its binary representation which can be used for storage. The integer **42** would convert to **`00101010`** in binary. But what about the letter d? What about Chinese characters? What about emojis? How do we represent non-numeric characters? The solution to this problem is to use a collectively agreed upon mapping (coded character set) that assigns each character a numeric value.

#### Character Set

A **character set** or a character repertoire is simply a **set of unordered characters**. The Latin alphabet and the Greek alphabet are both examples of character sets.

#### Coded Character Set

A **coded character set** maps each character in its repertoire to an **integer value**. Each character is essentially assigned a position in the character set. The integer that represents a character in a coded character set is called a "**Code Point**".

The term character set is quite commonly used to also refer to a coded character set. For the rest of this article, I will also be using the accepted convention of calling coded character set a character set.

### ASCII

ASCII or the American Standard Code for Information Exchange is a very popular, easy-to-understand character set. ASCII maps a set of control characters and Latin characters to numbers between 0 and 127.

> [!INFO] Control Characters
> Control characters, also known as non-printing characters (NPC), are characters in a character set that do not represent a written character or symbol. They are used to signal to the terminal to perform special action, such as ringing a bell, erasing the screen, or controlling where the next character will display. They include characters such as tab, line feed, and carriage return.

![ascii-table|640](images/character-encoding/ascii-table.png)

The ASCII character set provides a total of 128 characters.

### References

<iframe 
	width="560" height="315" src="https://www.youtube-nocookie.com/embed/MijmeoH9LT4?si=DKLzUB2NQHRvQJXy" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen>
</iframe>

<iframe 
	width="560" height="315" 
	src="https://www.youtube-nocookie.com/embed/ut74oHojxqo?si=dmKpMbFE2CuhrO7v" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen>
</iframe>

<iframe 
	width="560" height="315" src="https://www.youtube-nocookie.com/embed/jeIBNn5Y5fI?si=Au82ap2gQjwZB36o" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen>
</iframe>
