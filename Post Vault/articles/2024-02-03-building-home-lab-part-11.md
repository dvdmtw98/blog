---
categories:
  - Security
  - Home Lab
date: 2024-02-03 20:15:00 -0600
description: A step-by-step guide for building your very own Cybersecurity Home Lab using VirtualBox
img_path: /assets/
published: false
tags:
  - security
  - home-lab
  - virtualbox
  - networking
  - malware
title: "Building a Virtual Security Home Lab: Part 11 - Transferring Files to Malware Analysis Lab"
---

![building-home-lab-part-11-banner|640](images/building-home-lab-part-11/building-home-lab-part-11-banner.png)

Banner Background by [logturnal](https://www.freepik.com/free-vector/gradient-white-color-background-abstract-modern_34010189.htm) on Freepik  
Hacker Image by [catalyststuff](https://www.freepik.com/free-vector/hacker-operating-laptop-cartoon-icon-illustration-technology-icon-concept-isolated-flat-cartoon-style_11602236.htm) on Freepik

In module module, we will see how we can transfer files using SCP from "Tsurugi Linux" which is on the SECURITY subnet to VMs on the ISOLATED subnet. 

I recommend this approach to get Malware Samples into the Malware Analysis Lab. We can use other methods for transferring files to these VMs but since we are dealing with Malware Samples I want to keep the samples far from the Internet and the host machines filesystem.

## Tsurugi Linux Static IP Assignment

Start the pfSense VM if it was Shutdown. Once pfSense is up and running. Start the Tsurugi Linux VM. One the terminal and run the following command:

```bash
ip a
```

![malware-1|600](images/building-home-lab-part-11/malware-1.png)

Tsurugi Linux has been assigned the IP Address 10.10.10.12 by the DHCP server.

Start the Kali Linux VM and login into the pfSense Web UI.

![pfsense-27|600](images/building-home-lab-part-4/pfsense-27.png)

From the navigation bar select **`Status -> DHCP Leases`**.

![pfsense-53|600](images/building-home-lab-part-4/pfsense-53.png)

In the Leases section find Tsurugi Linux. Click on the hollow "+" icon (Add Static IP) on the right hand side.

![malware-2|580](images/building-home-lab-part-11/malware-2.png)

In the IP Address field enter 10.10.10.2. Scroll to the bottom and click on Save.

![malware-3|580](images/building-home-lab-part-11/malware-3.png)

A popup will appear at the top. Click on Apply Changes.

![malware-4|580](images/building-home-lab-part-11/malware-4.png)

### Refreshing Tsurugi Linux IP Address

On Tsurugi Linux from the terminal run the following command:

```bash
# Disable and then Enable the Network Adapter
sudo ip l set enp0s3 && sudo ip l set enp0s3 up
```

Restarting the adapter will cause the dynamic IP that was assigned to the VM to be release. Run the following command to confirm the VM is using the configured static IP.

```bash
ip a enp0s3
```

![malware-5|600](images/building-home-lab-part-11/malware-5.png)

Refresh the DHCP Leases page and we should see that Tsurugi Linux is now using the IP address that we configured. 

![malware-6|580](images/building-home-lab-part-11/malware-6.png)

## pfSense Firewall Configuration

From the navigation bar select **`Firewall -> Rules`**.

![pfsense-58|600](images/building-home-lab-part-4/pfsense-58.png)

Go to the **`ISOLATED`** subnet tab. Click on the "<u>Add rule to the top of the list</u>" button.

![malware-9|580](images/building-home-lab-part-11/malware-9.png)

Enter the details as shown below:  
Source: **`ISOLATED subnets`**  
Destination: **`Address or Alias - 10.10.10.2`**  
Destination Port Range: **`SSH (22)`**  
Description: **`Allows SSH access to DFIR VM`**

![malware-7|580](images/building-home-lab-part-11/malware-7.png)

A popup will appear at the top of the page. Click on **`Apply Changes`**.

![pfsense-98|560](images/building-home-lab-part-8/pfsense-98.png)

The final firewall rules will look as follows:

![malware-8|580](images/building-home-lab-part-11/malware-8.png)

## Enabling SSH

### Tsurugi Linux

Enter the following command to check if SSH is running.

```bash
systemctl status ssh
```

If SSH is disabled running the following command to enable it.

```bash
sudo systemctl start ssh
```

![malware-10|560](images/building-home-lab-part-11/malware-10.png)

### Flare VM (Windows)

Right-click on the Start menu icon. Select **`Windows PowerShell (Admin)`**.

![flare-23|240](images/building-home-lab-part-8/flare-23.png)

Enter the following command to check if SSH server is running.

```powershell
Get-Service sshd
```

Run the following to enable SSH server.

```powershell
Start-Service sshd
```

[How to SSH into a Windows 10 Machine from anywhere - Scott Hanselman's Blog](https://www.hanselman.com/blog/how-to-ssh-into-a-windows-10-machine-from-linux-or-windows-or-anywhere)

![malware-11|400](images/building-home-lab-part-11/malware-11.png)

### REMnux Linux

Running the following commands to check the status of SSH and enable it.

```bash
# Check Status
systemctl status ssh

# Enable SSH
sudo systemctl start ssh
```

![malware-12|560](images/building-home-lab-part-11/malware-12.png)

## Testing SSH Connectivity

### Finding Target VM IP Address

To connect to Flare VM and REMnux we need their IP address.

```powershell
ipconfig
```

![malware-13|440](images/building-home-lab-part-11/malware-13.png)

```bash
ip a
```

![malware-14|580](images/building-home-lab-part-11/malware-14.png)

### Connecting to Flare VM

In my case the IP address of Flare VM is **`10.99.99.11`**.

Use the following command to remote into Flare VM from Tsurugi Linux.

```bash
# ssh target-system-username@target-system-ip-address
ssh david@10.99.99.11
```

Type **`yes`** to add the fingerprint.  
Enter the password of the target system when prompted.

![malware-15|580](images/building-home-lab-part-11/malware-15.png)

This will log you into Flare VM.

![malware-16|320](images/building-home-lab-part-11/malware-16.png)

Type **`exit`** to quit the remote connection.

### Connecting to REMnux Linux

In my case the IP address for REMnux is **`10.99.99.12`**.

Use the following command to remote into REMnux from Tsurugi Linux.

```bash
# ssh target-system-username@target-system-ip-address
ssh remnux@10.99.99.12
```

Type **`yes`** to add the fingerprint.  
Enter the password of the target system when prompted.

![malware-17|580](images/building-home-lab-part-11/malware-17.png)

Type **`exit`** to quit the remote connection.

## SCP File Transfer

Now we know that we can connect to the Malware Analysis Lab VMs from Tsurugi Linux. 

To demonstrate how to transfer files from Tsurugi Linux to the Malware Analysis Lab VMs I will use an dummy text file. To follow along run the following commands on Tsurugi Linux:

```bash
cd Downloads
echo "Hello Hello World" > hello.txt
cat hello.txt
```

### File Transfer to Flare VM

To transfer **`hello.txt`** to the target systems we will use SCP which is can command line utility that uses SSH to securely copy files over the network.

Run the following command to copy the file to Flare VM.

```bash
# scp file-to-copy target-ysername@target-ip-address:destination-path
scp hello.txt david@10.99.99.11:/C:/Users/David/Downloads
```

![malware-18|580](images/building-home-lab-part-11/malware-18.png)

The above command will copy the file into the Downloads folder on Flare VM.

![malware-19|520](images/building-home-lab-part-11/malware-19.png)

### File Transfer to REMnux Linux

Using the same command we can move the file onto REMnux as well.

```bash
# scp file-to-copy target-ysername@target-ip-address:destination-path
scp hello.txt remnux@10.99.99.12:~/Downloads
```

![malware-20|580](images/building-home-lab-part-11/malware-20.png)

The above command will copy the file into the Downloads folder on REMnux.

![malware-21|340](images/building-home-lab-part-11/malware-21.png)

> [!INFO]
> To copy a whole folder use the **`-r`** (recursive) flag with the SCP command  
> [SCP Linux - Securely Copy Files Using SCP examples](https://linuxblog.io/linux-securely-copy-files-using-scp/)

## Disabling SSH

Once you copy the required files onto the Malware Analysis lab use the following commands to disable SSH on all the systems.

### Tsurugi Linux

```bash
sudo systemctl stop ssh
```

![malware-22|580](images/building-home-lab-part-11/malware-22.png)

### Flare VM (Windows)

```powershell
Stop-Service sshd
```

![malware-23|340](images/building-home-lab-part-11/malware-23.png)

### REMnux Linux

```bash
sudo systemctl stop ssh
```

![malware-24|580](images/building-home-lab-part-11/malware-24.png)
