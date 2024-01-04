---
categories:
  - Security
  - Home Lab
date: 2024-01-14 19:30:00 -0600
description: A step-by-step guide for building your very own Cybersecurity Home Lab using VirtualBox
img_path: /assets/
published: false
tags:
  - security
  - home-lab
  - virtualbox
  - networking
  - malware
title: "Building a Virtual Security Home Lab: Part 8 - Malware Analysis Lab Setup"
---

![banner-image|640](images/building-home-lab-part-8/building-home-lab-part-8-banner.png)

Banner Background by [logturnal](https://www.freepik.com/free-vector/gradient-white-color-background-abstract-modern_34010189.htm) on Freepik  
Hacker Image by [catalyststuff](https://www.freepik.com/free-vector/hacker-operating-laptop-cartoon-icon-illustration-technology-icon-concept-isolated-flat-cartoon-style_11602236.htm) on Freepik

In the module we are going to create a Malware Analysis Lab. This lab will consist of two VMs. One of the VM will run Windows will the other one will run Linux. More we start with the VM configuration we will have a look at VirtualBox CLI.

## Creating New Interface

VirtualBox GUI does not allow us to creating more than four Network Interface for a VM. 

![vbox-36|500](images/building-home-lab-part-8/vbox-36.png)

However, we can actually configure up to 8 interface per VM. To add more than 4 
interface we have to utilize the VirtualBox CLI.

### VirtualBox CLI Setup

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

**Note:** In the above commands "pfSense" is the name of my VM. In the 3rd command in place of "LAN 3" you can use a different name that matches your network name convention.

![vbox-44|400](images/building-home-lab-part-8/vbox-44.png)

Now of we look at the overview of the pfSense VM we should see Adapter 5.

![vbox-45|400](images/building-home-lab-part-8/vbox-45.png)

### Enabling the Interface

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

Enter `2` to select "Set interface(s) IP address". Enter `5` to select the OPT3 interface. 

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

### Renaming the Interface

Launch the Kali Linux VM. Login to the pfSense web portal. From the navigation bar select `Interfaces -> OPT3`. 

![pfsense-92|560](images/building-home-lab-part-8/pfsense-92.png)

In the description field enter `ISOLATED`. Scroll to the bottom and click on Save.

![pfsense-93|560](images/building-home-lab-part-8/pfsense-93.png)

Click on Apply Changes in the popup that appears to persist the changes.

![pfsense-94|560](images/building-home-lab-part-8/pfsense-94.png)

### Interface Firewall Configuration

From the navigation bar click on `Firewall -> Rules`.

![pfsense-95|560](images/building-home-lab-part-8/pfsense-95.png)

Select the ISOLATED tab. Click on the "Add" button to create a new rule.

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

**Note**: Since this Interface is going to be used for Malware Analysis we are blocking network access. This will ensure that malware does not have a way to spread to other systems using the network.

## Flare VM Setup

To install Flare we first need to configure a Windows machine. Flare can be setup on most modern versions of Windows. Since we already have the ISO for Windows 10 Enterprise I will be using it to configure Flare.

### Windows ISO Download

Go to the following URL: [Windows 10 Enterprise \| Microsoft Evaluation Center](https://www.microsoft.com/en-us/evalcenter/download-windows-10-enterprise)

Click on the 64-bit Enterprise ISO download option. The ISO file is ~5GB.

![win-download-2|560](images/building-home-lab-part-6/win-download-2.png)

### Creating the VM

Select Tools from the sidebar and click on New.

![flare-1|540](images/building-home-lab-part-8/flare-1.png)

Give the VM a name. Select the downloaded Windows 10 ISO Image. Check "Skip Unattended Installation".

![flare-2|540](images/building-home-lab-part-8/flare-2.png)

Increase Base Memory to 4096GB and click on Next.

![flare-3|540](images/building-home-lab-part-8/flare-3.png)

Increase the Hard Drive size to 100GB. Ensure Pre-allocate Full Size is not selected and click on Next.

![flare-4|540](images/building-home-lab-part-8/flare-4.png)

Confirm all the settings and click on Finish.

![flare-5|540](images/building-home-lab-part-8/flare-5.png)

#### Adding VM to Group

Right-click on the VM and select "Move to Group" and then click on New.

![flare-6|400](images/building-home-lab-part-8/flare-6.png)

Right-click on the group and rename it to "Malware Analysis".

![flare-7|300](images/building-home-lab-part-8/flare-7.png)

Right-click on the "Malware Analysis" group. Select "Move to Group" and then chose "Home Lab".

![flare-8|400](images/building-home-lab-part-8/flare-8.png)

The final result should look as follows:

![flare-9|300](images/building-home-lab-part-8/flare-9.png)

### Configuring the VM

Select the VM then from the toolbar select "Settings".

![flare-10|540](images/building-home-lab-part-8/flare-10.png)

Go to `System -> Motherboard` in Boot Order ensure Hard Drive is not the top followed by Optical. Uncheck Floppy.

![flare-11|540](images/building-home-lab-part-8/flare-11.png)

Leave Network on the default setting of NAT.

> **Note**  
> The ISOLATED interface does not have internet connection. To setup Flare we need Internet. Once we finish the configuration we will move it to the correct subnet. 

![flare-12|540](images/building-home-lab-part-8/flare-12.png)

### Installing Windows

Go to the Windows Installer. Refer to the previous module (Part 7) for details instructions on installing Windows 10 Enterprise.

![user-1|540](images/building-home-lab-part-7/user-1.png)

![user-2|540](images/building-home-lab-part-7/user-2.png)

![user-4|540](images/building-home-lab-part-7/user-4.png)

![user-5|540](images/building-home-lab-part-7/user-5.png)

![user-6|540](images/building-home-lab-part-7/user-6.png)

![user-7|540](images/building-home-lab-part-7/user-7.png)

Select "Domain join instead".

![user-10|540](images/building-home-lab-part-7/user-10.png)

Ensure to use a name that does not have special characters and spaces. This is very important. The installer for Flare will not work otherwise. 

![flare-13|540](images/building-home-lab-part-8/flare-13.png)

![user-13|540](images/building-home-lab-part-7/user-13.png)

![user-14|540](images/building-home-lab-part-7/user-14.png)

![user-15|540](images/building-home-lab-part-7/user-15.png)

Once on the desktop Windows will ask if access to Internet should be allowed click on "Yes".

#### Guest Additions Installation

Install Guest Additions to enable the resizing on the VM display. Once again refer to the last module (Part 7) for more detailed steps.

![user-17|500](images/building-home-lab-part-7/user-17.png)

![user-18|380](images/building-home-lab-part-7/user-18.png)

![user-19|540](images/building-home-lab-part-7/user-19.png)

![user-20|400](images/building-home-lab-part-7/user-20.png)

![user-22|400](images/building-home-lab-part-7/user-22.png)

![user-23|400](images/building-home-lab-part-7/user-23.png)

After rebooting the VM. Remove the Guest Addition Image.

![user-25|400](images/building-home-lab-part-7/user-25.png)

#### Creating VM Snapshot 1

Before we proceed we are going to take a snapshot of the VM. Snapshots allow us to rollback to a old configuration of the VM.

Shutdown the VM. Click on the hamburger menu on the right on the VM name in the sidebar. Select Snapshots.

![flare-21|540](images/building-home-lab-part-8/flare-21.png)

Click on Take.

![flare-30|460](images/building-home-lab-part-8/flare-30.png)

Give the Snapshot a name. You can optionally provide a Description as well. Click on Ok to create the Snapshot.

![flare-22|400](images/building-home-lab-part-8/flare-22.png)

Once again click on the Hamburger menu and click on Details to return back to the original page. 

### Flare VM Pre-Install Configuration

You can read more about Flare VM and its pre-requisites on the below link:  
[mandiant/flare-vm: A collection of scripts to setup a reverse engineering environment](https://github.com/mandiant/flare-vm)

We need to disable Windows Updates and Windows Defender before starting the installer.

#### Disabling Windows Update

[How to change account password on Windows 11 \| Windows Central](https://www.windowscentral.com/software-apps/windows-11/how-to-change-account-password-on-windows-11)

Click on Search and enter "Settings" and open the settings app.

![flare-14|500](images/building-home-lab-part-8/flare-14.png)

Click on "Update & Security".

![flare-16|560](images/building-home-lab-part-8/flare-16.png)

Click on "Pause updates for 7 days" button.

![flare-15|560](images/building-home-lab-part-8/flare-15.png)

#### Disabling Windows Defender

To disable Windows Defender we will use the following PowerShell script:  
[jeremybeaume/tools: Script to disable Windows Defender](https://github.com/jeremybeaume/tools/blob/master/disable-defender.ps1)

Right-click on the Shield icon on the taskbar and select "View Security Dashboard".

![flare-17|300](images/building-home-lab-part-8/flare-17.png)

Click on "Virus & threat protection".

![flare-18|580](images/building-home-lab-part-8/flare-18.png)

Select "Manage settings" below "Virus & threat protection settings".

![flare-19|300](images/building-home-lab-part-8/flare-19.png)

Disable all the feature that are shown in the below image:

![flare-20|340](images/building-home-lab-part-8/flare-20.png)

Right-click on the Start menu and select "Windows PowerShell (Admin)".

![flare-23|240](images/building-home-lab-part-8/flare-23.png)

Run the following command to download the script to disable Defender:

```powershell
# Save the script in the Downloads folder
Invoke-WebRequest "https://raw.githubusercontent.com/jeremybeaume/tools/master/disable-defender.ps1" -OutFile $HOME\Downloads\disable-defender.ps1
```

![flare-48|600](images/building-home-lab-part-8/flare-48.png)

Click `Windows+R` to open the Run dialog. Enter "msconfig" and click on Ok. 

![flare-24|340](images/building-home-lab-part-8/flare-24.png)

Navigate to the Boot tab and in the Boot options section enable "Safe boot" then click in Ok to save changes.

![flare-25|480](images/building-home-lab-part-8/flare-25.png)

Click on Restart to boot into Safe Mode.

![flare-26|340](images/building-home-lab-part-8/flare-26.png)

In save mode the VM size will not scale.

![flare-27|540](images/building-home-lab-part-8/flare-27.png)

Right-click on Start menu and select "Windows PowerShell (Admin)" and enter the following commands:

```powershell
# Change directory
cd .\Downloads\
# Unblock the downloaded script
Unblock-File .\disable-defender.ps1
# Disable the PowerShell policy preventing script execution 
Set-ExecutionPolicy Unrestricted -Force
# Start the script
.\disable-defender.ps1
```

![flare-28|500](images/building-home-lab-part-8/flare-28.png)

Once the script completes its execution click Enter to close the script. Reboot the VM for the changes to take place.

![flare-29|400](images/building-home-lab-part-8/flare-29.png)

Press `Windows+R` to open the Run dialog. Enter `msconfig` and click on Ok.

Navigate to the Boot tab and in the Boot options section disable "Safe boot".

![flare-31|480](images/building-home-lab-part-8/flare-31.png)

Once Windows boots normally. Wait for some time for Defender to load completely and then you will see that "Virus & threat protection" will show as disabled.

![flare-32|560](images/building-home-lab-part-8/flare-32.png)

#### Renaming the VM

Search for " This PC" and from the right-side click on "Properties".

![flare-35|500](images/building-home-lab-part-8/flare-35.png)

Select "Rename this PC".

![flare-36|400](images/building-home-lab-part-8/flare-36.png)

Give the PC a name. Click on Next and then select "Restart Now" for the changes to take effect. 

![flare-37|480](images/building-home-lab-part-8/flare-37.png)

#### Creating VM Snapshot 2

Shutdown the VM. Go to the Snapshot page using the Hamburger menu. Click on Take to create a new Snapshot.

![flare-33|540](images/building-home-lab-part-8/flare-33.png)

Give the Snapshot a descriptive name and click on Ok.

![flare-34|400](images/building-home-lab-part-8/flare-34.png)

Use the Hamburger menu and return to the Details page. Click on Start to boot the VM.

### Flare VM Installation

Right-click on the Start menu and select "Windows PowerShell (Admin)".

![flare-23|240](images/building-home-lab-part-8/flare-23.png)

Enter the following commands to download and execute the Flare VM script.

```powershell
# Download the FlareVM script
Invoke-WebRequest "https://raw.githubusercontent.com/mandiant/flare-vm/main/install.ps1" -OutFile $HOME/Downloads/install.ps1
# Go to Downloads Folder
cd $HOME/Downloads
# Unlock the downlaoded script
Unblock-File .\install.ps1
# Disable PowerShell script execution policy 
Set-ExecutionPolicy Unrestricted -Force
# Run the script
.\install.ps1
```

![flare-38|600](images/building-home-lab-part-8/flare-38.png)

The script makes some checks before starting the install. Enter `Y` when asked about Snapshot. Enter your password when prompted.

![flare-39|500](images/building-home-lab-part-8/flare-39.png)

After sometime the Flare VM configuration menu will open.

![flare-40|600](images/building-home-lab-part-8/flare-40.png)

In the Package Installation Customization section from the left side select "debloat.vm" and click on right arrow to select it for installation.

![flare-41|460](images/building-home-lab-part-8/flare-41.png)

Click on Ok to start the installer. The installer will being the download and install process. The VM will restart multiple times during the setup this is normal.

![flare-42|580](images/building-home-lab-part-8/flare-42.png)

The installer can take a very long time so be patient. Once the setup is complete we will get the following prompt click on Finish to complete the setup.

![flare-43|440](images/building-home-lab-part-8/flare-43.png)

After the install is complete. Restart the VM so that changes that where made by the script can be saved.

![flare-44|600](images/building-home-lab-part-8/flare-44.png)

### Post-Install Configuration

#### Moving VM to Isolated Network

Shutdown the VM. Now we can move the VM to the ISOLATED subnet.

Open the VM settings page and go to the Network section. For the Attached to option select Internal Network. For name select LAN 3. Click on Ok to save the changes.

![flare-45|540](images/building-home-lab-part-8/flare-45.png)

#### Creating VM Snapshot 3

Using the Hamburger menu open the Snapshot page. Click on Take to create a Snapshot. Give the Snapshot a descriptive name and click on Ok.

![flare-46|400](images/building-home-lab-part-8/flare-46.png)

In the end will should have 3 Snapshots. 

![flare-47|540](images/building-home-lab-part-8/flare-47.png)

## REMnux VM Setup

### Download Image

Go to the following link to download the image:   
[Get the Virtual Appliance - REMnux Documentation](https://docs.remnux.org/install-distro/get-virtual-appliance)

Click on Box to open the download page.

![remnux-14|500](images/building-home-lab-part-8/remnux-14.png)

Click on the blue Download button. The image is ~5GB.

![remnux-15|520](images/building-home-lab-part-8/remnux-15.png)

Once the download is complete we will have an `.ova` file.

![remnux-16|540](images/building-home-lab-part-8/remnux-16.png)

### Creating the VM

Click on Tools from the sidebar and then select Import.

![remnux-1|540](images/building-home-lab-part-8/remnux-1.png)

Select the downloaded OVA file and click on Next.

![remnux-2|540](images/building-home-lab-part-8/remnux-2.png)

Change the VM as required. Ensure the VM has 4096MB of RAM. For the MAC Address Policy select " Generate new MAC addresses for all network adapters" then click on Finish.

![remnux-3|540](images/building-home-lab-part-8/remnux-3.png)

#### Adding VM to Group

Once the import is complete right-click on the VM and select "Move to Group" and then select "Home Lab/Malware Analysis".

![remnux-4|400](images/building-home-lab-part-8/remnux-4.png)

### Configuring the VM

Select the VM and from the toolbar select Settings. Go to `System -> Motherboard`. In Boot Order ensure that Hard Disk is on the top followed by Optical. Uncheck Floppy. Click on Ok to save the changes.

![remnux-5|540](images/building-home-lab-part-8/remnux-5.png)

### Post-Install Configuration

Select the VM and from the toolbar click on Start.

![remnux-6|540](images/building-home-lab-part-8/remnux-6.png)

#### Updating Guest Additions

The VM will already have Guest Additions installed but it will be a older version. Click on Devices and select "Upgrade Guest Additions" to start the update.

![remnux-7|400](images/building-home-lab-part-8/remnux-7.png)

#### Upgrading Packages

Once Guest Additions are updated open a Terminal and enter the following command to update the system packages.

```bash
remnux upgrade
```

![remnux-8|540](images/building-home-lab-part-8/remnux-8.png)

Once the update is complete Restart the VM for the changes to take effect.

![remnux-9|260](images/building-home-lab-part-8/remnux-9.png)

![remnux-10|380](images/building-home-lab-part-8/remnux-10.png)

#### Moving VM to Isolated Network

Shutdown the VM and open the Settings menu and select Network. For the Attached to option select Internal Network. For name select LAN 3. Click on Ok to save the changes. This will move the VM to the ISOLATED interface that does not have internet access.

![remnux-11|540](images/building-home-lab-part-8/remnux-11.png)

#### Creating VM Snapshot

Click on the Hamburger menu and select Snapshot.

![remnux-17|400](images/building-home-lab-part-8/remnux-17.png)

Click on Take to create a Snapshot.

![remnux-18|540](images/building-home-lab-part-8/remnux-18.png)

Give the Snapshot a descriptive name and click on Ok.

![remnux-12|420](images/building-home-lab-part-8/remnux-12.png)

Use the Hamburger menu to go back to the Details page.

![remnux-13|540](images/building-home-lab-part-8/remnux-13.png)