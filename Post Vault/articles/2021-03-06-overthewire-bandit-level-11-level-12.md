---
title: 'OverTheWire: Bandit Level 11 → Level 12'
description: '![OverTheWire - Bandit](https://overthewire.org/wargames/bandit/bandit12.html)'
date: '2021-03-06 09:14:17 +0530'
categories: [Security, OverTheWire]
tags: [overthewire, bandit, ctf, security, linux]
published: true
img_path: /assets/
image: images/overthewire-banner.png
---

## Level Goal

> The password for the next level is stored in the file **data.txt**, where all lowercase (a-z) and uppercase (A-Z) letters have been rotated by 13 positions

## Commands you may need to solve this level

> grep, sort, uniq, strings, base64, tr, tar, gzip, bzip2, xxd

```
> whatis grep  
grep (1)             - print lines that match patterns

> whatis sort  
sort (1)             - sort lines of text files

> whatis uniq  
uniq (1)             - report or omit repeated lines

> whatis strings  
strings (1)          - print the sequences of printable characters in files

> whatis base64  
base64 (1)           - base64 encode/decode data and print to standard output

> whatis tr  
tr (1)               - translate or delete characters

> whatis tar  
tar (1)              - an archiving utility

> whatis gzip  
gzip (1)             - compress or expand files

> whatis bzip2  
bzip2 (1)            - a block-sorting file compressor, v1.0.8

> whatis xxd  
xxd (1)              - make a hexdump or do the reverse.
```

**Note:** All commands don't have to be used to complete level

## Helpful Reading Material

[ROT13 - Wikipedia](https://en.wikipedia.org/wiki/Rot13)

[Tr Command in Linux with Examples \| Linuxize](https://linuxize.com/post/linux-tr-command/)

## Solution

View the contents of the current working directory

```
bandit11@bandit:~$ ls  
data.txt
```

View the data that is present in the file

```
bandit11@bandit:~$ cat data.txt  
Gur cnffjbeq vf 5Gr8L4qetPEsPk8htqjhRK8XSP6x2RHh
```

We know that the characters in the data are rotated by 13 characters. We can get the characters to their original order using the `tr` command. The `tr` command is used to translate/ transform data from one form to another.

_(Refer to the attached resources for more information on the tr command)_

```
bandit11@bandit:~$ cat data.txt | tr 'A-Za-z' 'N-ZA-Mn-za-m'  
The password is 5Te8Y4drgCRfCx8ugdwuEX8KFC6k2EUu
```

We have found the password for the next level !!

Logout of the current session and use the password of user bandit12 to access the next level

```
> ssh bandit12@bandit.labs.overthewire.org -p 2220  
This is a OverTheWire game server. More information on http://www.overthewire.org/wargames

bandit12@bandit.labs.overthewire.org's password: 5Te8Y4drgCRfCx8ugdwuEX8KFC6k2EUu
```