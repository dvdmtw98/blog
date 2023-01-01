---
title: 'OverTheWire: Bandit Level 6 → Level 7'
description: 'https://overthewire.org/wargames/bandit/bandit7.html'
date: '2021-03-04 03:44:29 +0530'
categories: [Security, OverTheWire]
tags: [overthewire, ctf, security, linux]
img_path: /assets/
---

![OverTheWire Banner](images/overthewire-banner.png)

### Level Goal

> The password for the next level is stored **somewhere on the server** and has all of the following properties:  
> owned by user bandit7  
> owned by group bandit6  
> 33 bytes in size  

### Commands you may need to solve this level

> ls, cd, cat, file, du, find, grep

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

[35 Practical Examples of Linux Find Command](https://www.tecmint.com/35-practical-examples-of-linux-find-command/)

[An Introduction to Linux I/O Redirection \| DigitalOcean](https://www.digitalocean.com/community/tutorials/an-introduction-to-linux-i-o-redirection)

[Site Unreachable](https://linuxhint.com/what_is_dev_null/)

### Solution

Since we don't know where the file is we will have to search the entire server. We know some properties about the file that we can use to try and locate the file. Similar to the previous level we can use the `find` command for this task

```
bandit6@bandit:~$ find / -type f -user bandit7 -group bandit6 -size 33c
```

### Command Explanation

*   **/ :** Search the entire server (/ is the root directory on Linux similar to the C:/ Drive on Windows)
*   **-type f :** Search only for files (Exclude Directories)
*   **-user bandit7 :** Search for files which are owned by user bandit7
*   **-group bandit6 :** Search for files that belongs to the group bandit6
*   **-size 33c :** Look for files that are exactly 33 bytes in size (Find uses "c" to represent size in bytes)

This command alone is sufficient to get the result that we are looking for but since we are scanning the entire server we are going to encounter files what we do not have permission to access and which are going to show errors.

```
bandit6@bandit:~$ find / -type f -user bandit7 -group bandit6 -size 33c  
find: '/root': Permission denied  
find: '/home/bandit28-git': Permission denied  
find: '/home/bandit30-git': Permission denied  
find: '/home/bandit5/inhere': Permission denied  
find: '/home/bandit27-git': Permission denied  
find: '/home/bandit29-git': Permission denied  
find: '/home/bandit31-git': Permission denied  
find: '/lost+found': Permission denied  
find: '/etc/ssl/private': Permission denied  
find: '/etc/polkit-1/localauthority': Permission denied  
find: '/etc/lvm/archive': Permission denied  
find: '/etc/lvm/backup': Permission denied  
find: '/sys/fs/pstore': Permission denied
```

These errors can be filtered out by sending the error stream denoted by number 2 to `/dev/null` . NULL is a special device on Linux which destroys all that data that is send to it.

```
bandit6@bandit:~$ find / -type f -user bandit7 -group bandit6 -size 33c 2> /dev/null  
/var/lib/dpkg/info/bandit7.password
```

(For additional information on these concepts refer the attached resources)

Not that we have found the file lets view its contents

```
bandit6@bandit:~$ cat /var/lib/dpkg/info/bandit7.password  
HKBPTKQnIay4Fw76bEy8PVxKEDQRKTzs
```

We have found the password for the next level !!

Logout of current session and use password of user bandit7 to access next level

```
> ssh bandit7@bandit.labs.overthewire.org -p 2220  
This is a OverTheWire game server. More information on http://www.overthewire.org/wargames

bandit7@bandit.labs.overthewire.org's password: HKBPTKQnIay4Fw76bEy8PVxKEDQRKTzs
```