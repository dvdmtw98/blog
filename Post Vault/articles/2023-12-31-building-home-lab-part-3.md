---
title: "Building Your Own Home Lab: Part 3 - Kali Linux Setup"
description: A step-by-step guide to build your very own Cybersecurity Home Lab using VirtualBox
date: 2024-01-02 18:15:00 -0600
categories:
  - Security
  - Home Lab
tags:
  - security
  - home-lab
  - virtualbox
  - networking
published: false
img_path: /assets/
image: images/building-home-lab-part-3/building-home-lab-part-3-banner.png
---
Banner Background by <a href="https://www.freepik.com/free-vector/gradient-white-color-background-abstract-modern_34010189.htm#query=simple%20backgrounds&position=28&from_view=search&track=ais&uuid=96e36b2e-64b3-42e2-8fd8-4fd18a6e1d5d">logturnal</a> on Freepik  
Hacker Image by <a href="https://www.freepik.com/free-vector/hacker-operating-laptop-cartoon-icon-illustration-technology-icon-concept-isolated-flat-cartoon-style_11602236.htm#page=2&query=hacker&position=28&from_view=search&track=sph&uuid=070b0d8a-d045-434d-9a51-f239e46d5f17">catalyststuff</a> on Freepik

## Download Kali Linux

Go to the following link: [Get Kali \| Kali Linux](https://www.kali.org/get-kali/#kali-installer-images)

From the Installer Image section download the 64-bit Recommended Installer. The image is ~4GB in size so it will take sometime to download.

![kali-download-1|400](images/building-home-lab-part-3/kali-download-1.png)

Once its downloaded we should have an `.iso` file. As of writing the latest version of Kali Linux is `2023.4`.

![kali-download-2|500](images/building-home-lab-part-3/kali-download-2.png)

## Kali Linux VM Creation

Select Tools from the sidebar and then from the toolbar select New.

![vbox-19|540](images/building-home-lab-part-3/vbox-19.png)

For name enter the name to be give to the VM. Ensure Folder is set to the location where the Home Lab is going to be saved. Leave the ISO Image option empty. Ensure to select the correct option for Type and Version. Once everything looks right click Next. 

![vbox-20|540](images/building-home-lab-part-3/vbox-20.png)

On this page leave everything on its default values.

![vbox-21|540](images/building-home-lab-part-3/vbox-21.png)

Increase the disk size to 80GB and ensure Pre-allocate Full Size is not selected.

![vbox-22|540](images/building-home-lab-part-3/vbox-22.png)

Confirm that all the settings look right and click on Finish.

![vbox-23|540](images/building-home-lab-part-3/vbox-23.png)

The VM to install Kali Linux is ready.

![vbox-27|540](images/building-home-lab-part-3/vbox-27.png)

### Adding VM to Group

Similar to the previous module this is an optional step but its highly recommended as its helps to keep the Home Lab VMs organized and grouped together. Right click on the Kali Linux VM from the menu select Move to Group option and then chose New.

![vbox-24|400](images/building-home-lab-part-3/vbox-24.png)

The VM will new be added to a Group called New Group. Right click on the group name and select Rename Group. Name the group Management.

![vbox-8|240](images/building-home-lab-part-2/vbox-8.png)

Select the Firewall and Management group (Ctrl + Click). Right click on the name of one of the group. From the menu select Move to Group and then chose New.

![vbox-25|400](images/building-home-lab-part-3/vbox-25.png)

Now both the groups should be nested inside a group called New Group. Select the group and chose Rename Group. Give the group the name Home Lab.

![vbox-28|260](images/building-home-lab-part-3/vbox-28.png)

In the end we should have the following structure. The main group will be called Home Lab. It has two sub-groups. The first sub-group is called Firewall and has the pfSense VM. The second sub-group has the name Management and has the Kali Linux VM.

![vbox-26|540](images/building-home-lab-part-3/vbox-26.png)

## Kali Linux VM Configuration

Select the Kali Linux VM and then from the toolbar select Settings.

![vbox-29|540](images/building-home-lab-part-3/vbox-29.png)

### System Configuration

Select System from the sidebar. Under Motherboard for the Boot Order option ensure that Hard Drive in on the top followed by Optical. Uncheck Floppy.  

![vbox-30|540](images/building-home-lab-part-3/vbox-30.png)

### Boot Image Configuration

Select Storage from sidebar. Select the Empty disk that is present below Controller: IDE. Click on the small disk icon the the right side of the Optical Drive option.

![vbox-31|540](images/building-home-lab-part-3/vbox-31.png)

Select Choose a disk file and then select the downloaded `.iso` file for Kali Linux.

![vbox-32|260](images/building-home-lab-part-3/vbox-32.png)

The final setting should look as follows:

![vbox-33|540](images/building-home-lab-part-3/vbox-33.png)

### Network Configuration

Select Network from the sidebar. Under Adapter 1 check Enable Network Adapter. For Attached to select Internal Network. For name select LAN 0. Expand the Advanced option. For Adapter Type select Paravirtualized Network (virtio-net).

![vbox-34|540](images/building-home-lab-part-3/vbox-34.png)

## Kali Linux Installation

Remember to boot the pfSense VM if it was shutdown before proceeding with the Kali Linux installation.

Select Kali Linux from the sidebar and click on Start on the toolbar.

![vbox-35|540](images/building-home-lab-part-3/vbox-35.png)

From the Installer menu select Graphical Install.

![kali-1|540](images/building-home-lab-part-3/kali-1.png)

Select your Language, location and keyboard layout.

![kali-2|540](images/building-home-lab-part-3/kali-2.png)

![kali-3|540](images/building-home-lab-part-3/kali-3.png)

![kali-4|540](images/building-home-lab-part-3/kali-4.png)

Enter a name for the VM. You can use any name here. The hostname is used to identify the system on the network. It also shows up on the prompt on the terminal. The hostname can also be changed.

![kali-5|540](images/building-home-lab-part-3/kali-5.png)

Leave the domain name input blank and click on Continue.

![kali-6|540](images/building-home-lab-part-3/kali-6.png)

Enter your name. This name will be shown on the login screen.

![kali-7|540](images/building-home-lab-part-3/kali-7.png)

The username is used to create the home directory for the user. All the user related configuration will be stored in this folder.

![kali-8|540](images/building-home-lab-part-3/kali-8.png)

Enter a strong password for the VM. Re-enter the password in the second field and click on Continue.

![kali-9|540](images/building-home-lab-part-3/kali-9.png)

Select your timezone and then click on Continue.

![kali-10|540](images/building-home-lab-part-3/kali-10.png)

Select the drive (`sda`) and click on Continue.

![kali-11|540](images/building-home-lab-part-3/kali-11.png)

Select the option: All files in one partition and click on Continue. 

![kali-12|540](images/building-home-lab-part-3/kali-12.png)

Select Finish partitioning and write changes to disk and then click on Continue.

![kali-13|540](images/building-home-lab-part-3/kali-13.png)

Select Yes as the option and click on Continue.

![kali-14|540](images/building-home-lab-part-3/kali-14.png)

![kali-15|540](images/building-home-lab-part-3/kali-15.png)

Once the base system installation is complete we need to chose the desktop environment that will be installed for Kali Linux. I like GNOME so I have selected GNOME for installation. The default is XFCE while it does not look as pretty as GNOME it is much lighter and should provide better performance. KDE Plasma is the prettiest and offers a lot of bells and whistles in the UI department. I would only recommend KDE if you can spare 2 cores and 4GB RAM for this VM. Once the desktop environment is select click on Continue.

![kali-16|540](images/building-home-lab-part-3/kali-16.png)

The installation will take a long time. Once the installation is complete the GRUB menu needs to be configured. Select Yes and click on Continue. 

![kali-17|540](images/building-home-lab-part-3/kali-17.png)

![kali-18|540](images/building-home-lab-part-3/kali-18.png)

Click on Continue to Reboot the system.

![kali-19|540](images/building-home-lab-part-3/kali-19.png)

After reboot we should see the Login screen. Click Enter to login.

![kali-20|540](images/building-home-lab-part-3/kali-20.png)

Enter the password that was configured during the installation.

![kali-21|540](images/building-home-lab-part-3/kali-21.png)

## Kali Linux Configuration

Once on the desktop. From the dock at the bottom. Select the Terminal.

![kali-26|400](images/building-home-lab-part-3/kali-26.png)

On running `ip a` we can see that the Kali VM is connected to the `10.0.0.1` network which is the LAN network we had configured in pfSense. Without changing any firewall rules this network should be able to access the internet.

![kali-22|540](images/building-home-lab-part-3/kali-22.png)

Use the following command to update the system:

```bash
sudo apt update && sudo apt full-upgrade
```

Enter your password when prompted.

![kali-23|540](images/building-home-lab-part-3/kali-23.png)

Once the sources have been fetched we will be asked to confirm the update enter `Y` and press `Enter` or press `Enter` directly to start the update.

![kali-24|540](images/building-home-lab-part-3/kali-24.png)

After the update is complete run the following command to remove the unused packages:

```bash
sudo apt autoremove
```

![kali-25|440](images/building-home-lab-part-3/kali-25.png)

In the next module we are going to look at the pfSense UI and setup firewall rules for the different network interfaces.
