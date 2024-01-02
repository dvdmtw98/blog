---
title: 'OverTheWire: Bandit Level 19 → Level 20'
description: '[OverTheWire - Bandit](https://overthewire.org/wargames/bandit/bandit20.html)'
date: '2021-03-09 03:49:59 +0530'
categories: [Security, OverTheWire]
tags: [overthewire, bandit, ctf, security, linux]
published: true
img_path: /assets/
image: images/overthewire-banner.png
---

## Level Goal

> To gain access to the next level, you should use the setuid binary in the homedirectory. Execute it without arguments to find out how to use it. The password for this level can be found in the usual place (/etc/bandit_pass), after you have used the setuid binary.

## Helpful Reading Material

[Setuid - Wikipedia](https://en.wikipedia.org/wiki/Setuid)

[So you want to know what "ls -l" does… \| by Jenn Ogden \| Medium](https://medium.com/@jennogden95/so-you-want-to-know-what-ls-c-does-864bd4708be8)

## Solution

We have been told there is a binary file that is present in the home directory which somehow can help us to access the password of bandit20. Let's have a look at the binary

```
bandit19@bandit:~$ ls  
bandit20-do

bandit19@bandit:~$ ls -l  
total 8  
-rwsr-x--- 1 bandit20 bandit19 7296 May  7  2020 bandit20-do
```

We can see that the file is called `bandit20-do` and when we list the details of the file we can see that the binary file can be executed by the current user (bandit19) and it is owned by bandit20

To run an executable file we just need to specify its name along with the location. The file is in the current working directory so we can use `./<filename>` to access the file

```
bandit19@bandit:~$ ./bandit20-do  
Run a command as another user.  
  Example: ./bandit20-do id
```

The help menu of the binary tells us that it can be executed as another user. Let's view an example of running a command as another user using the id command

```
bandit19@bandit:~$ id  
uid=11019(bandit19) gid=11019(bandit19) groups=11019(bandit19)

bandit19@bandit:~$ ./bandit20-do id  
uid=11019(bandit19) gid=11019(bandit19) euid=11020(bandit20) groups=11019(bandit19)
```

We observe that when we use the binary file we are assigned the UID for bandit20 as well which means we can run commands as if we are bandit20

Now that we know we can run commands as bandit20 so let's use the binary to access the password of user bandit20

```
bandit19@bandit:~$ ./bandit20-do cat /etc/bandit_pass/bandit20  
GbKksEFF4yrVs6il55v6gwY5aVje5f0j
```

We have found the password for the next level !!!

Logout of the current session and start the next level using bandit20's password

```
> ssh bandit20@bandit.labs.overthewire.org -p 2220
This is a OverTheWire game server. More information on http://www.overthewire.org/wargames

bandit20@bandit.labs.overthewire.org's password: GbKksEFF4yrVs6il55v6gwY5aVje5f0j
```