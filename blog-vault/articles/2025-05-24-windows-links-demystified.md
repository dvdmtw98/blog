---
title: "Windows Links Demystified: Symbolic Links, Hard Links, and Junctions Explored"
description: Explore the intricacies of symbolic links, hard links, junctions, and shortcuts on Windows.
date: 2025-05-24 15:00:00 -0500
categories:
  - Operating System
  - Windows
tags:
  - filesystem
  - operating-system
  - command-line
  - windows
published: true
media_subpath: /assets/
---

![[symbolic-links-windows-banner.png|640]]
_Banner icon created using ChatGPT_

On Windows, there are several ways to reference files and folders without duplicating them. These include symbolic links, hard links, junctions, and shortcuts. While they all serve similar purposes, each one has unique characteristics that make them ideal for different use cases. This article explores how these linking methods work while highlighting their differences.

### Symbolic Links

![[windows-create-symlink-1.png|280]]
_Fig. 1: Files & directories used in example_

For the examples, I will be using the files and directory shown in Fig. 1. The “Source” and “Destination” directories are located on my `E:` drive.

#### Creating Symlink

On Windows we have 2 shells: PowerShell and Command Prompt. Both shells use different commands. Wherever possible, I have included the command for both the shells.

In PowerShell, symbolic links are created using `New-Item` with the `-ItemType` parameter set to `SymbolicLink`. Fig. 2 shows how this command can be used.

```powershell
New-item [Link] -ItemType SymbolicLink -Target [Target]
```

On Windows, the link argument comes before the target argument. This command is the reverse of the Linux command. Quick refresher: target is the real file/directory, and link is the symbolic link to be created.

Similar to Linux, if we try to create a link to a target that does not exist, we don’t get an error. If we try to create a link and an object with that name already exists, then the command will fail.

On Windows, symbolic links cannot be created by non-privileged users. This is the default setting and can be changed. To try these commands on your system, run them from an elevated PowerShell and Command Prompt.

![[windows-create-symlink-2.png|560]]
_Fig. 2: File symbolic link creation (PowerShell)_

Symlinks have the 1st bit in the mode section set to `l` (same as Linux). For directories, the 1st bit is `d`. For regular files, the 1st bit is empty.

Windows symbolic links can span partitions (volumes). This means the target and link can be on different drives. Symbolic links can also be created for objects stored on a network share. Windows symbolic links cannot span filesystems as they are implemented using a feature that is exclusive to NTFS.

Symlinks can be created using relative and absolute paths. In Figs. 2 and 3, symlinks are created using absolute paths. When using relative paths, the link has to be relative to the current working directory, and the target has to be relative to the link.

To create file symbolic links using Command Prompt, we have to use the `mklink` command. The 1st argument is the link, and the 2nd argument is the target.

```shell
mklink [Link] [Target]
```

![[windows-create-symlink-3.png|500]]
_Fig. 3: File symbolic link creation (Command Prompt)_

Actions that we perform on the link are transparently applied by the system on the target. Changing the permission of a symlink causes the permission of the target to change (same as Linux).

Most CMD commands can also be executed from PowerShell by prefixing them with `cmd /c`. So for this command, you could use:

```powershell
cmd /c mklink [Link] [Target]
```

Permission and access controls on Windows are quite complex. Windows uses ACL (Access Control List) for access management. ACLs are outside the scope of this article. In Figs. 4 and 5, just note how changing the permission on the link changes it on the target.

In Fig. 4, the owners & the permissions of the file and symlink are shown. The permissions are the same for both the files, but the owner is different. This makes sense, as the link was created using administrator privilege, so it's owned by the administrator.

![[windows-access-symlinks-1.png|450]]
_Fig. 4: Checking permission of symbolic link_

In Fig. 5 I have used the `icacls` command to remove the “Read” permission from the group Users. I performed this operation on the link, but the permission on the target also got changed.

![[windows-access-symlinks-2.png|450]]
_Fig. 5: Changing permission of symbolic link_

> [!NOTE]
> As per the `icacls` documentation, if the `/l` option is used, then only the permission on the link should change. The target would be left unchanged.
> 
> I tried this option but could not get it to work. If anyone knows of a way to change the permission of a link without changing the permission of the target, let me know. I would love to understand how it's done.

[Integrity Control Access Control Lists (icacls) \| Microsoft Learn](https://learn.microsoft.com/en-us/windows-server/administration/windows-commands/icacls)

Writing content in the file symlink causes the content to be written into the target. Figs. 6, 7, and 8 all show this operation using different approaches.

![[windows-create-symlink-4.png|600]]
_Fig. 6: Writing data into file symbolic link (PowerShell)_

![[windows-create-symlink-5.png|400]]
_Fig. 7: Writing data into file symbolic link (Command Prompt)_

In Fig. 8, observe how when the link file is opened, the target filename is shown. Notepad follows the link and opens the real file.

![[windows-create-symlink-6.gif|600]]
_Fig. 8: Writing data into file symbolic link (GUI)_

The command to create a directory and file symlink is the exact same in PowerShell.

![[windows-create-symlink-7.png|560]]
_Fig. 9: Creating directory symbolic link (PowerShell)_

In Command Prompt, to create a directory link, we have to use the `/D` option. Notice the link type shown in the output of Fig. 10. Command Prompt shows file links as `<SYMLINK>` and directory symlinks as `<SYMLINKD>`.

![[windows-create-symlink-8.png|500]]
_Fig. 10: Creating directory symbolic link (Command Prompt)_

In Figs. 11 and 12, we can see how accessing the symlink feels exactly like accessing the target directory.

![[windows-create-symlink-9.png|440]]
_Fig. 11: Accessing directory symbolic link_

![[windows-create-symlink-10.png|420]]
_Fig. 12: Comparing directory link with original real directory_

In Fig. 13 I have the symlink and the target open in different windows. You can see that when I create a file in the symlink, it immediately shows up in the target directory. When I rename the file, it also gets renamed in the target.

![[windows-create-symlink-11.gif|600]]
_Fig. 13: Creating file using inside directory symbolic link (GUI)_

#### Symlink Information

In Linux, symlinks are implemented with a file that only stores the path to the target. On Windows, links are implemented using reparse points (I will cover a bit more about them in a later section).

The `fsutil` command can be used to read reparse point files. This command shows us the raw data that is stored in the reparse file.

```powershell
fsutil reparsepoint query [Link]
```

![[windows-stats-symlink-1.png|500]]
_Fig. 14: Viewing content inside link_

The `Get-Item` command can also be used to fetch information about the link. This command is similar to the `stat` command on Linux.

![[windows-stats-symlink-2.png|580]]
_Fig. 15: Symbolic link information (File)_

![[windows-stats-symlink-3.png|560]]
_Fig. 16: Symbolic link information (Directory)_

#### Breaking Symlink

Moving the target causes the corresponding links to break. Windows does not differentiate between working and broken links. This makes them visually impossible to distinguish.

In Fig. 17, when I tried to access a broken link, I got the message target not found.

![[windows-broke-symlink-1.png|600]]
_Fig. 17: Accessing invalid/broken symbolic link_

In Fig. 18 we can see that even though the 2 links to the text file are broken, they appear like normal functioning links. Clicking on a broken link will not perform any action, and no error message will be shown.

![[windows-broke-symlink-2.png|420]]
_Fig. 18: Invalid/broken symbolic link (GUI)_

Windows does not have an `-sf` equivalent. Quick refresher: The `-sf` option deletes the existing link and creates a new link in its place. On Windows, when a link breaks, we have to manually delete the broken link and then create a new symlink.

#### Finding Symlink

Command Prompt does not have an option to only list symlinks. Using `dir` with the `/A:L` (All Links) option is the only choice. This will, however, list everything in the directory that is a reparse point.

![[windows-find-symlink-1.png|520]]
_Fig. 19: Finding symbolic links (Command Prompt)_

CMD does not have a simple way to list broken links. You could write a batch script, but that is outside the scope of this write-up.

On the other hand, PowerShell gives us robust commands that allow us to find all links and only broken links. Fig. 20 shows how all the links in a directory can be found. Fig. 21 shows how we can perform a lookup on the target to see if it exists.

```powershell
Get-ChildItem -Path "E:\Destination" -Recurse `
	| Where-Object { $_.LinkType -eq 'SymbolicLink' }
```

The `Get-ChildItem` command returns all the objects in the directory. Then, using `Where-Object` a check is performed to only return links.

![[windows-find-symlink-2.png|620]]
_Fig. 20: Finding symbolic links (PowerShell)_

```powershell
Get-ChildItem -Path "E:\Destination" -Recurse | Where-Object {
    $_.LinkType -eq 'SymbolicLink' -and -not (Test-Path $_.Target)
}
```

This command is similar to the previous one. We expand the condition to add a test to check if the target is accessible.

![[windows-find-symlink-3.png|620]]
_Fig. 21: Finding broken symbolic links (PowerShell)_

```powershell
Get-ChildItem -Path "E:\Destination" -Recurse | Where-Object {
    $_.LinkType -eq 'SymbolicLink' -and -not (Test-Path $_.Target)
} | Remove-Item -Force -WhatIf
```

This command chains the `Remove-Item` command to delete symlinks that are returned by the command on its left. The `-WhatIf` option allows us to safely see which files will be deleted if the command is executed. To actually delete the files, the option `-WhatIf` has to be removed.

```powershell
Get-ChildItem -Path "E:\Destination" -Recurse | Where-Object {
    $_.LinkType -eq 'SymbolicLink' -and -not (Test-Path $_.Target)
} | ForEach-Object {
    $answer = Read-Host "Delete broken symlink '$($_.FullName)'? (Y/N)"
    if ($answer -eq 'Y') { $_ | Remove-Item -Force }
}
```

This is yet another way to delete broken symlinks. This version will show a prompt for each broken link and, based on user input, make a decision.

#### Deleting Symlink

On Command Prompt to delete file symlinks, we have to use the `del` command, and for directory symlinks, we have to use the `rmdir` command.

![[windows-delete-symlink-1.png|520]]
_Fig. 22: Deleting symbolic link (Command Prompt)_

On PowerShell, file and directory symlinks can be removed using the `Remove-Item` command.

![[windows-delete-symlink-2.png|260]]
_Fig. 23: Deleting symbolic link (PowerShell)_

Be careful when using the delete commands. Make sure the path you are using is the path for the symlink. Deleting the wrong item can result in data loss. 

### Reparse Point

A reparse point is a special object in the NTFS filesystem that allows Windows to add new features to the NTFS filesystem. A reparse point is like a building block that can be used to implement different link-type objects. A reparse file contains information that instructs Windows how the file has to be handled.

A reparse point has 2 main fields. The reparse tag and reparse data. The reparse tag indicated the link type. In symbolic links, the reparse tag uses the value `IO_REPARSE_TAG_SYMLINK` (`0xA000000C`). The reparse data contains the path to the target. Now take a look at Fig. 14, and it should be much easier to understand.

<iframe 
	width="560" height="315" 
	src="https://www.youtube-nocookie.com/embed/RDH5IuyPJtk?si=iE6SUMzWNUAKL3pZ" 
	title="YouTube video player" 
	frameborder="0" 
	allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" 
	referrerpolicy="strict-origin-when-cross-origin" 
	allowfullscreen>
</iframe>

If you use OneDrive on Windows, you would have come across the feature that allows files to show up locally but be downloaded only when required. This functionality is also implemented using reparse points.

![[windows-reparse-1.png|400]]
_Fig. 24: OneDrive on-demand files_

![[windows-reparse-2.png|600]]
_Fig. 25: On-demand file reparse point_

As per the documentation, multiple tags exist to denote OneDrive files. The OneDrive on-demand files on my system use the tag `IO_REPARSE_TAG_CLOUD_6` (`0x9000601A`). The reparse data contains information about the file, its location in OneDrive, and its status.

[Reparse Point Tags \| Microsoft Learn](https://learn.microsoft.com/en-us/windows/win32/fileio/reparse-point-tags)

There are many other features in Windows that are implemented using reparse points. If all this was a bit much, just remember that a reparse point is a special file type, and it's used to implement symlinks on Windows.

### Shortcuts

Shortcuts on Windows are much more seamless than the Linux equivalent. On Windows, shortcuts are represented by the `.lnk` extension. Shortcuts on Windows are in binary format; we cannot open them in a text editor to view their content.

Creating shortcuts using CLI is a little tricky. There isn’t a one-liner to create it. Figs. 26, 27, and 28 show how we can create a shortcut using the GUI.

![[windows-shortcut-1.png|400]]
_Fig. 26: Creating Shortcut (GUI)_

![[windows-shortcut-2.png|450]]
_Fig. 27: Creating Shortcut (GUI)_

![[windows-shortcut-3.png|450]]
_Fig. 28: Creating Shortcut (GUI)_

Windows shortcuts can be placed anywhere on the system. They do not have to be in any specific location. This is different from how it was on Linux. Fig. 29 shows how shortcuts can be used from the GUI. Another thing to note is how the icons for shortcuts and symlinks are the same. It can be difficult to tell them at a glance. 

![[windows-shortcut-4.gif|600]]
_Fig. 29: Using Shortcut (GUI)_

Shortcuts are one of the few object types for which the extension is hidden in Explorer even when the “Show File Extension” option is enabled.

Since `.lnk` files use a binary format, they cannot be analyzed in a text editor. There are 3rd-party tools like the one developed by Eric that allow you to view the information stored in the shortcut.

![[windows-shortcut-5.png|540]]
_Fig. 30: Analyzing shortcut_

[Eric Zimmerman’s Tools \| MDwiki](https://ericzimmerman.github.io/#!index.md)

Shortcuts on Windows can be opened directly from PowerShell and Command Prompt. Fig. 31 shows how they can be launched from PowerShell, and Fig. 32 shows the same using Command Prompt.

![[windows-shortcut-6.gif|600]]
_Fig. 31: Using Shortcut (PowerShell)_

![[windows-shortcut-7.gif|600]]
_Fig. 32: Using Shortcut (Command Prompt)_

### Hard Links

A hard link is an alternative name (alias) for a file. Similar to Linux, hard links can only be created for files. Hard links on Windows function the same as Linux hard links, but both are implemented in a different manner. This is because hard links are a feature of the filesystem and vary based on the data structures used by the filesystems. Windows normally uses NTFS, while Linux normally uses the ext4 filesystem.

NTFS utilizes a centralized table to store the metadata of the files. This table is called MFT (Master File Table). This table is saved as a file on the filesystem itself. Each row in the table represents a new file. Each row stores information about various aspects of the file. The name of the file is also stored in the MFT (not true on Linux).

Each file also has an attribute called reference count. This field is incremented by one whenever a new hard link is created. When the file is deleted, the count is decremented by one. When the count becomes zero, the file is marked for deletion.

When a hard link is created, a new entry is added in the MFT. The metadata of this entry will be the same as the original file. The entry will also point to the exact same location on disk as the original file. Do note that from the point of view of the filesystem, there is no original file and hard-linked file; they are exactly the same. I am only using these terms to make it easy to explain the concept.

Hard links cannot be created across partitions (volumes) and filesystems. This makes sense; each partition has its own MFT, so each volume can only reference data that is present in its MFT. Since each filesystem implements hard links differently, it's not possible to create a link that spans filesystems. Additionally, hard links cannot point to files on network drives.

#### Creating Hard Link

In PowerShell, hard links are created using `New-Item` with the `-ItemType` parameter set to `HardLink`. Fig. 33 shows how a symlink can be created using PowerShell.

```powershell
New-item [Link] -ItemType HardLink -Target [Target]
```

You do not have to be an administrator to create hard links. Hard links, just like symlinks, can be created using absolute and relative paths.

In Fig. 33, see how the attributes for the hard link are exactly the same as the original file. This is expected as they are both the same file.

![[windows-hard-link-1.png|520]]
_Fig. 33: Creating Hard Link (PowerShell)_

To create symbolic links using Command Prompt, we have to use the `mklink` command with the `/H` flag. The 1st argument is the link, and the 2nd argument is the target. This has been shown in Fig. 34.

```shell
mklink /H [Link] [Target]
```

![[windows-hard-link-2.png|480]]
_Fig. 34: Creating Hard Link (Command Prompt)_

#### Modifying Hard Link

Just like Figs. 6 and 7, we can see in Fig. 35 that writing data into the link causes it to be updated in the original file. Remember, a hard link is just a different name for the file, so we are technically writing to the same location when using either name.

![[windows-hard-link-3.png|520]]
_Fig. 35: Modifying file using Hard Link_

#### Finding Hard Link

Hard links are not represented using any special icon. They are exactly the same as the original file.

![[windows-hard-link-4.png|300]]
_Fig. 36: Hard Link vs. Original File_

To view all the references (hard links) of a file, the `fsutil` command can be used. This command can be called from PowerShell and Command Prompt.

```powershell
fsutil hardlink link [File]
```

Since the linked file is equivalent to the original file, there isn’t a simple way to list all the files in a directory that have a reference point greater than 1. You would have to write a script to achieve something of that sort.

![[windows-hard-link-5.png|340]]
_Fig. 37: List all references of a file_

#### Deleting Hard Link

On PowerShell, hard links are deleted using the `Remove-Item` command.

![[windows-hard-link-6.png|420]]
_Fig. 38: Deleting Hard Link (PowerShell)_

On Command Prompt, the link is deleted using the `del` command. Deleting the original file has no effect on the hard link. I have shown this in Fig. 39. 

![[windows-hard-link-7.png|300]]
_Fig. 39: Deleting Hard Link (Command Prompt)_

### Junctions

Junctions are essentially symbolic links that can only be created for directories. Junction was introduced with the launch of NTFS 3.0 in Windows 2000. They are much older than symbolic links. Like symbolic links, they are implemented using reparse points.

Junctions can point to directories that exist on different volumes (partitions) on the same system. They cannot point to files on a different filesystem as it relies on a feature only found on NTFS. Junctions cannot be used to point to files that are on a network share.

Junctions can be created without elevated privileges. Similar to symlinks, moving/deleting the original file causes the junction to become broken. Junctions can be created using relative or absolute paths. But, unlike symlinks, the path is always stored in the reparse point as an absolute path.

#### Creating Junctions

In PowerShell, junctions are created using `New-Item` with the `-ItemType` parameter set to `Junction`. Fig. 40 shows how a junction can be created using PowerShell. Notice how the junction looks exactly like a symlink.

```powershell
New-item [Link] -ItemType Junction -Target [Target]
```

![[windows-junctions-1.png|520]]
_Fig. 40: Creating Junction (PowerShell)_

To create junctions using Command Prompt, we have to use the `mklink` command with the `/J` flag. The 1st argument is the link, and the 2nd argument is the target. This has been shown in Fig. 41.

```shell
mklink /J [Link] [Target]
```

![[windows-junctions-2.png|500]]
_Fig. 41: Creating Junction (Command Prompt)_

There is one thing in Fig. 41 that is quite peculiar. The path that is shown for the junction that was created using PowerShell starts with an `/??/`. This is a namespace (I will briefly touch on this concept in the next section). All paths on Windows are internally represented using this format. For now just accept the fact that both paths are the same.

#### Junction Information

Since junctions are created using reparse points, we can use `fsutil` to read its content.

```powershell
fsutil reparsepoint query [Link]
```

Observe the “Substitute Name” field in Fig. 42 and Fig. 43; they both point to the same location. The reason the junction created using CMD did not show this is because CMD adds an extra field called “Print Name” to the reparse point. This hides the real lookup path from the user.

![[windows-junctions-4.png|500]]
_Fig. 42: Reparse Point (Junction)_

The reparse tag for Junctions is `0xA0000003` (`IO_REPARSE_TAG_MOUNT_POINT`). 

![[windows-junctions-5.png|500]]
_Fig. 43: Reparse Point (Junction)_

Metadata about the reparse point can also be viewed using the `Get-Item` command.

![[windows-junctions-9.png|520]]
_Fig. 44: Junction Metadata_

#### Finding Junctions

Since Junctions use reparse points, they can be easily identified and filtered using PowerShell. Fig. 45 shows how we can list all the junctions in a directory.

```powershell
Get-ChildItem -Path "E:\Destination" -Recurse `
	| Where-Object { $_.LinkType -eq 'Junction' }
```

![[windows-junctions-6.png|540]]
_Fig. 45: Finding Junctions (PowerShell)_

Just like symbolic links, junctions can break. This happens when the source directory is deleted or moved. Windows will not visually indicate that the junction is broken. The following command can be used to list all broken junctions in a directory.

```powershell
Get-ChildItem -Path "E:\Destination" -Recurse | Where-Object {
    $_.LinkType -eq 'Junction' -and -not (Test-Path $_.Target)
}
```

Command Prompt does not have a command to only list junctions. The option `/A:L` will list all objects in the directory implemented using reparse point. The output in the terminal will show that type of the reparse point so that can be used to filter the results. You would have to write a batch script if you wanted a more granular output.

![[windows-junctions-10.png|500]]
_Fig. 46: Finding Junctions (Command Prompt)_

Just like symlinks, we can see in Fig. 47 that junctions are shown in the GUI with an arrow on the bottom left indicating that it's a link.

![[windows-junctions-11.png|320]]
_Fig. 47: Viewing Junctions (GUI)_

#### Deleting Junctions

Reparse points can be deleted using the `Remove-Item` command from PowerShell.

![[windows-junctions-7.png|540]]
_Fig. 48: Deleting Junction (PowerShell)_

From CMD we would have to use the `rmdir` command.

![[windows-junctions-8.png|400]]
_Fig. 49: Deleting Junction (Command Prompt)_

Be extra careful when deleting junctions, as deleting the wrong item will result in data loss.

### NT Object Manager Namespace

So when we were looking at paths for junctions, we noticed that they always begin with `/??/`. This is what NTFS calls a namespace object. This specific namespace is called “Global” and is also denoted as `/GLOBAL??/`. Global is the namespace that is used by the Windows kernel to map the logical volumes (`C:`, `D:`) to the physical volumes. The component of Windows that manages the namespaces is called the Object Manager.

The drive letters that we use are abstractions that only exist to make it easy for us to remember the volume on which our data is stored. The global namespace stores the real path, which the OS uses to find our data.

<iframe 
	width="560" height="315" 
	src="https://www.youtube-nocookie.com/embed/XkC64XM8XZY?si=s1LxTPCWZZB3Lynz" 
	title="YouTube video player" 
	frameborder="0" 
	allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" 
	referrerpolicy="strict-origin-when-cross-origin" 
	allowfullscreen>
</iframe>

We can think of the global namespace like the root (`/`) directory on Linux. It is the parent of all mounted volumes on Windows. In Fig. 49 we can see that the `E:` drive on my device corresponds to the partition `\Device\HarddiskVolume8`. `\Device\` is also a namespace. This namespace stores the low-level mapping for various devices on the system.

Fig. 49 shows how `WinObj` (a tool from the System Internal Suite) can be used to view the various namespaces available on Windows.

[WinObj - Sysinternals \| Microsoft Learn](https://learn.microsoft.com/en-us/sysinternals/downloads/winobj)

Every object under this namespace is listed as a symlink. And based on our discussion, this makes sense. When we access one of the drives, the kernel is redirecting the data lookup to `\Device\HarddiskVolumeX`. This is exactly what a symlink does. The symlinks present in the Object Manager are kernel-level symbolic levels. They are not the same as the ones we discussed previously. We cannot create them using `mklink` and `New-Item`.

![[windows-junctions-3.png|640]]
_Fig. 50: NT Kernel Drive Mapping_

[Object Manager - Wikipedia](https://en.wikipedia.org/wiki/Object_Manager)

> [!NOTE]
> I have simplified some of the concepts in this section. This is only a high-level look at the NT Object Manager. This is a very advanced topic. I would suggest looking at the official documentation to get a fuller understanding of how the object manager works.

### Summary Table

To wrap things up, I have created a table that compares and contrasts the different link objects.

| Feature                             | **Symbolic Link (File)** | **Symbolic Link (Directory)** | **Hard Link**            | **Junction**                 | **Shortcut (.lnk file)** |
| :---------------------------------- | :----------------------- | :---------------------------- | :----------------------- | :--------------------------- | :----------------------- |
| **Target Type**                     | File                     | Directory                     | File                     | Directory                    | File or Directory        |
| **Span Volumes**                    | Yes                      | Yes                           | No                       | Yes                          | Yes                      |
| **Span Network Drives**             | Yes                      | Yes                           | No                       | No                           | Yes                      |
| **Span Filesystems**                | Yes                      | Yes                           | No                       | No (NTFS-only for both ends) | Yes                      |
| **Requires Admin to Create**        | Yes (unless Dev Mode)    | Yes (unless Dev Mode)         | No                       | No                           | No                       |
| **Transparent to User**             | Yes (mostly)             | Yes (mostly)                  | Yes (fully)              | Yes (fully)                  | No (requires shell)      |
| **Breaks if Source Moved/Deleted?** | Yes (becomes dangling)   | Yes (becomes dangling)        | No (last link removed)   | Yes (becomes dangling)       | Yes (link broken)        |
| **Internal Path Type**              | Absolute or Relative     | Absolute or Relative          | N/A (same data)          | Absolute                     | Absolute (usually)       |
| **Implementation**                  | NTFS Reparse Point       | NTFS Reparse Point            | MFT Entry (same File ID) | NTFS Reparse Point           | Shell (file data)        |

**"Yes (mostly)" for Symbolic Links:** Some older applications might have issues, or their resolution might differ slightly depending on client versus server processing over a network.  
**"Yes (fully)" for Hard Links and Junctions:** These are resolved at a lower filesystem level and are extremely transparent.

### Conclusion

Understanding the differences between symbolic links, hard links, junctions, and shortcuts in Windows can help you manage your files more effectively. Each method offers distinct advantages. By choosing the appropriate linking method, you can enhance your workflow and file organization within the Windows environment.

### Further Reading

- [NTFS reparse point \| Wikipedia](https://en.wikipedia.org/wiki/NTFS_reparse_point?utm_source=chatgpt.com)
- [LNK File Analysis: LNKing It Together! \| Medium](https://syedhasan010.medium.com/forensics-analysis-of-an-lnk-file-da68a98b8415)
- [Create a shortcut (.lnk file) using PowerShell \| Stack Overflow](https://stackoverflow.com/questions/9701840/create-a-shortcut-lnk-file-using-powershell)
- [Managing Kernel Objects - Windows drivers \| Microsoft Learn](https://learn.microsoft.com/en-us/windows-hardware/drivers/kernel/managing-kernel-objects)
- [Meandering Through the Object Manager \| OSR Online](https://www.osronline.com/article.cfm%5Earticle=381.htm)
