---
title: 'OverTheWire: Bandit Level 16 → Level 17'
description: '[OverTheWire - Bandit](https://overthewire.org/wargames/bandit/bandit17.html)'
date: '2021-03-07 15:50:02 +0530'
categories: [Security, OverTheWire]
tags: [overthewire, bandit, ctf, security, linux]
published: true
img_path: /assets/
image: images/overthewire-banner.png
---

## Level Goal

> The credentials for the next level can be retrieved by submitting the password of the current level to **a port on localhost in the range 31000 to 32000**. First find out which of these ports have a server listening on them. Then find out which of those speak SSL and which don't. There is only 1 server that will give the next credentials, the others will simply send back to you whatever you send to it.

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

[Nmap Commands - 17 Basic Commands for Linux Network](https://phoenixnap.com/kb/nmap-command-linux-examples)

[openssl s_client commands and examples - Mister PKI](https://www.misterpki.com/openssl-s-client/)

[How to use SSH keys for authentication - UpCloud](https://upcloud.com/community/tutorials/use-ssh-keys-authentication/)

## Solution

We know there that the service that we need is running in the range of 31,000-32,000. We can find all services in that range using Nmap.

The -T4 flag is used to increase the speed of the scan while the -p flag is used to specify the ports and the -sV flag is used to identify the versions of the services.

_(For more information on the various flags provided by Nmap refer to the attached resources)_

```
bandit16@bandit:~$ nmap -sV -T4 -p 31000-32000 localhost

Starting Nmap 7.40 ( https://nmap.org ) at 2021-03-07 09:04 CET
Nmap scan report for localhost (127.0.0.1)
Host is up (0.00030s latency).
Not shown: 996 closed ports
PORT      STATE SERVICE     VERSION
31046/tcp open  echo
31518/tcp open  ssl/echo
31691/tcp open  echo
31790/tcp open  ssl/unknown
31960/tcp open  echo

1 service unrecognized despite returning data. If you know the service/version, please submit the following fingerprint at https://nmap.org/cgi-bin/submit.cgi?new-service :
SF-Port31790-TCP:V=7.40%T=SSL%I=7%D=3/7%Time=60448917%P=x86_64-pc-linux-gn
SF:u%r(GenericLines,31,"Wrong!\x20Please\x20enter\x20the\x20correct\x20cur
SF:rent\x20password\n")%r(GetRequest,31,"Wrong!\x20Please\x20enter\x20the\
SF:x20correct\x20current\x20password\n")%r(HTTPOptions,31,"Wrong!\x20Pleas
SF:e\x20enter\x20the\x20correct\x20current\x20password\n")%r(RTSPRequest,3
SF:1,"Wrong!\x20Please\x20enter\x20the\x20correct\x20current\x20password\n
SF:")%r(Help,31,"Wrong!\x20Please\x20enter\x20the\x20correct\x20current\x2
SF:0password\n")%r(SSLSessionReq,31,"Wrong!\x20Please\x20enter\x20the\x20c
SF:orrect\x20current\x20password\n")%r(TLSSessionReq,31,"Wrong!\x20Please\
SF:x20enter\x20the\x20correct\x20current\x20password\n")%r(Kerberos,31,"Wr
SF:ong!\x20Please\x20enter\x20the\x20correct\x20current\x20password\n")%r(
SF:FourOhFourRequest,31,"Wrong!\x20Please\x20enter\x20the\x20correct\x20cu
SF:rrent\x20password\n")%r(LPDString,31,"Wrong!\x20Please\x20enter\x20the\
SF:x20correct\x20current\x20password\n")%r(LDAPSearchReq,31,"Wrong!\x20Ple
SF:ase\x20enter\x20the\x20correct\x20current\x20password\n")%r(SIPOptions,
SF:31,"Wrong!\x20Please\x20enter\x20the\x20correct\x20current\x20password\
SF:n");

Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 89.88 seconds
```

From our scan results, we can see that multiple services are running in that range but if we look at the results more closely we see that on port 31790 there is a service that returns the message "Enter correct password". As we need to find a service to send passwords we can conclude that this is the service that we need.

We know that the service uses SSL encryption. So we need to use the `openssl` and `s_client` commands to connect to the port and pass the password of the current user

_(Refer to the previous level if not sure how to use these commands)_

```
bandit16@bandit:~$ cat /etc/bandit_pass/bandit16  
cluFn7wTiGryunymYOu4RcffSxQluehdbandit16@bandit:~$ openssl s_client --connect localhost:31790  
CONNECTED(00000003)  
.  
.  
.  
---  
cluFn7wTiGryunymYOu4RcffSxQluehd  
Correct!  
-----BEGIN RSA PRIVATE KEY-----  
MIIEogIBAAKCAQEAvmOkuifmMg6HL2YPIOjon6iWfbp7c3jx34YkYWqUH57SUdyJ  
imZzeyGC0gtZPGujUSxiJSWI/oTqexh+cAMTSMlOJf7+BrJObArnxd9Y7YT2bRPQ  
Ja6Lzb558YW3FZl87ORiO+rW4LCDCNd2lUvLE/GL2GWyuKN0K5iCd5TbtJzEkQTu  
DSt2mcNn4rhAL+JFr56o4T6z8WWAW18BR6yGrMq7Q/kALHYW3OekePQAzL0VUYbW  
JGTi65CxbCnzc/w4+mqQyvmzpWtMAzJTzAzQxNbkR2MBGySxDLrjg0LWN6sK7wNX  
x0YVztz/zbIkPjfkU1jHS+9EbVNj+D1XFOJuaQIDAQABAoIBABagpxpM1aoLWfvD  
KHcj10nqcoBc4oE11aFYQwik7xfW+24pRNuDE6SFthOar69jp5RlLwD1NhPx3iBl  
J9nOM8OJ0VToum43UOS8YxF8WwhXriYGnc1sskbwpXOUDc9uX4+UESzH22P29ovd  
d8WErY0gPxun8pbJLmxkAtWNhpMvfe0050vk9TL5wqbu9AlbssgTcCXkMQnPw9nC  
YNN6DDP2lbcBrvgT9YCNL6C+ZKufD52yOQ9qOkwFTEQpjtF4uNtJom+asvlpmS8A  
vLY9r60wYSvmZhNqBUrj7lyCtXMIu1kkd4w7F77k+DjHoAXyxcUp1DGL51sOmama  
+TOWWgECgYEA8JtPxP0GRJ+IQkX262jM3dEIkza8ky5moIwUqYdsx0NxHgRRhORT  
8c8hAuRBb2G82so8vUHk/fur85OEfc9TncnCY2crpoqsghifKLxrLgtT+qDpfZnx  
SatLdt8GfQ85yA7hnWWJ2MxF3NaeSDm75Lsm+tBbAiyc9P2jGRNtMSkCgYEAypHd  
HCctNi/FwjulhttFx/rHYKhLidZDFYeiE/v45bN4yFm8x7R/b0iE7KaszX+Exdvt  
SghaTdcG0Knyw1bpJVyusavPzpaJMjdJ6tcFhVAbAjm7enCIvGCSx+X3l5SiWg0A  
R57hJglezIiVjv3aGwHwvlZvtszK6zV6oXFAu0ECgYAbjo46T4hyP5tJi93V5HDi  
Ttiek7xRVxUl+iU7rWkGAXFpMLFteQEsRr7PJ/lemmEY5eTDAFMLy9FL2m9oQWCg  
R8VdwSk8r9FGLS+9aKcV5PI/WEKlwgXinB3OhYimtiG2Cg5JCqIZFHxD6MjEGOiu  
L8ktHMPvodBwNsSBULpG0QKBgBAplTfC1HOnWiMGOU3KPwYWt0O6CdTkmJOmL8Ni  
blh9elyZ9FsGxsgtRBXRsqXuz7wtsQAgLHxbdLq/ZJQ7YfzOKU4ZxEnabvXnvWkU  
YOdjHdSOoKvDQNWu6ucyLRAWFuISeXw9a/9p7ftpxm0TSgyvmfLF2MIAEwyzRqaM  
77pBAoGAMmjmIJdjp+Ez8duyn3ieo36yrttF5NSsJLAbxFpdlc1gvtGCWW+9Cq0b  
dxviW8+TFVEBl1O4f7HVm6EpTscdDxU+bCXWkfjuRb7Dy9GOtt9JPsX8MBTakzh3  
vBgsyi/sN3RqRBcGU40fOoZyfAMT8s1m/uYv52O6IgeuZ/ujbjY=  
-----END RSA PRIVATE KEY-----closed
```

We did not get any password but got an RSA Key that can be used with SSH to access the next level. We need to save the key in a file to be used with SSH. As we don't have permission in the current working directory to make a file. We create a folder in the `/tmp` directory and work from there.

```
bandit16@bandit:~$ mkdir /tmp/random_sshkey

bandit16@bandit:~$ cd /tmp/random_sshkey

bandit16@bandit:/tmp/random_sshkey$ touch private.key

bandit16@bandit:/tmp/random_sshkey$ vim private.key
```

**Note:** We can use any text editor to save the key in the file but here we are using the Vim editor

*   Once Vim opens Press "i" to enter insert mode
*   Then use Ctrl + Shift + V to paste the copied key

![SSH RSA Key|500](images/bandit-16-17/ssh-rsa-key.png)

*   Press the "Esc" key to return to normal mode
*   Then type `:wq` to save and exit the file

Change the permissions of the file so that other users cannot access the file

_(This step is required as when we try to use the key without changing the permission we are going to get an error preventing us from using the key)_

```
bandit16@bandit:/tmp/random_sshkey$ chmod 400 private.keybandit16@bandit:/tmp/random_sshkey$ ls -l  
total 4  
-r-------- 1 bandit16 root 1676 Mar  7 09:23 private.key
```

Now we can use the key file with the `ssh` command to access the next level

```
bandit16@bandit:/tmp/random_sshkey$ ssh -i private.key 
bandit17@localhost
```

_(If asked to accept a fingerprint enter "yes")_

```
Linux bandit.otw.local 5.4.8 x86_64 GNU/Linux      
	  ,----..            ,----,          .---.
     /   /   \         ,/   .`|         /. ./|
    /   .     :      ,`   .'  :     .--'.  ' ;
   .   /   ;.  \   ;    ;     /    /__./ \ : |
  .   ;   /  ` ; .'___,/    ,' .--'.  '   \' .
  ;   |  ; \ ; | |    :     | /___/ \ |    ' '
  |   :  | ; | ' ;    |.';  ; ;   \  \;      :
  .   |  ' ' ' : `----'  |  |  \   ;  `      |
  '   ;  \; /  |     '   :  ;   .   \    .\  ;
   \   \  ',  /      |   |  '    \   \   ' \ |
    ;   :    /       '   :  |     :   '  |--"
     \   \ .'        ;   |.'       \   \ ;
  www. `---` ver     '---' he       '---" ire.org
  
Welcome to OverTheWire!
.
.
.
bandit17@bandit:~$
```

We have gained access to the next level

Let us capture the password of the current level so we can log in later if required

```
bandit17@bandit:~$ cat /etc/bandit_pass/bandit17  
xLYVMN9WE5zQ5vHacb0sZEVqbrp7nBTn
```

We have found the password for the current level !!!

Logout of the current session (bandit17) and the previous session (bandit16) and use the password of bandit17 to access the next level

```
> ssh bandit17@bandit.labs.overthewire.org -p 2220  
This is a OverTheWire game server. More information on http://www.overthewire.org/wargames

bandit17@bandit.labs.overthewire.org's password: xLYVMN9WE5zQ5vHacb0sZEVqbrp7nBTn
```