---
title: 'OverTheWire: Bandit Level 21 → Level 22'
description: 'https://overthewire.org/wargames/bandit/bandit22.html'
date: '2021-03-10 05:04:40 +0530'
categories: [Security, OverTheWire]
tags: [overthewire, bandit, ctf, security, linux]
published: true
img_path: /assets/
image: images/overthewire-banner.png
---

## Level Goal

> A program is running automatically at regular intervals from **cron**, the time-based job scheduler. Look in **/etc/cron.d/** for the configuration and see what command is being executed.

## Commands you may need to solve this level

> cron, crontab, crontab(5) (use "man 5 crontab" to access this)

```
> whatis cron  
cron (8)         - daemon to execute scheduled commands (Vixie Cron)

> whatis crontab  
crontab (1)      - maintain crontab files for individual users (Vixie Cron)  
crontab (5)      - tables for driving cron
```

## Helpful Reading Material

[Linux/Mac Tutorial: Cron Jobs - How to Schedule Commands with crontab - YouTube](https://www.youtube.com/watch?v=QZJ1drMQz1A)

[Linux crontab command help and examples](https://www.computerhope.com/unix/ucrontab.htm)

[11 Cron Scheduling Task Examples in Linux](https://www.tecmint.com/11-cron-scheduling-task-examples-in-linux/)

## Solution

Since we know there is a task that is being executed by cron let's have a look at all the cron jobs on the system

```
bandit21@bandit:~$ ls /etc/cron.d/  
cronjob_bandit15_root  cronjob_bandit22  cronjob_bandit24  
cronjob_bandit17_root  cronjob_bandit23  cronjob_bandit25_root
```

Since we require the password for bandit22 the task that we are looking for should be `cronjob_bandit22`

```
bandit21@bandit:~$ cat /etc/cron.d/cronjob_bandit22
@reboot bandit22 /usr/bin/cronjob_bandit22.sh &> /dev/null
* * * * * bandit22 /usr/bin/cronjob_bandit22.sh &> /dev/null
```

When we look at the cron job for bandit22 we see that there is a shell script that is being executed every second

_(For detailed information on the syntax of cron jobs refer to the attached resources)_

Let's have a look at the contents of the script and try to understand what is it trying to perform

```
bandit21@bandit:~$ cat /usr/bin/cronjob_bandit22.sh
#!/bin/bash
chmod 644 /tmp/t7O6lds9S0RqQh9aMcz6ShpAoZKF7fgv
cat /etc/bandit_pass/bandit22 > /tmp/t7O6lds9S0RqQh9aMcz6ShpAoZKF7fgv
```

When we look at the script we see that it is creating a file called `t7O6lds9S0RqQh9aMcz6ShpAoZKF7fgv` in the `/tmp` directory and then saving the password for the next level into that file.

Let's view the content of the file that is created by the script

```
bandit21@bandit:~$ cat /tmp/t7O6lds9S0RqQh9aMcz6ShpAoZKF7fgv  
Yk7owGAcWjwMVRwrTesJEwB7WVOiILLI
```

And there we go we have the password for the next level !!!

Logout of the current session and start the next level as bandit22

```
> ssh bandit22@bandit.labs.overthewire.org -p 2220
This is a OverTheWire game server. More information on http://www.overthewire.org/wargames

bandit22@bandit.labs.overthewire.org's password: Yk7owGAcWjwMVRwrTesJEwB7WVOiILLI
```