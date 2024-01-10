---
categories:
  - Security
  - Home Lab
date: 2024-01-26 19:45:00 -0600
description: A step-by-step guide for building your very own Cybersecurity Home Lab using VirtualBox
img_path: /assets/
published: false
tags:
  - security
  - home-lab
  - virtualbox
  - networking
  - dfir
title: "Building a Virtual Security Home Lab: Part 9 - Tsurugi Linux (DFIR) Setup"
---

![banner-image|640](images/building-home-lab-part-9/building-home-lab-part-9-banner.png)

Banner Background by [logturnal](https://www.freepik.com/free-vector/gradient-white-color-background-abstract-modern_34010189.htm) on Freepik  
Hacker Image by [catalyststuff](https://www.freepik.com/free-vector/hacker-operating-laptop-cartoon-icon-illustration-technology-icon-concept-isolated-flat-cartoon-style_11602236.htm) on Freepik

In this module we are going to setup Tsurugi Linux which is an Linux based OS that is configured with the commonly used Digital Forensics & Incident Response tools. Before deploying the VM we will create a new Interface called Security that will have our DFIR VM and in the future other security tools.

## Creating New Interface

To run our DFIR VM require to create a new Interface for our router. As discussed in the last module using VirtualBox GUI we cannot create more than more Interface but using the CLI we can create up to 8 Interfaces. So let us use the CLI to create a new interface.

### Creating new Interface

Before creating the interface we need the name of the pfSense VM. In my case the VM is called "pfSense" also ensure the VM is "Powered Off" before running the commands.

![vbox-45|540](images/building-home-lab-part-8/vbox-45.png)

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

**Note:** In the above commands "pfSense" is the name of my VM. In the 3rd command in place of "LAN 3" you can use a different name that matches your network name convention.

![vbox-46|400](images/building-home-lab-part-9/vbox-46.png)

The pfSense VM will now have an Adapter 6.

![vbox-47|540](images/building-home-lab-part-9/vbox-47.png)

### Enabling the Interface

Start the pfSense VM. pfSense will not detect the new interface. We need to onboard the interface before if shows up.

![pfsense-100|540](images/building-home-lab-part-9/pfsense-100.png)

Enter `1` to select "Assign Interfaces".  
Should VLANs be set up now? `n`

![pfsense-101|540](images/building-home-lab-part-9/pfsense-101.png)

Enter the WAN interface name: `vtnet0`  
Enter the LAN interface name: `vtnet1`  
Enter the Optional 1 interface name: `vtnet2`  
Enter the Optional 2 interface name: `vtnet3`  
Enter the Optional 3 interface name: `vtnet4`  
Enter the Optional 4 interface name: `vtnet5`

![pfsense-102|540](images/building-home-lab-part-9/pfsense-102.png)

Do you want to proceed?: `y`

![pfsense-103|540](images/building-home-lab-part-9/pfsense-103.png)

The new interface is onboarded. Now we need to assign it an IP address.

![pfsense-104|540](images/building-home-lab-part-9/pfsense-104.png)

Enter `2` to select "Set interface(s) IP address". Enter `6` to select the OPT4 interface.

![pfsense-105|540](images/building-home-lab-part-9/pfsense-105.png)

Configure IPv4 address OPT3 interface via DHCP?: `n`  
Enter the new OPT3 IPv4 address: `10.10.10.1`  
Enter the new OPT3 IPv4 subnet bit count: `24`  

For the next question directly press `Enter`. Since this is an `LAN` interface we do not have to worry about configuring upstream gateway.

![pfsense-106|540](images/building-home-lab-part-9/pfsense-106.png)

Configure IPv6 address OPT3 interface via DHCP6: `n`  
For the new OPT3 IPv6 address question press `Enter`.  
Do you want to enable the DHCP server on OPT3?: `y`  
Enter the start address of the IPv4 client address range: `10.10.10.11`  
Enter the end address of the IPv4 client address range: `10.10.10.243`  
Do you want to revert to HTTP as the webConfigurator protocol?: `n`

![pfsense-107|540](images/building-home-lab-part-9/pfsense-107.png)

Now interface OPT4 will have an IP address.

![pfsense-108|540](images/building-home-lab-part-9/pfsense-108.png)

### Renaming the Interface

Launch the Kali Linux VM. Login to the pfSense web portal. From the navigation bar select `Interfaces -> OPT4`. 

![pfsense-109|580](images/building-home-lab-part-9/pfsense-109.png)

In the description field enter `SECURITY`. Scroll to the bottom and click on Save.

![pfsense-110|580](images/building-home-lab-part-9/pfsense-110.png)

Click on Apply Changes in the popup that appears to persist the changes.

![pfsense-111|580](images/building-home-lab-part-9/pfsense-111.png)

### Interface Firewall Configuration

From the navigation bar click on `Firewall -> Rules`.

![pfsense-95|560](images/building-home-lab-part-8/pfsense-95.png)

Select the SECURITY tab. Click on the "Add" button to create a new rule.

![pfsense-112|580](images/building-home-lab-part-9/pfsense-112.png)

Change the values as follows:  
Action: `Block`  
Address Family: `IPv4+IPv6`  
Protocol: `Any`  
Source: `SECURITY subnets`  
Destination: `WAN subnets`  
Description: `Block access to services on WAN interface`

Scroll to the bottom and click on Save.

![pfsense-113|580](images/building-home-lab-part-9/pfsense-113.png)

Ignore the popup for saving changes. Click on "Add" to create a new rule.

Change the values as follows:  
Action: `Block`  
Address Family: `IPv4+IPv6`  
Protocol: `Any`  
Source: `SECURITY subnets`  
Destination: `LAN subnets`  
Description: `Block access to services on LAN`

Scroll to the bottom and click on Save.

![pfsense-114|580](images/building-home-lab-part-9/pfsense-114.png)

Click on "Add" to create a new rule.

Change the values as follows:  
Address Family: `IPv4+IPv6`  
Protocol: `Any`  
Source: `SECURITY subnets`  
Description: `Block traffic to all subnets and Internet`

Scroll to the bottom and click on Save.

![pfsense-115|580](images/building-home-lab-part-9/pfsense-115.png)

In the popup click on Apply Changes to persist the new rule.

![pfsense-116|580](images/building-home-lab-part-9/pfsense-116.png)

The final result will be as follows:

![pfsense-117|580](images/building-home-lab-part-9/pfsense-117.png)

## Tsurugi Linux Setup

### Download Image

Go to the following URL: [Tsurugi Linux - Downloads](https://tsurugi-linux.org/downloads.php). Select one of the Mirror Links.

![tsurugi-1|580](images/building-home-lab-part-9/tsurugi-1.png)

Download the ISO image. As of writing the latest version of Tsurugi Linux is `2023.2`.  
The ISO is ~16GB. It will take a while to download.

![tsurugi-2|440](images/building-home-lab-part-9/tsurugi-2.png)

After download is complete we will have a `.iso` file.

![tsurugi-29|600](images/building-home-lab-part-9/tsurugi-29.png)

### Creating the VM

Select Tools from the sidebar and then select New.

![tsurugi-3|540](images/building-home-lab-part-9/tsurugi-3.png)

Give the VM a name and then select the downloaded ISO image. Click on Next.

![tsurugi-4|540](images/building-home-lab-part-9/tsurugi-4.png)

Increase the Base Memory to 4096MB and then click on Next.

![tsurugi-5|540](images/building-home-lab-part-9/tsurugi-5.png)

Increase the Hard Disk size to 150GB. Ensure that Pre-allocate Full Size is not selected.

**Note:** Tsurugi Linux installation will not work if we provide less than 110GB of storage.

![tsurugi-6|540](images/building-home-lab-part-9/tsurugi-6.png)

Click if all the settings look right and then click on Finish.

![tsurugi-7|540](images/building-home-lab-part-9/tsurugi-7.png)

#### Adding VM to Group

Right-click on the VM name and select "Move to Group" and then chose New.

![tsurugi-8|400](images/building-home-lab-part-9/tsurugi-8.png)

Right-click on the group name, select "Rename Group" and call it "Security".

![tsurugi-9|300](images/building-home-lab-part-9/tsurugi-9.png)

Right-click on the group name, select "Move to Group" and then select "Home Lab".

![tsurugi-10|400](images/building-home-lab-part-9/tsurugi-10.png)

The final result should match the following:

![tsurugi-11|300](images/building-home-lab-part-9/tsurugi-11.png)

### Configuring the VM

Select the VM and then from the toolbar select "Settings".

![tsurugi-12|540](images/building-home-lab-part-9/tsurugi-12.png)

Go to `System -> Motherboard`. In Boot Order ensure that Hard Disk is on top followed by Optical. Uncheck Floppy.

![tsurugi-13|540](images/building-home-lab-part-9/tsurugi-13.png)

Go to `Network -> Adapter 1`. For Attached to option select Internal Network. For name select LAN 4. Click on Ok to save the changes.

![tsurugi-14|540](images/building-home-lab-part-9/tsurugi-14.png)

### Installing Tsurugi Linux

Select the VM and from the toolbar select Start.

![tsurugi-15|540](images/building-home-lab-part-9/tsurugi-15.png)

Press Enter to start the Tsurugi Linux in GUI mode.

![tsurugi-16|500](images/building-home-lab-part-9/tsurugi-16.png)

Once on the desktop double-click on Displays.

![tsurugi-17|560](images/building-home-lab-part-9/tsurugi-17.png)

In the Resolution window select 1600x1050 and click on Apply.

![tsurugi-18|560](images/building-home-lab-part-9/tsurugi-18.png)

Click on Keep This Configuration to confirm the changes.

**Note:** Without changing the resolution of the screen you will not be able to see the buttons that exist at the bottom of the Installer.

![tsurugi-19|460](images/building-home-lab-part-9/tsurugi-19.jpg)

Double-click on the "Install Tsurugi Linux 2023.2" icon to start the installer.

![tsurugi-20|560](images/building-home-lab-part-9/tsurugi-20.png)

Once the installer starts. Use the scrollbar on the right side of the VM display and scroll to the bottom. Select your language and click on Continue.

![tsurugi-21|540](images/building-home-lab-part-9/tsurugi-21.png)

Select Keyboard and click on Continue.

![tsurugi-22|540](images/building-home-lab-part-9/tsurugi-22.png)

Enable "Install third party software for graphics and Wi-Fi hardware and additional media features" and click on Continue. 

![tsurugi-23|540](images/building-home-lab-part-9/tsurugi-23.png)

Click on Install Now.

![tsurugi-24|540](images/building-home-lab-part-9/tsurugi-24.png)

Click on Continue.

![tsurugi-25|540](images/building-home-lab-part-9/tsurugi-25.png)

Select your location/timezone using the map and click on Continue.

![tsurugi-26|540](images/building-home-lab-part-9/tsurugi-26.png)

Provide a username, computer name and password then click on Continue.

![tsurugi-27|540](images/building-home-lab-part-9/tsurugi-27.png)

Wait for the Operating System to install.

![tsurugi-28|540](images/building-home-lab-part-9/tsurugi-28.jpg)

After the install is complete click on "Restart Now".

![tsurugi-30|400](images/building-home-lab-part-9/tsurugi-30.png)

When the VM reboots you might get the following screen. VirtualBox will automatically remove this disk. Press Enter to continue.

![tsurugi-31|540](images/building-home-lab-part-9/tsurugi-31.png)

Login using the password that was configured.

![tsurugi-32|540](images/building-home-lab-part-9/tsurugi-32.png)

### Post-Install Configuration

#### Guest Additions Installation

Click on `Devices -> Inert Guest Additions CD Image`. This will insert the ISO image.

![tsurugi-33|400](images/building-home-lab-part-9/tsurugi-33.png)

You might be prompted for credentials. Enter the password and click on Authenticate.

![tsurugi-34|400](images/building-home-lab-part-9/tsurugi-34.png)

From the top right-corner click on the CD icon then select `Mount VBox_GAs`.

![tsurugi-35|300](images/building-home-lab-part-9/tsurugi-35.png)

The ISO image will not be visible on the desktop. Double-click on the Image icon.

![tsurugi-36|540](images/building-home-lab-part-9/tsurugi-36.png)

From the toolbar select `Tools -> Open Current Folder in Terminal`.

![tsurugi-45|580](images/building-home-lab-part-9/tsurugi-45.png)

Run the following command to install Guest Additions.

```bash
sudo ./VBoxLinuxAdditions.run
```

![tsurugi-46|500](images/building-home-lab-part-9/tsurugi-46.png)

Once the install is complete. Press `Right Ctrl+F` to enter Fullscreen mode. The same key can be used to exit Fullscreen the VM will scale to fit the window size. From the top right-corner select `Eject VBox_GAs` to remove the ISO image.

![tsurugi-38|300](images/building-home-lab-part-9/tsurugi-38.png)

To Shutdown the system click on the icon beside the clock then select "Shut Down".

![tsurugi-39|300](images/building-home-lab-part-9/tsurugi-39.png)

Select "Shut Down".

![tsurugi-40|400](images/building-home-lab-part-9/tsurugi-40.png)

#### Updating the System

Open `terminator` and run the following command:

```bash
sudo apt update && sudo apt full-upgrade
```

![tsurugi-44|560](images/building-home-lab-part-9/tsurugi-44.png)

If there are any updates click Enter to start the install. Provide password when prompted.

#### Creating VM Snapshot

Use the Hamburger menu beside the VM name to access the Snapshot page.

![tsurugi-41|540](images/building-home-lab-part-9/tsurugi-41.png)

Click on Take to create a Snapshot.

![tsurugi-42|540](images/building-home-lab-part-9/tsurugi-42.png)

Give the Snapshot a descriptive name and click on Ok.

![remnux-12|400](images/building-home-lab-part-8/remnux-12.png)

Use the Hamburger menu and click on Details to return to the main page.

![tsurugi-43|540](images/building-home-lab-part-9/tsurugi-43.png)

In the next module, we will install Ubuntu and then download and setup Splunk. We will also install the Splunk Universal Forwarder on the Domain Controller in our Active Directory Lab. This will allow us to capture capture the events that are generated on the DC.