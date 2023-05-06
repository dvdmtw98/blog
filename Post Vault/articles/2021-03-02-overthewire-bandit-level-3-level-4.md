---
title: 'OverTheWire: Bandit Level 3 → Level 4'
description: 'https://overthewire.org/wargames/bandit/bandit4.html'
date: '2021-03-02 16:53:43 +0530'
categories: [Security, OverTheWire]
tags: [overthewire, ctf, security, linux]
published: true
img_path: /assets/
---

![OverTheWire Banner](images/overthewire-banner.png)

### Level Goal

> The password for the next level is stored in a hidden file in the **inhere** directory.

### Commands you may need to solve this level

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

### Helpful Reading Material

[15 Basic 'ls' Command Examples for Linux Beginners](https://www.tecmint.com/15-basic-ls-command-examples-in-linux/)

### Solution

View the files that are present in the current working directory using the `ls` command

```
bandit3@bandit:~$ ls  
inhere
```

Move into the `inhere/` directory. This can be done using the `cd` command

```
bandit3@bandit:~$ cd inhere/
```

View files that are in the directory using the `ls` command. Since we know the file is hidden we have to use the `-a` flag to view hidden files.

(For more information on the `ls` command and its various flags refer to `man ls` or `ls --help` )

```
bandit3@bandit:~/inhere$ ls -a  
.  ..  .hidden
```

View the content of the `.hidden` file using the `cat` command

```
bandit3@bandit:~/inhere$ cat .hidden  
pIwrPrtPN36QITSp3EQaw936yaFoFgAB
```

We have found the password for the next level !!

Logout of the current session and use the password of user bandit4 to access the next level

```
> ssh bandit4@bandit.labs.overthewire.org -p 2220  
This is a OverTheWire game server. More information on http://www.overthewire.org/wargames

bandit4@bandit.labs.overthewire.org's password: pIwrPrtPN36QITSp3EQaw936yaFoFgAB
```