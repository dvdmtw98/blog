---
title: "TryHackMe: MBR and GPT Analysis"
description: Learn how MBR and GPT forensics are carried out to identify attacks during the boot process.
date: 2025-01-24 18:55:00 -0600
categories:
  - Security
  - TryHackMe
tags:
  - security
  - tryhackme
  - walkthrough
  - forensics
  - operating-system
published: true
media_subpath: /assets/
---

![[mbr-and-gpt-analysis-banner.png|640]]

Banner background by [BiZkettE1](https://www.freepik.com/free-vector/modern-business-background-with-geometric-shapes_5287944.htm) on Freepik

[TryHackMe \| MBR and GPT Analysis](https://tryhackme.com/r/room/mbrandgptanalysis)

> [!IMPORTANT]  
> Read the material that accompanies each task before taking a look at this guide. This guide will only cover content that is necessary to answer the questions.

### Task 1: Introduction

**1. What are the separate sections on a disk known as?**

![[thm-soln-1.png|640]]

> Partition

**2. Which type of malware infects the boot process?**

![[thm-soln-2.png|640]]

> Bootkit

### Task 2: Boot Process

**1. What is the name of the hardware diagnostic check performed during the boot process?**

![[thm-soln-3.png|640]]

> Power-Nn-Self-Test

**2. Which firmware supports a GPT partitioning scheme?**

![[thm-soln-4.png|640]]

> UEFI

**3. Which device has the operating system to boot the system?**

![[thm-soln-5.png|640]]

> Bootable Device

### Task 3: What if MBR?

**1. Which component of the MBR contains the details of all the partitions present on the disk?**

![[thm-soln-6.png|640]]

> Partition Table

**2. What is the standard sector size of a disk in bytes?**

![[thm-soln-7.png|640]]

> 512

**3. Which component of the MBR is responsible for finding the bootable partition?**

![[thm-soln-8.png|640]]

> Bootloader Code

**4. What is the magic number inside the MBR?**

![[thm-soln-9.png|640]]

> 55 AA

**5. What is the maximum number of partitions MBR can support?**

![[thm-soln-10.png|640]]

> 4

**6. What is the size of the second partition in the MBR attached to the machine? (rounded to the nearest GB)**

Launch the VM and load the MBR file in HxD Editor. To calculate the size of the partition we first need to locate the partition table. 

From the write-up we know that the partition table starts at byte 446. We also know that each entry in the partition table is 16 bytes. Using this information we can deduce that the entry for the 2nd partition will start from byte `462` (446 + 16).

We can directly jump to this location using “Search → Go to”.

![[thm-soln-16.png|240]]

The below image shows the partition table entry for the 2nd partition.

![[thm-soln-11.png|500]]

From the table provided in the write-up we know that the last 4 bytes of the partition table entry contains the count of sectors in a partition.

![[thm-soln-12.png|500]]

The value store in the partition table uses little-endian representation, we need to reverse the bytes to get the big-endian representation so that we can convert it to decimal.

`00 38 EB 01` becomes `01 EB 38 00` in big-endian representation. When this hex value is converted to decimal we get `3219512`. We know that each sector is `512` bytes. To get the size of the partition we need to multiply the sector count with the sector size. This gives us `16482566144` (32192512 * 512). This is the size of the partition in bytes.

![[thm-soln-14.png|400]]

> [!INFO]  
> Disk size can be represented as a multiple of 2 (1 KB = 1024 bytes) or multiple of 10 (1 KB = 1000 bytes). The notation that is used depends on the OS. Windows and Linux use the binary notation (1024 bytes) while MacOS uses the decimal notation (1000 bytes). Most disk manufactures also use the decimal notation as it makes their disk appear larger. 

This room expects the sizes in multiples of 10. So to convert bytes to gigabytes we have to divide the `16482566144` trice by 1000 (B → KB → MB → GB).

![[thm-soln-15.png|240]]

> 16

### Task 4: Threats Targeting MBR

**1. Complete this task.**

> No answer required

### Task 5: MBR Tampering Case

In this task we have been instructed to fix `MBR_Corrupted_Disk`. On loading the image in HxD we can see that the Magic Number of the MBR partition is corrupted (correct value is `55 AA`). We are also told in the write-up that the LBA field of the bootable partition has been corrupted.

![[thm-soln-17.png|500]]

The values can be modified by double clicking in the hex editor and then typing the new value. Once done save the file to persist the changes.

![[thm-soln-18.png|500]]

**1. How many partitions are on the disk?**

If we look at the above images we can see that only the first 16 bytes in the partition table has any value. Every byte after that is set to 0. From this we can conclude that this disk only has a single partition.

> 1

**2. What is the first byte at the starting LBA of the partition? (represented by two hexadecimal digits)**

From the write-up we know that the LBA address field contains the sector from which the data for this partition starts. Since this value is in little-endian we need to reverse it to get the big-endian notation. Once its reversed we can calculate the decimal value. The data for the partition starts at sector `2048`.

![[thm-soln-19.png|240]]

We need the address, for that we need to multiply the value by `512` (sector size) which gives us `1048576`.

![[thm-soln-20.png|140]]

We can use “Search → Go to” to jump to the address.

![[thm-soln-21.png|240]]

We can see that the 1st byte at this address has the value `EB`.

![[thm-soln-22.png|500]]

> EB

**3. What is the type of the partition?**

In the above image if we look at the ASCII column we can see that the partition uses NTFS. Alternatively, we can load the modified image in FTK Imager to get the partition type.

![[thm-soln-23.png|260]]

> NTFS

**4. What is the size of the partition? (rounded to the nearest GB)**

FTK shows us the size of the partition in MB besides the partition name. FTK shows the size in binary notation but in this room we are required to provide the sizes in decimal notation. So, we first need to multiply the size twice by 1024 to get the size in bytes then we can divide it thrice by 1000 to get the size in GB. 

![[thm-soln-24.png|300]]

An alternative approach would be to use the value provided in the no. of sectors field (last field) in the partition entry.

![[thm-soln-25.png|500]]

Flip the bits to get the big-endian representation, then convert the value to decimal. This will give us `62910464`. This is the no. of sectors that make up the partition to get the size we need to multiple this value by `512` which will give us the size in bytes. We divide this value thrice by 1000 to get the size in GB. 

![[thm-soln-26.png|360]]

![[thm-soln-27.png|300]]

> 32

**5. What is the flag hidden in the Administrator's Documents folder?**

The Documents folder is located under the users home directory. The home directory for all users are stored in `Users`. In this directory there is a file called `MBR Flag.txt` which contains the flag.

![[thm-soln-28.png|500]]

> THM{Cure_The_MBR}

### Task 6: What if GPT?

**1. How many partitions are supported by the GPT?**

![[thm-soln-29.png|640]]

> 128

**2. What is the partition type GUID of the 2nd partition given in the attached GPT file?**

From the write-up we learn that the partition related metadata is stored in the GPT Partition Array. The partition array is located in the 3rd sector on the disk. Each entry in the partition array is 128 bytes. Each sector on the disk is 512 bytes.

We can get the starting address for the 3rd sector by calculating `512 * 2`. We multiply by 2 as the sector count starts from 0 so the 3rd sector becomes the 2nd sector. To this value we need to add 128 (size of entry in partition array) to get the start of the 2nd entry in the partition array. This comes out to `1152` ((512 \* 2) + 128).

![[thm-soln-30.png|240]]

From the table provided in the write-up we know that the first 16 bytes represent the partition type GUID. By following the instructions provided we can get the GUID in the correct format.

![[thm-soln-31.png|500]]

> E3C9E316-0B5C-4DB8-817D-F92DF00215AE

### Task 7: Threats Targeting GPT

**1. Complete this task**

> No answer required

### Task 8: UEFI Bootkit Case

**1. Which partition has the bootloader in it?**

![[thm-soln-32.png|640]]

> EFI System Partition

**2. What is the malicious string embedded in the bootloader?**

For this task we need to use `bootmgr.efi`. On scrolling a few lines I noticed a string that ended in “\==”.  Strings that end with equal signs are almost always base64 encoded.

![[thm-soln-33.png|500]]

```
SGVsbG8sIEVGSSBCb290a2l0IQ==
```

On decoding the string we get the malicious message.

[CyberChef - Decode Recipie](https://gchq.github.io/CyberChef/#recipe=From_Base64('A-Za-z0-9%2B/%3D',true,false)&input=U0dWc2JHOHNJRVZHU1NCQ2IyOTBhMmwwSVE9PQ)

![[thm-soln-34.png|600]]

> Hello, EFI Bootkit!
