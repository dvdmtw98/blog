---
categories:
  - Security
  - Home Lab
date: 2024-01-12 19:15:00 -0600
description: A step-by-step guide for building your very own Cybersecurity Home Lab using VirtualBox
img_path: /assets/
published: false
tags:
  - security
  - home-lab
  - virtualbox
  - networking
  - active-directory
title: "Building a Virtual Security Home Lab: Part 7 - Active Directory Lab Setup - Part 2"
---

![banner-image|640](images/building-home-lab-part-7/building-home-lab-part-7-banner.png)

Banner Background by [logturnal](https://www.freepik.com/free-vector/gradient-white-color-background-abstract-modern_34010189.htm) on Freepik  
Hacker Image by [catalyststuff](https://www.freepik.com/free-vector/hacker-operating-laptop-cartoon-icon-illustration-technology-icon-concept-isolated-flat-cartoon-style_11602236.htm) on Freepik

In the last module we had installed Windows Server 2019 and setup Active Directory as well as the DHCP and DNS servers. In this module we continue with the remaining configuration.

## Windows Server 2019 Setup

### User Configuration

#### AD Admin Setup

Open the Start menu click on "Windows Administrative Tools" and then select "Active Directory Users and Computers".

![dc-64|400](images/building-home-lab-part-7/dc-64.png)

Right-click on the domain name (in my case `ad.lab`) in the sidebar. Then chose New and then select User.  

![dc-65|500](images/building-home-lab-part-7/dc-65.png)

This will open the New User configuration. Enter the First Name, Last Name and User logon name for the user. You can chose whatever name you want. This user is going to be the Administrator for the Domain Controller.

![dc-66|400](images/building-home-lab-part-7/dc-66.png)

Enter the Password for the user. Uncheck all options leaving "Password never expires". Click on Next to create the user.

![dc-67|400](images/building-home-lab-part-7/dc-67.png)

Expand the dropdown on the domain name from the sidebar. Click on Users. Then double-click on "Domain Admins".

![dc-68|500](images/building-home-lab-part-7/dc-68.png)

Select the Members tab and click on Add.

![dc-69|400](images/building-home-lab-part-7/dc-69.png)

Enter the name of the user and check on Check Names.

![dc-70|400](images/building-home-lab-part-7/dc-70.png)

It should find the correct user automatically. Click on Ok to save changes.

![dc-71|400](images/building-home-lab-part-7/dc-71.png)

Click on Apply then Ok to persist the changes.

![dc-72|400](images/building-home-lab-part-7/dc-72.png)

Open the Start menu and click on the user logo and then select Sign Out.

![dc-73|400](images/building-home-lab-part-7/dc-73.png)

From the login screen select "Other user". Then enter the logon name as password that you configured for your domain administrator.

![dc-74|600](images/building-home-lab-part-7/dc-74.jpg)

#### AD User 1 Setup

Open the Start menu. Select "Windows Administrative Tools" and then chose "Active Directory Users and Computers".

![dc-75|400](images/building-home-lab-part-7/dc-75.png)

Right-click on the domain name in the sidebar. Chose New and then select User.

![dc-76|500](images/building-home-lab-part-7/dc-76.png)

Enter the details for the user.

![dc-77|400](images/building-home-lab-part-7/dc-77.png)

Give the user as password. Check the "User cannot change password" and "Password never expires" options. Click Next to create user.

![dc-78|400](images/building-home-lab-part-7/dc-78.png)

#### AD User 2 Setup

Follow the same steps as above to create a second AD User.

![dc-76|500](images/building-home-lab-part-7/dc-76.png)

![dc-79|400](images/building-home-lab-part-7/dc-79.png)

![dc-80|400](images/building-home-lab-part-7/dc-80.png)

### Group Policy Configuration

Open the Start menu and click on "Windows Administrative Tools" then chose "Group Policy Management".

![dc-81|400](images/building-home-lab-part-7/dc-81.png)

Expand Forest and then expand Domains.

![dc-102|400](images/building-home-lab-part-7/dc-102.png)

Right-click on the domain name. Select "Create a GPO in the domain and link here".

![dc-82|500](images/building-home-lab-part-7/dc-82.png)

Enter the name of the GPO as "Disable Protections".

![dc-83|400](images/building-home-lab-part-7/dc-83.png)

Expand the domain name. Right-click on "Disable Protections" and chose Edit.

![dc-84|600](images/building-home-lab-part-7/dc-84.png)

This will open the Group Policy Management Editor. In the sidebar expand the folders will to reach `Computer Configuration -> Policies -> Administrative Templates -> Windows Components -> Windows Defender Antivirus`.

![dc-85|600](images/building-home-lab-part-7/dc-85.png)

Select "Windows Defender Antivirus". From the right side select "Turn off Windows Defender Antivirus" and click on "Edit policy setting".

![dc-86|600](images/building-home-lab-part-7/dc-86.png)

Set it to Enabled. Click on Apply then Ok to save the changes.

![dc-87|600](images/building-home-lab-part-7/dc-87.png)

Expand the sidebar folders until: `Computer Configuration -> Policies -> Administrative Templates -> Network -> Network Connections -> Windows Defender Firewall -> Domain Profile`. Once "Domain Profile" is selected from the right-side select "Windows Defender Firewall: Protect all network connections". Click on "Edit policy settings".

![dc-88|600](images/building-home-lab-part-7/dc-88.png)

Set it to disabled. Click on Apply then Ok to save the changes. 

![dc-89|600](images/building-home-lab-part-7/dc-89.png)

Close Group Policy Management Editor. From the sidebar right-click on "Disable Protections" and chose "Enforced". 

![dc-90|600](images/building-home-lab-part-7/dc-90.png)

Now we need this policy to be enforced when new devices join the network.

Right-click on the Start menu and select Windows PowerShell (Admin).

![dc-91|300](images/building-home-lab-part-7/dc-91.png)

In the terminal enter the following and click Enter.

```powershell
gpupdate /force
```

![dc-92|560](images/building-home-lab-part-7/dc-92.png)

This completes all the configuration that needs to be made on the Domain Controller.

## Windows 10 Enterprise VM1 Setup

Select Windows 10 Enterprise VM1 from the sidebar then click on Start.

![user-45|540](images/building-home-lab-part-7/user-45.png)

### OS Installation

Click on Next.

![user-1|540](images/building-home-lab-part-7/user-1.png)

Click on Install now.

![user-2|540](images/building-home-lab-part-7/user-2.png)

Accept the agreement and then click on Next.

![user-3|540](images/building-home-lab-part-7/user-3.png)

Select "Custom: Install Windows only (advanced)"

![user-4|540](images/building-home-lab-part-7/user-4.png)

Select Disk 0 and then click on Next.

![user-5|540](images/building-home-lab-part-7/user-5.png)

Wait for the install to complete. It will take some time. The VM will reboot multiple times during the installation.

![user-6|540](images/building-home-lab-part-7/user-6.png)

Select your Region and Keyboard Layout.

![user-7|540](images/building-home-lab-part-7/user-7.png)

![user-8|540](images/building-home-lab-part-7/user-8.png)

Click on Skip.

![user-9|540](images/building-home-lab-part-7/user-9.png)

Select "Domain join instead". This will allow us to configure a local account.

![user-10|540](images/building-home-lab-part-7/user-10.png)

Enter a username and click on Next. 

> **Note**  
> While we can enter any username in this step to avoid confusion I would recommend using the First Name of one of the users that was created in AD. In my case the two clients are John Doe and Jane Doe. For this VM I have chose John when i configure the next VM I will use Jane.

![user-11|540](images/building-home-lab-part-7/user-11.png)

Enter a password. This password can be different from the password that was configured in Active Directory.

![user-12|540](images/building-home-lab-part-7/user-12.png)

Configure the security questions for the user. Remember to note down these details in a secure location.

![user-13|540](images/building-home-lab-part-7/user-13.png)

Disable all the features that are shown. Then click on Accept.

![user-14|540](images/building-home-lab-part-7/user-14.png)

Select "Not now".

![user-15|540](images/building-home-lab-part-7/user-15.png)

Once the setup is complete we will be able to access the desktop. The prompt to allow internet access should show up click on Yes.

![user-16|540](images/building-home-lab-part-7/user-16.png)

### Guest Additions Installation

Similar to the Windows 2019 Server VM we need to install Guest Additions to enable Fullscreen mode. From the VM toolbar select `Devices -> Remove disk for virtual drive`. This will remove the Windows 10 image.

![user-17|500](images/building-home-lab-part-7/user-17.png)

Click on `Devices -> Insert Guest Additions CD image`.

![user-18|380](images/building-home-lab-part-7/user-18.png)

Open File Explorer. Once the disk has loaded from the sidebar select the disk drive. Double click `VBoxWindowsAdditions` to start the installer. 

![user-19|540](images/building-home-lab-part-7/user-19.png)

Click Next.

![user-20|400](images/building-home-lab-part-7/user-20.png)

Click Next.

![user-21|400](images/building-home-lab-part-7/user-21.png)

Click on Install to start the install.

![user-22|400](images/building-home-lab-part-7/user-22.png)

Select "Reboot now" and then click on Finish. The VM will reboot.

![user-23|400](images/building-home-lab-part-7/user-23.png)

Use the password that was set when this VM was being configured to access the system. 

![user-24|540](images/building-home-lab-part-7/user-24.png)

From the toolbar select `Optical Devices -> Remove disk from virtual drive` to remove the Guest Additions image.

![user-25|400](images/building-home-lab-part-7/user-25.png)

### Adding VM1 to Domain

Now we can add this device into the AD domain we created and login as one the user we configured in AD.

Click on the Search Bar and search for "This PC". Right-click on it and select Properties.

![user-26|500](images/building-home-lab-part-7/user-26.png)

Click on Advanced system settings.

![user-27|540](images/building-home-lab-part-7/user-27.png)

Select the "Computer Name" tab and click on Change.

![user-28|360](images/building-home-lab-part-7/user-28.png)

In the Computer name field enter an name that can be used to easily identify this VM. In the Member of section select Domain and enter the name of user domain (in my case `ad.lab`). Then click on More.

![user-29|360](images/building-home-lab-part-7/user-29.png)

In the Primary DNS suffix of this computer field enter the domain name. Click on Ok.

![user-30|360](images/building-home-lab-part-7/user-30.png)

Click on Ok.

![user-31|360](images/building-home-lab-part-7/user-31.png)

Now a popup should appear. Enter the logon name and password of the Domain Admin that we had configured and click on Ok.

![user-32|300](images/building-home-lab-part-7/user-32.png)

Now the device is added into the AD environment. Click on Ok.

![user-33|260](images/building-home-lab-part-7/user-33.png)

The device needs to be rebooted to save the changes. Click on Ok.

![user-34|300](images/building-home-lab-part-7/user-34.png)

Click on "Restart Now".

![user-35|300](images/building-home-lab-part-7/user-35.png)

Once on the login screen. Click on "Other user". Enter the logon name and password of one of the users that was created in AD and press Enter. You are now logged in as the AD user.

![user-36|600](images/building-home-lab-part-7/user-36.jpg)

To confirm this we can open PowerShell and run `whoami`.

![user-37|540](images/building-home-lab-part-7/user-37.png)

## Windows 10 Enterprise VM2 Setup

Follow the same steps as above to configure the VM for the second user.

![user-46|540](images/building-home-lab-part-7/user-46.png)

### OS Installation

![user-1|540](images/building-home-lab-part-7/user-1.png)

![user-2|540](images/building-home-lab-part-7/user-2.png)

![user-4|540](images/building-home-lab-part-7/user-4.png)

![user-5|540](images/building-home-lab-part-7/user-5.png)

![user-6|540](images/building-home-lab-part-7/user-6.png)

![user-7|540](images/building-home-lab-part-7/user-7.png)

![user-10|540](images/building-home-lab-part-7/user-10.png)

Use the First Name of the second user that was configured in AD.

![user-38|540](images/building-home-lab-part-7/user-38.png)

![user-12|540](images/building-home-lab-part-7/user-12.png)

![user-13|540](images/building-home-lab-part-7/user-13.png)

![user-14|540](images/building-home-lab-part-7/user-14.png)

![user-15|540](images/building-home-lab-part-7/user-15.png)

![user-16|540](images/building-home-lab-part-7/user-16.png)

### Guest Additions Installation

![user-17|500](images/building-home-lab-part-7/user-17.png)

![user-18|380](images/building-home-lab-part-7/user-18.png)

![user-19|540](images/building-home-lab-part-7/user-19.png)

![user-20|400](images/building-home-lab-part-7/user-20.png)

![user-22|400](images/building-home-lab-part-7/user-22.png)

![user-23|400](images/building-home-lab-part-7/user-23.png)

![user-39|540](images/building-home-lab-part-7/user-39.png)

![user-25|400](images/building-home-lab-part-7/user-25.png)

### Adding VM2 to Domain

![user-26|500](images/building-home-lab-part-7/user-26.png)

![user-27|540](images/building-home-lab-part-7/user-27.png)

![user-28|360](images/building-home-lab-part-7/user-28.png)

![user-40|360](images/building-home-lab-part-7/user-40.png)

![user-44|360](images/building-home-lab-part-7/user-44.png)

![user-41|360](images/building-home-lab-part-7/user-41.png)

![user-32|300](images/building-home-lab-part-7/user-32.png)

![user-33|260](images/building-home-lab-part-7/user-33.png)

![user-34|300](images/building-home-lab-part-7/user-34.png)

![user-35|300](images/building-home-lab-part-7/user-35.png)

Login using the AD credentials of the second user.

![user-42|600](images/building-home-lab-part-7/user-42.jpg)

![user-43|540](images/building-home-lab-part-7/user-43.png)

## Appendix

With this we have completed the setup of the Active Directory lab. To wrap up, in the Active Directory Setup module we setup 3 VMs. The 1st VM is the Domain Controller for the AD environment and the other 2 VMs are client devices that have access to the environment. Additionally, in the DC VM we enabled DHCP and DNS services. 

### DNS & DHCP Verification

To verify that the clients VMs are indeed connected to the AD environment you can open the DHCP Manager and compare the IP address shown with the IP address that has been assigned to the VM.

![misc-1|600](images/building-home-lab-part-7/misc-1.png)

Similarly we can use the DNS Manager to see that new entries with the name of the devices have been added.

![misc-2|600](images/building-home-lab-part-7/misc-2.png)

### Taking VM Snapshots

![misc-3|540](images/building-home-lab-part-7/misc-3.png)

![misc-8|540](images/building-home-lab-part-7/misc-8.png)

![misc-4|400](images/building-home-lab-part-7/misc-4.png)

![misc-5|540](images/building-home-lab-part-7/misc-5.png)

![misc-6|540](images/building-home-lab-part-7/misc-6.png)

![misc-7|540](images/building-home-lab-part-7/misc-7.png)

### Alternative AD Setup

There is a lot of other services and features that can enabled in AD. Refer the resources for variations on the installation process.

- [How to Setup a Basic Home Lab Running Active Directory - YouTube](https://www.youtube.com/watch?v=MHsI8hJmggI)
- [How to Build an Active Directory Hacking Lab - YouTube](https://www.youtube.com/watch?v=xftEuVQ7kY0)