---
title: 'OverTheWire: Bandit Level 14 → Level 15'
description: 'https://overthewire.org/wargames/bandit/bandit15.html'
date: '2021-03-07 15:46:08 +0530'
categories: [Security, OverTheWire]
tags: [overthewire, bandit, ctf, security, linux]
published: true
img_path: /assets/
image: images/overthewire-banner.png
---

### Level Goal

> The password for the next level can be retrieved by submitting the password of the current level to **port 30000 on localhost**.

### Commands you may need to solve this level

> ssh, telnet, nc, openssl, s_client, nmap

```
> whatis ssh  
ssh (1)              - OpenSSH remote login client  

> whatis telnet  
telnet (1)           - user interface to the TELNET protocol  

> whatis nc      
nc (1)               - TCP/IP swiss army knife  

> whatis openssl  
openssl (1ssl)       - OpenSSL command line tool  

> whatis s_client  
s_client (1ssl)      - SSL/TLS client program  

> whatis nmap      
nmap (1)             - Network exploration tool and security/ port scanner
```

**Note:** Not all commands are required to complete the level

### Helpful Reading Material

[IP address - Wikipedia](https://en.wikipedia.org/wiki/IP_address)

[Ports - How Web Servers Work \| HowStuffWorks](https://computer.howstuffworks.com/web-server8.htm)

[Port (computer networking) - Wikipedia](https://en.wikipedia.org/wiki/Port_%28computer_networking%29)

[Netcat (nc) Command with Examples \| Linuxize](https://linuxize.com/post/netcat-nc-command-with-examples/)

[8 Netcat (nc) Command with Examples](https://www.tecmint.com/netcat-nc-command-examples/)

### Solution

From the question, we know that there is a service that is running on port 30,000. We can try to connect to the service using Netcat

_(For the syntax of netcat and additional usage refer to the attached resources)_

**Note:** `nc` is an alias for `netcat` and can be used interchangeably

```
bandit14@bandit:~$ netcat localhost 30000  
Password  
Wrong! Please enter the correct current password
```

When we enter a random value we see that we get a message saying the password is incorrect

We know that the current level password is stored in `/etc/band_pass/bandit14` we can try to provide that as a value to the service and see if we get the password for the next level

```
bandit14@bandit:~$ cat /etc/bandit_pass/bandit14  
4wcYUJFw0k0XLShlDzztnTBHiqxU3b3e

bandit14@bandit:~$ netcat localhost 30000  
4wcYUJFw0k0XLShlDzztnTBHiqxU3b3e  
Correct!  
BfMYroe26WYalil77FoDi9qh59eK5xNr
```

We have found the password for the next level !!!

Logout of the current session and login into the next level using the bandit15 password

```
> ssh bandit15@bandit.labs.overthewire.org -p 2220

This is a OverTheWire game server. More information on http://www.overthewire.org/wargames

bandit15@bandit.labs.overthewire.org's password: BfMYroe26WYalil77FoDi9qh59eK5xNr
```