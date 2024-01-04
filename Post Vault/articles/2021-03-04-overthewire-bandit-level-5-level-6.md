---
categories:
- Security
- OverTheWire
date: 2021-03-04 03:43:57 +0530
description: '[OverTheWire - Bandit](https://overthewire.org/wargames/bandit/bandit6.html)'
img_path: /assets/
published: true
tags:
- overthewire
- bandit
- ctf
- security
- linux
title: 'OverTheWire: Bandit Level 5 → Level 6'
---

![banner-image|640](images/overthewire-banner.png)

## Level Goal

> The password for the next level is stored in a file somewhere under the **inhere** directory and has all of the following properties:  
> human-readable  
> 1033 bytes in size  
> not executable  

## Commands you may need to solve this level

> ls, cd, cat, file, du, find

```
> whatis ls                                                                           
ls (1)          - list directory contents  

> whatis cd  
cd  (1)         - change working directory  

> whatis cat                                                                                                       
cat (1)         - concatenate files and print on the standard output  

> whatis file  
file (1)        - determine file type  

> whatis du    
du (1)          - estimate file space usage  

> whatis find  
find (1)        - search for files in a directory hierarchy
```

**Note:** All commands don't have to be used to complete level

## Helpful Reading Material

[35 Practical Examples of Linux Find Command](https://www.tecmint.com/35-practical-examples-of-linux-find-command/)

[How to Use Grep Command in Linux [12 Useful Examples]](https://www.tecmint.com/12-practical-examples-of-linux-grep-command/)

[What is a simple explanation for how pipes work in Bash? - Stack Overflow](https://stackoverflow.com/questions/9834086/what-is-a-simple-explanation-for-how-pipes-work-in-bash)

## Solution

View the files that are present in the current working directory

```
bandit5@bandit:~$ ls  
inhere
```

Move into the `inhere/` directory using the `cd` command

```
bandit5@bandit:~$ cd inhere/
```

View files that are in the directory

```
bandit5@bandit:~/inhere$ ls  
maybehere00  maybehere03  maybehere06  maybehere09  
maybehere12  maybehere15  maybehere18  
maybehere01  maybehere04  maybehere07  maybehere10  
maybehere13  maybehere16  maybehere19  
maybehere02  maybehere05  maybehere08  maybehere11  
maybehere14  maybehere17
```

To search for the file that we require using the properties that are specified in the question we can make use of the `find` command.

(Refer to `man pages` to read more on the various options that can be used along with the find command)

```
bandit5@bandit:~/inhere$ find . -type f -size 1033c -not -executable -exec file {} + | grep ASCII  
./maybehere07/.file2: ASCII text, with very long lines
```

## Command Explanation

* `.`: Search the current working directory only
* `-type f`: Look for files only (Exclude Directories)
* `-size 1033c`: Look for files that are exactly 1033 bytes in size (Find uses "c" to represent bytes)
* `-not -executable`: Find only non-executable files
* `-exec file {} +`: Execute the "file" command on all the results returns by find

**Note:** {} is a placeholder for the location where the names of the files found by find are going to be substituted. The "+" sign is used to terminate the statement

From the previous level, we know that the file command will return the value "ASCII Text" for human-readable files. So by using grep we are filtering the output to only show results that contain that string

**Note:** Grep is a command that is used to find patterns in strings and is very helpful when trying to find files. For more examples refer to the attached resources

The pipe `|` operator is used for sending the output of one command as the input of another command

Not that we have found the file let's view its contents

```
cat ./maybehere07/.file2  
DXjZPULLxYr17uwoI01bNLQbtFemEgo7
```

We have found the password for the next level !!

Logout of the current session and use the password of user bandit6 to access the next level

```
> ssh bandit6@bandit.labs.overthewire.org -p 2220  
This is a OverTheWire game server. More information on http://www.overthewire.org/wargames

bandit6@bandit.labs.overthewire.org's password: DXjZPULLxYr17uwoI01bNLQbtFemEgo7
```