---
title: 'OverTheWire: Bandit Level 17 → Level 18'
description: 'https://overthewire.org/wargames/bandit/bandit18.html'
date: '2021-03-09 03:48:30 +0530'
categories: [Security, OverTheWire]
tags: [overthewire, bandit, ctf, security, linux]
published: true
img_path: /assets/
image: images/overthewire-banner.png
---

## Level Goal

> There are 2 files in the homedirectory: **passwords.old and passwords.new**. The password for the next level is in **passwords.new** and is the only line that has been changed between **passwords.old and passwords.new**  
> **NOTE: if you have solved this level and see 'Byebye!' when trying to log into bandit18, this is related to the next level, bandit19**

## Commands you may need to solve this level

> cat, grep, ls, diff

```
> whatis cat  
cat (1)              - concatenate files and print on the standard output

> whatis grep  
grep (1)             - print lines that match patterns

> whatis ls  
ls (1)               - list directory contents

> whatis diff  
diff (1)             - list different between files
```

**Note:** Not all commands need to be used to complete level

## Helpful Reading Material

[Diff Command in Linux \| Linuxize](https://linuxize.com/post/diff-command-in-linux/)

## Solution

View the files that are present in the home directory

```
bandit17@bandit:~$ ls  
passwords.new  passwords.old
```

We know that both the files differ in only one line and that line consists of the password that we require. We can view the changes that have been made in files using the `diff` command

```
bandit17@bandit:~$ diff passwords.old passwords.new  
42c42  
< w0Yfolrc5bwjS4qw5mq1nnQi6mF03bii  
---  
> kfBf3eYk5BPBRzwjqutbbfE887SVc5Yd
```

**Note:** The `<` sign represents the lines that have been removed and the `>` sign represents the lines that have been added in its place

The line after the `>` sign is the password for the next level

Logout of the current session and login into the next level using the password for bandit18

```
> ssh bandit18@bandit.labs.overthewire.org -p 2220
This is a OverTheWire game server. More information on http://www.overthewire.org/wargames

bandit18@bandit.labs.overthewire.org's password: kfBf3eYk5BPBRzwjqutbbfE887SVc5Yd
.
.
.
Byebye !
Connection to bandit.labs.overthewire.org closed.
```

**Note:** When we try to log in we are going to get kicked out saying "Bye-bye!". This is normal, this is part of the challenge for the next level