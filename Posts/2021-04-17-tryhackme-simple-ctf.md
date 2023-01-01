---
title: TryHackMe - Simple CTF
description: Beginner level ctf
date: '2021-04-17 11:21:39 +0530'
categories: [Security, TryHackMe]
tags: [tryhackme, ctf, security, linux]
img_path: /assets/
---

![TryHackMe Simple CTF](images/thm-simple-ctf/thm-simple-ctf.png)

### Task 1 : Simple CTF

The first task that is performed when we are given an target to exploit is to find the services that are running on the target. To find services running on the machine I will be using "RustScan" which is an port scanner similar to Nmap but much faster (RustScan in ideal conditions can scan all the ports on the device in under 3 seconds). RustScan also integrates with Nmap so we can find open ports quickly with RustScan and then pipe the results to nmap for using Nmap features.

[GitHub - RustScan/RustScan: 🤖 The Modern Port Scanner 🤖](https://github.com/RustScan/RustScan)

![RustScan Results|520](images/thm-simple-ctf/rustscan-results.png)

#### Command Options

*   **-a :** Target IP Address
*   **--ulimit :** Number of parallel connections to target
*   **-sV :** Service Versioning
*   **-A :** Aggressive Scan
*   **-oN :** Normal output file

**Note:** All the flags after the `--` along with the ports found by RustScan are going to be passed to nmap for processing

#### Nmap Equivalent

> nmap -vvv -p- -Pn -sV -A -oN nmap_output.txt 10.10.230.250

![Nmap Results](images/thm-simple-ctf/nmap-results.png)

1. **How many services are running under port 1000 ?**

> 2

2. **What is running on the higher port ?**

> SSH

As we have found 3 ports that are open on the target device. Lets enumerate them one by one and see if we can find any vulnerability in them that we can exploit.

I started out with FTP which is running on port 22.

![Connect with FTP Server|280](images/thm-simple-ctf/ftp-connect.png)

Even though I was able to connect to the FTP service I could not run any commands since it required authentication. Since I had no idea on what these credentials could be I moved on to the next service which is an Web server running on port 80.

![Accessing Web Server](images/thm-simple-ctf/web-server-connect.png)

On accessing the server from my browser I was greeted with the default Apache Server page which did not provide anything useful. Next I checked to see if the server has an "robots.txt" file.

[What Is A Robots.txt File? Best Practices For Robot.txt Syntax - Moz](https://moz.com/learn/seo/robotstxt)

![Robots File in Web App|450](images/thm-simple-ctf/webapp-robots-file.png)

The server did have an "robots.txt" file and there seemed to be an directory that was hidden from being accessed by web crawlers. But on visiting the page I received the "Not Found" error.

![Accessing Directory on Web App|500](images/thm-simple-ctf/webapp-directory-access.png)

Since by looking around the web server manually I wasn't able to find anything I decided by run an directory brute force attack on the server to see if I can uncover any hidden directories.

![Gobuster Results](images/thm-simple-ctf/gobuster-results.png)

#### Command Options

*   **dir :** Perform directory brute forcing
*   **-u :** URL of Target
*   **-x :** Extensions of files to find
*   **-w :** Wordlist
*   **-t :** Threads (Used for parallelization)

**Note:** The `2> /dev/null` at the end is used to redirect any errors that might occur during the brute forcing process to `/dev/null` (NULL is an special device on Linux that destroys any data that is send to it)

From the scan I discovered there is an directory called `/simple` on the server.

![WebApp Landing Page](images/thm-simple-ctf/webapp-landing-page.png)

There is an website called "CMS Made Simple" that was present on this path. On just checking out the tabs that where present on the website I wasn't able to find any login/ upload fields that I could hijack for uploading a reverse shell.

So I decided to use "Searchsploit" and look if there are any know exploits that are available for this service. On scrolling to the bottom of the main page we are able to see the version of the CMS system that is running on the server.

![WebApp CMS Version](images/thm-simple-ctf/webapp-version.png)

![Searching for Exploit](images/thm-simple-ctf/finding-exploit.png)

Searchsploit found an SQL Injection exploit that is present for the version of the CMS system that was running on the server.

**Note:** Searchsploit is just can command line based tool for searching ExploitDB. If we directly use the website we will get the same results

![Exploit CVE Details](images/thm-simple-ctf/exploit-details.png)

![Exploit Version|500](images/thm-simple-ctf/exploit-version.png)

3. **What's the CVE you're using against the application ?**

> CVE-2019–9053

4. **To what kind of vulnerability is the application vulnerable ?**

> SQLi

**Note:** SQLi is short for SQL Injection

On downloading the exploit and trying to run it using python I noticed that the code was written in Python 2 because of which it couldn't run it on my system.

**Note 1:** New versions of Kali have Python 2 but don't have pip installer, without which we cant install any python modules. Python 2 support is going to be completely remove soon.

**Note 2:** If we look online we will find an Python 3 version of the script as well which will work directly. Since I wanted to understand how to get this code to work with Python 3 so I decided to convert it myself.

I know that python has an module called "2to3" which helps to convert Python 2 code to Python 3 code. I used that to convert the code to Python 3.

![Python Script Converter](images/thm-simple-ctf/python-script-converter.png)

![Running Script Converter](images/thm-simple-ctf/running-script-converter.png)

After the conversion now when I run the code I get some output telling me how to use the script.

![Running Exploit Script](images/thm-simple-ctf/running-exploit.png)

When I ran the script with the required parameters the script started performing the SQL Injection but after sometime I noticed that the script failed again as it ran into an error. On inspecting the error I understood there was an function that required some changing.

![Exploit Script Errors|450](images/thm-simple-ctf/exploit-script-error.png)

![Fixing Exploit Script Error](images/thm-simple-ctf/exploit-script-error-fix.png)

On changing the line as showing in the above image I ran the code again and this time I was successfully able to perform the Injection attack and get the username and password.

![Running Exploit Script|420](images/thm-simple-ctf/running-exploit-script.png)

**Note:** If your network connection is slow the script is not going to return the correct results in this case increase the "TIME" variable in the code to an higher number.

![Changing Exploit Parameters|220](images/thm-simple-ctf/exploit-parameters.png)

5. **What's the password ?**

> secret

At this stage I ran an directory brute force attack on the `/simple` directory to see if there are any hidden login pages present.

![Gobuster Results](images/thm-simple-ctf/gobuster-results-2.png)

The results showed that there is an directory called `/admin` present for the CMS system on opening it I found an login page. On entering the credentials that was found using the SQL Injection I was able to login into the admin control panel.

![WebApp Login Form](images/thm-simple-ctf/webapp-login-form.png)

![WebApp Dashboard](images/thm-simple-ctf/webapp-dashboard.png)

Looking around the control panel I could not find anything I looked like it could be used to get access into the system so I logged out and decided to try the SSH service that is running on port 2222.

![SSH Login|460](images/thm-simple-ctf/ssh-login.png)

6. **Where can you login with the details obtained ?**

> SSH

On looking around I found a file called as "user.txt" which is the first flag we require.

![Viewing Flag File 1](images/thm-simple-ctf/flag-file-1.png)

7. **What's the user flag ?**

> G00d j0b, keep up!

8. **Is there any other user in the home directory ? What's its name ?**

> sunbath

Now that I had got a foothold on the system my next task was to find a way to elevate my privileges and become the root user.

I run "sudo -l" command to see if there are any commands on the system that I can run without root privileges.

![Sudoers File Content](images/thm-simple-ctf/sudoers-file-content.png)

I found that on the system Vim could be run without root privileges

9. **What can you leverage to spawn a privileged shell ?**

> Vim

Whenever we have an system binary that could be exploited the first place to visit is GTOBins. If a system binary can be exploited then they will definitely have directions on how that could be done.

[GTFOBins](https://gtfobins.github.io/)

![Binary Exploit Usage Instruction](images/thm-simple-ctf/binary-exploit-instruction.png)

If we search for Vim and look under the Sudo session we see multiple approaches that could be used to evaluate our privileges. I used the first one to get root access and find the root flag.

![Flag File Content](images/thm-simple-ctf/flag-file-2.png)

10. **What's the root flag ?**

> W3ll d0n3. You made it!

That's all. Happy Hacking :)