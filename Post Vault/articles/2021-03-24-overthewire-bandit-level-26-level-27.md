---
title: 'OverTheWire: Bandit Level 26 → Level 27'
description: 'https://overthewire.org/wargames/bandit/bandit27.html'
date: '2021-03-24 10:57:21 +0530'
categories: [Security, OverTheWire]
tags: [overthewire, ctf, security, linux]
published: true
img_path: /assets/
---

![OverTheWire Banner](images/overthewire-banner.png)

### Level Goal

> Good job getting a shell! Now hurry and grab the password for bandit27!

### Commands you may need to solve this level

> ls

```
> whatis ls
ls (1)               - list directory contents
```

### Helpful Reading Material

[How to Use SUID, SGID, and Sticky Bits on Linux](https://www.howtogeek.com/656646/how-to-use-suid-sgid-and-sticky-bits-on-linux/)

### Solution

If at the end of the last level you logged out perform the same steps as the last level to login back as bandit26 but this time from our system.

Make the terminal height-wise short so that the more command will enter interactive mode

```
> ssh bandit26@bandit.labs.overthewire.org -p 2220

This is a OverTheWire game server. More information on http://www.overthewire.org/wargames

bandit26@bandit.labs.overthewire.org's password: 5czgV9L3Xx8JPOyRbXh6lQbmIOWvPT6Z
```

![More Editor](images/bandit-26-27/more-command.png)

Press "v" to open the file in a text editor (Default vim) then enter the commands below to start a bash shell.

![Set Default Shell](images/bandit-26-27/set-default-shell.png)
![Launch Shell](images/bandit-26-27/start-default-shell.png)
![Access Bandit26](images/bandit-26-27/access-bandit26.png)

If the above steps were performed properly you should have a bash shell and be logged in as bandit26.

**Note:** If the above steps did not make sense refer to my previous article where I have explained the process in detail.

Let's see if there are any files in the current working directory

```
bandit26@bandit:~$ ls  
bandit27-do  text.txt

bandit26@bandit:~$ ls -l  
total 12  
-rwsr-x--- 1 bandit27 bandit26 7296 May  7  2020 bandit27-do  
-rw-r----- 1 bandit26 bandit26  258 May  7  2020 text.txt
```

We see a binary file called "bandit27-do". If we look at its properties we see that the file is owned by bandit27 and the SUID bit of the file is set as well. This means that using the binary if we run any other command that command will have the same permissions as the owner of the binary (in this case the commands will have bandit27 permissions)

So let us try to cat the content of the password file of bandit27 using the binary.

```
bandit26@bandit:~$ ./bandit27-do cat /etc/bandit_pass/bandit27  
3ba3118a22e93127a4ed485be72ef5ea
```

There we go we have the password for the next level !!!

Logout of the current session and login into the next level as banddit27

```
> ssh bandit27@bandit.labs.overthewire.org -p 2220

This is a OverTheWire game server. More information on http://www.overthewire.org/wargames

bandit27@bandit.labs.overthewire.org's password: 3ba3118a22e93127a4ed485be72ef5ea
```