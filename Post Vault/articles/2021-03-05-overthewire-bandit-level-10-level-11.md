---
title: 'OverTheWire: Bandit Level 10 → Level 11'
description: 'https://overthewire.org/wargames/bandit/bandit11.html'
date: '2021-03-05 05:00:59 +0530'
categories: [Security, OverTheWire]
tags: [overthewire, ctf, security, linux]
published: true
img_path: /assets/
---

![OverTheWire Banner](images/overthewire-banner.png)

### Level Goal

> The password for the next level is stored in the file **data.txt**, which contains base64 encoded data

### Commands you may need to solve this level

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

### Helpful Reading Material

[Base64 - Wikipedia](https://en.wikipedia.org/wiki/Base64)

[Bash base64 encode and decode](https://linuxhint.com/bash_base64_encode_decode/)

### Solution

View the contents of the current working directory

```
bandit10@bandit:~$ ls  
data.txt
```

View the data that is present in the file

```
bandit10@bandit:~$ cat data.txt  
VGhlIHBhc3N3b3JkIGlzIElGdWt3S0dzRlc4TU9xM0lSRnFyeEUxaHhUTkViVVBSCg==
```

Looking at the content it looks like an string of random characters but from the question we know that the data is base64 encoded. We can decode this data using the `base64` command that is present on Unix systems. The `-d` flag is used to decode the data

_(For detailed information on base64 encoding refer the attached article)_

```
bandit10@bandit:~$ cat data.txt | base64 -d  
The password is IFukwKGsFW8MOq3IRFqrxE1hxTNEbUPR
```

We have found the password for the next level !!

Logout of current session and use password of user bandit11 to access next level

```
> ssh bandit11@bandit.labs.overthewire.org -p 2220  
This is a OverTheWire game server. More information on http://www.overthewire.org/wargames

bandit11@bandit.labs.overthewire.org's password: IFukwKGsFW8MOq3IRFqrxE1hxTNEbUPR
```