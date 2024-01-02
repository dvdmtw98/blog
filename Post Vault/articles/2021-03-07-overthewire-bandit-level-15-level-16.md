---
title: 'OverTheWire: Bandit Level 15 → Level 16'
description: '![OverTheWire - Bandit](https://overthewire.org/wargames/bandit/bandit16.html)'
date: '2021-03-07 15:46:41 +0530'
categories: [Security, OverTheWire]
tags: [overthewire, bandit, ctf, security, linux]
published: true
img_path: /assets/
image: images/overthewire-banner.png
---

## Level Goal

> The password for the next level can be retrieved by submitting the password of the current level to **port 30001 on localhost** using SSL encryption.  
> **Helpful note: Getting "HEARTBEATING" and "Read R BLOCK"? Use -ign_eof and read the "CONNECTED COMMANDS" section in the manpage. Next to 'R' and 'Q', the 'B' command also works in this version of that command…**

## Commands you may need to solve this level

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

## Helpful Reading Material

[Transport Layer Security - Wikipedia](https://en.wikipedia.org/wiki/Transport_Layer_Security)

[Ping Identity Support](https://support.pingidentity.com/s/article/OpenSSL-s-client-Commands)

[ncat(1) - Linux manual page](https://man7.org/linux/man-pages/man1/ncat.1.html)

## Solution

We know that we have to connect to a service on port 30,001 using SSL encryption. The simplest way to achieve this is using the `openssl` command along with `s_client` which allows us to connect to services on our machine using SSL.

```
bandit15@bandit:~$ openssl s_client -connect localhost:30001

CONNECTED(00000003)
depth=0 CN = localhost
verify error:num=18:self signed certificate
verify return:1
depth=0 CN = localhost
verify return:1
---
Certificate chain
 0 s:/CN=localhost
   i:/CN=localhost
---
.
.
.Start Time: 1615101060
    Timeout   : 7200 (sec)
    Verify return code: 18 (self signed certificate)
    Extended master secret: yes
---
Password
Wrong! Please enter the correct current password
closed
```

When we provide the password as "Password" as get an error saying the provided the wrong password

Let's provide the correct password and see if we get the password for the next level. The password for the current level can be found at `/etc/bandit_pass/bandit15`

```
bandit15@bandit:~$ cat /etc/bandit_pass/bandit15  
BfMYroe26WYalil77FoDi9qh59eK5xNr

bandit15@bandit:~$ openssl s_client -connect localhost:30001  
BfMYroe26WYalil77FoDi9qh59eK5xNr  
Correct!  
cluFn7wTiGryunymYOu4RcffSxQluehd
```

We have found the password for the next level !!!

**Note:** We can achieve the same result using the `ncat` command which is an advanced version of `netcat` that is developed by the creators of Nmap. If using ncat make use of the same command as the previous level and add the `--ssl` flag

Logout of the current session and start the next level using the bandit16 password

```
> ssh bandit16@bandit.labs.overthewire.org -p 2220

This is a OverTheWire game server. More information on http://www.overthewire.org/wargames

bandit16@bandit.labs.overthewire.org's password: cluFn7wTiGryunymYOu4RcffSxQluehd
```