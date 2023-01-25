---
title: 'OverTheWire: Bandit Level 22 → Level 23'
description: 'https://overthewire.org/wargames/bandit/bandit23.html'
date: '2021-03-10 05:05:42 +0530'
categories: [Security, OverTheWire]
tags: [overthewire, ctf, security, linux]
published: true
img_path: /assets/
---

![OverTheWire Banner](images/overthewire-banner.png)

### Level Goal

> A program is running automatically at regular intervals from **cron**, the time-based job scheduler. Look in **/etc/cron.d/** for the configuration and see what command is being executed.  
> **NOTE:** Looking at shell scripts written by other people is a very useful skill. The script for this level is intentionally made easy to read. If you are having problems understanding what it does, try executing it to see the debug information it prints.

### Commands you may need to solve this level

> cron, crontab, crontab(5) (use "man 5 crontab" to access this)

```
> whatis cron  
cron (8)         - daemon to execute scheduled commands (Vixie Cron)

> whatis crontab  
crontab (1)      - maintain crontab files for individual users (Vixie Cron)  
crontab (5)      - tables for driving cron
```

### Helpful Reading Material

[Linux/Mac Tutorial: Cron Jobs - How to Schedule Commands with crontab - YouTube](https://www.youtube.com/watch?v=QZJ1drMQz1A)

[Linux crontab command help and examples](https://www.computerhope.com/unix/ucrontab.htm)

[11 Cron Scheduling Task Examples in Linux](https://www.tecmint.com/11-cron-scheduling-task-examples-in-linux/)

### Solution

Since we know there is an task that is being executed by cron lets have an look at all the cron jobs on the system

```
bandit22@bandit:~$ ls /etc/cron.d/  
cronjob_bandit15_root  cronjob_bandit22  cronjob_bandit24  
cronjob_bandit17_root  cronjob_bandit23  cronjob_bandit25_root
```

Since we require the password for bandit23 the task that we are looking for should be `cronjob_bandit23`

```
bandit22@bandit:~$ cat /etc/cron.d/cronjob_bandit23
@reboot bandit23 /usr/bin/cronjob_bandit23.sh  &> /dev/null
* * * * * bandit23 /usr/bin/cronjob_bandit23.sh  &> /dev/null
```

When we look at the cron job for bandit23 we see that there is an shell script that is being executed every second

_(For detailed information on the syntax of cron jobs refer the attached resources)_

Lets have a look at the contents of the script and try to understand what is it trying to perform

```
bandit22@bandit:~$ cat /usr/bin/cronjob_bandit23.sh
#!/bin/bash

myname=$(whoami)
mytarget=$(echo I am user $myname | md5sum | cut -d ' ' -f 1)

echo "Copying passwordfile /etc/bandit_pass/$myname to /tmp/$mytarget"

cat /etc/bandit_pass/$myname > /tmp/$mytarget
```

Lets break down the script line by line

*   The output of `whoami` command is getting saved in a variable called `myname` (Since this script is being executed for bandit23 the output of `whoami` will be `bandit23` which is saved in the `myname` variable)
*   Next the sentence "I am user bandit23" is passed to the `md5sum` command which will calculate the md5sum of the given string and lastly using `cut` command the first field from the output of the `md5sum` command is selected and saved in the variable `mytarget`
*   Then an file is being created in the /tmp directory with the name of the file being same as the value of "mytarget"
*   And finally the password of bandit23 is being saved into that file

So looking at this script we can say that our goal is to find the value of "mytarget". Since we know that the value of "myname" is bandit23 lets see if we can able to generate the value of "mytarget".

```
bandit22@bandit:~$ echo "I am user bandit23" | md5sum | cut -d ' ' -f 1  
8ca319486bfbbc3663ea0fbe81326349
```

We have got the value of "mytarget" that the script creates for bandit23. Now that we have the value lets get the password for bandit23

View the content of the file `8ca319486bfbbc3663ea0fbe81326349` that is present in the `/tmp` directory

```
bandit22@bandit:~$ cat /tmp/8ca319486bfbbc3663ea0fbe81326349  
jc1udXuA1tiHqjIsL8yaapX5XIAI6i0n
```

And there we go we have the password for the next level !!!

Logout of the current session and start next level as bandit23

```
> ssh bandit23@bandit.labs.overthewire.org -p 2220
This is a OverTheWire game server. More information on http://www.overthewire.org/wargames

bandit23@bandit.labs.overthewire.org's password: jc1udXuA1tiHqjIsL8yaapX5XIAI6i0n
```