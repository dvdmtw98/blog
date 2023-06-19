---
title: 'OverTheWire: Bandit Level 9 → Level 10'
description: 'https://overthewire.org/wargames/bandit/bandit10.html'
date: '2021-03-05 05:00:42 +0530'
categories: [Security, OverTheWire]
tags: [overthewire, bandit, ctf, security, linux]
published: true
img_path: /assets/
image: images/overthewire-banner.png
---

### Level Goal

> The password for the next level is stored in the file **data.txt** in one of the few human-readable strings, preceded by several '=' characters.

### Commands you may need to solve this level

> grep, sort, uniq, strings, base64, tr, tar, gzip, bzip2, xxd

```
> whatis grep  
grep (1)             - print lines that match patterns

> whatis sort  
sort (1)             - sort lines of text files

> whatis uniq  
uniq (1)             - report or omit repeated lines

> whatis strings  
strings (1)          - print the sequences of printable characters in files

> whatis base64  
base64 (1)           - base64 encode/decode data and print to standard output

> whatis tr  
tr (1)               - translate or delete characters

> whatis tar  
tar (1)              - an archiving utility

> whatis gzip  
gzip (1)             - compress or expand files

> whatis bzip2  
bzip2 (1)            - a block-sorting file compressor, v1.0.8

> whatis xxd  
xxd (1)              - make a hexdump or do the reverse.
```

**Note:** All commands don't have to be used to complete level

### Helpful Reading Material

[Learn Piping and Redirection - Linux Tutorial](https://ryanstutorials.net/linuxtutorial/piping.php)

[How to Use Grep Command in Linux [12 Useful Examples]](https://www.tecmint.com/12-practical-examples-of-linux-grep-command/)

[strings - Unix, Linux Command](https://www.tutorialspoint.com/unix_commands/strings.htm)

### Solution

View the contents of the current working directory

```
bandit9@bandit:~$ ls  
data.txt
```

Peek at the data that is present in the file. This can be achieved using the `head` command

```
bandit9@bandit:~$ head -n 4 data.txt�L�lω;��ßOܛ��ǤX��NdT$��x7��@D@�o��+D��B��M֢�Z/,_��w��#�5���
                                                              Ў�e�&�-��Ϣ�6Q8��J�%fa�
�np�6l
|c���WW"&8��f��
��VJ�$�S~����d�
                 �p�k�U�;ֿ�v�Am��H��tɘ�3�ߘ�(ǟ�E'
                                                     ���'��:��uP�ע���������g�
```

(The -n flag allows us to specify how many lines to print from the start of the file. We can use the `tail` command to look at the last n lines of a file)

Human-readable strings in a file can be found using the `strings` command. The `-e` flag is used to specify the character encoding. We are assuming the human-readable line is ASCII text so we use "s" for the encoding type 

*(Refer to attached resources for more information)*

We also know that the line with the password starts with a few "=" characters. We can look for this pattern in the file using the `grep` command. We can combine all these commands into a single line using the `|` (pipe) operator

```
bandit9@bandit:~$ cat data.txt | strings -e s | grep ==
========== the*2i"4
========== password
Z)========== is
&========== truKLdjsbJ5g7yyJ2X2R0o3a5HQJFuLk
```

**Note:** The `cat` command is used to read the data from the file which is then passed as input to the next command in the line using pipes
 
We have found the password for the next level !!

Logout of the current session and use the password of user bandit10 to access the next level

```
> ssh bandit10@bandit.labs.overthewire.org -p 2220
This is a OverTheWire game server. More information on http://www.overthewire.org/wargames

bandit10@bandit.labs.overthewire.org's password: truKLdjsbJ5g7yyJ2X2R0o3a5HQJFuLk
```