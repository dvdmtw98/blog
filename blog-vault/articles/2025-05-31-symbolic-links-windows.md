---
title: "Symbolic Links Demystified – Part 2: A Deep Dive into Windows Symlinks"
description: Explore the intricacies of symbolic links, hard links, junctions and shortcuts in Windows.
date: 2025-05-09 17:35:00 -0500
categories:
  - Operating System
  - Command Line
tags:
  - filesystem
  - operating-system
  - command-line
  - windows
published: false
media_subpath: /assets/
---

![[symbolic-links-windows-banner.png|640]]
_Banner icon created using ChatGPT_

On Windows, there are several ways to reference files and folders without duplicating them. These include symbolic links, hard links, junctions, and shortcuts. While they all serve similar purposes, each one has unique characteristics which makes them ideal for different use cases. This article explores how these linking methods work while highlighting their differences.

### Symbolic Links

![[windows-create-symlink-1.png|280]]
_Fig. 1: Files & directories used in example_

For the Windows examples, I will be using the files and directory shown in Fig. 1. The `Source` and `Destination` directory are located on my `F:` drive.

#### Creating Symlink

On Windows there are 2 shells: PowerShell and Command Prompt. Both shells use different commands to perform the same operation. Were ever possible I have included both the commands.

In PowerShell symbolic links are created using the `New-Item` command with the `-ItemType` parameter set to `SymbolicLink`. Fig. 2 shows how symlink can be created using PowerShell.

```powershell
New-item [Link] -ItemType SymbolicLink -Target [Target]
```

On windows the link argument comes before the target argument. This is the exact opposite of the Linux command. Quick refresher, target is the real file/directory and link is the symbolic link to be created. 

Just link Linux if we try to create a link to a target that does not exist we don’t get an error. If we try to create a link and a object will that name already exists then the command will fail.

On windows to create a symbolic link we need to be an administrator. Symbolic links cannot be created by non-privileged users. This is the default and can be changed. To try these commands on your system run them from an elevated PowerShell and Command prompt.

![[windows-create-symlink-2.png|560]]
_Fig. 2: File symbolic link creation (PowerShell)_

Symlinks have the 1st bit in the mode section set to `l` (same as Linux). For directories the 1st bit is `d`. For regular files the 1st bit is empty.

On Windows symbolic Links can span volumes. This means the target and link can be on different drives.

Symlinks can be created using relative and absolute paths. In Fig. 2 and 3 symlinks are created using absolute paths. When using relative paths the link has to be relative to the current working directory and the target had to be relative to the link.

To create file symbolic links using Command Prompt we have to use the `mklink` command. The 1st argument is the link and the 2nd argument is the target.

```shell
mklink [Link] [Target]
```

![[windows-create-symlink-3.png|500]]
_Fig. 3: File symbolic link creation (Command Prompt)_

Just like on Linux actions that we perform on the link are transparently applied by the system on the target. Changing the permission of a symlink causes the permission of the target to change (same as Linux).

Permission management is quite complex on Windows. Windows uses ACL (Access Control List) to control access. ACLs are outside the scope of this article. For the next demonstration don’t focus on the commands just observe how changing the permission on the link changes it on the target.

Fig. 4 shows the owners & the permissions of the file and symlink. The permissions are the same for both the files but the owner is different. This makes sense as the link was created using administrator privilege so its owned by the administrator.

![[windows-access-symlinks-1.png|450]]
_Fig. 4: Checking permission of symbolic link_

In Fig. 5 I have used the `icacls` command to remove the Read permission from the group Users. I performed this operation on the link but the permission on the target also got changed.

![[windows-access-symlinks-2.png|450]]
_Fig. 5: Changing permission of symbolic link_

> [!INFO]  
> As per the `icacls` documentation if the `/l` option is used then only the permission on the link should change. The target would be left unchanged.  
>   
> I tried this option multiple times but could not get it to work. I am not sure why it does not work. If anyone has any information on this option or in general if its possible to change the permission of link without changing the permission of the target let me know I would love to chat.

[Integrity Control Access Control Lists (icacls) \| Microsoft Learn](https://learn.microsoft.com/en-us/windows-server/administration/windows-commands/icacls)

Just like on Linux, writing content in the file symlink causes the content to written into the target. Fig. 6, 7 and 8 all show this operation using different approaches.

![[windows-create-symlink-4.png|600]]
_Fig. 6: Writing data into file symbolic link (PowerShell)_

![[windows-create-symlink-5.png|400]]
_Fig. 7: Writing data into file symbolic link (Command Prompt)_

In Fig. 8 observe how when the link file is opened the target filename is shown. Notepad follows the link and opens the real file. 

![[windows-create-symlink-6.gif|600]]
_Fig. 8: Writing data into file symbolic link (GUI)_

The command to create a directory and file symlink is the exact same in PowerShell.

![[windows-create-symlink-7.png|560]]
_Fig. 9: Creating directory symbolic link (PowerShell)_

In Command Prompt to create a directory link we have to use the `/D` option. Notice the link type showing in the output of Fig. 10. Command Prompt shows file links as `<SYMLINK>` and directory symlinks as `<SYMLINKD>`.

![[windows-create-symlink-8.png|500]]
_Fig. 10: Creating directory symbolic link (Command Prompt)_

In Fig. 11 and 12 we can we how accessing the symlink feels exactly like accessing the target directory.

![[windows-create-symlink-9.png|440]]
_Fig. 11: Accessing directory symbolic link_

![[windows-create-symlink-10.png|420]]
_Fig. 12: Comparing directory link with original real directory_

In Fig. 13 I have the symlink and the target open in different windows. You can see that when I create a file in the symlink it immediately shows up in the target directory. When I rename the file it also gets renamed in the target.

![[windows-create-symlink-11.gif|600]]
_Fig. 13: Creating file using inside directory symbolic link (GUI)_

#### Symlink Information

In Linux symlinks are implemented with a file that only stores the path to the target. On Windows links are implemented using reparse points (I will cover a bit more about them it a later section). With the symlink target the reparse file also stores some metadata.

The `fsutil` command can be used to read reparse point files.

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

Just like Linux moving the target causes the corresponding links to become broken. Windows does not differentiate between working and broken links. This makes them visually impossible to distinguish.

In Fig. 17 when I tried to access a broken link I told the target could not be found.

![[windows-broke-symlink-1.png|600]]
_Fig. 17: Accessing invalid/broken symbolic link_

In Fig. 18 we can see that even though the 2 links to the text file is broken they appear like normal functioning links. Clicking on broken link will not perform any action and no error message will be shown.

![[windows-broke-symlink-2.png|420]]
_Fig. 18: Invalid/broken symbolic link (GUI)_

Windows does not have a `-sf` equivalent. Quick refresher: The `-sf` option deletes the existing link and creates a new link in its place. On Windows when a link breaks we have to manually delete the broken link and then create a new symlink.

#### Finding Symlink

Symlinks can be found from the Command Prompt using the `dir` command with the `/A:L` (All Links) option.

![[windows-find-symlink-1.png|520]]
_Fig. 19: Finding symbolic links (Command Prompt)_

Command Prompt does not have a simple way to list broken links. The only option is to write a Batch script which is outside the scope of this write-up.

PowerShell provides us with robust commands that allow us to find all links and broken links separately. Fig. 20 shows how all the links in a directory can be found. Fig. 21 shows how we can perform a lookup on the target to see if it exists.

```powershell
Get-ChildItem -Path "E:\Destination" -Recurse `
	| Where-Object { $_.LinkType -eq 'SymbolicLink' }
```

The `Get-ChildItem` command returns all the objects in the directory. Then using `Where-Object` a conditional check is performed to only return links.

![[windows-find-symlink-2.png|620]]
_Fig. 20: Finding symbolic links (PowerShell)_

```powershell
Get-ChildItem -Path "C:\path\to\folder" -Recurse | Where-Object {
    $_.LinkType -eq 'SymbolicLink' -and -not (Test-Path $_.Target)
}
```

This command is similar to the previous one. We expand the condition to add a test to check if the target is accessible.  

![[windows-find-symlink-3.png|620]]
_Fig. 21: Finding broken symbolic links (PowerShell)_

```powershell
Get-ChildItem -Path "C:\path\to\folder" -Recurse | Where-Object {
    $_.LinkType -eq 'SymbolicLink' -and -not (Test-Path $_.Target)
} | Remove-Item -Force -WhatIf
```

This command chains the `Remove-Item` command to delete symlinks that are returned by the command on its left. The `-WhatIf` option allows us to safely see which files will be deleted if the command is executed. To actually delete the files the `-WhatIf` option has to be removed.

```powershell
Get-ChildItem -Path "C:\path\to\folder" -Recurse | Where-Object {
    $_.LinkType -eq 'SymbolicLink' -and -not (Test-Path $_.Target)
} | ForEach-Object {
    $answer = Read-Host "Delete broken symlink '$($_.FullName)'? (Y/N)"
    if ($answer -eq 'Y') { $_ | Remove-Item -Force }
}
```

This is yet another way to delete broken symlinks. This version will show a prompt for each broken link and based on users input make a decision. 

#### Deleting Symlink

On Command Prompt to delete file symlinks we have to use the `del` command and for directory symlinks we have to use the `rmdir` command.

![[windows-delete-symlink-1.png|520]]
_Fig. 22: Deleting symbolic link (Command Prompt)_

On PowerShell file and directory symlink can be removed using the `Remove-Item` command.

![[windows-delete-symlink-2.png|260]]
_Fig. 23: Deleting symbolic link (PowerShell)_

Be careful when using the delete commands. Make sure the path you are using is the path for the symlink. Deleting the wrong item can result in data loss. 

### Reparse Point

A reparse point is a special object in NTFS filesystem that allows Windows to extend the functionality of the NTFS filesystem. Using it Windows can implement different link type objects. A reparse file contains information which instructs Windows that it had to be handled in a different manner than usual.

A reparse point has 2 main fields. The reparse tag and reparse data. The reparse tag indicated the link type. In symbolic links the reparse tag uses the value `IO_REPARSE_TAG_SYMLINK` (`0xA000000C`). The reparse data contains the path to the target. Now take a look at Fig. 14 and it should be must easier to understand.

<iframe 
	width="560" height="315" 
	src="https://www.youtube-nocookie.com/embed/RDH5IuyPJtk?si=iE6SUMzWNUAKL3pZ" 
	title="YouTube video player" 
	frameborder="0" 
	allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" 
	referrerpolicy="strict-origin-when-cross-origin" 
	allowfullscreen>
</iframe>

If you use OneDrive you would have come across the feature that allows files to show up locally but be downloaded only when required. This functionality is also implemented using reparse points.

![[windows-reparse-1.png|400]]
_Fig. 24: OneDrive on-demand files_

![[windows-reparse-2.png|600]]
_Fig. 25: On-demand file reparse point_

As per the documentation multiple tags are available to denote OneDrive files. The OneDrive on-demand files on my system use the tag `IO_REPARSE_TAG_CLOUD_6` (`0x9000601A`). The reparse data contains information about the file, its location in OneDrive and its status.

[Reparse Tags \| Microsoft Learn](https://learn.microsoft.com/en-us/openspecs/windows_protocols/ms-fscc/c8e77b37-3909-4fe6-a4ea-2b9d423b1ee4)

There are many other features in Windows that is implemented using reparse points. If this was a bit much just remember that reparse point is a special filetype and its used to implement symlinks on Windows.

### Shortcuts

Shortcuts on Windows are much more seamless when the Linux equivalent. On Windows shortcuts are represented by the `.lnk` extension. Shortcuts on Windows are in binary format we cannot open then in a text editor to view its content.

Creating shortcuts using CLI is a little tricky. There isn’t a one liner to create it. Fig. 26, 27 and 28 shows how we can create a shortcut using the GUI. 

![[windows-shortcut-1.png|400]]
_Fig. 26: Creating Shortcut (GUI)_

![[windows-shortcut-2.png|450]]
_Fig. 27: Creating Shortcut (GUI)_

![[windows-shortcut-3.png|450]]
_Fig. 28: Creating Shortcut (GUI)_

Windows shortcuts can be placed anywhere on the system. They do not have to be in any specific location. This is different from how its on Linux. Fig. 29 shows how shortcuts can be used from the GUI. Another thing to note is how the icons for shortcuts and symlinks are the same. It can be difficult to tell them at a glance. 

![[windows-shortcut-4.gif|600]]
_Fig. 29: Using Shortcut (GUI)_

Shortcuts are one of the few objects type for which the extension is hidden in Explorer even when the “File name Extensions” option is enabled.

Since `.lnk` files use binary format they cannot be analyzed in a text editor. There are 3rd party tools like the one developed by Eric that allows to use view view the information stored in the shortcut.

![[windows-shortcut-5.png|540]]
_Fig. 30: Analyzing shortcut_

[Eric Zimmerman’s Tools \| MDwiki](https://ericzimmerman.github.io/#!index.md)

Shortcuts on Windows can be opened directly from PowerShell and Command Prompt. Fig. 31 shows how they can be launched from PowerShell and Fig. 32 shows the same using Command Prompt.

![[windows-shortcut-6.gif|600]]
_Fig. 31: Using Shortcut (PowerShell)_

![[windows-shortcut-7.gif|600]]
_Fig. 32: Using Shortcut (Command Prompt)_

### Hard Links

### Junctions

### Conclusion

Understanding the differences between symbolic links, hard links, junctions, and shortcuts in Windows can help you manage your files more effectively. Each method offers distinct advantages. By choosing the appropriate linking method, you can enhance your workflow and file organization within the Windows environment.

### Further Reading

- [NTFS reparse point \| Wikipedia](https://en.wikipedia.org/wiki/NTFS_reparse_point?utm_source=chatgpt.com)
- [LNK File Analysis: LNKing It Together! \| Medium](https://syedhasan010.medium.com/forensics-analysis-of-an-lnk-file-da68a98b8415)
- [Create a shortcut (.lnk file) using PowerShell \| Stack Overflow](https://stackoverflow.com/questions/9701840/create-a-shortcut-lnk-file-using-powershell)
