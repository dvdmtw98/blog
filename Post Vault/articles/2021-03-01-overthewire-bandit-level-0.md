---
title: 'OverTheWire: Bandit Level 0'
description: 'https://overthewire.org/wargames/bandit/bandit0.html'
date: '2021-03-01 10:04:29 +0530'
categories: [Security, OverTheWire]
tags: [overthewire, ctf, security, linux]
published: true
img_path: /assets/
image: images/overthewire-banner.png
---

### Level Goal

> The goal of this level is for you to log into the game using SSH. The host to which you need to connect is **bandit.labs.overthewire.org**, on port 2220. The username is **bandit0** and the password is **bandit0**. Once logged in, go to the Level 1 page to find out how to beat Level 1

### Commands you may need to solve this level

> ssh

```
> whatis ssh   
ssh (1) - OpenSSH remote login client
```

### Helpful Reading Material

[Secure Shell - Wikipedia](https://en.wikipedia.org/wiki/SSH_(Secure_Shell))

[How to Use SSH (with Pictures) - wikiHow](https://www.wikihow.com/Use-SSH)

### Known Information

*   Username: `bandit0`
*   Hostname: `bandit.labs.overthewire.org`
*   Port: `2220`
*   Password: `bandit0`

### Solution

Open Terminal (On Windows use PowerShell)

To login into Level 0 we have to use the SSH command

SSH Command: `ssh <username>@<hostname> -p <port>`

**Note:** If asked to accept any fingerprint type "yes" and press Enter

When asked for a password type **bandit0** and press Enter

```
> ssh bandit0@bandit.labs.overthewire.org -p 2220   
This is a OverTheWire game server. More information on http://www.overthewire.org/wargames

bandit0@bandit.labs.overthewire.org's password: bandit0
```

If the login was successful you will see a banner that looks as follows:

![Logged into Level 0|360](images/bandit-0/level-0-login.png)

To quit the SSH session type `exit` or use the keyboard shortcut `Ctrl + D`