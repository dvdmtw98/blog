---
title: 'OverTheWire: Bandit Level 13 → Level 14'
description: [OverTheWire - Bandit](https://overthewire.org/wargames/bandit/bandit14.html)'
date: '2021-03-06 09:15:28 +0530'
categories: [Security, OverTheWire]
tags: [overthewire, bandit, ctf, security, linux]
published: true
img_path: /assets/
image: images/overthewire-banner.png
---

## Level Goal

> The password for the next level is stored in **/etc/bandit_pass/bandit14 and can only be read by user bandit14**. For this level, you don't get the next password, but you get a private SSH key that can be used to log into the next level. **Note:** **localhost** is a hostname that refers to the machine you are working on

## Commands you may need to solve this level

> ssh, telnet, nc, openssl, s_client, nmap

## Helpful Reading Material

[SSH/OpenSSH/Keys - Community Help Wiki](https://help.ubuntu.com/community/SSH/OpenSSH/Keys)

[How to use SSH keys for authentication - UpCloud](https://upcloud.com/community/tutorials/use-ssh-keys-authentication/)

## Solution

View the contents of the current working directory

```
bandit13@bandit:~$ ls  
sshkey.private
```

We have an SSH private key. We can use the SSH command with the "-i" flag to use the private key

```
bandit13@bandit:~$ ssh -i sshkey.private bandit14@localhost
```

(If asked for fingerprint confirmation type "yes")

![Login to Level 14|460](images/bandit-13-14/level-14-accessed.png)

We have logged in as bandit14 we can confirm this by looking at your prompt

```
bandit14@bandit:~$
```

Get the password for the current user

```
bandit14@bandit:~$ cat /etc/bandit_pass/bandit14  
4wcYUJFw0k0XLShlDzztnTBHiqxU3b3e
```

We have found the password for bandit14 !!

Logout of the current (bandit14) session then log out of the bandit13 session and use the password of user bandit14 to access the next level

```
> ssh bandit14@bandit.labs.overthewire.org -p 2220  
This is a OverTheWire game server. More information on http://www.overthewire.org/wargames

bandit14@bandit.labs.overthewire.org's password: 4wcYUJFw0k0XLShlDzztnTBHiqxU3b3e
```