---
title: "OverTheWire: Bandit Level 18 → Level 19"
description: "The Bandit wargames are aimed at absolute beginners. It will teach the basics needed to be able to play other wargames."
date: 2021-03-09 03:49:28 +0530
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

> The password for the next level is stored in a file **readme** in the homedirectory. Unfortunately, someone has modified **.bashrc** to log you out when you log in with SSH.

## Commands you may need to solve this level

> ssh, ls, cat

```
> whatis ssh  
ssh (1)              - OpenSSH remote login client

> whatis ls  
ls (1)               - list directory contents

> whatis cat  
cat (1)              - concatenate files and print on the standard output
```

**Note:** Not all commands are required to complete the level

## Solution

From reading the question we understand that we cannot log in directly as the default shell "Bash" has been modified to not allow any login using SSH. So we need to use a shell other than bash to access the system.

The details of all the shells that are available on a system are stored under `/etc/shells`. Let's look at the file on our system to get an idea of what are the different shells that could be present on the target (Only on Linux)

```
> cat /etc/shells  
# /etc/shells: valid login shells  
/bin/sh  
/bin/bash  
/usr/bin/bash  
/bin/rbash  
/usr/bin/rbash  
/bin/dash  
/usr/bin/dash  
/usr/bin/tmux  
/usr/bin/screen
```

**Note:** Each line in the file represents a shell that is present in the system

Now that we have an idea of some of the shells that should be preset on all systems we can try logging in with them via SSH. The `-t` flag of the SSH command is used to specify the shell to be used to login into the system.

```
$ ssh bandit18@bandit.labs.overthewire.org -p 2220 -t "/bin/sh"

This is a OverTheWire game server. More information on http://www.overthewire.org/wargames

bandit18@bandit.labs.overthewire.org's password: kfBf3eYk5BPBRzwjqutbbfE887SVc5Yd
$
```

We have managed to log in successfully using the "sh" shell

Find the password that is present in the readme file

```
$ ls  
readme

$ cat readme  
IueksS7Ubh8G3DCwVzrTd8rAVOwq3M5x
```

We have got the password for the next level !!!

Logout of the current session and login into the next level using the password for bandit19

```
> ssh bandit19@bandit.labs.overthewire.org -p 2220
This is a OverTheWire game server. More information on http://www.overthewire.org/wargames

bandit19@bandit.labs.overthewire.org's password: IueksS7Ubh8G3DCwVzrTd8rAVOwq3M5x
```