---
title: "Building Your Own Home Lab: Part 8 - Malware Analysis Lab Setup"
description: A step-by-step guide to build your very own Cybersecurity Home Lab using VirtualBox
date: 2024-01-14 19:30:00 -0600
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
image: images/building-home-lab-part-8/building-home-lab-part-8-banner.png
---

Banner Background by <a href="https://www.freepik.com/free-vector/gradient-white-color-background-abstract-modern_34010189.htm#query=simple%20backgrounds&position=28&from_view=search&track=ais&uuid=96e36b2e-64b3-42e2-8fd8-4fd18a6e1d5d">logturnal</a> on Freepik  
Hacker Image by <a href="https://www.freepik.com/free-vector/hacker-operating-laptop-cartoon-icon-illustration-technology-icon-concept-isolated-flat-cartoon-style_11602236.htm#page=2&query=hacker&position=28&from_view=search&track=sph&uuid=070b0d8a-d045-434d-9a51-f239e46d5f17">catalyststuff</a> on Freepik

In the module we are going to create a Malware Analysis Lab. This lab will consist of two VMs. One of the VM will run Windows will the other one will run Linux. More we start with the VM configuration we will have a look at VirtualBox CLI.

## Creating New Interface

VirtualBox GUI does not allow us to creating more than four Network Interface for a VM. 

![vbox-36|500](images/building-home-lab-part-8/vbox-36.png)

However, we can actually configure up to 8 interface per VM. To add more than 4 
interface we have to utilize the VirtualBox CLI.

### VirtualBox CLI

The CLI binary is called `VBoxManage.exe`.

![vbox-37|500](images/building-home-lab-part-8/vbox-37.png)

Before using the CLI we need to add it location as an environment variable.  
VirtualBox is by default installed  in: `C:\Program Files\Oracle\VirtualBox`.

Open Search and type "Environment". Click on "Edit environment variables for your account".

![vbox-38|440](images/building-home-lab-part-8/vbox-38.png)

In the top window select the variable named "Path" and then click on "Edit".

![vbox-40|460](images/building-home-lab-part-8/vbox-40.png)

Click on "New" and then paste the VirtualBox install location. Click on Ok.

![vbox-41|400](images/building-home-lab-part-8/vbox-41.png)

Click on Ok to close the Environment Variables menu.

To test if the variable was added successfully open PowerShell. Then enter the following command:

```powershell
# List all installed VMs
VBoxManage.exe list vms
```

![vbox-42|400](images/building-home-lab-part-8/vbox-42.png)

### Creating new Interface

Before we create the new interfaces we need to know the name of the pfSense VM. Additionally, ensure that is VM is "Powered Off".

![vbox-43|540](images/building-home-lab-part-8/vbox-43.png)

To create the interface running the following commands:

```powershell
# Create a Internet Network
VBoxManage modifyvm "pfSense" --nic5 intnet

# Use the Paravirtualized Adapter
VBoxManage modifyvm "pfSense" --nictype5 virtio

# Give it the name LAN 3
VBoxManage modifyvm "pfSense" --intnet5 "LAN 3"

# Network Interface is connected by Cable
VBoxManage modifyvm "pfSense" --cableconnected5 on
```

**Note:** In the above commands "pfSense" is the name of my VM. In the 3rd command in place of "LAN 3" you can use a different name.

![vbox-44|400](images/building-home-lab-part-8/vbox-44.png)

Now of we look at the overview of the pfSense VM we should see Adapter 5.

![vbox-45|540](images/building-home-lab-part-8/vbox-45.png)

### Adding the Interface

Start the pfSense VM. On boot you will notice that there is still only 4 interfaces. The new interface needs to be onboarded before it shown up.

![pfsense-83|500](images/building-home-lab-part-8/pfsense-83.png)

Enter `1` to select "Assign Interfaces".  
Should VLANs be set up now? `n`

![pfsense-84|500](images/building-home-lab-part-8/pfsense-84.png)

Enter the WAN interface name: `vtnet0`  
Enter the LAN interface name: `vtnet1`  
Enter the Optional 1 interface name: `vtnet2`  
Enter the Optional 2 interface name: `vtnet3`  
Enter the Optional 3 interface name: `vtnet4`

![pfsense-85|500](images/building-home-lab-part-8/pfsense-85.png)

Do you want to proceed?: `y`

![pfsense-86|500](images/building-home-lab-part-8/pfsense-86.png)

The new interface has been added. Now we need to assign the interface an IP address.

![pfsense-87|500](images/building-home-lab-part-8/pfsense-87.png)

Enter `2` to select "Set interface(s) IP address". Enter `5` to select the new interface. 

![pfsense-88|500](images/building-home-lab-part-8/pfsense-88.png)

Configure IPv4 address OPT3 interface via DHCP?: `n`  
Enter the new OPT3 IPv4 address: `10.99.99.1`  
Enter the new OPT3 IPv4 subnet bit count: `24`  

For the next question press Enter since we are configuring a LAN interface.

![pfsense-89|500](images/building-home-lab-part-8/pfsense-89.png)

Configure IPv6 address OPT3 interface via DHCP6: `n`  
For the new OPT3 IPv6 address question press Enter.  
Do you want to enable the DHCP server on OPT3?: `y`  
Enter the start address of the IPv4 client address range: `10.99.99.11`  
Enter the end address of the IPv4 client address range: `10.99.99.243`  
Do you want to revert to HTTP as the webConfigurator protocol?: `n`

![pfsense-90|500](images/building-home-lab-part-8/pfsense-90.png)

Now interface OPT3 will have an IP address.

![pfsense-91|500](images/building-home-lab-part-8/pfsense-91.png)

### Renaming Interface

Launch the Kali Linux VM that is configured on the LAN interface. Login to the pfSense web portal. From the navigation bar select `Interfaces -> OPT3`. 

![pfsense-92|560](images/building-home-lab-part-8/pfsense-92.png)

In the description field enter `ISOLATED`. Scroll to the bottom and click on Save.

![pfsense-93|560](images/building-home-lab-part-8/pfsense-93.png)

Click on Apply Changes in the popup that appears to persist the changes.

![pfsense-94|560](images/building-home-lab-part-8/pfsense-94.png)

### Interface Firewall Configuration

From the navigation bar click on `Firewall -> Rules`.

![pfsense-95|560](images/building-home-lab-part-8/pfsense-95.png)

Select the ISOLATED tab. This interface will not have any rules configured. Click on the "Add" button to create a new rule.

![pfsense-96|560](images/building-home-lab-part-8/pfsense-96.png)

Change the values as follows:  
Action: `Block`  
Address Family: `IPv4+IPv6`  
Protocol: `Any`  
Source: `ISOLATED subnets`  
Description: `Block access to everything`

Scroll to the bottom and click on Save.

![pfsense-97|560](images/building-home-lab-part-8/pfsense-97.png)

In the popup click on Apply Changes to persist the new rule.

![pfsense-98|560](images/building-home-lab-part-8/pfsense-98.png)

![pfsense-99|560](images/building-home-lab-part-8/pfsense-99.png)

**Note**: Since this Interface is going to be used for Malware Analysis we are blocking network access. This will ensure that the malware does not spread to other systems using the network.

## Flare VM Setup

To install Flare we first need to configure a Windows machine. Flare can be setup on most modern versions of Windows. Since we already have the ISO for Windows 10 Enterprise I will be using it to configure Flare.

## REMnux VM Setup
