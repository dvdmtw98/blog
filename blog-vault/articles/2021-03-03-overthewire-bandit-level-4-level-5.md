---
categories:
- Security
- OverTheWire
date: 2021-03-03 04:52:01 +0530
description: '[OverTheWire - Bandit](https://overthewire.org/wargames/bandit/bandit5.html)'
img_path: /assets/
published: true
tags:
- overthewire
- bandit
- ctf
- security
- linux
title: 'OverTheWire: Bandit Level 4 → Level 5'
---

![banner-image|640](images/overthewire-banner.png)

## Level Goal

> The password for the next level is stored in the only human-readable file in the **inhere** directory.   
> Tip: if your terminal is messed up, try the "reset" command.

## Commands you may need to solve this level

> ls, cd, cat, file, du, find

```
> whatis ls                                                                           
ls (1)          - list directory contents  

> whatis cd  
cd  (1)         - change working directory  

> whatis cat                                                                                                       
cat (1)         - concatenate files and print on the standard output  

> whatis file  
file (1)        - determine file type  

> whatis du    
du (1)          - estimate file space usage  

> whatis find  
find (1)        - search for files in a directory hierarchy
```

**Note:** All commands don't have to be used to complete level

## Helpful Reading Material

[Linux File Command - javatpoint](https://www.javatpoint.com/linux-file)

[Linux File Globbing - javatpoint](https://www.javatpoint.com/linux-file-globbing)

## Solution

View the files that are present in the current working directory using the `ls` command

```
bandit4@bandit:~$ ls  
inhere
```

Move into the `inhere/` directory. This can be done using the `cd` command

```
bandit4@bandit:~$ cd inhere/
```

View files that are in the directory using the `ls` command

```
bandit4@bandit:~/inhere$ ls  
-file00  -file01  -file02  -file03  -file04  -file05  -file06  -file07  
-file08  -file09
```

We know we have to find a file whose content is in Human Readable format. This check can be performed using the `file` command. File command returns the type of data that is found in the file

```bash
bandit4@bandit:~/inhere$ file ./*  
./-file00: data  
./-file01: data  
./-file02: data  
./-file03: data  
./-file04: data  
./-file05: data  
./-file06: data  
./-file07: ASCII text  
./-file08: data  
./-file09: data
```

**Note:** The `*` here means to look for all files in the directory. For more information on globbing refer to the attached reference resources

View the content of `-file07` using the `cat` command

```
bandit4@bandit:~/inhere$ cat ./-file07  
koReBOKuIDDepwhWk7jZC0RTdopnAYKh
```

We have found the password for the next level !!

Logout of the current session and use the password of user bandit5 to access the next level

```
> ssh bandit5@bandit.labs.overthewire.org -p 2220  
This is a OverTheWire game server. More information on http://www.overthewire.org/wargames

bandit5@bandit.labs.overthewire.org's password: koReBOKuIDDepwhWk7jZC0RTdopnAYKh
```