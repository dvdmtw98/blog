---
title: 'OverTheWire: Bandit Level 8 → Level 9'
description: 'https://overthewire.org/wargames/bandit/bandit9.html'
date: '2021-03-05 05:00:25 +0530'
categories: [Security, OverTheWire]
tags: [overthewire, ctf, security, linux]
img_path: /assets/
---

![OverTheWire Banner](images/overthewire-banner.png)

### Level Goal

> The password for the next level is stored in the file **data.txt** and is the only line of text that occurs only once

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

[Learn Piping and Redirection - Linux Tutorial](https://ryanstutorials.net/linuxtutorial/piping.php)

[Back to Basics: Sort and Uniq \| Linux Journal](https://www.linuxjournal.com/content/back-basics-sort-and-uniq)

### Solution

View the contents of the current working directory

```
bandit8@bandit:~$ ls  
data.txt
```

Peek at the data that is present in the file. This can be achieved using the `head` command

```
bandit8@bandit:~$ head -n 10 data.txt   
VkBAEWyIibVkeURZV5mowiGg6i3m7Be0  
zdd2ctVveROGeiS2WE3TeLZMeL5jL7iM  
sYSokIATVvFUKU4sAHTtMarfjlZWWj5i  
ySvsTwlMgnUF0n86Fgmn2TNjkSOlrV72  
NLWvtQvL7EaqBNx2x4eznRlQONULlCYZ  
LfrBHfAh0pP9bgGAZP4QrVkut3pysAYC  
U0NYdD3wHZKpfEg9qGQOLJimAJy6qxhS  
flyKxCbHB8uLTaIB5LXqQNuJj3yj00eh  
TThRArdF2ZEXMO47TIYkyPPLtvzzLcDf  
cIPbot7oYveUPNxDMhv1hiri50CqpkTG
```

(The -n flag allows us to specify how many lines to print from start of the file. We can use the `tail` command to look at the last n lines of a file)

Since we know there are repeating lines in the file. We can use `uniq` command with the `-u` flag to print the unique line. Uniq command expects the repeating (similar) lines to be next to each other (adjacent) so we need to sort our data before we can find the unique line.

For sorting we can use the `sort` command which will sort the data in the file line wise. Finally we can combine all these commands together into an one liner using the `|` (pipe) operator

(For more reference on these commands refer the attached websites)

```
bandit8@bandit:~$ cat data.txt | sort | uniq -u  
UsvVyFSfZZWbi6wgC7dAFyFuR6jQQUhR
```

**Note:** The `cat` command is used to read the data from the file which is then passed as input to the next command in line using pipes

We have found the password for the next level !!

Logout of current session and use password of user bandit9 to access next level

```
> ssh bandit9@bandit.labs.overthewire.org -p 2220  
This is a OverTheWire game server. More information on http://www.overthewire.org/wargames

bandit9@bandit.labs.overthewire.org's password: UsvVyFSfZZWbi6wgC7dAFyFuR6jQQUhR
```