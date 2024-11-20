---
title: "NTFS Filesystem: Alternate Data Stream (ADS)"
description: A deep dive into concepts related to the NTFS Filesystem
date: 2024-04-08 14:05:00 -0500
categories:
  - Windows
  - Filesystem
tags:
  - windows
  - filesystem
  - ntfs
  - security
  - forensics
published: true
media_subpath: /assets/
---

![[ntfs-alternate-streams-banner.png|640]]

In this article, we will start by briefly discussing how data is stored on hard drives. Then we will take a look at the NTFS filesystem and alternative data streams. After that, we will go over Zone Identifier a feature of Windows that uses data streams to store data about the origin of a file. Finally, we will also take a brief look at how data streams can be used to hide data.

### Storage Device

It is the hardware component that allows us to store and retrieve information from our computer. HDDs, SSDs and Thumb drives are all examples of storage devices.

![[hdd-platter.png|380]]

To understand how data is stored on storage devices we need to first understand some of the terms that are used to represent data on a disk. The below image represents a hard drive platter.

![[disk-structure.png|320]]

[Hard Disk Drive Basics - NTFS.com](https://www.ntfs.com/hard-disk-basics.htm)

The platter surface is divided into concentric circles called tracks. Each track forms a circular path around the disk. In the above image, the red region denotes a track.

The platter is also divided into geometric sectors which look like pizza slices. In the image above the blue region represents a geometric sector. The term geometric sector is not commonly used in the discussion of storage.

The intersection of the track and geometric sector creates a disk sector. A sector is the smallest unit that can be accessed on a storage device. All sectors on a disk hold the same amount of data. In the context of storage when the term sector is used it always means disk sector. In the above image, the label C represents a sector. The sector size is a physical property that is fixed by the storage device manufacturer and cannot be changed. 

A group of contiguous sectors is called a cluster. A cluster is made of one or more sectors. Clusters are also sometimes called Allocation Units. A cluster is the smallest logical amount of space that can be allocated for storing a file. The green section in the above image shows a cluster. Cluster size is a logical property and is set by the filesystem when the disk is formatted.

The sector is the smallest unit that the OS kernel/driver uses to read and write from the disk. Cluster on the other hand is the smallest unit used by the filesystem to read and write data from the disk. The cluster and sector size can be the same but usually, this is not the case. A cluster is always larger than a sector.  

[Disk sector - Wikipedia](https://en.wikipedia.org/wiki/Disk_sector)

![[disk-format-menu.png|220]]

The concept of sectors and clusters also applies to storage devices that use Flash memory for storage but, it is important to understand that this is only an abstraction to make it easy to understand data storage. The process of storing data on SSDs is different from the process used by HDDs.

### Filesystem

A filesystem is a logical and physical system for organizing, managing and accessing data on a storage device. Without a filesystem, an Operating System (OS) would see large chunks of data on the disk but would have no idea of how to read them. Think of the storage device as a large room that has piles of papers scattered all over the place. Locating a specific file in such a room would be quite difficult. A filesystem is like a filing cabinet that takes the scattered papers and organizes them making it easy to find the paper we require. 

[File system - Wikipedia](https://en.wikipedia.org/wiki/File_system)

There are many filesystem designs and implementations. Based on the implementation filesystems can have varying characteristics, some filesystems are optimized for speed while others are designed to be flexible and secure. Different Operating Systems utilize different file systems for storing their data. By default, Windows uses the NTFS (New Technology File System), Apple uses APFS (Apple File System) and Linux uses ext4 (Fourth Extended Filesystem).

### NTFS Filesystem

It is the default filesystem used by Windows since Windows 3.1. It is a proprietary filesystem and was designed by Microsoft to replace the FAT filesystem. NTFS is supported natively by Linux and BSD. NTFS supports features like an access control list (ACL), disk encryption, symbolic links and journaling.

[NTFS - Wikipedia](https://en.wikipedia.org/wiki/NTFS)

The layout of NTFS  can be broadly divided into four parts: Partition Boot Sector (PBS), Master File Table (MFT), System Files (Metadata Files) and User Files.

![[ntfs-filesystem-structure.png|520]]

The PBS makes up the first 16 sectors of the NTFS filesystem. This section contains the information that is used by the filesystem to access the actual data.

The MFT is a special file that represents each file that is present on the filesystem. All information about the file including the size, creation time, permissions and data content is stored in the MFT. The OS uses the MFT to locate the file it requires from the filesystem. Each file record in the MFT is 1KB (1024 bytes) in size. 

[File Recovery software and NTFS Master File Table (MFT)](https://www.file-recovery.com/recovery-NTFS-master-file-table-MFT.htm)

The starting entries in the MFT are used to represent system files that store metadata related to the filesystem. The first record of the MFT describes the MFT itself. The 2nd entry is the MFT mirror a copy of the MFT that is used if the main MFT is corrupted.

![[mft-structure.png|420]]

[34 File Entries on a Brand New $MFT – Half Full of Security](https://jon.glass/blog/34-file-entries-on-a-brand-new-mft/)

Depending on the OS and version of NTFS being used the amount of system files that are present on the filesystem can vary.

#### NTFS File Record

<iframe 
	width="560" height="315" 
	src="https://www.youtube-nocookie.com/embed/l4IphrAjzeY?si=XWttXw0_EWymYQ_w" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen>
</iframe>

The first 42 bytes of the File Record is used for file metadata. The header has a fixed size and structure. The remainder of the file record is used to store file attributes. 

Each unit of information associated with a file - name, security information, timestamp, content is implemented as a file attribute. Each attribute starts with a header. An attribute record contains the attribute type, an optional name and the attribute value. 

[File Record - Concept - NTFS Documentation](https://flatcap.github.io/linux-ntfs/ntfs/concepts/file_record.html)

![[ntfs-file-attributes.png|360]]

Attributes can be resident or non-resident. Attributes that can fit into the MFT are called resident attributes. Attributes like filename (`$FILE_NAME`) and timestamp (`$STANDARD_INFORMATION` and `$FILE_NAME`) are always stored in the MFT file record. When the attribute is too large to be stored in the MFT it is stored outside the MFT. Attributes stored outside the MFT are called non-resident attributes. The `$DATA` attribute stores the data of the file and is usually a non-resident attribute.

[Data Runs - Concept - NTFS Documentation](https://www.reddragonfly.org/ntfs/concepts/data_runs.html)

### Alternate Data Stream (ADS)

It is a feature of NTFS that allows files to contain more than one data stream. ADS makes it possible to store files within files. This feature was designed to provide compatibility with the MacOS Hierarchical Filesystem (HFS). HFS used a resource fork and a data fork (2 streams) to store the data of a file.

[Introduction to ADS – Alternate Data Streams \| hasherezade's 1001 nights](https://hshrzd.wordpress.com/2016/03/19/introduction-to-ads-alternate-data-streams/)

Alternate Data Streams are not shown in the File Explorer on Windows. Even command-line tools do not show ADS by default. The file size that is reported by Windows does not include the size of alternate file streams. From a security point of view, we should be cautious of ADS as it makes it possible to hide data within files.

[NtfsAlternateDataStreams.pdf](https://www.winitor.com/pdf/NtfsAlternateDataStreams.pdf)

#### List ADS Names

The following commands can be used to view the ADS of a file:

```powershell
Get-ChildItem | ForEach-Object {Get-Item -Path $_.FullName -Stream *} | Select-Object Filename, Stream, Length
```

![[ps-list-ads.png|640]]

```batch
dir /R
```

![[cmd-list-ads.png|600]]

```batch
streams -nobanner -s .
```

![[streams-list-ads.png|560]]

[Streams - Sysinternals \| Microsoft Learn](https://learn.microsoft.com/en-us/sysinternals/downloads/streams)

#### Zone Identifier

The most common use of ADS is to store "zone" data. This is a feature that was introduced with Windows 10. Zone Identifier is used to store details about the origin of the file. It is additional metadata that is added to files when they are downloaded from the Internet. 

Zone Identification data is stored in the `Zone.Identifier` stream. The stream contains the Zone ID, Host URL and Referrer URL. Zone ID is an integer that denotes the origin of the file. Files downloaded from the Internet have the ID 3. The host URL contains the URL from which the file was downloaded. The referrer URL contains the name of the domain that led the user to the domain from which the file was downloaded.

![[url-security-zones.png|280]]

Zone Identifier is an evolution of the URL Security Zone feature that was introduced in Windows XP. It was used by Internet Explorer to classify URLs into zones. Based on the zone different policies and security controls could be applied to the URLs. These options can still be accessed from the Internet Options menu.

![[internet-options-dialog.png|310]]

All modern browsers add zone data to downloaded files. Files downloaded using 3rd party download managers do not contain Zone Identifier data.

Applications can be programmed to handle files differently based on the existence of zone data. Microsoft Office will open files with zone data in Protected Mode. If we enable editing for the file the Zone Identifier stream is deleted.

![[office-protected-view.png|640]]

If we decompress a file with zone data using the Windows built-in extraction tools Zone Identifier stream is automatically added to all the files that are extracted. This does not occur when third-party archival software is used.

#### View ADS Content

The content of ADS can be viewed using the following commands:

```powershell
 Get-Content .\CS437.Lecture4.NTFS.pdf -Stream Zone.Identifier
```

![[ps-view-ads.png|640]]

```batch
more < CS437.Lecture4.NTFS.pdf:Zone.Identifier
```

![[cmd-view-ads.png|640]]

Depending on the source of the files all three fields may not be present.

```batch
more < 2024_02_07_anticast_All-About-Systemd-Timers_Hal-Pomeranz.pdf:Zone.Identifier
```

![[cmd-view-ads-2.png|640]]

#### Deleting Zone Identifier

Depending on who you ask Zone Identifier could be considered invasive. It makes it possible for a forensic investigator to analyze your device and find the origin of the downloaded files.

```powershell
Unblock-File .\CS437.Lecture4.NTFS.pdf
```

![[ps-delete-zone.png|560]]

```batch
streams -nobanner -d .\CS437.Lecture4.NTFS.pdf
```

![[streams-delete-zone.png|560]]

The properties menu of a file with zone data will always show a security warning. By unblocking the file the Zone Identifier data is deleted. 

![[gui-delete-zone.png|320]]

Zone Identifier can be permanently disabled using Group Policy.

[How to get rid of Zone.Identifier files - Realhe.ro blog](https://blog.realhe.ro/how-to-get-rid-of-zone-identifier-files/)

#### Custom Data Streams

It is possible to create custom data streams. Data streams can be created for directories as well. Using ADS it is possible to any data (even images, executes and DDLs) within other files. 

[ThreatSpike Blog: Exploring NTFS Alternate Data Streams](https://www.threatspike.com/blogs/alternate-data-streams)

To create a Alternate Data Stream we mention the stream name after the filename.

```powershell
Write-Output "Super Duper Secret Text" > .\ordinary.txt:SecretText
```

![[ps-create-ads.png|500]]

`Remove-Item` is a generic command for removing alternate data streams. It can also be used to remove Zone Identifiers. 

```powershell
Remove-Item .\ordinary.txt -Stream SecretText
```

![[ps-delete-ads.png|500]]

The following image shows ADS being used to hide executables.

![[ads-malware.png|420]]

### Further Reading

[Everything I Know About NTFS](https://kcall.co.uk/ntfs/)

[An Introduction to NTFS - New Technology File System](https://thestarman.pcministry.com/asm/mbr/IntNTFSfs.htm)

[CS 537 Notes - Section #26: Windows (NT) File Systems](https://pages.cs.wisc.edu/~bart/537/lecturenotes/s26.html)

[Forensic Analysis of the Zone.Identifier Stream - Digital Detective](https://www.digital-detective.net/forensic-analysis-of-zone-identifier-stream/)

[Windows Alternate Data Streams - BleepingComputer](https://www.bleepingcomputer.com/tutorials/windows-alternate-data-streams/)
