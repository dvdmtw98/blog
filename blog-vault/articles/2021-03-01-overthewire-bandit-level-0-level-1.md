---
title: "OverTheWire: Bandit Level 0 → Level 1"
description: "The Bandit wargames are aimed at absolute beginners. It will teach the basics needed to be able to play other wargames."
date: 2021-03-01 12:31:28 +0530
categories:
  - Security
  - OverTheWire
tags:
  - overthewire
  - bandit
  - ctf
  - security
  - linux
published: true
media_subpath: /assets/
---

![banner-image|640](images/bandit-0/overthewire-banner.png)

## Level Goal

> The password for the next level is stored in a file called **readme** located in the home directory. Use this password to log into bandit1 using SSH. Whenever you find a password for a level, use SSH (on port 2220) to log into that level and continue the game.

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

[13 Basic Cat Command Examples in Linux Terminal](https://www.tecmint.com/13-basic-cat-command-examples-in-linux/)

[15 Basic 'ls' Command Examples for Linux Beginners](https://www.tecmint.com/15-basic-ls-command-examples-in-linux/)

[15 'pwd' (Print Working Directory) Command Examples in Linux](https://www.tecmint.com/pwd-command-examples/)

## Solution

View the files that are present in the current working directory using the `ls` command  
(The "pwd" command can be used to view the current working directory)

```bash
bandit0@bandit:~$ ls  
readme
```

We see there is a file named `readme` to view the contents of this file we can use the `cat` command.

```bash
bandit0@bandit:~$ cat readme   
boJ9jbbUNNfktd78OOpsqOltutMc3MY1
```

We have found the password for the next level !!


Use the password found above to log in as bandit1 and access the next level

```bash
> ssh bandit1@bandit.labs.overthewire.org -p 2220  
This is a OverTheWire game server. More information on http://www.overthewire.org/wargames

bandit1@bandit.labs.overthewire.org's password: boJ9jbbUNNfktd78OOpsqOltutMc3MY1
```
