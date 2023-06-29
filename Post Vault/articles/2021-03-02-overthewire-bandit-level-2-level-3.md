---
title: 'OverTheWire: Bandit Level 2 → Level 3'
description: 'https://overthewire.org/wargames/bandit/bandit3.html'
date: '2021-03-02 12:32:00 +0530'
categories: [Security, OverTheWire]
tags: [overthewire, bandit, ctf, security, linux]
published: true
img_path: /assets/
image: images/overthewire-banner.png
---

## Level Goal

> The password for the next level is stored in a file called **spaces in this filename** located in the home directory

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

[How to Read a Filename with Spaces in Linux](https://linoxide.com/linux-command/how-to-read-filename-with-spaces-in-linux/)

[command line - How to access files/directories with spaces in the name? - Ask Ubuntu](https://askubuntu.com/questions/516772/how-to-access-files-directories-with-spaces-in-the-name)

## Solution

View the files that are present in the current working directory using the `ls` command

```
bandit2@bandit:~$ ls  
spaces in this filename
```

View the content of the file named `spaces in this filename` using the `cat` command

**Note:** We command directly open this file as there are spaces in the filename. The spaces in the name can be escaped using `\`, another approach is to enclose the filename in `".."` (quotes)

**Note:** The name of any file on the system can be auto-completed using the `Tab` key.

```
bandit2@bandit:~$ cat spaces\ in\ this\ filename  
UmHadQclWmgdLOKQ3YNgjWxGoRMb5luK

bandit2@bandit:~$ cat "spaces in this filename"  
UmHadQclWmgdLOKQ3YNgjWxGoRMb5luK
```

We have found the password for the next level !!

Logout of the current session and use the password of user bandit3 to access the next level

```
> ssh bandit3@bandit.labs.overthewire.org -p 2220  
This is a OverTheWire game server. More information on http://www.overthewire.org/wargames

bandit3@bandit.labs.overthewire.org's password: UmHadQclWmgdLOKQ3YNgjWxGoRMb5luK
```