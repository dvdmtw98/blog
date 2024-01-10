---
categories:
  - Security
  - Home Lab
date: 2024-01-30 20:00:00 -0600
description: A step-by-step guide for building your very own Cybersecurity Home Lab using VirtualBox
img_path: /assets/
published: false
tags:
  - security
  - home-lab
  - virtualbox
  - networking
  - splunk
title: "Building a Virtual Security Home Lab: Part 10 - Splunk Setup & Configuration"
---

![banner-image|640](images/building-home-lab-part-10/building-home-lab-part-10-banner.png)

Banner Background by [logturnal](https://www.freepik.com/free-vector/gradient-white-color-background-abstract-modern_34010189.htm) on Freepik  
Hacker Image by [catalyststuff](https://www.freepik.com/free-vector/hacker-operating-laptop-cartoon-icon-illustration-technology-icon-concept-isolated-flat-cartoon-style_11602236.htm) on Freepik

In this module we will setup Splunk (SIEM) in a Ubuntu VM. The VM will be added to the SECURITY subnet. Then we will configure a Universal Forwarder on the Windows Server 2019 VM which will forward logs and events from the DC to Splunk.

## Ubuntu Setup

### Downloading the Image

Go to the following URL: [Download Ubuntu Desktop | Download | Ubuntu](https://ubuntu.com/download/desktop).  
Download the latest LTS version of Ubuntu. As of writing the latest version is `2022.04.3`

The ISO is ~5GB.

![ubuntu-1|600](images/building-home-lab-part-10/ubuntu-1.png)

After the download is complete we will have a `.iso` file.

![ubuntu-2|560](images/building-home-lab-part-10/ubuntu-2.png)

### Creating the VM

Click on Tools and then from the toolbar select New.

![ubuntu-3|540](images/building-home-lab-part-10/ubuntu-3.png)

Give the VM a name. And select the downloaded ISO image. Select the "Skip Unattended Installation" option and click on Next.

![ubuntu-4|540](images/building-home-lab-part-10/ubuntu-4.png)

Increase the Base Memory to 4096MB (4GB) and click on Next.

![ubuntu-5|540](images/building-home-lab-part-10/ubuntu-5.png)

Increase the Hard Disk size to 100GB. Ensure that Pre-allocate Full Size is not selected and click on Next.

![ubuntu-6|540](images/building-home-lab-part-10/ubuntu-6.png)

Confirm that all the settings are correct and click on Finish.

![ubuntu-7|540](images/building-home-lab-part-10/ubuntu-7.png)

#### Adding VM to Group

Right-click the VM and select "Move to Group" then choose `Home Lab/Security`.

![ubuntu-8|400](images/building-home-lab-part-10/ubuntu-8.png)

The final result should be as follows:

![ubuntu-9|300](images/building-home-lab-part-10/ubuntu-9.png)

### Configuring the VM

Select the VM and click on Settings in the toolbar.

![ubuntu-10|540](images/building-home-lab-part-10/ubuntu-10.png)

Go to `System -> Motherboard`. In Boot Order ensure that Hard Disk is on the top followed by Optical. Uncheck Floppy.

![ubuntu-11|540](images/building-home-lab-part-10/ubuntu-11.png)

Go to `Network -> Adapter 1`. For Attached to field select Internal Network. For name select LAN 4. Click on Ok to save changes.

![ubuntu-12|540](images/building-home-lab-part-10/ubuntu-12.png)

### Installing Ubuntu

Select the VM and click on Start.

![ubuntu-13|540](images/building-home-lab-part-10/ubuntu-13.png)

Press Enter to start the Graphical Installer.

![ubuntu-14|540](images/building-home-lab-part-10/ubuntu-14.png)

Select language and click on "Install Ubuntu".

![ubuntu-15|540](images/building-home-lab-part-10/ubuntu-15.png)

Select Keyboard Layout and click on Continue.

![ubuntu-16|540](images/building-home-lab-part-10/ubuntu-16.png)

Enable "Install third-party software for graphics and Wi-Fi hardware and additional media formats" and click on Continue.

![ubuntu-17|540](images/building-home-lab-part-10/ubuntu-17.png)

Click on Install Now.

![ubuntu-18|540](images/building-home-lab-part-10/ubuntu-18.png)

Click on Continue.

![ubuntu-19|540](images/building-home-lab-part-10/ubuntu-19.png)

Select your location/timezone  and click on Continue.

![ubuntu-20|540](images/building-home-lab-part-10/ubuntu-20.png)

Enter your name, password and name for the VM and click on Continue.

![ubuntu-21|540](images/building-home-lab-part-10/ubuntu-21.png)

Wait for the installer to finish.

![ubuntu-22|540](images/building-home-lab-part-10/ubuntu-22.png)

Click on Restart Now to boot into the system.

![ubuntu-23|400](images/building-home-lab-part-10/ubuntu-23.png)

VirtualBox will automatically remove the image press Enter to resume the boot.

![ubuntu-24|540](images/building-home-lab-part-10/ubuntu-24.png)

Login using your password.

![ubuntu-25|540](images/building-home-lab-part-10/ubuntu-25.png)

Complete the post-install setup as shown. Click on Skip.

![ubuntu-26|540](images/building-home-lab-part-10/ubuntu-26.png)

Click on Next.

![ubuntu-27|540](images/building-home-lab-part-10/ubuntu-27.png)

Select "No, don't send system info" and click on Next.

![ubuntu-28|540](images/building-home-lab-part-10/ubuntu-28.png)

Ensure this setting in disabled and click on Next.

![ubuntu-29|540](images/building-home-lab-part-10/ubuntu-29.png)

Click on Done to close the wizard.

![ubuntu-30|540](images/building-home-lab-part-10/ubuntu-30.png)

### Post-Install Configuration

#### Install Guest Additions

From the VM toolbar click on Devices and select "Install Guest Additions CD image".

![ubuntu-31|400](images/building-home-lab-part-10/ubuntu-31.png)

The disk should show up in the dock. Click on it to view the content of the disk.

![ubuntu-32|540](images/building-home-lab-part-10/ubuntu-32.png)

Right-click anywhere in the empty area in the File Explorer and select "Open in Terminal".

![ubuntu-34|540](images/building-home-lab-part-10/ubuntu-34.png)

Run the following command to install Guest Additions:

```bash
sudo ./VBoxLinuxAdditions.run
```

![ubuntu-35|500](images/building-home-lab-part-10/ubuntu-35.png)

Once the install is complete close the terminal, right-click on the disk icon in the dock and select Eject.

![ubuntu-36|260](images/building-home-lab-part-10/ubuntu-36.png)

#### Installing Updates

Press `Ctrl+Alt+T` to open a new terminal then enter the following command to update the installed packages:

```bash
sudo apt update && sudo apt dist-upgrade
```

Provide password when prompted. If there are updates press Enter to start the install.

![ubuntu-37|600](images/building-home-lab-part-10/ubuntu-37.png)

#### Creating VM Snapshot

Shutdown the VM. Click on the Hamburger menu beside the VM name and select Snapshots.

![ubuntu-38|540](images/building-home-lab-part-10/ubuntu-38.png)

Click on Take to create Snapshot.

![ubuntu-39|540](images/building-home-lab-part-10/ubuntu-39.png)

Provide a descriptive name and click on Ok.

![remnux-12|400](images/building-home-lab-part-8/remnux-12.png)

Click on the Hamburger menu and click on Details to return to the main page.

![ubuntu-40|540](images/building-home-lab-part-10/ubuntu-40.png)

## Splunk Installation

We will install Splunk on the Ubuntu VM that we just configured. Start the VM and then follow the steps outlined below.

### Splunk Download

Go to the following URL to download Splunk: [Splunk Enterprise Free Trial \| Splunk](https://www.splunk.com/en_us/download/splunk-enterprise.html)  
As of writing the latest version of Splunk Enterprise is `9.1.2`.

To download Splunk we have to create a account. Fill in the details in the form, accept the agreement and click on "Create the Account".

![splunk-1|580](images/building-home-lab-part-10/splunk-1.png)

After login select the Linux tab and click on the "Download Now" button for the `.deb` file.

![splunk-2|580](images/building-home-lab-part-10/splunk-2.png)

Scroll down and accept the agreement and then click on "Access to program" to start the download.

![splunk-3|580](images/building-home-lab-part-10/splunk-3.png)

Alternatively use the following link should directly start the download:  
[Splunk Enterprise 9.1.2 - Linux (.deb) - Direct Download Link](https://download.splunk.com/products/splunk/releases/9.1.2/linux/splunk-9.1.2-b6b9c8185839-linux-2.6-amd64.deb)

### Splunk Installation

Once the download is complete we will have a `.deb` file. Open the Terminal (`Ctrl+Alt+t`) and navigate to the Downloads folder.

```bash
cd Downloads
```

![splunk-5|580](images/building-home-lab-part-10/splunk-5.png)

Run the following to install curl:

```bash
sudo apt install curl
```

Enter password when prompted.

![splunk-6|580](images/building-home-lab-part-10/splunk-6.png)

Run the following command to install Splunk:

```bash
sudo dpkg -i splunk-9.1.2-b6b9c8185839-linux-2.6-amd64.deb
```

![splunk-7|580](images/building-home-lab-part-10/splunk-7.png)

After the install run the following command to launch Splunk:

```bash
sudo /opt/splunk/bin/splunk start --accept-license --answer-yes
```

Provide a name and password when prompted. These credentials are used to log into Splunk. 

![splunk-8|580](images/building-home-lab-part-10/splunk-8.png)

Once the setup is complete we see the Splunk is running on `http://127.0.0.1:8000`

![splunk-9|580](images/building-home-lab-part-10/splunk-9.png)

Run the following to ensure that Splunk starts automatically when the system is booted.

```bash
sudo /opt/splunk/bin/splunk enable boot-start
```

![splunk-10|460](images/building-home-lab-part-10/splunk-10.png)

### Creating VM Snapshot

Shutdown the VM. Using the Hamburger menu access the Snapshot page and create a Snapshot. Give the Snapshot a descriptive name.

![splunk-11|500](images/building-home-lab-part-10/splunk-11.png)

![splunk-12|540](images/building-home-lab-part-10/splunk-12.png)

### Splunk Configuration

Before we can install Universal Forwarder there are a few settings to change in Splunk. Open Splunk by going to `http://127.0.0.1:8000`.

![splunk-13|540](images/building-home-lab-part-10/splunk-13.png)

From the toolbar select Settings and then click on "Forwarding and receiving".

![splunk-14|500](images/building-home-lab-part-10/splunk-14.png)

Click on "Add new" in the Receive data section.

![splunk-15|580](images/building-home-lab-part-10/splunk-15.png)

Enter `9997` as the port to listen for incoming data. Click on Save.

![splunk-16|580](images/building-home-lab-part-10/splunk-16.png)

![splunk-17|580](images/building-home-lab-part-10/splunk-17.png)

## Universal Forwarder Installation

The next steps need to be performed on the Domain Controller VM (Windows Server 2019). We are going to ingest the log data that is generated by this device in Splunk.

### Universal Forwarder Download

Go to the following link to download Universal Forwarder: [Download Universal Forwarder for Remote Data Collection \| Splunk](https://www.splunk.com/en_us/download/universal-forwarder.html)

You will need to login to start the download the setup. Select the Windows tab and then click on Download Now beside the 64-bit option.

![splunk-4|580](images/building-home-lab-part-10/splunk-4.png)

Alternatively, Universal Forwarder can be downloaded directly from the below link:  
[Splunk Universal Forwarder 9.1.2 - Windows (.msi) - Direct Download Link](https://download.splunk.com/products/universalforwarder/releases/9.1.2/windows/splunkforwarder-9.1.2-b6b9c8185839-x64-release.msi)

### Universal Forwarder Install

Double-click on the `.msi` file to begin installation.

![splunk-18|560](images/building-home-lab-part-10/splunk-18.png)

Check the box on the top to accept the agreement and then click on Next.

![splunk-19|460](images/building-home-lab-part-10/splunk-19.png)

Provide a username and password for the Forwarder. I would recommend using the same credentials as the account that was configured on Splunk.

![splunk-20|460](images/building-home-lab-part-10/splunk-20.png)

For the new step we require the IP address of Ubuntu (Splunk) VM.

```bash
ip a
```

Using the IP address shown under enp0s3.

![splunk-21|560](images/building-home-lab-part-10/splunk-21.png)

Enter the IP address of the Splunk VM (in my case `10.10.10.13`) and enter port as 8089 then click on Next.

![splunk-22|460](images/building-home-lab-part-10/splunk-22.png)

Enter the Splunk VM IP address and enter port as 9997. This is the port we configured in Splunk. Click on Next to continue.

![splunk-23|460](images/building-home-lab-part-10/splunk-23.png)

Click on Install.

![splunk-24|460](images/building-home-lab-part-10/splunk-24.png)

Click on Finish to close the installer.

![splunk-25|460](images/building-home-lab-part-10/splunk-25.png)

## Data Ingestion Configuration

Now that we have Splunk and Universal Forwarder configured we need to link both the pieces together so that Splunk can collect data.

### Adding Data Source

In Splunk select "Settings" from the toolbar and select "Add Data".

![splunk-26|500](images/building-home-lab-part-10/splunk-26.png)

Click on "Forward".

![splunk-27|560](images/building-home-lab-part-10/splunk-27.png)

Our DC should automatically show up in the left box. Click on it to add it to the right box. In the "New Source Class Name" field provide a name for the source. Click on Next to continue.

![splunk-28|560](images/building-home-lab-part-10/splunk-28.png)

Select "Local Event Logs". Click on the "add all" button above the left box to ingest all the logs generated by the DC. Click on Next once done.

![splunk-29|560](images/building-home-lab-part-10/splunk-29.png)

Click on "Create a new index". Index is the Splunk equivalent of Tables from SQL. It is used to store data of similar type.

![splunk-30|560](images/building-home-lab-part-10/splunk-30.png)

Provide the Index a name. Keep all the other fields on its default value and click on Save then click on Next.

![splunk-31|560](images/building-home-lab-part-10/splunk-31.png)

Confirm all the options look correct and click on Submit.

![splunk-32|560](images/building-home-lab-part-10/splunk-32.png)

### Querying Data

From the Splunk toolbar select Apps and click on "Search & Reporting".

![splunk-34|300](images/building-home-lab-part-10/splunk-34.png)

In the search box enter the following to few the ingested data:

```sql
index="windows"
```

![splunk-35|600](images/building-home-lab-part-10/splunk-35.png)