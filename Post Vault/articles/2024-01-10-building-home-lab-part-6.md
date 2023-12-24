---
title: "Building Your Own Home Lab: Part 6 - Active Directory Lab Setup - Part 1"
description: A step-by-step guide to build your very own Cybersecurity Home Lab using VirtualBox
date: 2024-01-10 19:00:00 -0600
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
image: images/building-home-lab-part-6/building-home-lab-part-6-banner.png
---

Banner Background by <a href="https://www.freepik.com/free-vector/gradient-white-color-background-abstract-modern_34010189.htm#query=simple%20backgrounds&position=28&from_view=search&track=ais&uuid=96e36b2e-64b3-42e2-8fd8-4fd18a6e1d5d">logturnal</a> on Freepik  
Hacker Image by <a href="https://www.freepik.com/free-vector/hacker-operating-laptop-cartoon-icon-illustration-technology-icon-concept-isolated-flat-cartoon-style_11602236.htm#page=2&query=hacker&position=28&from_view=search&track=sph&uuid=070b0d8a-d045-434d-9a51-f239e46d5f17">catalyststuff</a> on Freepik

For the Active Directory (AD) Lab we are going to configure three VMs. The first VM will be the Domain Controller (DC) of the environment. We will use Windows Server 2019 for this machine. The other two VMs are going to be the clients that use this environment. For the client VMs we will use Windows 10 Enterprise. 

Microsoft provided Evaluation copies for both these versions of Windows. Windows Server 2019 have a license of 180 days while Windows 10 Enterprise has a license of 90 days. Both should work just fine even after the evaluation period has expired. Alternatively, after setting up the lab we can create a snapshot of the VM which can be used to rollback to the start of the evaluation period once it expires.  

> **Note**  
> We can create an Active Directory Lab using a single client as well but there are certain AD attacks that require two clients to perform. Depending on your use case you may skip the setup for the second 2nd client. 

## Downloading Windows ISO Files

### Windows Server 2019

Go to the following URL: [Windows Server 2019 \| Microsoft Evaluation Center](https://www.microsoft.com/en-us/evalcenter/download-windows-server-2019)

Click on 64-bit ISO download. The ISO file is ~5GB.

![win-download-1|560](images/building-home-lab-part-6/win-download-1.png)

### Windows 10 Enterprise

Go to the following URL: [Windows 10 Enterprise \| Microsoft Evaluation Center](https://www.microsoft.com/en-us/evalcenter/download-windows-10-enterprise)

Click on the 64-bit Enterprise ISO download option. The ISO file is ~5GB.

![win-download-2|560](images/building-home-lab-part-6/win-download-2.png)

### ISO File Names

Pay attention to the names of the downloaded files. Microsoft uses the OS build number as the filename. You can rename the files to avoid confusing.

![win-download-3|540](images/building-home-lab-part-6/win-download-3.png)

| ISO Name | OS Name |
| :--: | :--: |
| `17763.3650.221105-1748.rs5_release_svc_refresh_SERVER_EVAL_x64FRE_en-us` | `Windows Server 2019` |
| `19045.2006.220908-0225.22h2_release_svc_refresh_CLIENTENTERPRISEEVAL_OEMRET_x64FRE_en-us` | `Windows 10 Enterprise` |

**Note:** The build number in your case can be different. A newer version of the ISO will use a different build number.

![win-download-4|560](images/building-home-lab-part-6/win-download-4.png)

## Creating the VMs

### Windows Server 2019

Click on Tools from the VirtualBox sidebar and select New.

![windows-1|540](images/building-home-lab-part-6/windows-1.png)

Gave the VM a name. Ensure that Folder points to the location where all the Home Lab related VMs are saved. For the ISO Image select the Windows Server 2019 image. Select the `Skip Unattended Installation` option and then click on Next. 

![windows-2|540](images/building-home-lab-part-6/windows-2.png)

Increase the Memory to `4096MB` (4GB) and click on Next.

![windows-3|540](images/building-home-lab-part-6/windows-3.png)

Increase the Hard Drive size to 100GB. Ensure that Pre-allocated Fill Size is not checked then click on Next.

![windows-4|540](images/building-home-lab-part-6/windows-4.png)

Confirm that all the values look correct and click on Finish.

![windows-5|540](images/building-home-lab-part-6/windows-5.png)

#### Adding VM to Group

Right-click on the Windows Server 2019 VM and chose Move to Group then click on New.

![windows-6|400](images/building-home-lab-part-6/windows-6.png)

Right-click on the group name and select Rename Group. Name the group `Active Directory`.

![windows-7|260](images/building-home-lab-part-6/windows-7.png)

Right-click on the group name (Active Directory) and chose Move to Group and select Home Lab.

![windows-8|400](images/building-home-lab-part-6/windows-8.png)

The final output should look as follows:

![windows-9|300](images/building-home-lab-part-6/windows-9.png)

### Windows 10 Enterprise VM1

From the VirtualBox sidebar select Tools and then click on New.

![windows-10|540](images/building-home-lab-part-6/windows-10.png)

Give the VM a name. Ensure the Folder is pointing to the location where all the Home Lab VMs are saved. For ISO Image select the Windows 10 Enterprise image. Tick the `Skip Unattended Installation` option. Click on Next to continue.

![windows-11|540](images/building-home-lab-part-6/windows-11.png)

Leave the Memory and CPU on its default value and click Next.

![windows-12|540](images/building-home-lab-part-6/windows-12.png)

Increase the Hard Disk size to 100GB. Ensure that Pre-allocate Full Size is not selected then click on Next. 

![windows-13|540](images/building-home-lab-part-6/windows-13.png)

Verify that all the options are correct and then click on Finish.

![windows-14|540](images/building-home-lab-part-6/windows-14.png)

#### Adding VM to Group

Right-click on the VM and then chose Move to Group and select `Home Lab/Active Directory`.

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

Select the Windows Server 2019 VM and click on Settings from the toolbar.

![windows-17|540](images/building-home-lab-part-6/windows-17.png)

Go to `System -> Motherboard`. For Boot Order ensure Hard Disk is not the top followed by Optical. Disable Floppy.

![windows-18|540](images/building-home-lab-part-6/windows-18.png)

Go to `Network -> Adapter 1`. Ensure that Enable Network Adapter is enabled. For the Attacked to field select Internal Network. For name select LAN 2. Expand the Advanced options section. For Adapter Type select `Intel PRO/1000 MT Desktop`. Click on Ok to save the settings.

![windows-19|540](images/building-home-lab-part-6/windows-19.png)

### Windows 10 Enterprise VM1

Select Windows 10 Enterprise VM1 from the sidebar and from the toolbar chose Settings.

![windows-20|540](images/building-home-lab-part-6/windows-20.png)

Go to `System -> Motherboard`. For Boot Order ensure Hard Disk is not the top followed by Optical. Disable Floppy.

![windows-21|540](images/building-home-lab-part-6/windows-21.png)

Go to `Network -> Adapter 1`. Ensure that Enable Network Adapter is enabled. For the Attacked to field select Internal Network. For name select LAN 2. Expand the Advanced options section. For Adapter Type select `Intel PRO/1000 MT Desktop`. Click on Ok to save the settings.

![windows-26|540](images/building-home-lab-part-6/windows-26.png)
### Windows 10 Enterprise VM2

Follow the same steps as above to change the settings for the AD User 2 VM.

![windows-27|540](images/building-home-lab-part-6/windows-27.png)

![windows-28|540](images/building-home-lab-part-6/windows-28.png)

![windows-29|540](images/building-home-lab-part-6/windows-29.png)

## Windows Server 2019 Setup

### OS Installation

Select Windows Server 2019 from the sidebar and click on Start from the toolbar.

![dc-1|540](images/building-home-lab-part-6/dc-1.png)

Click on Next.

![dc-2|540](images/building-home-lab-part-6/dc-2.png)

Click on Install now.

![dc-3|540](images/building-home-lab-part-6/dc-3.png)

Select `Windows Server 2019 Standalone Evaluation (Desktop Experience)` and click on Next.

![dc-4|540](images/building-home-lab-part-6/dc-4.png)

Accept the agreement and click on Next.

![dc-5|540](images/building-home-lab-part-6/dc-5.png)

Select `Custom: Install Windows only (Advanced)`.

![dc-6|540](images/building-home-lab-part-6/dc-6.png)

Select Disk 0 and click on Next.

![dc-7|540](images/building-home-lab-part-6/dc-7.png)

The installation process will take some time. The VM will restart a couple of times during the installation process.

![dc-8|540](images/building-home-lab-part-6/dc-8.png)

### OS Setup & Configuration

Once the install is complete we will be asked to set the password for the Administrator account. Once set click on Finish.

![dc-9|540](images/building-home-lab-part-6/dc-9.png)

We wont be able to login on clicking `Ctrl+Alt+Delete`. This will open the system settings menu of our host system.

VirtualBox has a shortcut configured to perform this action. Use `Right Ctrl+ Delete` to access the login screen. Enter the configured password to access the VM. 

![dc-10|540](images/building-home-lab-part-6/dc-10.png)

To view the shortcuts that are configured in VirtualBox click on `File -> Preferences`. Select `Input` and then chose the Virtual Machine tab. If we scroll down we should see that `Ctrl+Alt+Delete` has been mapped to `Host+Delete`. The default mapping for host key is `Right Ctrl`.

![dc-100|540](images/building-home-lab-part-6/dc-100.png)

Once we login. Server Manager will automatically open. A popup will also open asking us to try Windows Admin Center. Click on Don't show this message again and then click on `X` to close the popup.

![dc-11|540](images/building-home-lab-part-6/dc-11.png)

#### Guest Additions Installation

Now lets make the VM Fullscreen for this feature to work we need to install Guest Additions. From the VM toolbar click on `Devices -> Optical Devices -> Remove disk from virtual drive`. This will remove the Windows Server 2019 image from the disk drive.  

![dc-12|500](images/building-home-lab-part-6/dc-12.png)

Once again click on `Devices` then select `Insert Guest Additions CD image`.

![dc-13|360](images/building-home-lab-part-6/dc-13.png)

From the taskbar open File Explorer. Once the disk is loaded it will show up in the sidebar. Click on it to view its content. Double-click `VBoxWindowsAdditions` (4th file from bottom) to start the installer.

![dc-14|540](images/building-home-lab-part-6/dc-14.png)

Click on Next.

![dc-15|540](images/building-home-lab-part-6/dc-15.png)

Click on Next.

![dc-16|540](images/building-home-lab-part-6/dc-16.png)

Click on Next again to install the requirement components.

![dc-17|540](images/building-home-lab-part-6/dc-17.png)

Once the install is complete. The VM needs to be restarted. Select `Reboot now` and click on Finish.

![dc-18|540](images/building-home-lab-part-6/dc-18.png)

After reboot, login into the system. From the VM toolbar click on `Devices -> Optical Drivers -> Remove disk from virtual drive` to remove the Guest Additions image.  

![dc-93|500](images/building-home-lab-part-6/dc-93.png)

Use the shortcut `Ctrl+F` to enter Fullscreen mode. The VM will automatically scale to fill the entire screen. Use the same shortcut to exit Fullscreen mode.

#### Network Configuration

During the pfSense setup module (Part 2) we disabled DHCP on AD_LAB interface because of this our VM will not be automatically assigned a IP address. From the taskbar right-click on the network icon and select `Open Network & Internet settings`. 

![dc-19|300](images/building-home-lab-part-6/dc-19.png)

Click on "Change adapter options".

![dc-20|540](images/building-home-lab-part-6/dc-20.png)

In the Network Connections page we should see the Ethernet adapter. Right-click on the adapter and select Properties.

![dc-21|540](images/building-home-lab-part-6/dc-21.png)

Select `Internet Protocol Version 4 (TCP/IPv4)` and click on Properties.

![dc-22|400](images/building-home-lab-part-6/dc-22.png)

Enter the details as shown below and then click on Ok. Click on Ok again to close the Ethernet Properties menu.

![dc-23|400](images/building-home-lab-part-6/dc-23.png)

Windows will display a banner to allow internet access click on Yes.

![dc-24|560](images/building-home-lab-part-6/dc-24.png)

Close the Network Connections page. In the Settings app click on the Home button in the sidebar.

![dc-20|540](images/building-home-lab-part-6/dc-20.png)

#### Renaming the System

Before we can setup the machine to be a Domain Controller let us rename the PC to have an easily identifiable name. Select "System".

![dc-25|540](images/building-home-lab-part-6/dc-25.png)

Click on About on the sidebar and then click on the "Rename this PC" button. An popup will open give the PC a easy to remember name and then click on Next.

![dc-26|540](images/building-home-lab-part-6/dc-26.png)

Click on "Restart now" for the changes to take effect.

![dc-27|540](images/building-home-lab-part-6/dc-27.png)

#### Active Directory & DNS Installation

After login wait for Server Manager to load. Click on the Manage button from the top right corner and select "Add Roles and Features".

![dc-28|360](images/building-home-lab-part-6/dc-28.png)

Click on Next till you reach the Server Roles page.

![dc-29|540](images/building-home-lab-part-6/dc-29.png)

On this page enable "Active Directory Domain Services" and "DNS Server". Ensure to select the correct Active Directory feature.

![dc-30|540](images/building-home-lab-part-6/dc-30.png)

When you enable a feature the "Add Roles and Features Wizard" will open click on "Add Features" to confirm selection.

![dc-31|540](images/building-home-lab-part-6/dc-31.png)

![dc-32|540](images/building-home-lab-part-6/dc-32.png)

Once both the features are selected click on Next to proceed with installation.

![dc-33|540](images/building-home-lab-part-6/dc-33.png)

Click Next tell you reach the Conformation page. Here click on Install to start the installation of the selected features.

![dc-34|540](images/building-home-lab-part-6/dc-34.png)

![dc-35|540](images/building-home-lab-part-6/dc-35.png)

Once the installation is complete click on Close to exit the Wizard.

#### Active Directory Configuration

Click on the Flag icon present in the top right of the toolbar. From the dropdown click on "Promote this server to a domain controller".

![dc-36|400](images/building-home-lab-part-6/dc-36.png)

The AD Domain Servers Configuration Wizard will open. For deployment operation select `Add a new Forest`. Give the domain a name. For my setup I will be using the name `ad.lab`. After selecting the name click on Next.

**Note**: The name assigned to the domain has to consist of two words that are separated by a period.

![dc-37|540](images/building-home-lab-part-6/dc-37.png)

On this page enter a password to use for using the AD Restore feature.

![dc-38|540](images/building-home-lab-part-6/dc-38.png)

Ignore the warning that is shown and click on Next.

![dc-39|540](images/building-home-lab-part-6/dc-39.png)

The NetBIOS name should automatically get filled. It will be the first part of the domain name. Click on Next to continue.

![dc-40|540](images/building-home-lab-part-6/dc-40.png)

Click on Next.

![dc-41|540](images/building-home-lab-part-6/dc-41.png)

Click on Next.

![dc-42|540](images/building-home-lab-part-6/dc-42.png)

Click on Install to start the Domain Services setup process.

![dc-43|540](images/building-home-lab-part-6/dc-43.png)

Once the install process is complete the machine will need to be restarted. Click on Close to reboot the system.

![dc-44|540](images/building-home-lab-part-6/dc-44.png)

On restart you will notice that the name that is shown on the login page has changed. The first part of the domain name is prepended to the username. This means the machine has successfully been configured as the domain controller. Login using the Administrator password.

![dc-45|600](images/building-home-lab-part-6/dc-45.jpg)

#### DNS Configuration

Since we enabled DNS on this machine (Domain Controller). This machine (DC) will act as the DNS server for devices that are connected to the `ad.lab` environment. We need to configure a Forwarder. The Forwarder is the device to which DNS queries will be sent when the DC cannot resolve the query. In our case we need to forward the request to pfSense. The DNS service of pfSense will then perform the lookup.

Open the Start menu expand the "Windows Administrative Tools" folder and select DNS.

![dc-94|300](images/building-home-lab-part-6/dc-94.png)

In the sidebar select the Domain Controller (in my case DC1) and from the right menu double-click on "Forwarders".

![dc-95|540](images/building-home-lab-part-6/dc-95.png)

For the Forwarders tab of the Properties menu click on Edit.

![dc-96|540](images/building-home-lab-part-6/dc-96.png)

This will open the Forwarder configuration page. Enter the IP address of the AD_LAB interface (`10.80.80.1`) and press Enter. 

![dc-97|540](images/building-home-lab-part-6/dc-97.png)

Once added. Click on Ok to confirm the change.

![dc-98|540](images/building-home-lab-part-6/dc-98.png)

Click on Apply then Ok to save the changes.

![dc-99|540](images/building-home-lab-part-6/dc-99.png)

#### DHCP Installation

Since we had disabled DHCP on the `AD_LAB` interface when new devices are added to this network they will not be assigned an IP address automatically. We can enable the DHCP service on the DC. Once setup devices that connect to the `AD_LAB` network will be automatically assigned a IP address.  

Click on Manage from the toolbar in Server Manager. Then chose "Add Roles and Features".

![dc-46|400](images/building-home-lab-part-6/dc-46.png)

Keep clicking Next till you reach the "Server Roles" page. Enable "DHCP Server" then click on "Add Features". 

![dc-47|540](images/building-home-lab-part-6/dc-47.png)

![dc-48|540](images/building-home-lab-part-6/dc-48.png)

Keep clicking next till you reach the Confirmation page. Click install to enable DHCP.

![dc-49|540](images/building-home-lab-part-6/dc-49.png)

#### DHCP Configuration

After the installation is complete click on the Flag present in the toolbar of Server Manager and click on "Complete DHCP configuration".

![dc-61|400](images/building-home-lab-part-6/dc-61.png)

Click on Commit.

![dc-62|540](images/building-home-lab-part-6/dc-62.png)

Click on Close to complete the install.

![dc-63|540](images/building-home-lab-part-6/dc-63.png)

From the start menu click on "Windows Administrative Tools" and then chose DHCP.

![dc-50|400](images/building-home-lab-part-6/dc-50.png)

Expand the dropdown for the DHCP server (in my case `dc1.ad.lab`).

![dc-101|400](images/building-home-lab-part-6/dc-101.png)

Right-click on IPv4. Then select "New Scope". The scope defines the range of IP addresses that can be assigned to devices by the DHCP server.

![dc-51|440](images/building-home-lab-part-6/dc-51.png)

Enter a Name and Description for the new scope.

![dc-52|400](images/building-home-lab-part-6/dc-52.png)

Enter the details as shown below.

> **Note**  
> You can chose the Start IP address to be `10.80.80.3`. I have purposely left the starting IP addresses out of the DHCP scope. In the future if the need arises I can use these IPs for static IP assignment.  

![dc-53|400](images/building-home-lab-part-6/dc-53.png)

At the moment we don't have any Exclusions. Leave everything empty and click on Next.

![dc-54|400](images/building-home-lab-part-6/dc-54.png)

Increase the lease time to 365 days and click on Next 

Since we increase the lease duration when a IP address is assigned to a device the device will be allowed to use that IP address without requesting a new IP address for 365 days. 

![dc-55|400](images/building-home-lab-part-6/dc-55.png)

Select "Yes, I want to configure these options now" and click on Next.

![dc-56|400](images/building-home-lab-part-6/dc-56.png)

In the IP address field enter the default gateway for the `AD_LAB` interface (`10.80.80.1`) and then click on Add. Once added click on Next.

![dc-57|400](images/building-home-lab-part-6/dc-57.png)

Click on Next.

![dc-58|400](images/building-home-lab-part-6/dc-58.png)

We are not configuring a WINS Server for our environment so click on Next.

![dc-59|400](images/building-home-lab-part-6/dc-59.png)

Select "Yes, I want to activate this scope now" and click on Next.

![dc-60|400](images/building-home-lab-part-6/dc-60.png)

So far we have installed Windows Server 2019, configured it to be the Domain Controller (DC), setup DNS Forwarder and configured DHCP. 

We still need to create users in the DC and setup client machines to the AD environment. We will cover these topics in part 2 of this module.
