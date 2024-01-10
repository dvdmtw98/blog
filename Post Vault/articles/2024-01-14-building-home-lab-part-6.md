---
categories:
  - Security
  - Home Lab
date: 2024-01-14 19:00:00 -0600
description: A step-by-step guide for building your very own Cybersecurity Home Lab using VirtualBox
img_path: /assets/
published: false
tags:
  - security
  - home-lab
  - virtualbox
  - networking
  - active-directory
title: "Building a Virtual Security Home Lab: Part 6 - Active Directory Lab Setup - Part 1"
---

![banner-image|640](images/building-home-lab-part-6/building-home-lab-part-6-banner.png)

Banner Background by [logturnal](https://www.freepik.com/free-vector/gradient-white-color-background-abstract-modern_34010189.htm) on Freepik  
Hacker Image by [catalyststuff](https://www.freepik.com/free-vector/hacker-operating-laptop-cartoon-icon-illustration-technology-icon-concept-isolated-flat-cartoon-style_11602236.htm) on Freepik

For the Active Directory (AD) Lab we are going to configure three VMs. The first VM will be the Domain Controller (DC) of the environment. We will use Windows Server 2019 for this machine. The other two VMs will be the clients that use this environment. For the client VMs, we will use Windows 10 Enterprise. 

Microsoft provided Evaluation copies for both of them. Windows Server 2019 has a license of 180 days while Windows 10 Enterprise has a license of 90 days. They should function just fine even after the evaluation period expires. After setting up the lab we will create snapshots for the VMs. The snapshots can also be used to roll back to the start of the evaluation period once it expires.  

> [!INFO] 
> We can create an Active Directory Lab using a single client as well but there are certain AD attacks that require two clients to perform. Depending on your use case you may skip the setup of the second 2nd client. 

## Downloading Windows ISO Files

### Windows Server 2019

Go to the following URL: [Windows Server 2019 \| Microsoft Evaluation Center](https://www.microsoft.com/en-us/evalcenter/download-windows-server-2019)

Click on the **`64-bit edition`** download. The ISO file is ~5GB.

![win-download-1|560](images/building-home-lab-part-6/win-download-1.png)

### Windows 10 Enterprise

Go to the following URL: [Windows 10 Enterprise \| Microsoft Evaluation Center](https://www.microsoft.com/en-us/evalcenter/download-windows-10-enterprise)

Click on the **`64-bit edition`** Enterprise ISO download option. The ISO file is ~5GB.

![win-download-2|560](images/building-home-lab-part-6/win-download-2.png)

### ISO File Names

Pay attention to the names of the downloaded files. Microsoft uses the OS build number as the filename. You can rename the files to avoid confusion.

![win-download-3|540](images/building-home-lab-part-6/win-download-3.png)

|                                          ISO Name                                          |         OS Name         |
| :----------------------------------------------------------------------------------------: | :---------------------: |
|         `17763.3650.221105-1748.rs5_release_svc_refresh_SERVER_EVAL_x64FRE_en-us`          |  `Windows Server 2019`  |
| `19045.2006.220908-0225.22h2_release_svc_refresh_CLIENTENTERPRISEEVAL_OEMRET_x64FRE_en-us` | `Windows 10 Enterprise` |

> [!INFO]
> The build number maybe different when you download the images. These are the latest versions that are available as for writing of this module (Dec, 2023).

![win-download-4|560](images/building-home-lab-part-6/win-download-4.png)

## Creating the VMs

### Windows Server 2019

Click on <u>Tools</u> from the VirtualBox sidebar and select **`New`**.

![windows-1|540](images/building-home-lab-part-6/windows-1.png)

Gave the VM a <u>name</u>. Ensure that the <u>Folder</u> option points to the location where all the Home Lab-related VMs are saved. For the <u>ISO Image</u> select the downloaded Windows Server 2019 image. Select the **`Skip Unattended Installation`** option and then click on **`Next`**. 

![windows-2|540](images/building-home-lab-part-6/windows-2.png)

Increase the <u>Memory</u> to **`4096MB`** (4GB) and click on **`Next`**.

![windows-3|540](images/building-home-lab-part-6/windows-3.png)

Increase the <u>Hard Drive</u> size to **`100GB`** and then click on **`Next`**.

![windows-4|540](images/building-home-lab-part-6/windows-4.png)

Confirm that all the values look correct and then click on **`Finish`**.

![windows-5|540](images/building-home-lab-part-6/windows-5.png)

#### Adding VM to Group

Right-click on the Windows Server 2019 VM and choose **`Move to Group -> [New]`**.

![windows-6|400](images/building-home-lab-part-6/windows-6.png)

Right-click on the group name and select **`Rename Group`**. Name the group **`Active Directory`**.

![windows-7|260](images/building-home-lab-part-6/windows-7.png)

Right-click on the group name (Active Directory) and choose **`Move to Group -> Home Lab`**.

![windows-8|400](images/building-home-lab-part-6/windows-8.png)

The final output should look as follows:

![windows-9|300](images/building-home-lab-part-6/windows-9.png)

### Windows 10 Enterprise VM1

From the VirtualBox sidebar select <u>Tools</u> and then click on **`New`**.

![windows-10|540](images/building-home-lab-part-6/windows-10.png)

Give the VM a <u>name</u>. Ensure that the <u>Folder</u> option is pointing to the location where all the Home Lab VMs are saved. For the <u>ISO Image</u> option select the Windows 10 Enterprise image. Tick the **`Skip Unattended Installation`** option. Click on **`Next`** to continue.

![windows-11|540](images/building-home-lab-part-6/windows-11.png)

Leave Memory and CPU on its default value. Click on **`Next`**.

![windows-12|540](images/building-home-lab-part-6/windows-12.png)

Increase the <u>Hard Disk</u> size to **`100GB`** and then click on **`Next`**. 

![windows-13|540](images/building-home-lab-part-6/windows-13.png)

Verify that all the options are correct and then click on **`Finish`**.

![windows-14|540](images/building-home-lab-part-6/windows-14.png)

#### Adding VM to Group

Right-click on the VM and then choose **`Move to Group -> Home Lab/Active Directory`**.

![windows-15|400](images/building-home-lab-part-6/windows-15.png)

The final result should match the following:

![windows-16|300](images/building-home-lab-part-6/windows-16.png)

### Windows 10 Enterprise VM2

Follow the same steps as above to create the VM for the second AD user. 

![windows-22|540](images/building-home-lab-part-6/windows-22.png)

![windows-23|540](images/building-home-lab-part-6/windows-23.png)

![windows-12|540](images/building-home-lab-part-6/windows-12.png)

![windows-13|540](images/building-home-lab-part-6/windows-13.png)

![windows-24|540](images/building-home-lab-part-6/windows-24.png)

#### Adding VM to Group

![windows-25|400](images/building-home-lab-part-6/windows-25.png)

![windows-30|300](images/building-home-lab-part-6/windows-30.png)

## Configuring the VMs

### Windows Server 2019

Select the Windows Server 2019 VM and click on **`Settings`** from the toolbar.

![windows-17|540](images/building-home-lab-part-6/windows-17.png)

Go to **`System -> Motherboard`**. For <u>Boot Order</u> ensure **`Hard Disk`** is not the top followed by **`Optical`**. Disable **`Floppy`**.

![windows-18|540](images/building-home-lab-part-6/windows-18.png)

Go to **`Network -> Adapter 1`**. For the <u>Attacked to</u> field select **`Internal Network`**. For <u>name</u> select **`LAN 2`**. Click on **`OK`** to save the settings.

![windows-19|540](images/building-home-lab-part-6/windows-19.png)

### Windows 10 Enterprise VM1

Select Windows 10 Enterprise VM1 from the sidebar and then from the toolbar choose **`Settings`**.

![windows-20|540](images/building-home-lab-part-6/windows-20.png)

Go to **`System -> Motherboard`**. For <u>Boot Order</u> ensure **`Hard Disk`** is on the top followed by **`Optical`**. Disable **`Floppy`**.

![windows-21|540](images/building-home-lab-part-6/windows-21.png)

Go to **`Network -> Adapter 1`**. For the <u>Attacked to</u> field select **`Internal Network`**. For <u>name</u> select **`LAN 2`**. Click on **`OK`** to save the settings.

![windows-26|540](images/building-home-lab-part-6/windows-26.png)
### Windows 10 Enterprise VM2

Follow the same steps as above to change the settings for the AD User 2 VM.

![windows-27|540](images/building-home-lab-part-6/windows-27.png)

![windows-28|540](images/building-home-lab-part-6/windows-28.png)

![windows-29|540](images/building-home-lab-part-6/windows-29.png)

## Windows Server 2019 Setup

### OS Installation

Select Windows Server 2019 from the sidebar and click on **`Start`** from the toolbar.

![dc-1|540](images/building-home-lab-part-6/dc-1.png)

Click on **`Next`**.

![dc-2|540](images/building-home-lab-part-6/dc-2.png)

Click on **`Install now`**.

![dc-3|540](images/building-home-lab-part-6/dc-3.png)

Select **`Windows Server 2019 Standalone Evaluation (Desktop Experience)`** and click on **`Next`**.

![dc-4|540](images/building-home-lab-part-6/dc-4.png)

<u>Accept</u> the agreement and click on **`Next`**.

![dc-5|540](images/building-home-lab-part-6/dc-5.png)

Select **`Custom: Install Windows only (Advanced)`**.

![dc-6|540](images/building-home-lab-part-6/dc-6.png)

Select **`Disk 0`** and click on **`Next`**.

![dc-7|540](images/building-home-lab-part-6/dc-7.png)

The VM will restart a couple of times during the installation process.

![dc-8|540](images/building-home-lab-part-6/dc-8.png)

### OS Setup & Configuration

Once the installation is complete we will be asked to set the password for the Administrator account. Once set click on **`Finish`**.

![dc-9|540](images/building-home-lab-part-6/dc-9.png)

We won't be able to log in by using the **`Ctrl+Alt+Delete`** shortcut. This will open the system settings menu of the host system.

VirtualBox has a shortcut configured to perform this action. Use the shortcut **`Right Ctrl+Delete`** to access the login screen. Enter the configured password to access the VM. 

![dc-10|540](images/building-home-lab-part-6/dc-10.png)

To view the configured shortcuts from the main VirtualBox window click on **`File -> Preferences`**. 

![dc-103|260](images/building-home-lab-part-6/dc-103.png)

Select **`Input -> Virtual Machine`**. If we scroll down we should see that **`Ctrl+Alt+Delete`** has been mapped to **`Host+Delete`**. The default mapping for the host key is **`Right Ctrl`**.

![dc-100|540](images/building-home-lab-part-6/dc-100.png)

Once we log in. <u>Server Manager</u> will automatically open. A popup will also open asking us to try Windows Admin Center. Click on <u>Don't show this message again</u> and then click on **`X`** to close the popup.

![dc-11|540](images/building-home-lab-part-6/dc-11.png)

#### Guest Additions Installation

To make the VM screen size bigger we need to install <u>Guest Additions</u>. From the VM toolbar click on **`Devices -> Optical Devices -> Remove disk from virtual drive`**. This will remove the Windows Server 2019 image from the disk drive.  

![dc-12|500](images/building-home-lab-part-6/dc-12.png)

Then select **`Devices -> Insert Guest Additions CD image`**.

![dc-13|360](images/building-home-lab-part-6/dc-13.png)

From the <u>taskbar</u> open **`File Explorer`**. Once the disk is loaded it will show up in the <u>sidebar</u>. Click on it to view its content. Double-click on **`VBoxWindowsAdditions`** (4th file from bottom) to start the installer.

![dc-14|540](images/building-home-lab-part-6/dc-14.png)

Click on **`Next`**.

![dc-15|540](images/building-home-lab-part-6/dc-15.png)

Click on **`Next`**.

![dc-16|540](images/building-home-lab-part-6/dc-16.png)

Click on **`Next`** again to install the requirement components.

![dc-17|540](images/building-home-lab-part-6/dc-17.png)

Choose **`Reboot now`** and click on **`Finish`**. The VM will restart automatically.

![dc-18|540](images/building-home-lab-part-6/dc-18.png)

After restart, log into the system. From the VM toolbar click on **`Devices -> Optical Drivers -> Remove disk from virtual drive`** to remove the Guest Additions image.  

![dc-93|500](images/building-home-lab-part-6/dc-93.png)

Use the shortcut **`Right Ctrl+F`** to enter <u>Fullscreen mode</u>. The VM will automatically scale to fill the entire screen. Use the same shortcut to exit Fullscreen mode.

#### Network Configuration

During the pfSense setup module (Part 2) we disabled <u>DHCP</u> on the **`AD_LAB`** interface because of this our VM will not be automatically assigned an IP address. From the taskbar right-click on the <u>network icon</u> and select **`Open Network & Internet settings`**. 

![dc-19|300](images/building-home-lab-part-6/dc-19.png)

Click on "<u>Change adapter options</u>".

![dc-20|540](images/building-home-lab-part-6/dc-20.png)

On the Network Connections page, we should see the <u>Ethernet adapter</u>. Right-click on the adapter and select **`Properties`**.

![dc-21|540](images/building-home-lab-part-6/dc-21.png)

Select **`Internet Protocol Version 4 (TCP/IPv4)`** and click on **`Properties`**.

![dc-22|400](images/building-home-lab-part-6/dc-22.png)

Enter the details as shown below and then click on **`OK`**. Click on **`OK`** again to close the Ethernet Properties menu.

IP address: **`10.80.80.2`**  
Subnet mask: **`255.255.255.0`**  
Default gateway: **`10.80.80.1`**  
Preferred DNS Server: **`10.80.80.2`**

![dc-23|400](images/building-home-lab-part-6/dc-23.png)

Windows will display a banner to allow internet access click on **`Yes`**.

![dc-24|560](images/building-home-lab-part-6/dc-24.png)

Close the Network Connections page.

In the <u>Settings app</u> click on the **`Home`** button (above search bar).

![dc-20|540](images/building-home-lab-part-6/dc-20.png)

#### Renaming the System

Before we can set up the machine to be a Domain Controller let us rename the PC. Select "<u>System</u>".

![dc-25|540](images/building-home-lab-part-6/dc-25.png)

Click on <u>About</u> on the sidebar and then click on the "<u>Rename this PC</u>" button. Give the PC an easy-to-remember name and then click on **`Next`**.

![dc-26|540](images/building-home-lab-part-6/dc-26.png)

Click on "<u>Restart now</u>" for the changes to take effect.

![dc-27|540](images/building-home-lab-part-6/dc-27.png)

#### Active Directory & DNS Installation

After login wait for Server Manager to load. Click on the **`Manage`** button from the top right corner and select "<u>Add Roles and Features</u>".

![dc-28|360](images/building-home-lab-part-6/dc-28.png)

Click on **`Next`** till you reach the <u>Server Roles</u> page.

![dc-29|540](images/building-home-lab-part-6/dc-29.png)

On this page enable "<u>Active Directory Domain Services</u>" and "<u>DNS Server</u>".

![dc-30|540](images/building-home-lab-part-6/dc-30.png)

When you enable a feature the "<u>Add Roles and Features Wizard</u>" will open click on "<u>Add Features</u>" to confirm the selection.

![dc-31|540](images/building-home-lab-part-6/dc-31.png)

![dc-32|540](images/building-home-lab-part-6/dc-32.png)

Once both the features are selected click on **`Next`** to proceed with installation.

![dc-33|540](images/building-home-lab-part-6/dc-33.png)

Click **`Next`** till you reach the Confirmation page. Here click on **`Install`** to start the installation of the selected features.

![dc-34|540](images/building-home-lab-part-6/dc-34.png)

![dc-35|540](images/building-home-lab-part-6/dc-35.png)

Once the installation is complete click on **`Close`** to exit the Wizard.

#### Active Directory Configuration

Click on the Flag icon present in the top right of the toolbar in Server Manager. From the dropdown click on "<u>Promote this server to a domain controller</u>".

![dc-36|400](images/building-home-lab-part-6/dc-36.png)

The AD Domain Servers Configuration Wizard will open. For <u>deployment operation</u> select **`Add a new Forest`**. Give the domain a <u>name</u>. For my setup, I will be using the domain name **`ad.lab`**. After selecting the name click on **`Next`**.

![dc-37|540](images/building-home-lab-part-6/dc-37.png)

> [!INFO]
> The name assigned to the domain has to be made of two words that are separated by a period.

On this page enter a <u>password</u> to use for using the AD Restore feature.

![dc-38|540](images/building-home-lab-part-6/dc-38.png)

Ignore the warning that is shown and click on **`Next`**.

![dc-39|540](images/building-home-lab-part-6/dc-39.png)

The <u>NetBIOS name</u> should automatically be filled. It will be the first part of the domain name. Click on **`Next`** to continue.

![dc-40|540](images/building-home-lab-part-6/dc-40.png)

Click on **`Next`**.

![dc-41|540](images/building-home-lab-part-6/dc-41.png)

Click on **`Next`**.

![dc-42|540](images/building-home-lab-part-6/dc-42.png)

Click on **`Install`** to start the Domain Services setup process.

![dc-43|540](images/building-home-lab-part-6/dc-43.png)

Once the install process is complete the machine will need to restart. Click on **`Close`** to reboot the system.

![dc-44|540](images/building-home-lab-part-6/dc-44.png)

On restart, you will notice that the name that is shown on the login page has changed. The first part of the domain name is prepended to the username. This means the machine has successfully been configured as the domain controller. Log in using the Administrator password.

![dc-45|600](images/building-home-lab-part-6/dc-45.jpg)

#### DNS Configuration

Since we enabled <u>DNS</u> on this machine (Domain Controller). This machine (DC) will act as the DNS server for devices that are connected to the **`ad.lab`** environment. For the DNS service to function properly we need to configure a <u>Forwarder</u>. Forwarder is the device to which the DNS queries will be sent when the DC cannot resolve it. In our case, we need to forward the request to <u>pfSense</u>. The DNS service of pfSense will then perform the lookup.

Open the <u>Start</u> menu expand the "<u>Windows Administrative Tools</u>" folder and select **`DNS`**.

![dc-94|300](images/building-home-lab-part-6/dc-94.png)

In the sidebar select the <u>Domain Controller</u> (in my case DC1) and from the right menu double-click on "<u>Forwarders</u>".

![dc-95|540](images/building-home-lab-part-6/dc-95.png)

Go to **`Forwarders -> Edit`**.

![dc-96|540](images/building-home-lab-part-6/dc-96.png)

This will open the Forwarder configuration page. Enter the IP address of the **`AD_LAB`** interface (**`10.80.80.1`**) and press **`Enter`**. 

![dc-97|540](images/building-home-lab-part-6/dc-97.png)

Once added. Click on **`OK`** to confirm the change.

![dc-98|540](images/building-home-lab-part-6/dc-98.png)

Click on **`Apply`** then **`OK`** to save the changes.

![dc-99|540](images/building-home-lab-part-6/dc-99.png)

#### DHCP Installation

Since <u>DHCP</u> is disabled on the **`AD_LAB`** interface when new devices are added they will not be assigned an IP address. We will enable the DHCP service on the DC. Once set devices that connect to the **`AD_LAB`** network will be automatically assigned an IP address by the Domain Controller DHCP server.  

Click on <u>Manage</u> from the toolbar in Server Manager. Then choose "<u>Add Roles and Features</u>".

![dc-46|400](images/building-home-lab-part-6/dc-46.png)

Keep clicking **`Next`** till you reach the "<u>Server Roles</u>" page. Enable "<u>DHCP Server</u>" then click on "<u>Add Features</u>". 

![dc-47|540](images/building-home-lab-part-6/dc-47.png)

![dc-48|540](images/building-home-lab-part-6/dc-48.png)

Keep clicking **`Next`** till you reach the Confirmation page. Click **`Install`** to enable DHCP.

![dc-49|540](images/building-home-lab-part-6/dc-49.png)

#### DHCP Configuration

After the installation is complete click on the <u>Flag</u> present in the toolbar of Server Manager and click on "<u>Complete DHCP configuration</u>".

![dc-61|400](images/building-home-lab-part-6/dc-61.png)

Click on **`Commit`**.

![dc-62|540](images/building-home-lab-part-6/dc-62.png)

Click on **`Close`** to complete the installation.

![dc-63|540](images/building-home-lab-part-6/dc-63.png)

From the <u>Start</u> menu click on "<u>Windows Administrative Tools</u>" and then choose **`DHCP`**.

![dc-50|400](images/building-home-lab-part-6/dc-50.png)

Expand the DHCP server (in my case **`dc1.ad.lab`**) dropdown on the left side of the window.

![dc-101|400](images/building-home-lab-part-6/dc-101.png)

Right-click on **`IPv4`**. Then select "<u>New Scope</u>". The scope defines the range of IP addresses that can be assigned to devices by the DHCP server.

![dc-51|440](images/building-home-lab-part-6/dc-51.png)

Enter a <u>Name</u> and <u>Description</u> for the new scope.

![dc-52|400](images/building-home-lab-part-6/dc-52.png)

Enter the details as shown below.

Start IP address: **`10.80.80.11`**  
End IP address: **`10.80.80.253`**  
Length: **`24`**  
Subnet mask: **`255.255.255.0`**

![dc-53|400](images/building-home-lab-part-6/dc-53.png)

> [!NOTE]  
> You can chose the Start IP address to be **`10.80.80.3`**. I have purposely left the starting IP addresses out of the DHCP scope. In the future if the need arises I can use these IPs for static IP assignment.  

We don't have any Exclusions (static IP assignment). Leave all the options empty and click on **`Next`**.

![dc-54|400](images/building-home-lab-part-6/dc-54.png)

Increase the lease time to **`365`** days and click on **`Next`**.

![dc-55|400](images/building-home-lab-part-6/dc-55.png)

> [!INFO]
> Since we increased the lease duration when a IP address is assigned to a device the device will be allowed to use that IP address without requesting a new IP address for 365 days. 

Select "<u>Yes, I want to configure these options now</u>" and click on **`Next`**.

![dc-56|400](images/building-home-lab-part-6/dc-56.png)

In the <u>IP address</u> field enter the default gateway for the **`AD_LAB`** interface (**`10.80.80.1`**) and then click on **`Add`**. Once added click on **`Next`**.

![dc-57|400](images/building-home-lab-part-6/dc-57.png)

Click on **`Next`**.

![dc-58|400](images/building-home-lab-part-6/dc-58.png)

We are not configuring a WINS Server for our environment so click on **`Next`**.

![dc-59|400](images/building-home-lab-part-6/dc-59.png)

Select "<u>Yes, I want to activate this scope now</u>" and click on **`Next`**.

![dc-60|400](images/building-home-lab-part-6/dc-60.png)

So far we have installed Windows Server 2019, installed Guest Additions, configured the VM to be the Domain Controller (DC), set up a DNS Forwarder and configured DHCP. We still need to create users in the DC and set up client machines to use the AD environment. We will cover these topics in part 2 of this module.