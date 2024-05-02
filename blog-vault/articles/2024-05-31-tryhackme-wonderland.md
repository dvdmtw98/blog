---
title: TryHackMe - Wonderland
description: Fall down the rabbit hole and enter wonderland
date: 2024-05-31 13:25:00 -0500
categories:
  - Security
  - TryHackMe
tags:
  - security
  - tryhackme
  - ctf
  - linux
published: false
img_path: /assets/
---

![[thm-wonderland-banner.png|640]]

Cover Image by [BiZkettE1](https://www.freepik.com/free-vector/modern-business-background-with-geometric-shapes_5287944.htm) on Freepik

[TryHackMe \| Wonderland](https://tryhackme.com/r/room/wonderland)

In this room inspired by Alice in Wonderland, we are tasked with finding two flags that are hidden on the target system.

## Reconnaissance

To find the running services on the target I performed a port scan.

[GitHub - RustScan/RustScan: 🤖 The Modern Port Scanner 🤖](https://github.com/RustScan/RustScan)

```bash
sudo rustscan -a 10.10.95.75 --ulimit 5000 -- -sS -Pn -sV -O -T4 -oN rustscan.txt
```

`-a`: IP Address  
`--ulimit`: No. of Sockets (connections) to open (Parallelism)  
`-sS`: Stealth Scan (Uses partial TCP handshake)  
`-Pn`: Skip Ping scan (Consider all the ports to be open)  
`-sV`: Service Versioning  
`-O`: OS Detection  
`-T4`: Timing Template (Aggressive) - Faster Scan  
`-oN`: Save result as Text (Normal Output)

![[rustscan-1.png|500]]

Port 22 and 80 are open on the target.

![[rustscan-2.png|640]]

Port 22 (SSH) - OpenSSH 7.6p1  
Port 80 (HTTP) - Golang HTTP Server  

OS Detection module detected that the target is running Linux. From the SSH banner we see that the target is running Ubuntu.

## Enumeration

### Port 22 (SSH)

The target is running a newish version of SSH. This version of SSH does not have any known exploits. I did not see any point in trying to perform an dictionary attack against SSH at this point.

### Port 80 (HTTP)

On the webapp we get an page that tells us to "Follow the White Rabbit". 

I checked the source code for the page and did not find anything. I also checked to see if there was a `robots.txt` file, the site did not have one configured. 

![[articles/images/thm-wonderland/website-1.png|560]]

Since I could not find anything useful on the webpage. I ran an directory fuzzing scan to look for hidden directories. 

```bash
gobuster dir --url http://10.10.95.75:80/ -w /usr/share/wordlists/dirb/common.txt | tee gobuster.txt
```

`dir`: Perform Directory Traversal  
`--url`: Target URL  
`-w`: Wordlist for brute forcing the directories  

The `| tee gobuster.txt` command is used to save the output of the command that is used before the `|` symbol to a file while simultaneously outputting it to the terminal.

The scan find the hidden directory `/r`.

![[articles/images/thm-wonderland/website-2.png|540]]

The new page tells us to "Keep Going" (i.e. continue using the same technique) so I once again ran a directory fuzzing scan. The scan was performed on the `/r` route.

![[articles/images/thm-wonderland/website-3.png|500]]

```bash
gobuster dir --url http://10.10.95.75:80/r/ -w /usr/share/wordlists/dirb/common.txt | tee gobuster2.txt
```

The scan found the `/a` directory.

![[articles/images/thm-wonderland/website-4.png|540]]

This page also tells us to "Keep Going". I realized at this point that the the final route will spell out the word `rabbit`. This makes sense in the start we were told to follow the "White Rabbit". 

![[articles/images/thm-wonderland/website-5.png|500]]

![[articles/images/thm-wonderland/website-6.png|500]]

![[articles/images/thm-wonderland/website-7.png|500]]

![[articles/images/thm-wonderland/website-8.png|500]]

Finally we get to a page that tells us to "Open the door and enter wonderland". 

![[articles/images/thm-wonderland/website-9.png|580]]

I checked the source code of the page and noticed a username and password hidden in the markup. I suspected this was a credential that could be used to access the target system using SSH.

![[articles/images/thm-wonderland/website-10.png|640]]

Username: `alice`  
Password: `HowDothTheLittleCrocodileImproveHisShiningTail`  

## Initial Access

Using the credential we can log into the target system as Alice.

```bash
ssh alice@10.10.95.75
```

![[access-1.png|500]]

I checked the `/home` directory and found out that there are 3 other users that have a account on this system.

```bash
ls -lah /home/
```

`-l`: Long (Detailed) Listing  
`-a`: Show Hidden Files  
`-h`: Show file size in Human-Readable Format

![[access-2.png|440]]

I listed the content of Alice's home directory and noticed the `root.txt` and `walrus_and_the_carpenter.py` files.

![[access-3.png|460]]

The content of `root.txt` cannot be read, it is owned by `root` and only `root` has the permission required to read its content.

## Privilege Escalation

### Rabbit

The `.py` script contains a a string with the lyrics to the poem "The Walrus and the Carpenter" by Lewis Carroll. At the end of the file we can see code that uses the python `random` module to print 10 random lines from the poem.

```bash
nano walrus_and_the_carpenter.py
```

![[alice-1.png|300]]

```bash
python3 walrus_and_the_carpenter.py
```

![[alice-2.png|380]]

I checked the `sudo` configuration for Alice to see if any special privileges were configured. Alice did have a special privilege.

Configurations for `sudo` the format: `User Host = (Runas-User:Group) Command`

When we use the command `sudo -l` only configuration that apply to the current user are shown. To view the `sudo` configuration of all the users we can use the command `visudo`. The `sudo` configuration is stored in the file `/etc/sudoers`.

The output of `sudo -l` will have the structure: `Host = (Runas-User:Group) Command`

If we were logged in as `root` the configuration `ALL = (ALL:ALL) ALL` would be read as "**User Root can Run Any Command as Any User from Any Group on Any Host**"

It is common to find configurations without the `Host` and `Group` part. The simplest form of the configuration is: `(Runas-User) Command`.

[Linux Fundamentals: A to Z of a Sudoers File \| by Harsha Koushik \| Medium](https://medium.com/kernel-space/linux-fundamentals-a-to-z-of-a-sudoers-file-a5da99a30e7f)

[A Deep Dive into the Sudoers File \| DigitalOcean](https://www.digitalocean.com/community/questions/a-deep-dive-into-the-sudoers-file)

The configuration on the target is `(rabbit) /usr/bin/python3.6 /home/alice/walrus_and_the_carpenter.py` which is read as **User Alice can Run '/usr/bin/python3.6 /home/alice/walrus_and_the_carpenter.py' as Rabbit**.

In short when Alice runs the `.py` script the script it is run with the permissions of the user `rabbit`.

```bash
sudo -l
```

`-l`: List current user privileges

![[alice-3.png|640]]

Using the command `python3 -c 'import sys;print(sys.path)'` we can find the directories that are searched to locate modules that are used in a script. Python searches these locations in the same order that is shown in the output. The empty string denotes that directory which the executed script is located. This is the 1st location that python looks for modules used in the code. 

If the module required is found in the 1st directory the remaining directories are not searched. If the module required is not found in any of the listed locations then we get the error "Module Not Found".

Using the command `python3 -c 'import random;print(random.__file__)'` we can find the location were the module `random` is located. From the output we can see that `random` is located in the directory `/usr/lib/python3.6/`. If we look at the output of `sys.path` we notice that this is the 3rd location that is searched.

```bash
# Python Path Variable
python3 -c 'import sys;print(sys.path)'

# Random Module Location
python3 -c 'import random;print(random.__file__)'
```

`-c`: Program passed as String

[How do I find the location of Python module sources? - Stack Overflow](https://stackoverflow.com/questions/269795/how-do-i-find-the-location-of-python-module-sources)

[Why is the first element in Python's sys.path an empty string? - Stack Overflow](https://stackoverflow.com/questions/49559003/why-is-the-first-element-in-pythons-sys-path-an-empty-string)

![[alice-4.png|640]]

We know that the `.py` file is executed as the user Rabbit. If we create our own `random.py` file and place it in a directory that comes before the directory were the real `random.py` file is located then python would load our code in place of the actual code. If we include code to spawn a shell in our `random.py` code then we can get a shell were we are the user Rabbit.

Since the directory which contains the executed code is the first location that python looks for modules we can create our `random.py` in the same location as the script (i.e. `/home/alice/`) to have python execute our code in place of the real `random.py` code.

```bash
nano random.py
```

![[alice-5.png|220]]

```python
# Code to Spawn Shell
import pty
pty.spawn("/bin/bash")
```

When we execute the script we need to use the full path as in `sudoers` file this is how it has been configured.

```bash
sudo -u rabbit /usr/bin/python3.6 /home/alice/walrus_and_the_carpenter.py
```

`-u`: Run-as User

![[alice-6.png|520]]

### Hatter

Once I become the user Rabbit I listed the files in the home directory.

```bash
cd /home/rabbit
ls -lah
```

The directory contains an binary executable with the name `teaParty`. The file also has the SUID (s-bit) enabled. Files that have SUID bit enabled are executed with the permissions of the user that owns the file rather than the permissions of the user executing the file. Since this file is owned by the user root it will be executed with the permissions of root (This observation is not entirely true for this specific executable, more on that later).

[Linux permissions: SUID, SGID, and sticky bit \| Enable Sysadmin](https://www.redhat.com/sysadmin/suid-sgid-sticky-bit)

[What is SUID, GUID and Sticky Bit in Linux? How to Use Them?](https://linuxhandbook.com/suid-sgid-sticky-bit/)

![[rabbit-1.png|500]]

When I ran the program, it crashed with the error "Segmentation Fault (core dumped)". This error occurs in C/C++ code when we try to access data that we do not have permission to access.

[What is "Segmentation fault (core dumped)?" - Stack Overflow](https://stackoverflow.com/questions/19641597/what-is-segmentation-fault-core-dumped)

[Segmentation Fault in C/C++ - GeeksforGeeks](https://www.geeksforgeeks.org/segmentation-fault-c-cpp/)

![[rabbit-2.png|440]]

Without looking at the source code it difficult to understand that operations an application performs. An simple way to find the human readable strings in a binary file is to use the `strings` command. The target machine did not have this command installed. This meant I had to download the file over to my system to analyze it.

Since the target system has python I use it to setup an HTTP server. With the server setup I could download all files present in the directory that has hosted by the server onto my machine.

```bash
python3 -m http.server 9000
```

`-m`: Run module as Script

![[rabbit-3.png|500]]

On my machine using `curl` I downloaded the file.

```bash
curl -LO http://10.10.95.75:9000/teaParty
```

`-L`: Follow Redirect  
`-O`: Save file with same name as Remote

![[rabbit-4.png|500]]

The file could also have been downloaded using `netcat`.

<iframe 
	width="560" height="315" 
	src="https://www.youtube-nocookie.com/embed/Vh0wXXWZ4kQ?si=jO8Jb_tSOzW4gzEo" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen>
</iframe>

Using the `strings` command I located the human-readable text from the binary file. We see the that program uses the `echo` and `date` commands provided by Linux. 

For the `echo` command the full path to the binary is used. For `date` the full path is not used. This means that when the program is executed the `date` binary is located on the system by scanning through the directories mentioned in the `$PATH` variable. This is true for all commands executed from the terminal (even the ones we have used so far) that are run without using the full path.

The output also contained the string "Segmentation Fault" which is strange as Segmentation Fault and other runtime errors are generated by the Operating System. These error messages are never stored in the program’s binary. This meant that the error message that we got when we ran the program was not real.

![[rabbit-5.png|400]]

To take a closer look at the binary I used a "Decompiler". A decompiler is a program that can convert binary (machine) code to high level source code. This is the reverse of the process performed by a compiler.

[Decompiler Explorer](https://dogbolt.org/)

As suspected we can see that "Segmentation Fault (core dumped)" is an string that is being printed to the terminal using the `puts()` command. It is not a real error message.

Line 164 and 165 is interesting. The `setuid()` function is used to change the user permission with which the code is executed. This function takes user ID as the parameter. This is the C code equivalent of the Linux SUID flag. The `setgid()` function is used to change the group permission with which the code is executed. This function takes group ID as the parameter. This is the C code equivalent of the Linux SGID flag.

![[rabbit-6.png|560]]

The ID value passed to the functions is in hexadecimal. The decimal equivalent of the number is `1003`.

![[rabbit-7.png|260]]

From the `/etc/passwd` file we can see that `1003` is the ID for the user "Hatter".

![[rabbit-8.png|500]]

Putting everything that we have observed together we can know that when the binary is executed it starts with the permissions of the `root` user but once the `setuid()` and `setgid()` functions are executed the program is executed with the permissions of the user Hatter.

![[rabbit-9.png|480]]

![[rabbit-10.png|360]]

![[rabbit-11.png|540]]

### Root

![[hatter-1.png|500]]

![[hatter-2.png|560]]

![[hatter-3.png|600]]

![[hatter-4.png|400]]

![[hatter-5.png|500]]

![[hatter-6.png|500]]

![[hatter-7.png|600]]

![[hatter-8.png|500]]

![[hatter-9.png|580]]

![[hatter-10.png|560]]

## Finding Flags

![[articles/images/thm-wonderland/root-1.png|500]]

## Misc. Clues

![[articles/images/thm-wonderland/misc-1.png|500]]