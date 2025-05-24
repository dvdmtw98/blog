---
title: "Linux Links Demystified: Symbolic Links and Hard Links Explored"
description: Explore the intricacies of symbolic links, hard links, and shortcuts on Linux.
date: 2025-05-10 21:00:00 -0500
categories:
  - Operating System
  - Linux
tags:
  - filesystem
  - operating-system
  - command-line
  - linux
published: true
media_subpath: /assets/
---

![[symbolic-links-linux-banner.png|640]]
_Banner icon created using ChatGPT_

> [!IMPORTANT] Changelog  
> - **May. 24, 2025**
> 	- Added a summary table at the end of the article.
> 	- Renamed the article to accurately capture the full scope of the article.
> 	- Updated cover image to align with the name change.

Symbolic links are special constructs that allow us to efficiently manage files. People commonly use them to create shortcuts, manage configurations, and organize files. While symlinks are the most prevalent link type, they're not the only option. This article explores the nuances of symlinks in Linux and briefly compares them to other link types: hard links and shortcuts.

### Symbolic Links

A symbolic link is a filesystem object that stores the path to another filesystem object (file/directory), also called “target.” When a symlink is accessed, the OS transparently resolves the path and moves us to that location. They are like a portal that teleports us to a different location on the system. Symlinks allow us to access the same file at multiple locations without duplicating its content.

A symbolic link is a filesystem abstraction. Symlinks can be used by all types of applications (e.g., GUI, CLI, scripts). To every application, the symlink will look and function like the target file/directory.

Symlinks can span filesystems (point to files on a different filesystem) and can also point to files on network shares. You do not have to be a root user to create them.

<iframe 
	width="560" height="315" 
	src="https://www.youtube-nocookie.com/embed/zfSa-PEU3h4?si=XxBlkyOKs4yzD6E-" 
	title="YouTube video player" 
	frameborder="0" 
	allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" 
	referrerpolicy="strict-origin-when-cross-origin" 
	allowfullscreen>
</iframe>

Most Unix-based systems (Linux, MacOS, FreeBSD) support symbolic links natively, and Windows has had support for them since Windows Vista. While symlinks function the same across all supported systems, the way they are implemented can be different.

![[linux-create-symlink-1.png|240]]
_Fig. 1: Files & Directories used in example_

For the examples, I will be using the files and directories shown in Fig. 1. “Source” and “Destination” are both in my home directory.

#### Creating Symlink

Symbolic links are created using the `ln` command with the `-s` option. 

```bash
ln -s [Target] [Link]
```

The 1st argument (target) is the path to the real file/directory. The 2nd argument (link) is the symlink that will be created. The command will fail if the link already exists. The command will create a symlink even if the target is invalid.

Symlinks can be created using absolute and relative paths. In Fig. 2 I have created a symlink using absolute paths. Creating symlinks using relative paths is confusing and is generally discouraged. For relative paths, the 1st argument (target) has to be defined relative to the 2nd argument (link). The 2nd argument (link) has to be defined relative to the current working directory.

![[linux-create-symlink-2.png|600]]
_Fig. 2: Creating symbolic link (for File)_

The file/directory to which the symlink is connected can be viewed by using the `-l` option of the `ls` command. Link files will always have their type bit (the 1st bit in the permission string) set to `l`.

[Linux File Permissions \| Digital Archive](https://notes.davidvarghese.net/operating-system/linux/commands/linux-file-permissions)

#### Modifying Symlink

Symlinks always have their permission set to 777 (`rwxrwxrwx`). This permission is never used, it is just a placeholder. Link files do not have their own permissions. They have the same permission as the target. 

If we change the permission on the link as shown in Fig. 3, the target’s permission will get changed. The permission on the symlink can never be changed. When any action is taken on the link the OS performs a permission check on the target to see if that action should be permitted.

![[linux-permission-link-1.png|550]]
_Fig. 3: Changing symbolic link permissions_

In Fig. 4, I modify the link file by writing data into it. This causes the data to also get written into the target. This makes sense, as a symlink is just a link. When we use the link, we are transparently accessing the file that is the target of the link. So any action we perform on the link, the OS applies that to the real file.

![[linux-create-symlink-3.png|500]]
_Fig. 4: Editing file using symbolic link_

Fig. 5 shows the same operation (data modification) being performed using the UI. Symlink behaves in the same way when accessed from GUI.

![[linux-create-symlink-4.gif|600]]
_Fig. 5: Editing file using symbolic link (GUI)_

Directory symlinks are created using the same syntax as file symlinks. 

![[linux-create-symlink-5.png|550]]
_Fig. 6: Creating symbolic link (Directory)_

Directory symlinks also set the type bit to `l` and have the permission set to 777. 

![[linux-create-symlink-6.png|540]]
_Fig. 7: Accessing directory using symbolic link_

If we create a file/directory using the directory link, the file/directory will get created inside the target directory. 

![[linux-create-symlink-7.png|360]]
_Fig. 8: Comparing original directory with symbolic link_

In the UI, the directory link will be shown as a directory. This is just an illusion. All link files (including directory links) are files. And the file only stores the path to its target.

![[linux-create-symlink-8.gif|600]]
_Fig. 9: Accessing directory using symbolic link (GUI)_

#### Symlink Information

We have already seen that we can view the target of a symlink using `ls -l`. Linux also has other commands that can display information about the symlink.

The `readlink` command will print the target of the link. The `stat` command can be used to view a lot all metadata pertaining to the link.

![[linux-stats-symlink-1.png|500]]
_Fig. 10: File symbolic link details_

![[linux-stats-symlink-2.png|500]]
_Fig. 11: Directory symbolic link details_

#### Broken Symlink

Sometimes symlinks can become invalid/broken. This happens when the original object (target) is moved/deleted. Symbolic links are not updated when the target is moved/deleted.

In Fig. 12 I moved `original.txt` to a different location. The link now points to an object that does not exist. This makes it invalid.

![[linux-broke-symlink-1.png|600]]
_Fig. 12: Moving original file breaks symbolic link_

Most modern Linux systems will use a different color/icon to denote a broken link. So identifying a broken link shouldn’t be a big challenge. There are also commands to find broken links.

![[linux-broke-symlink-2.png|440]]
_Fig. 13: Broken symbolic link (GUI)_

A broken link can be fixed with the `ln` command with the `-sf` option. This option will delete the existing link and create a new link in its place.

![[linux-create-symlink-9.png|520]]
_Fig. 14: Fixing broken symbolic link_

#### Finding Symlink

The `find` command provides an option that makes it easy to locate all the links on a system.

![[linux-find-symlink-1.png|640]]
_Fig. 15: Finding symbolic links_

In its simplest form, this command allows us to locate all the links that are located in a directory (includes broken links).

```bash
find ~/Destination -type l -ls
```

This slightly more complicated version can be used to find only broken links. This command tests the target of each link to check if it exists.

```bash
find ~/Destination -type l -not -exec test -e {} \; -ls
```

The `-ls` at the end of the command can be replaced with `-delete` to delete all the broken links in the directory. This can be dangerous. Only use this option if you know what you are doing.

[The Complete Guide to Searching Files in Linux | Steve's Data Tips and Tricks](https://www.spsanderson.com/steveondata/posts/2024-12-27/)

#### Deleting Symlink

If we don’t need a link anymore, we can delete it using the `unlink` command. Links can be deleted from the GUI just like regular files. Links can also be deleted using the `rm` command.

![[linux-delete-symlink-1.png|540]]
_Fig. 16: Deleting symbolic link_

Be careful when using these command. They will result in data loss if executed on the target.

### Hard Links

On Linux, every file is associated with an inode. It is a data structure that is used by the ext4 filesystem to store file metadata. Every file gets its own inode. Each row in the inode stores an attribute of the file. Some of the metadata stored include the inode number, file size, permission, and location of data on disk. Importantly, inode does not store the filename.

[DevOps on Linux - Filesystem \| Medium](https://freedium.cfd/https%3A%2F%2Fmedium.com%2Fgeekculture%2Fdevops-in-linux-file-system-933b1458789a)

A hard link is an alternative name (alias) for a file. It is a label that points to the same inode as the original file. Hard links share all of their metadata with the original file (leaving the name if created in a different directory). From the point of view of the filesystem, there isn’t an original and linked file. A hard-linked file is indistinguishable from the original file. I am using the terms “original” and “hard linked” only to make it easy to differentiate between them.

While symbolic links are considered a filesystem abstraction, the OS plays a huge role in making them work. The OS has to redirect all the operations performed on the link to the real file/directory. Hard links, on the other hand, do not need any special handling from the OS. It is a pure filesystem abstraction. Hard link is a feature in the data structure used to represent files that allows multiple labels to be created that point to the same data on disk.

Hard links cannot span filesystems. Also, they cannot be used to point to files on network shares. They can be created without root permissions.

#### Creating Hard Link

Hard links are created using the `ln` command without the `-s` option. In Fig. 17, observe how the attributes of `linked.txt` are the same as `original.txt`. Compare that with Fig. 3 from the symbolic link section. Also observe how, for hard links, the inode numbers (1st column in output) are the same. This is not true in the case of symlink.

```bash
ln [Target] [Link]
```

We know that hard links pull data from the same inode as the original file. So it makes sense that the values are the same as the original file. A symlink, on the other hand, is a new file, so it gets its own inode, so it does not share its attributes with the original file.

![[linux-hardlink-1.png|460]]
_Fig. 17: Creating hard link_

#### Modifying Hard Link

Hard links cannot be created for directories. For them the only option is to use a symlink. In Fig. 18 I am writing data into the linked file, and we can see the same data is accessible from the original file.

![[linux-hardlink-2.png|460]]
_Fig. 18: Modifying content using link_

#### Finding Hard Link

Finding all the hard links of a file is complicated. From the point of view of the OS the hard linked file is nothing special. You would have to write a script to combine the results from multiple commands to be able to find the hard links for all files in a directory.

The `-links +1` option of the `find` command will list files that have hard links. The results of this command, along with the `-samefile` option, can be used to find other files that have the same inode.

![[linux-hardlink-3.png|500]]
_Fig. 19: Finding hard links_

Hard links do not become invalid/broken. Since they point to an inode they can be moved freely without any side effect.

#### Deleting Hark Link

Since the original and hard-linked file are the same, we can delete either of them without losing data. This has been demonstrated in Fig. 20. This is different from symlinks, where deleting the original file will cause data loss.

![[linux-hardlink-4.png|340]]
_Fig. 20: Deleting hard link_

### Shortcuts

Shortcuts are just text files. They are user-level objects. They use the `.desktop` extension. Along with the target path, they store metadata information like shortcut name, icon, and launch arguments. Shortcut files can only be followed by shell-aware (GUI) applications (e.g., File Explorer). Special programs are required to resolve them from the CLI. A shortcut on Linux will never look and function like the original file/directory.

To show how different shortcuts are different from links, I have included some examples to demonstrate how they behave when accessed from CLI and GUI.

![[linux-shortcut-1.png|440]]
_Fig. 21: Shortcut to open a file_

The `Exec` line denotes the action to be performed when the shortcut is clicked.

![[linux-shortcut-2.png|440]]
_Fig. 22: Shortcut to open a directory_

Shortcuts behave differently based on where they are located on the system. 

Fig. 23 shows how shortcuts behave when accessed from most locations on the system. For a shortcut to work, it needs to be placed in specific directories.

![[linux-shortcut-3.gif|600]]
_Fig. 23: Launching shortcut from arbitrary location_

In Fig. 24 we see how shortcuts behave when placed in `~/Desktop`. This is a special folder. Shortcuts placed in this directory show up on the desktop. Using the shortcut from the desktop will run the command mentioned in the `Exec` line.

![[linux-shortcut-4.gif|600]]
_Fig. 24: Launching shortcut from Desktop_

Shortcuts cannot be opened natively from the CLI as shown in Fig. 25. Only shell-aware (GUI) programs know how to parse the shortcut file.

![[linux-shortcut-5.gif|600]]
_Fig. 25: Launching shortcut from terminal_

Third-party programs like `dex` can be downloaded that parse shortcuts and launching them from the terminal.

### Summary Table

To wrap things up, I have created a table that compares and contrasts the different link objects.

| Feature                             | **Symbolic Link**           | **Hard Link**                | **Shortcut (.desktop file)** |
| :---------------------------------- | :-------------------------- | :--------------------------- | :--------------------------- |
| **Target Type**                     | File or Directory           | File                         | File or Directory            |
| **Span Network Drives**             | Yes                         | No                           | Yes                          |
| **Span Filesystems**                | Yes                         | No                           | Yes                          |
| **Requires Admin to Create**        | No (just write permission)  | No (just write permission)   | No                           |
| **Transparent to User**             | Yes (fully)                 | Yes (fully)                  | No (requires desktop env.)   |
| **Breaks if Source Moved/Deleted?** | Yes (becomes dangling)      | No (last link removed)       | Yes (link broken)            |
| **Internal Path Type**              | Absolute or Relative        | N/A (same inode)             | Absolute (usually)           |
| **Implementation**                  | Special Inode (stores path) | Directory Entry (same Inode) | Plain text file              |

### Conclusion

Mastering symbolic links enhances your ability to manage files and directories efficiently. Understanding the distinctions between symlinks, hard links, and shortcuts is crucial for understanding when each should be used. As we've seen, each one tries to solve the same problem but achieves it in different ways.

In Part 2, we'll explore how these concepts translate into the Windows operating system. These articles combined should provide you with a comprehensive cross-platform perspective on this topic.

[Windows Links Demystified: Symbolic Links, Hard Links, and Junctions Explored](https://blog.davidvarghese.net/posts/windows-links-demystified)

### Further Reading

- [Hard and symbolic link explained in a simple way \| Reddit](https://www.reddit.com/r/linuxquestions/comments/uiv84r/can_anyone_describe_the_purpose_of_hard_and/)
- [Purpose of creating a symbolic links \| Stack Overflow](https://stackoverflow.com/questions/58314491/what-is-the-purpose-of-creating-a-symbolic-link-between-files)
- [10 ways to use the Linux find command \| Red Hat Blog](https://www.redhat.com/en/blog/linux-find-command)
- [Desktop Entries \| Arch Linux](https://wiki.archlinux.org/title/Desktop_entries)
- [What is a directory if everything is a file? \| Ask Ubuntu](https://askubuntu.com/questions/1073802/what-are-directories-if-everything-on-linux-is-a-file)
