---
title: 'OverTheWire: Bandit Level 12 → Level 13'
description: '![OverTheWire - Bandit](https://overthewire.org/wargames/bandit/bandit13.html)'
date: '2021-03-06 09:14:59 +0530'
categories: [Security, OverTheWire]
tags: [overthewire, bandit, ctf, security, linux]
published: true
img_path: /assets/
image: images/overthewire-banner.png
---

## Level Goal

> The password for the next level is stored in the file **data.txt**, which is a hexdump of a file that has been repeatedly compressed. For this level it may be useful to create a directory under /tmp in which you can work using mkdir. For example: mkdir /tmp/myname123. Then copy the datafile using cp, and rename it using mv (read the manpages!)

## Commands you may need to solve this level

> grep, sort, uniq, strings, base64, tr, tar, gzip, bzip2, xxd, mkdir, cp, mv, file

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

> whatis mkdir  
mkdir (1)            - make directories

> whatis cp  
cp (1)               - copy files and directories

> whatis mv  
mv (1)               - move (rename) files

> whatis file  
file (1)             - determine file type
```

**Note:** All commands don't have to be used to complete level

## Helpful Reading Material

[Hex dump - Wikipedia](https://en.wikipedia.org/wiki/Hex_dump)

[Gzip Command in Linux \| Linuxize](https://linuxize.com/post/gzip-command-in-linux/)

[Tar Command in Linux (Create and Extract Archives) \| Linuxize](https://linuxize.com/post/how-to-create-and-extract-archives-using-the-tar-command-in-linux/)

[How to Compress and Decompress .bz2 files in Linux Using bzip2 Command - The Geek Diary](https://www.thegeekdiary.com/how-to-compress-and-decompress-bz2-files-in-linux-using-bzip2-command/)

[xxd(1): make hex dump/do reverse - Linux man page](https://linux.die.net/man/1/xxd)

## Solution

View the contents of the current working directory

```
bandit12@bandit:~$ ls  
data.txt
```

View the data that is present in the file

```
bandit12@bandit:~$ head data.txt
00000000: 1f8b 0808 0650 b45e 0203 6461 7461 322e  .....P.^..data2.
00000010: 6269 6e00 013d 02c2 fd42 5a68 3931 4159  bin..=...BZh91AY
00000020: 2653 598e 4f1c c800 001e 7fff fbf9 7fda  &SY.O...........
00000030: 9e7f 4f76 9fcf fe7d 3fff f67d abde 5e9f  ..Ov...}?..}..^.
00000040: f3fe 9fbf f6f1 feee bfdf a3ff b001 3b1b  ..............;.
00000050: 5481 a1a0 1ea0 1a34 d0d0 001a 68d3 4683  T......4....h.F.
00000060: 4680 0680 0034 1918 4c4d 190c 4000 0001  F....4..LM..@...
00000070: a000 c87a 81a3 464d a8d3 43c5 1068 0346  ...z..FM..C..h.F
00000080: 8343 40d0 3400 0340 66a6 8068 0cd4 f500  .C@.4..@f..h....
00000090: 69ea 6800 0f50 68f2 4d00 680d 06ca 0190  i.h..Ph.M.h.....
```

Looking at the data we see that the file consists of hexadecimal data. We have to convert this hexadecimal data to binary to get back the actual file. We can make use of the `xxd` command that allows us to manipulate hexadecimal data. The `-r` flag is used to tell xxd to reverse the operation (hex to binary)

But before we do any of this we first need to create a temporary working directory in the `/tmp` directory as we do not have permission to create new files in the current location. We can do this using the `mkdir` command. To move into the new directory we can use the `cd` command

```
bandit12@bandit:~$ mkdir /tmp/random_dir

bandit12@bandit:~$ cd /tmp/random_dir

bandit12@bandit:/tmp/random_dir$
```

We now need to move `data.txt` to this new location. We can do this using the `cp` command. And then we rename the file to remove the `.txt` extension as we know the file is not a text file

```
bandit12@bandit:/tmp/random_dir$ cp ~/data.txt .

bandit12@bandit:/tmp/random_dir$ ls  
data.txt

bandit12@bandit:/tmp/random_dir$ mv data.txt data

bandit12@bandit:/tmp/random_dir$ ls  
data
```

Now that the data is in the new directory we can now use xxd to convert the data into its binary equivalent

```
bandit12@bandit:/tmp/random_dir$ xxd -r data > binary

bandit12@bandit:/tmp/random_dir$ ls  
binary  data
```

Now that we have converted the data back into its binary form we can use the `file` command to see what type of data is stored in the file

```
bandit12@bandit:/tmp/random_dir$ file binary
binary: gzip compressed data, was "data2.bin", last modified: Thu May  7 18:14:30 2020, max compression, from Unix
```

### Gzip Decompression

We can see that the file was compressed using gzip so we can decompress the data using the `gunzip` command. When trying to decompress a gzip file the file must have the correct extension.

**Note:** Gunzip is shorthand for `gzip -d`

```
bandit12@bandit:/tmp/random_dir$ mv binary binary.gz

bandit12@bandit:/tmp/random_dir$ gunzip binary.gz

bandit12@bandit:/tmp/random_dir$ ls  
binary  data
```

### Bzip Decompression

Using the `file` command we can again look at the type of data that is stored in the file

```
bandit12@bandit:/tmp/random_dir$ file binary  
binary: bzip2 compressed data, block size = 900k
```

We see that the data is compressed using bzip2. For decompressing a bzip2 file we can use the `bunzip2` command

```
bandit12@bandit:/tmp/random_dir$ bunzip2 binary  
bunzip2: Can't guess original name for binary -- using binary.out

bandit12@bandit:/tmp/random_dir$ ls  
binary.out  data
```

**Note:** `bunzip2` is an shorthand for the `bzip2 -d` command

### Gzip Decompression (Again)

Using the `file` command we can look at the type of data that is stored in the file

```
bandit12@bandit:/tmp/random_dir$ file binary.out  
binary.out: gzip compressed data, was "data4.bin", last modified: Thu May  7 18:14:30 2020, max compression, from Unix
```

We see that it is once more gzip compressed file we use the same procedure as Step 5 to decompress the file

**Note:** Remember to rename the file with the `.gz` extension for the file to be decompressed properly

```
bandit12@bandit:/tmp/random_dir$ mv binary.out binary.gz

bandit12@bandit:/tmp/random_dir$ gunzip binary.gz

bandit12@bandit:/tmp/random_dir$ ls  
binary  data
```

### Tar Archive

Using the `file` command we look at the type of data that is present in the file

```
bandit12@bandit:/tmp/random_dir$ file binary  
binary: POSIX tar archive (GNU)
```

We see that the data is saved in a tar archive. For extracting a tar file we use the `tar` command. The `-r` flag is used to specify that we what to extract the data and the `-f` flag is used for specifying the filename

```
bandit12@bandit:/tmp/random_dir$ tar -xf binary

bandit12@bandit:/tmp/random_dir$ ls  
binary  data  data5.bin
```

We use the `file` command to see the file type and we see that the data is again in a tar archive.

It looks like the password file has recursively been compressed using "tar", "gzip" and "bzip2". We keep repeating the above steps tell we get the password file

```
bandit12@bandit:/tmp/random_dir$ rm binary data

bandit12@bandit:/tmp/random_dir$ file data5.bin  
data5.bin: POSIX tar archive (GNU)

bandit12@bandit:/tmp/random_dir$ tar -xf data5.bin

bandit12@bandit:/tmp/random_dir$ ls  
data5.bin  data6.bin

bandit12@bandit:/tmp/random_dir$ rm data5.bin

bandit12@bandit:/tmp/random_dir$ file data6.bin  
data6.bin: bzip2 compressed data, block size = 900k  
  
bandit12@bandit:/tmp/random_dir$ bunzip2 data6.bin  
bunzip2: Can't guess original name for data6.bin -- using data6.bin.out

bandit12@bandit:/tmp/random_dir$ ls  
data6.bin.out

bandit12@bandit:/tmp/random_dir$ file data6.bin.out  
data6.bin.out: POSIX tar archive (GNU)

bandit12@bandit:/tmp/random_dir$ tar -xf data6.bin.out

bandit12@bandit:/tmp/random_dir$ ls  
data6.bin.out  data8.bin

bandit12@bandit:/tmp/random_dir$ rm data6.bin.out

bandit12@bandit:/tmp/random_dir$ file data8.bin  
data8.bin: gzip compressed data, was "data9.bin", last modified: Thu May  7 18:14:30 2020, max compression, from Unix

bandit12@bandit:/tmp/random_dir$ mv data8.bin data8.gz

bandit12@bandit:/tmp/random_dir$ gunzip data8.gz

bandit12@bandit:/tmp/random_dir$ ls  
data8

bandit12@bandit:/tmp/random_dir$ file data8  
data8: ASCII text

bandit12@bandit:/tmp/random_dir$ cat data8  
The password is 8ZjyCRiBWFYkneahHwxCv3wb2a1ORpYL
```

We have found the password for the next level !!

Logout of the current session and use the password of user bandit13 to access the next level

```
> ssh bandit13@bandit.labs.overthewire.org -p 2220  
This is a OverTheWire game server. More information on http://www.overthewire.org/wargames

bandit13@bandit.labs.overthewire.org's password: 8ZjyCRiBWFYkneahHwxCv3wb2a1ORpYL
```