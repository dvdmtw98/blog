---
title: 'OverTheWire: Bandit Level 1 → Level 2'
description: 'https://overthewire.org/wargames/bandit/bandit2.html'
date: '2021-03-02 04:14:02 +0530'
categories: [Security, OverTheWire]
tags: [overthewire, ctf, security, linux]
published: true
img_path: /assets/
image: images/overthewire-banner.png
---

### Level Goal

> The password for the next level is stored in a file called-located in the home directory

### Commands you may need to solve this level

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

### Helpful Reading Material

[Linux - How to open a "-" dashed filename using terminal? - Stack Overflow](https://stackoverflow.com/questions/42187323/how-to-open-a-dashed-filename-using-terminal)

[Input Output & Error Redirection in Linux [Beginner's Guide]](https://linuxhandbook.com/redirection-linux/)

### Solution

View the files that are present in the current working directory using the `ls` command

```
bandit1@bandit:~$ ls  
-
```

We can view the content of the file named `-` using the `cat` command

**Note:** Directly specifying the filename as shown in the previous level is not going to work as `-` is a special character on Linux that is used to denote Standard Input/ Standard Output (STDIN/ STDOUT). We have to use the concept of redirection or specify the absolute path to the file to access it.

```
bandit1@bandit:~$ cat < -  
CV1DtqXWVFXTvM2F0k09SHz0YwRINYA9

bandit1@bandit:~$ cat ./-  
CV1DtqXWVFXTvM2F0k09SHz0YwRINYA9
```

We have found the password for the next level !!

To access the next level log out of the current session. This can be done by typing `exit` or using `Ctrl + D`

Use the password found above of user bandit2 to access the next level

```
> ssh bandit2@bandit.labs.overthewire.org -p 2220  
This is a OverTheWire game server. More information on http://www.overthewire.org/wargames

bandit2@bandit.labs.overthewire.org's password: CV1DtqXWVFXTvM2F0k09SHz0YwRINYA9
```