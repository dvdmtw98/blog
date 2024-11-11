---
title: "Building a Virtual Security Home Lab: Part 3 - Kali Linux Setup"
description: A step-by-step guide for building your very own Cybersecurity Home Lab using VirtualBox
date: 2024-01-04 08:50:00 -0600
categories:
  - Security
  - Home Lab
tags:
  - security
  - home-lab
  - virtualbox
  - networking
  - linux
published: true
media_subpath: /assets/
---

![banner-image|640](images/building-home-lab-part-3/building-home-lab-part-3-banner.png)

Banner Background by [logturnal](https://www.freepik.com/free-vector/gradient-white-color-background-abstract-modern_34010189.htm) on Freepik  
Hacker Image by [catalyststuff](https://www.freepik.com/free-vector/hacker-operating-laptop-cartoon-icon-illustration-technology-icon-concept-isolated-flat-cartoon-style_11602236.htm) on Freepik

> [!IMPORTANT] Changelog
> - **Nov. 10, 2024**
> 	- Added note about settings that could fix the “black screen on boot” problem that occurs on certain machines.
> 	- Updated Kali Linux VM setup steps to include configuration that is recommended by Offensive Security.

In this module, we are going to install Kali Linux. We will use this VM in the next module also to complete the pfSense setup. 

## Download Kali Linux

Go to the following link: [Get Kali \| Kali Linux](https://www.kali.org/get-kali/#kali-installer-images)

Download the <u>64-bit Recommended Installer</u>. The image is ~4GB in size so it will take some time to download.

As of writing the latest version of Kali Linux is **`2023.4`**.

![kali-download-1|400](images/building-home-lab-part-3/kali-download-1.png)

Once it is downloaded we should have an **`.iso`** file. 

![kali-download-2|500](images/building-home-lab-part-3/kali-download-2.png)

## Kali Linux VM Creation

Launch VirtualBox. Select **`Tools`** from the sidebar and then click on **`New`** from the toolbar.

![vbox-19|540](images/building-home-lab-part-3/vbox-19.png)

Give the VM a <u>Name</u>. Set the <u>Folder</u> option to the location where the Home Lab VMs are going to be saved. Leave the <u>ISO Image</u> option empty. Select <u>Type</u> as **`Linux`** and <u>Version</u> as **`Debian (64-bit)`** then click on **`Next`**. 

![vbox-20|540](images/building-home-lab-part-3/vbox-20.png)

Leave everything on its default values. Click on **`Next`**.

![vbox-21|540](images/building-home-lab-part-3/vbox-21.png)

Increase the <u>Disk Size</u> to **`80GB`** and click on **`Next`**.

![vbox-22|540](images/building-home-lab-part-3/vbox-22.png)

Ensure that all the settings look right and click on **`Finish`**.

![vbox-23|540](images/building-home-lab-part-3/vbox-23.png)

![vbox-27|540](images/building-home-lab-part-3/vbox-27.png)

### Adding VM to Group

Right-click on the Kali Linux VM from the sidebar, select **`Move to Group -> [New]`**.

![vbox-24|400](images/building-home-lab-part-3/vbox-24.png)

The VM will now be added to a <u>Group</u> called **`New Group`**. Right-click on the group name and select **`Rename Group`**. Name the group **`Management`**.

![vbox-8|240](vbox-08.png)

Select the <u>Firewall</u> and <u>Management</u> group (**`Ctrl+Click`**). Right-click on the name of one of the groups. From the menu select **`Move to Group -> [New]`**.

![vbox-25|400](images/building-home-lab-part-3/vbox-25.png)

Now both the groups should be nested inside a <u>group</u> called **`New Group`**. Right-click on the group and choose **`Rename Group`**. Give the group the name **`Home Lab`**.

![vbox-28|260](images/building-home-lab-part-3/vbox-28.png)

In the end, we should have the following structure:

![vbox-26|300](images/building-home-lab-part-3/vbox-26.png)

## Kali Linux VM Configuration

Select the Kali Linux VM and then from the toolbar select **`Settings`**.

![vbox-29|540](images/building-home-lab-part-3/vbox-29.png)

### System Configuration

Go to **`System -> Motherboard`**. For the <u>Boot Order</u> option ensure that the **`Hard Disk`** is on the top followed by **`Optical`**. Uncheck **`Floppy`**.  

![vbox-30|540](images/building-home-lab-part-3/vbox-30.png)

Go to **`System -> Processor`**. From Extended Features list select **`Enable PAE/NX`**.

![[vbox-74.png|540]]

Go to **`Display -> Screen`** and increase the <u>Video Memory</u> to **`128 MB`**.

![[vbox-75.png|540]]

### Boot Image Configuration

Go to the **`Storage`** tab. Select the Empty disk present below **`Controller: IDE`** then click on the small disk icon on the right side of the <u>Optical Drive</u> option.

![vbox-31|540](images/building-home-lab-part-3/vbox-31.png)

Select **`Choose a disk file`** and then select the downloaded **`.iso`** file for Kali Linux.

![vbox-32|260](images/building-home-lab-part-3/vbox-32.png)

The final result should look as follows:

![vbox-33|540](images/building-home-lab-part-3/vbox-33.png)

### Network Configuration

Go to **`Network -> Adapter 1`**. For the <u>Attached to</u> field select **`Internal Network`**. For <u>Name</u> select **`LAN 0`**. Expand the <u>Advanced</u> section. For <u>Adapter Type</u> select **`Paravirtualized Network (virtio-net)`**.

![vbox-34|540](images/building-home-lab-part-3/vbox-34.png)

## Kali Linux Installation

Remember to boot the pfSense VM if it was shut down before starting the Kali Linux installation.

Select Kali Linux from the sidebar and click on **`Start`** on the toolbar.

![vbox-35|540](images/building-home-lab-part-3/vbox-35.png)

From the Installer menu select <u>Graphical Install</u>.

![kali-1|540](images/building-home-lab-part-3/kali-1.png)

Select your Language, location and keyboard layout.

![kali-2|540](images/building-home-lab-part-3/kali-2.png)

![kali-3|540](images/building-home-lab-part-3/kali-3.png)

![kali-4|540](images/building-home-lab-part-3/kali-4.png)

Enter a <u>name</u> for the VM. You can use any name here. The hostname is used to identify the system on the network. The hostname can also be changed after installation.

![kali-5|540](images/building-home-lab-part-3/kali-5.png)

Leave the domain name input blank and click on **`Continue`**.

![kali-6|540](images/building-home-lab-part-3/kali-6.png)

Enter your <u>name</u>. This name will be shown on the login screen.

![kali-7|540](images/building-home-lab-part-3/kali-7.png)

The <u>username</u> is used to create the home directory for the user. All the user-related configurations are stored in this folder.

![kali-8|540](images/building-home-lab-part-3/kali-8.png)

Enter a strong password. Re-enter the password in the second field and click on **`Continue`**.

![kali-9|540](images/building-home-lab-part-3/kali-9.png)

Select your <u>clock</u> and then click on **`Continue`**.

![kali-10|540](images/building-home-lab-part-3/kali-10.png)

Select the drive (**`sda`**) and click on **`Continue`**.

![kali-11|540](images/building-home-lab-part-3/kali-11.png)

Select <u>Guided - use entire disk</u> and then click on **`Continue`**.

![kali-27|540](images/building-home-lab-part-3/kali-27.png)

Select the option: <u>All files in one partition</u> and click on **`Continue`**. 

![kali-12|540](images/building-home-lab-part-3/kali-12.png)

Select <u>Finish partitioning and write changes to disk</u>. Then click on **`Continue`**.

![kali-13|540](images/building-home-lab-part-3/kali-13.png)

Select **`Yes`** and click on **`Continue`**.

![kali-14|540](images/building-home-lab-part-3/kali-14.png)

![kali-15|540](images/building-home-lab-part-3/kali-15.png)

After the base system installation is complete we need to choose the desktop environment that will be installed. I have selected <u>GNOME</u> for installation. 

The default is XFCE it does not look as pretty as GNOME it is much lighter and should have better performance. KDE Plasma is the fanciest with a lot of bells and whistles. I would only recommend KDE if you can assign <u>2 cores</u> and <u>4GB RAM</u> for this VM. Once the desktop environment is selected click on **`Continue`**.

![kali-16|540](images/building-home-lab-part-3/kali-16.png)

The installation will take some time. Select **`Yes`** and click on **`Continue`**. 

![kali-17|540](images/building-home-lab-part-3/kali-17.png)

![kali-18|540](images/building-home-lab-part-3/kali-18.png)

Click on **`Continue`** to Reboot the system.

![kali-19|540](images/building-home-lab-part-3/kali-19.png)

After reboot, we should see the Login screen. Click **`Enter`** to log in. Enter the password that was configured during the installation.

![kali-21|540](images/building-home-lab-part-3/kali-21.png)

## Post-Installation Configuration

Kali Linux installer can detect when it is run from a VM because of this it automatically installs <u>Guest Addons</u>.

Press **`Right Ctrl+F`** to enter Fullscreen mode. The VM should scale to fill the entire screen. Press **`Right Ctrl+F`** again to exit Fullscreen mode. From the dock at the bottom of the screen. Select the <u>Terminal</u>.

![kali-26|400](images/building-home-lab-part-3/kali-26.png)

Run the command: **`ip a`**. We can see that the Kali VM has been assigned an IP address from the LAN network range. The VM should be able to access the internet as well.

![kali-22|540](images/building-home-lab-part-3/kali-22.png)

Use the following command to update the system:

```bash
sudo apt update && sudo apt full-upgrade
```

Enter password when prompted.

![kali-23|540](images/building-home-lab-part-3/kali-23.png)

Once the sources have been fetched we will be asked if we want to continue. Enter **`Y`** and then press **`Enter`** to start the update.

![kali-24|540](images/building-home-lab-part-3/kali-24.png)

After the update is complete run the following command to remove the unused packages:

```bash
sudo apt autoremove
```

![kali-25|440](images/building-home-lab-part-3/kali-25.png)

The **`.iso`** file that was downloaded to create the VM can be deleted now if you do not plan to store it for future use.

> [!IMPORTANT] Black Screen on Boot
> On certain machines starting the Kali VM results in a black screen. This issue occurs usually after updating the VM. There isn’t a definitive solution to this problem. The issue may popup from time to time.  
> 
> Some users have reported that changing the “Graphics Controller” to `VBoxSVGA` seems to resolve the problem for them. This option is located under `Settings → Display → Screen`.
> 
> Forcefully powering off the VM and starting it back up also seems to fix the issue. The VM might need to be restarted 2-3 times before the VM loads properly.

In the next module, we will access the pfSense Web UI and complete the remaining configuration.

[Part 4 - pfSense Firewall Configuration](https://blog.davidvarghese.net/posts/building-home-lab-part-4/)
