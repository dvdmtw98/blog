---
title: "Building a Virtual Security Home Lab: Part 9 - Tsurugi Linux (DFIR) Setup"
description: A step-by-step guide for building your very own Cybersecurity Home Lab using VirtualBox
date: 2024-02-02 10:15:00 -0600
categories:
  - Security
  - Home Lab
tags:
  - security
  - home-lab
  - virtualbox
  - networking
  - dfir
published: true
media_subpath: /assets/
---

![banner-image|640](images/building-home-lab-part-9/building-home-lab-part-9-banner.png)

Banner Background by [logturnal](https://www.freepik.com/free-vector/gradient-white-color-background-abstract-modern_34010189.htm) on Freepik  
Hacker Image by [catalyststuff](https://www.freepik.com/free-vector/hacker-operating-laptop-cartoon-icon-illustration-technology-icon-concept-isolated-flat-cartoon-style_11602236.htm) on Freepik


> [!IMPORTANT] Changelog
> - **Oct. 31, 2024**
> 	- Updated instructions to reflect additonal step required to install Tsurugi Linux 2024.1+

In this module, we are going to set up Tsurugi Linux which is an OS that comes pre-configured with many of the commonly used Digital Forensics & Incident Response tools. Before deploying the VM we will create a new Interface in pfSense called Security that will have our DFIR VM and in the future other security tools.

## Creating New Interface

As discussed in the last module using VirtualBox GUI we cannot create more than 4 interfaces but using the CLI we can create up to 8 Interfaces.

### Creating new Interface

Before creating the interface we need the name of the pfSense VM. In my case, the VM is called "<u>pfSense</u>". Also, ensure the VM is "Powered Off" before running the commands. 

The last Adapter we created is called <u>Adapter 5</u>.

![vbox-45|420](images/building-home-lab-part-8/vbox-45.png)

Launch PowerShell and run the following commands:

```powershell
# Create a Internet Network
VBoxManage modifyvm "pfSense" --nic6 intnet

# Use the Paravirtualized Adapter
VBoxManage modifyvm "pfSense" --nictype6 virtio

# Give it the name LAN 3
VBoxManage modifyvm "pfSense" --intnet6 "LAN 4"

# Network Interface is connected by Cable
VBoxManage modifyvm "pfSense" --cableconnected6 on
```

> [!NOTE]
> In the above commands "pfSense" is the name of my VM.  
> In the 3rd command in place of "LAN 3" you can use a different name that matches your network name convention.

![vbox-46|400](images/building-home-lab-part-9/vbox-46.png)

The pfSense VM will now have an Adapter 6.

![vbox-47|540](images/building-home-lab-part-9/vbox-47.png)

### Enabling the Interface

Start the pfSense VM. pfSense will not detect the new interface. We need to onboard the interface before it shows up.

![pfsense-100|540](images/building-home-lab-part-9/pfsense-100.png)

Enter **`1`** to select "Assign Interfaces".  
Should VLANs be set up now? **`n`**

![pfsense-101|540](images/building-home-lab-part-9/pfsense-101.png)

Enter the WAN interface name: **`vtnet0`**  
Enter the LAN interface name: **`vtnet1`**  
Enter the Optional 1 interface name: **`vtnet2`**  
Enter the Optional 2 interface name: **`vtnet3`**  
Enter the Optional 3 interface name: **`vtnet4`**  
Enter the Optional 4 interface name: **`vtnet5`**

![pfsense-102|540](images/building-home-lab-part-9/pfsense-102.png)

Do you want to proceed?: **`y`**

![pfsense-103|540](images/building-home-lab-part-9/pfsense-103.png)

The new interface is onboarded. Now we need to assign it an IP address.

![pfsense-104|540](images/building-home-lab-part-9/pfsense-104.png)

Enter **`2`** to select "<u>Set interface(s) IP address</u>". Enter **`6`** to select the OPT4 interface.

![pfsense-105|540](images/building-home-lab-part-9/pfsense-105.png)

Configure IPv4 address OPT3 interface via DHCP?: **`n`**  
Enter the new OPT4 IPv4 address: **`10.10.10.1`**  
Enter the new OPT4 IPv4 subnet bit count: **`24`**  

For the next question directly press **`Enter`**. Since this is an **`LAN`** interface we do not have to worry about configuring the upstream gateway.

![pfsense-106|540](images/building-home-lab-part-9/pfsense-106.png)

Configure IPv6 address OPT4 interface via DHCP6: **`n`**  
For the new OPT4 IPv6 address question press **`Enter`**.  
Do you want to enable the DHCP server on OPT4?: **`y`**  
Enter the start address of the IPv4 client address range: **`10.10.10.11`**  
Enter the end address of the IPv4 client address range: **`10.10.10.243`**  
Do you want to revert to HTTP as the webConfigurator protocol?: **`n`**

![pfsense-107|540](images/building-home-lab-part-9/pfsense-107.png)

Now interface OPT4 will have an IP address.

![pfsense-108|540](images/building-home-lab-part-9/pfsense-108.png)

### Renaming the Interface

Launch the Kali Linux VM. Login to the pfSense web portal. From the navigation bar select **`Interfaces -> OPT4`**. 

![pfsense-109|580](images/building-home-lab-part-9/pfsense-109.png)

In the description field enter **`SECURITY`**. Scroll to the bottom and click on **`Save`**.

![pfsense-110|580](images/building-home-lab-part-9/pfsense-110.png)

Click on **`Apply Changes`** in the popup that appears to persist the changes.

![pfsense-111|580](images/building-home-lab-part-9/pfsense-111.png)

### Interface Firewall Configuration

From the navigation bar click on **`Firewall -> Rules`**.

![pfsense-95|560](images/building-home-lab-part-8/pfsense-95.png)

Select the SECURITY tab. Click on the "Add" button to create a new rule.

![pfsense-112|580](images/building-home-lab-part-9/pfsense-112.png)

Change the values as follows:  
Action: **`Block`**  
Address Family: **`IPv4+IPv6`**  
Protocol: **`Any`**  
Source: **`SECURITY subnets`**  
Destination: **`WAN subnets`**  
Description: **`Block access to services on WAN interface`**

Scroll to the bottom and click on **`Save`**.

![pfsense-113|580](images/building-home-lab-part-9/pfsense-113.png)

Ignore the popup for saving changes. Click on "Add" to create a new rule.

Change the values as follows:  
Action: **`Block`**  
Address Family: **`IPv4+IPv6`**  
Protocol: **`Any`**  
Source: **`SECURITY subnets`**  
Destination: **`LAN subnets`**  
Description: **`Block access to services on LAN`**

Scroll to the bottom and click on **`Save`**.

![pfsense-114|580](images/building-home-lab-part-9/pfsense-114.png)

Click on "Add" to create a new rule.

Change the values as follows:  
Address Family: **`IPv4+IPv6`**  
Protocol: **`Any`**  
Source: **`SECURITY subnets`**  
Description: **`Allow traffic to all subnets and Internet`**

Scroll to the bottom and click on **`Save`**.

![pfsense-115|580](images/building-home-lab-part-9/pfsense-115.png)

In the popup click on **`Apply Changes`** to persist the new rule.

![pfsense-116|580](images/building-home-lab-part-9/pfsense-116.png)

The final result will be as follows:

![pfsense-117|580](images/building-home-lab-part-9/pfsense-117.png)

### Reboot pfSense

Now we need to restart pfSense to ensure that the firewall rules are propagated properly. From the navigation bar select **`Diagnostics -> Reboot`**.

![pfsense-118|600](images/building-home-lab-part-4/pfsense-118.png)

Click on **`Submit`**.

![pfsense-119|600](images/building-home-lab-part-4/pfsense-119.png)

Once pfSense boots up you will be redirected to the login page.

## Tsurugi Linux Setup

### Download Image

Go to the following URL: [Tsurugi Linux - Downloads](https://tsurugi-linux.org/downloads.php). Select one of the Mirror Links.

![tsurugi-1|580](images/building-home-lab-part-9/tsurugi-1.png)

Download the ISO image. As of writing the latest version of Tsurugi Linux is **`2023.2`**.  
The ISO is ~16GB. It will take a while to download.

![tsurugi-2|440](images/building-home-lab-part-9/tsurugi-2.png)

After the download is complete we will have a **`.iso`** file.

![tsurugi-29|600](images/building-home-lab-part-9/tsurugi-29.png)

### Creating the VM

Select Tools from the sidebar and then select **`New`**.

![tsurugi-3|540](images/building-home-lab-part-9/tsurugi-3.png)

Give the VM a <u>name</u> and then select the downloaded <u>ISO image</u>. Click on **`Next`**.

![tsurugi-4|540](images/building-home-lab-part-9/tsurugi-4.png)

Increase the Base <u>Memory</u> to **`4096MB`** and then click on **`Next`**.

![tsurugi-5|540](images/building-home-lab-part-9/tsurugi-5.png)

Increase the <u>Hard Disk</u> size to **`150GB`**.

> [!NOTE]
> Tsurugi Linux installation will not work if we provide less than **`110GB`** of storage.

![tsurugi-6|540](images/building-home-lab-part-9/tsurugi-6.png)

Click if all the settings look right and then click on **`Finish`**.

![tsurugi-7|540](images/building-home-lab-part-9/tsurugi-7.png)

#### Adding VM to Group

Right-click on the VM name and then select "<u>Move to Group</u>" and then choose **`New`**.

![tsurugi-8|400](images/building-home-lab-part-9/tsurugi-8.png)

Right-click on the group name, select "<u>Rename Group</u>" and call it "<u>Security</u>".

![tsurugi-9|300](images/building-home-lab-part-9/tsurugi-9.png)

Right-click on the group name, select "<u>Move to Group</u>" and then select "<u>Home Lab</u>".

![tsurugi-10|400](images/building-home-lab-part-9/tsurugi-10.png)

The final result should match the following:

![tsurugi-11|300](images/building-home-lab-part-9/tsurugi-11.png)

### Configuring the VM

Select the VM and then from the toolbar select "<u>Settings</u>".

![tsurugi-12|540](images/building-home-lab-part-9/tsurugi-12.png)

Go to **`System -> Motherboard`**. In <u>Boot Order</u> ensure that Hard Disk is on top followed by Optical. Uncheck Floppy.

![tsurugi-13|540](images/building-home-lab-part-9/tsurugi-13.png)

> [!ATTENTION] Tsurugi Linux 2024.1+ Additional Step  
> Tsurugi Linux 2024.1 onwards it is necessary to also enabled the “Enable EFI” option in VirtualBox. If this option is not enabled the OS installation will fail.  
> 
> ![[tsurugi-47.png|360]]

Go to **`Network -> Adapter 1`**. For the <u>Attached to</u> option select **`Internal Network`**. For <u>name</u> select **`LAN 4`**. Click on **`OK`** to save the changes.

![tsurugi-14|540](images/building-home-lab-part-9/tsurugi-14.png)

### Installing Tsurugi Linux

Select the VM and from the toolbar select **`Start`**.

![tsurugi-15|540](images/building-home-lab-part-9/tsurugi-15.png)

Press **`Enter`** to start the Tsurugi Linux in GUI mode.

![tsurugi-16|500](images/building-home-lab-part-9/tsurugi-16.png)

Once on the desktop double-click on **`Displays`**.

![tsurugi-17|560](images/building-home-lab-part-9/tsurugi-17.png)

In the Resolution window select <u>1600x1050</u> and click on **`Apply`**.

![tsurugi-18|560](images/building-home-lab-part-9/tsurugi-18.png)

Click on "<u>Keep This Configuration</u>" to confirm the changes.

> [!NOTE]
> Without changing the resolution of the screen you will not be able to see the buttons that are present at the bottom of the Installer.

![tsurugi-19|460](images/building-home-lab-part-9/tsurugi-19.jpg)

Double-click on the "<u>Install Tsurugi Linux 2023.2</u>" icon to start the installer.

![tsurugi-20|560](images/building-home-lab-part-9/tsurugi-20.png)

Once the installer starts. Use the scrollbar on the right side of the VM display and scroll to the bottom. Select your <u>language</u> and click on **`Continue`**.

![tsurugi-21|540](images/building-home-lab-part-9/tsurugi-21.png)

Select <u>Keyboard</u> and click on **`Continue`**.

![tsurugi-22|540](images/building-home-lab-part-9/tsurugi-22.png)

Enable "<u>Install third-party software for graphics and Wi-Fi hardware and additional media features</u>" and click on **`Continue`**. 

![tsurugi-23|540](images/building-home-lab-part-9/tsurugi-23.png)

Click on **`Install Now`**.

![tsurugi-24|540](images/building-home-lab-part-9/tsurugi-24.png)

Click on **`Continue`**.

![tsurugi-25|540](images/building-home-lab-part-9/tsurugi-25.png)

Select your <u>location/timezone</u> using the map and click on **`Continue`**.

![tsurugi-26|540](images/building-home-lab-part-9/tsurugi-26.png)

Provide a username, computer name and password then click on **`Continue`**.

![tsurugi-27|540](images/building-home-lab-part-9/tsurugi-27.png)

![tsurugi-28|540](images/building-home-lab-part-9/tsurugi-28.jpg)

After the installation is complete click on "<u>Restart Now</u>".

![tsurugi-30|400](images/building-home-lab-part-9/tsurugi-30.png)

When the VM reboots you might get the following screen. VirtualBox should automatically remove this disk when the screen appears. Press **`Enter`** to continue.

![tsurugi-31|540](images/building-home-lab-part-9/tsurugi-31.png)

Login using the password that was configured.

![tsurugi-32|540](images/building-home-lab-part-9/tsurugi-32.png)

### Post-Install Configuration

#### Guest Additions Installation

Click on **`Devices -> Inert Guest Additions CD Image`**. This will insert the ISO image.

![tsurugi-33|400](images/building-home-lab-part-9/tsurugi-33.png)

You might be prompted for credentials. Enter the <u>password</u> and click on **`Authenticate`**.

![tsurugi-34|400](images/building-home-lab-part-9/tsurugi-34.png)

From the top right corner click on the CD icon then select **`Mount VBox_GAs`**.

![tsurugi-35|300](images/building-home-lab-part-9/tsurugi-35.png)

The <u>ISO image</u> will not be visible on the desktop. Double-click on the Image icon.

![tsurugi-36|540](images/building-home-lab-part-9/tsurugi-36.png)

From the toolbar select **`Tools -> Open Current Folder in Terminal`**.

![tsurugi-45|580](images/building-home-lab-part-9/tsurugi-45.png)

Run the following command to install Guest Additions.

```bash
sudo ./VBoxLinuxAdditions.run
```

![tsurugi-46|500](images/building-home-lab-part-9/tsurugi-46.png)

Once the installation is complete. Press **`Right Ctrl+F`** to enter <u>Fullscreen</u> mode. The same key can be used to exit Fullscreen the VM will scale to fit the window size. From the top right corner select **`Eject VBox_GAs`** to remove the ISO image.

![tsurugi-38|300](images/building-home-lab-part-9/tsurugi-38.png)

To Shutdown the system click on the <u>power icon</u> beside the clock then select "<u>Shut Down</u>".

![tsurugi-39|300](images/building-home-lab-part-9/tsurugi-39.png)

Select "<u>Shut Down</u>"

![tsurugi-40|400](images/building-home-lab-part-9/tsurugi-40.png)

#### Updating the System

Open the **`terminator`** app from the desktop and run the following command:

```bash
sudo apt update && sudo apt full-upgrade
```

![tsurugi-44|560](images/building-home-lab-part-9/tsurugi-44.png)

If there are any updates click **`Enter`** to start the installation. Provide your password when prompted.

#### Creating VM Snapshot

Shut down the VM before creating a Snapshot. Use the <u>Hamburger menu</u> beside the VM name to access the Snapshot page.

![tsurugi-41|540](images/building-home-lab-part-9/tsurugi-41.png)

Click on **`Take`** to create a Snapshot.

![tsurugi-42|540](images/building-home-lab-part-9/tsurugi-42.png)

Give the Snapshot a descriptive <u>name</u> and click on **`OK`**.

![remnux-12|400](images/building-home-lab-part-8/remnux-12.png)

Use the Hamburger menu and click on Details to return to the main page.

![tsurugi-43|540](images/building-home-lab-part-9/tsurugi-43.png)

In the next module, we will install **`Ubuntu`** and then download and set up **`Splunk`**. We will also install the Splunk Universal Forwarder on the Domain Controller in our Active Directory Lab. This will allow us to capture the events that are generated on the Domain Controller.

[Part 10 - Splunk Setup & Configuration](https://blog.davidvarghese.dev/posts/building-home-lab-part-10/)
