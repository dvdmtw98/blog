---
title: TryHackMe - Mr. Robot CTF
description: Based on the Mr. Robot show, can you root this box?
date: 2024-04-26 12:10:00 -0500
categories:
  - Security
  - TryHackMe
tags:
  - security
  - tryhackme
  - ctf
  - linux
published: true
img_path: /assets/
---

![[thm-mr-robot-banner.png|640]]

Cover Image by [BiZkettE1](https://www.freepik.com/free-vector/modern-business-background-with-geometric-shapes_5287944.htm) on Freepik

[TryHackMe \| Mr. Robot CTF](https://tryhackme.com/r/room/mrrobot)

In this room inspired by the show Mr. Robot, we are tasked with finding three flags that are hidden across the target system. 

Connect to the TryHackMe networking using your `.ovpn` file.

```bash
sudo openvpn tryhackme-vpn.ovpn
```

[TryHackMe \| OpenVPN](https://tryhackme.com/r/room/openvpn)

This machine can also be downloaded from VulnHub and setup locally.

[Mr-Robot: 1 \~ VulnHub](https://www.vulnhub.com/entry/mr-robot-1,151/)

## Reconnaissance

To discover the services that are running on the target I performed a port scan.

[GitHub - RustScan/RustScan: 🤖 The Modern Port Scanner 🤖](https://github.com/RustScan/RustScan)

```bash
sudo rustscan -a 10.10.84.69 --ulimit 5000 -- -sS -Pn -sV -O -T4 -oN rustscan.txt
```

`-a`: IP Address  
`--ulimit`: Amount of sockets (connections) that are opened  
`-sS`: Stealth Scan (Uses incomplete TCP handshake)  
`-Pn`: Skip Ping scan (Consider all the ports to be open)  
`-sV`: Service Versioning    
`-O`: OS Detection  
`-T4`: Timing Template (Aggressive) - Faster Scan  
`-oN`: Normal Output

![[articles/images/thm-mr-robot/rustscan-result.png|500]]

Ports 80 and 443 are open on the target.

![[nmap-result.png|600]]

Both these ports are used by HTTP traffic (websites). From the scan, we also see that the target is running Linux.

## Enumeration

Port 80 and 443 both lead to the same website. On visiting the site we are shown the Linux boot sequence eventually, we get an input prompt. 

![[articles/images/thm-mr-robot/website-1.png|640]]

![[articles/images/thm-mr-robot/website-2.png|640]]

If we select `prepare` we are shown a video

If we select `fsociety` we are asked if we are ready to join the group

If we select `inform` we are shown some news articles

![[articles/images/thm-mr-robot/website-3.png|480]]

If we select `question` we are shown some images

![[website-4.jpg|600]]

If we select `wakeup` we are shown a video

![[articles/images/thm-mr-robot/website-5.png|600]]

If we select `join` we are shown a prompt to provide our email address

![[articles/images/thm-mr-robot/website-6.png|640]]

These commands did not reveal anything about the target system. I decided to brute force the website using `gobuster` for hidden directories.

![[gobuster-result.png|460]]

The `/0` route loads a blog.

![[articles/images/thm-mr-robot/website-7.png|640]]

The `/dashboard` and `/login` route lead to a WordPress login panel.

![[articles/images/thm-mr-robot/website-8.png|500]]

The `/readme` route loads the following page.

![[website-12.png|420]]

The `/robots` and `/robots.txt` routes take us to a page that shows us the name of the file that contains our 1st flag.

![[articles/images/thm-mr-robot/website-9.png|420]]

![[website-13.png|400]]

**What is key 1?**

> 073403c8a58a1f80d943455fb30724b9

## Initial Access

#### Approach 1

A file called `fsociety.dic` is also present on the site which I downloaded.

![[website-14.png|640]]

When I checked the content of the file I realized that it is a wordlist. I ran the list through `uniq` and discovered that it contains a lot of duplicate entries. I got rid of the duplicates and saved the result into the file `wordlist.txt`

```bash
# Lists top 10 values with their count 
cat fsociety.dic | sort | uniq -c | more -n 10

# Writes deduplicated values to file
cat fsociety.dic | sort | uniq > wordlist.txt
```

![[wordlist-2.png|300]]

Now that we have a wordlist we can use it to perform a dictionary attack against the WordPress login page. Since it is an online (live) site we can use `hydra` to launch the attack. 

Before using `hydra` we need to find the following details:
* Request type that is used to submit the data  
* Variables that store the user-provided data  
* Element that is present on the page when login is unsuccessful

These three pieces of information are used to craft the command required to perform the attack.

If we open Developer Tools, enter random values and submit the form we can see that WordPress uses POST requests to submit the data to the server.

![[wordpress-1.png|640]]

If we go to the "Request" tab of the same request we can see all the values that are getting sent to the server when the form is submitted.

![[wordpress-2.png|420]]

The message "Invalid Username" is shown when the user provides an invalid username.

![[wordpress-3.png|540]]

This this knowledge we can now craft the command to find out the username. Once we have the username we can modify the command to find the password.

[How to Brute Force Websites & Online Forms Using Hydra \| Infinite Logins](https://infinitelogins.com/2020/02/22/how-to-brute-force-websites-using-hydra/)

```bash
hydra -L wordlist.txt -p admin -f -v 10.10.84.69 -s 80 http-post-form "/wp-login.php:log=^USER^&password=admin&wp-submit=Log+In&redirect_to=http%3A%2F%2F10.10.84.69%2Fwp-admin%2F&testcookie=1:Invalid username."
```

`-L`: Username wordlist  
`-p`: Password  
`-f`: Stop when the first match is found  
`-v`: Verbose Output  
`-s`: Service (Port)  
`http-post-form`: POST request  

The last argument can be broken into three distinct parts: `target:paramters:condition`. The target is the page that contains the form that we want to attack. Parameters are key-value pairs that represent the data being sent to the backend when the form is submitted. If there are multiple parameters then each parameter should be separated by the `&` sign. The condition can be a success condition or failure condition the default is the fail condition (text that will be on the page when the guess is wrong). The fail condition can be written as `F=condition`.

`^USER^` is the substitution placeholder used for usernames.

![[wordlist-3.png|640]]

From this, we discover that the username is `ELLIOT`.

```bash
hydra -l ELLIOT -P wordlist.txt -f -v 10.10.84.69 -s 80 http-post-form "/wp-login.php:log=ELLIOT&password=^PASS^&wp-submit=Log+In&redirect_to=http%3A%2F%2F10.10.84.69%2Fwp-admin%2F&testcookie=1:S=302"
```

`-l`: Username  
`-P`: Password Wordlist  

In the last argument, the 3rd parameter is `S=302` which denotes a success condition. 302 is the HTTP status code returned when the user is redirected to the next page.

`^PASS^` is the substation placeholder used for the password.

![[wordlist-4.png|640]]

For this, I found out that the password is `ER28-0652`.

### Approach 2

The `/license` route loads to the following page. If we scroll to the bottom of the page we get a string that is base64 encoded.

![[articles/images/thm-mr-robot/website-10.png|640]]

![[articles/images/thm-mr-robot/website-11.png|340]]

We can decode the string using the following command:

```bash
echo ZWxsaW90OkVSMjgtMDY1Mgo= | base64 --decode
```

![[base64-decode.png|350]]

This also gives us the username and password.


![[wordpress-8.png|300]]

## Exploitation

There are multiple ways to exploit WordPress websites. I decided to replace the 404 error page code with code that spawns a reverse shell. The code will get invoked every time the user visits a page that does not exist.

> [!INFO]  
> Another method to exploit WordPress sites is by installing an custom plugin that contains reverse shell code. I wasn't able to get this method to work.  
> [WordPress Plugin : Reverse Shell](https://sevenlayers.com/index.php/179-wordpress-plugin-reverse-shell)

![[wordpress-4.png|640]]

Before uploading the code we have to set up a listener to listen for incoming connections. This can be set up using `netcat`.

```bash
netcat -nvlp 9000
```

`-n`: Don't perform DNS  
`-v`: Verbose  
`-l`: Listen Mode  
`-p`: Listening Port

![[wordpress-5.png|320]]

The code that I used is located on Kali Linux at `/usr/share/webshells/php/php-reverse-shell.php`. Make a copy of the script in your working directory.

[pentestmonkey/php-reverse-shell · GitHub](https://github.com/pentestmonkey/php-reverse-shell/blob/master/php-reverse-shell.php)

```bash
cp /usr/share/webshells/php/php-reverse-shell.php .
```

Change the IP address in the script to the IP address of the `tun0` interface (TryHackMe VPN Connection interface). Change the port in the script to the port on which `netcat` is listening.

![[exploit-8.png|340]]

> [!NOTE]  
> You can get the TryHackMe VPN interface IP Address by using the command `ip a l tun0`. You need the value that is listed under `inet`.

If you have `xclip` installed you can easily put the content of the file into your clipboard using the following command:

```bash
# Copy content of file to clipboard
xclip -sel c < php-reverse-shell.php
```

Using the sidebar launch the template editor.

![[wordpress-9.png|360]]

Select the "404 Template" from the right side panel. Replace the existing template with the reverse shell code. Click on "Upload File" to save the changes.

![[wordpress-6.png|640]]

Now access a route like `http://10.10.84.69/404.php` that does not exist. This will cause the 404 template code to get executed which will give us a reverse shell.

![[wordpress-7.png|600]]

## Privilege Escalation

![[articles/images/thm-mr-robot/exploit-1.png|540]]

I opened the `/home` directory and saw that the system has a user called `robot`. The home directory of the user robot contained the 2nd flag. I could not read the content of this file as I did not have the required permissions. The directory had a file called `password.raw-md5` which contained the MD5 hash for robot's password.

![[articles/images/thm-mr-robot/exploit-2.png|300]]

I copied the hash into a file called `robot.txt` then using `john` I cracked the hash.

```bash
john --wordlist=/usr/share/wordlists/rockyou.txt --format=raw-md5 robot.txt
```

![[articles/images/thm-mr-robot/exploit-3.png|600]]

Password: `abcdefghijklmnopqrstuvwxyz`

When I tried to log in as `robot` I was given the error that I wasn't running a TTY shell. Using Python I spawned a TTY shell.

```bash
python -c 'import pty;pty.spawn("/bin/bash");'
```

[Spawning a TTY Shell \| SecWiki](https://wiki.zacheller.dev/pentest/privilege-escalation/spawning-a-tty-shell)

![[articles/images/thm-mr-robot/exploit-4.png|340]]

**What is key 2?**

> 822c73956184f694993bede3eb39f959

Now that we have access to the system our need goal is to become the root user. I used the `find` command to check if there are unusual binaries that have the SUID bit set.

```bash
# Find files that have SUID bit set and are owned by root
find / -perm -4000 -user root 2> /dev/null
```

The expression `2> /dev/null` is used to redirect error messages into `null`. `null` is a special file on Linux that acts like a black hole destroying any data that is sent to it.

[What is /dev/null in Linux?](https://linuxhandbook.com/dev-null/)

Binaries that have the SUID bit set are executed with the permissions of the user that owns the file. If a file is owned by root the file will be run as root. A shell launched from such a process would have the permissions of the root user. 

[What is SUID, GUID and Sticky Bit in Linux? How to Use Them?](https://linuxhandbook.com/suid-sgid-sticky-bit/)

I saw that the binary for `nmap` had the SUID bit set which is not normal.

![[exploit-5.png|380]]

Using GTFOBins I found out that it was possible to get a shell from `nmap` using the `--interactive` flag. 

![[exploit-6.png|600]]

[nmap \| GTFOBins](https://gtfobins.github.io/gtfobins/nmap/)

```bash
nmap --interactive
!sh
```

With this shell, I had become the root user. I navigated to the `/root` directory and found the 3rd and final flag.

![[exploit-7.png|380]]

**What is key 3?**

> 04787ddef27c3dee1ee161b21670b4e4
