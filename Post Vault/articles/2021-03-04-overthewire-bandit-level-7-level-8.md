---
title: 'OverTheWire: Bandit Level 7 → Level 8'
description: 'https://overthewire.org/wargames/bandit/bandit8.html'
date: '2021-03-04 04:17:03 +0530'
categories: [Security, OverTheWire]
tags: [overthewire, bandit, ctf, security, linux]
published: true
img_path: /assets/
image: images/overthewire-banner.png
---

## Level Goal

> The password for the next level is stored in the file **data.txt** next to the word **millionth**

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

[How to Use Grep Command in Linux [12 Useful Examples]](https://www.tecmint.com/12-practical-examples-of-linux-grep-command/)

[Head command in Linux with examples - GeeksforGeeks](https://www.geeksforgeeks.org/head-command-linux-examples/)

## Solution

View the contents of the current working directory

```
bandit7@bandit:~$ ls  
data.txt
```

Peek at the data that is present in the file. This can be achieved using the `head` command

```
bandit7@bandit:~$ head -n 10 data.txt   
binning WnfnFPqkuhl2nwHBohzn2C4L5W0gwcLq  
abuts v8PAwDdkGDdp5NsJ7ZFM5A7TJ5MkYDbm  
fathead wBhCy0fqvbQdexz5kMKBtGoSWgXw7s0H  
attacks 3GzwnGiZnBDdVuHivJk1pEfOOYu7uOTa  
lopping H9hzviFp1QO4WF8EzcQNl5MDz5r1bzUC  
tyrannosaurus WxtYXVar4sgInHp7YUpTzOjdUw1Ww0x8  
reservists QDidoX6BN1MDTi0QwA6Vt82L9Rb64cm3  
atrophy's mSpCwP9VgcGRn1SCD8R9bb9cPBl2yqkW  
bolt's 726RB3lt2RmeCtbWEQ8lhUAxVBJfepy0  
Klondikes wVh3ILxQAsKg8WNnFHp8GxtnSu213GbR
```

(The -n flag allows us to specify how many lines to print from the start of the file. We can use the `tail` command to look at the last n lines of a file)

We know the password is next to the word "millionth" in the file. We can look for this pattern by using the `grep` command

```
bandit7@bandit:~$ grep millionth data.txt   
millionth cvX2JJa4CFALtqS87jk27qwqGhBM9plV
```

We have found the password for the next level !!

Logout of the current session and use the password of user bandit8 to access the next level

```
> ssh bandit8@bandit.labs.overthewire.org -p 2220  
This is a OverTheWire game server. More information on http://www.overthewire.org/wargames

bandit8@bandit.labs.overthewire.org's password: cvX2JJa4CFALtqS87jk27qwqGhBM9plV
```