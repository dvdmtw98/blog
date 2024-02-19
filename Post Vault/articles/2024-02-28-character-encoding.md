---
title: "Character Set, ASCII, Unicode, UTF-8 & More: Simply Explained"
description: Character Encoding concepts explained in a simple easy to understand manner
date: 2024-02-28 21:56:01 -0600
categories:
  - Operating System
  - Encoding
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

First, we need to understand how data is stored. All data on a computer is stored as 0s and 1s either in the RAM (Memory) or on the Disk (Hard Drive, SSD). Whether it's a number like 42 or a character like the letter d it is transformed into bits (the most basic unit of data on computers) for storage. For numbers, it makes sense to transform them into their equivalent in the Base-2 number system which gives us its binary representation which can be used for storage. The integer **42** would convert to **`00101010`** in binary. But what about the letter d? What about Chinese characters? What about emojis? How do we represent non-numeric characters? The solution to this problem is to use a collectively agreed upon mapping (coded character set) that assigns each character a numeric value.

### Character Set

A **character set** or a character repertoire is simply a **set of unordered characters**. The Latin alphabet and the Greek alphabet are both examples of character sets.

### Coded Character Set

A **coded character set** maps each character in its repertoire to an **integer value**. Each character is essentially assigned a position in the character set. The integer that represents a character in a coded character set is called a "**Code Point**". The range of numeric values that span the entire coded character set is called a "**Code Space**". 

The term character set is commonly used to also refer to a coded character set. For the rest of this article, I will be using the term character set to refer to a coded character set.

### ASCII

ASCII or the American Standard Code for Information Exchange is a very popular, easy-to-understand character encoding standard. ASCII maps a set of control characters, Arabic numbers, Latin characters and punctuations to numbers between 0 and 127.

> [!INFO] Control Characters
> Control characters, also known as non-printing characters (NPC), are characters in a character set that do not represent a written character or symbol. They are used to signal to the terminal to perform special action, such as ringing a bell, erasing the screen, or controlling where the next character will display. They include characters such as tab, line feed, and carriage return.

![ascii-table|640](images/character-encoding/ascii-table.png)

The character set that is used by ASCII is also called ASCII. The ASCII character set provides a total of 128 usable characters. To represent all 128 characters in binary 7-bits ($2^7 = 128$) are required. To convert a string like "Hello" to ASCII we would look up the relevant value of each character in ASCII, convert the number into binary and concatenate them all together to get a storage-ready version. The process of representing a character in its binary form using a character set is called "**Character Encoding**". To decode the string the same steps are performed in reverse.

![hello-ascii-value|600](images/character-encoding/hello-ascii-value.png)

Some of you will be wondering why 7-bits why not clean a byte (8-bits). ASCII was created well before 8-bit bytes became ubiquitous. The notion of calling 8 bits a byte was not yet established. 

In later iterations of ASCII that were released after the concept of a byte was established 8 bits were used to encode each character. The MSB in each encoded character was used for error correction. Nowadays, ASCII is represented using 8-bits with the MSB value set to 0.

**MSB (Most Significant Bit)**: Bit that has the highest value in value in a bit stream. It is usually the bit that is farthest to the left.

ASCII has one big disadvantage, the 128-character code space was not large enough to store characters that are used by other languages. The need for additional characters eventually led to the creation of Extended ASCII. 

### Extended ASCII

Extended ASCII is a character encoding standard that utilizes 8-bits ($2^8 = 256$) to encode each character. Extended ASCII includes the original ASCII character set, plus an additional 128 characters. A formal definition for "Extended ASCII" was never created. As a result, different countries and organizations assigned different characters to the extended code space. In essence, different character sets were created that could all be represented using the Extended ASCII encoding. To be able to correctly display text data that included code points from the extended ASCII code space we need to know the exact character set that was used to encode the data.

### Code Page

When using products from vendors like Microsoft and Oracle you may come across the term "**code page**". A code page is just another term for a character set. The term code page was coined by IBM to market the support of different character sets on their Mainframe systems. Code pages that pertain to ASCII typically have the first 127 code points representing the original ASCII characters. The upper 128 code points (values 128-255) of each code page differed considerably. Each code page represented a different variant of Extended ASCII.

> [!INFO]
> While ASCII and Extended ASCII were the most popular character encodings around at the time they were not the only character encodings in use. Many countries created their character encodings or used variations of ASCII. Japan created multiple encoding standards to represent Japanese characters. The encodings that were used in Japan were all incompatible with each other. This meant that text data sent from a computer had a very high chance of appearing garbled on the receiving computer. The incompatibility was such a big issue that there is a word in Japanese to describe it - "Mojibake" (garbled text).

Once the internet came around and global communication became commonplace the use of wildly different, incompatible encoding standards became a problem. To fix this issue, the Unicode consortium was established. The group was tasked with designing a standard that would support characters from all of the world's major writing systems.

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
