---
categories:
  - Security
  - Home Lab
date: 2024-01-20 18:00:00 -0600
description: A step-by-step guide for building your very own Cybersecurity Home Lab using VirtualBox
img_path: /assets/
published: true
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

In the previous module, we installed Windows Server 2019, installed AD Domain Services, configured DHCP and set up a DNS Forwarder. In this module, we will continue building out the AD Lab by completing the Domain Controller setup and adding devices to the AD environment.

## Windows Server 2019 Setup

### Domain Configuration

#### Certificate Service Installation

Select **`Manage`** from the top right corner of Server Manager and then select "<u>Add Roles and Features</u>".

![dc-28|360](images/building-home-lab-part-6/dc-28.png)

Click **`Next`** till you reach the <u>Server Roles</u> page. Enable "<u>Active Directory Certificate Services</u>".

![dc-107|580](images/building-home-lab-part-7/dc-107.png)

Click on **`Add Features`**.

![dc-108|580](images/building-home-lab-part-7/dc-108.png)

Click on **`Next`** to continue.

![dc-109|580](images/building-home-lab-part-7/dc-109.png)

Click **`Next`** till you reach the **`Role Services`** Page. Enable "<u>Certificate Authority</u>". Click on **`Next`** to continue.

![dc-110|580](images/building-home-lab-part-7/dc-110.png)

Click on **`Install`** to start the setup.

![dc-111|580](images/building-home-lab-part-7/dc-111.png)

After the installation is complete the server has to be restarted. Open the <u>Start Menu</u>, click on the <u>Power</u> icon and then select **`Restart`**.

![dc-119|240](images/building-home-lab-part-7/dc-119.png)

Click on **`Continue`** to restart the system.

![dc-120|300](images/building-home-lab-part-7/dc-120.png)

#### Certificate Service Configuration

After the restart once Server Manager loads. Click on the <u>Flag</u> icon on the top right side and select "<u>Configure Active Directory Certificate Services</u>"

![dc-112|400](images/building-home-lab-part-7/dc-112.png)

Click on **`Next`**.

![dc-113|580](images/building-home-lab-part-7/dc-113.png)

Enable "<u>Certification Authority</u>" and click on **`Next`**.

![dc-114|580](images/building-home-lab-part-7/dc-114.png)

Click on **`Next`**.

![dc-115|580](images/building-home-lab-part-7/dc-115.png)

Click on **`Next`**.

![dc-116|580](images/building-home-lab-part-7/dc-116.png)

Click on **`Next`** till you reach the <u>Confirmation</u> page. Click on **`Configure`** to save the changes.

![dc-117|580](images/building-home-lab-part-7/dc-117.png)

Click on **`Close`**.

![dc-118|580](images/building-home-lab-part-7/dc-118.png)

### User Configuration

#### AD Admin Setup

Open the <u>Start menu</u> click on "<u>Windows Administrative Tools</u>" and then select **`Active Directory Users and Computers`**.

![dc-64|400](images/building-home-lab-part-7/dc-64.png)

Right-click on the <u>domain name</u> (in my case **`ad.lab`**) in the sidebar. Then select **`New -> User`**.  

![dc-65|500](images/building-home-lab-part-7/dc-65.png)

Enter the <u>First Name</u>, <u>Last Name</u> and <u>User logon name</u> for the new user. This user will be the **`Administrator`** for the Domain Controller.

![dc-66|400](images/building-home-lab-part-7/dc-66.png)

Enter the <u>Password</u> for the user. Uncheck all options leaving "<u>Password never expires</u>". Click on **`Next`** to create the user.

![dc-67|400](images/building-home-lab-part-7/dc-67.png)

Expand the dropdown on the domain name from the sidebar. Click on **`Users`**. Then double-click on "<u>Domain Admins</u>".

![dc-68|500](images/building-home-lab-part-7/dc-68.png)

Go to **`Members -> Add`**.

![dc-69|400](images/building-home-lab-part-7/dc-69.png)

Enter the <u>name</u> of the user and check on **`Check Names`**.

![dc-70|400](images/building-home-lab-part-7/dc-70.png)

Click on **`OK`**.

![dc-71|400](images/building-home-lab-part-7/dc-71.png)

Click on **`Apply`** then **`OK`** to persist the changes.

![dc-72|400](images/building-home-lab-part-7/dc-72.png)

Open the <u>Start</u> menu and then click on the <u>user logo</u> and then select **`Sign out`**.

![dc-73|400](images/building-home-lab-part-7/dc-73.png)

From the login screen select "<u>Other user</u>". Then enter the <u>login name</u> and <u>password</u> that was configured for your domain administrator.

![dc-74|600](images/building-home-lab-part-7/dc-74.jpg)

#### AD User 1 Setup

Open the <u>Start menu</u>. Select "<u>Windows Administrative Tools</u>" and then choose **`Active Directory Users and Computers`**.

![dc-75|400](images/building-home-lab-part-7/dc-75.png)

Right-click on the <u>domain name</u> from the sidebar. Select **`New -> User`**.

![dc-76|500](images/building-home-lab-part-7/dc-76.png)

Enter the details for the user.

![dc-77|400](images/building-home-lab-part-7/dc-77.png)

Give the user a <u>password</u>. Check the "<u>User cannot change password</u>" and "<u>Password never expires</u>" options. Click **`Next`** to create a user.

![dc-78|400](images/building-home-lab-part-7/dc-78.png)

#### AD User 2 Setup

Follow the same steps as above to create a second AD User.

![dc-76|500](images/building-home-lab-part-7/dc-76.png)

![dc-79|400](images/building-home-lab-part-7/dc-79.png)

![dc-80|400](images/building-home-lab-part-7/dc-80.png)

## Making AD Lab Exploitable

To make the Active Directory Lab vulnerable we need to change some settings. We will use a PowerShell script and change so and Group Policies to achieve the desired result.

> [!INFO]
> You can skip this section and continue from the "<u>Windows 10 Enterprise VM1 Setup</u>" step if you do not plan to make your Active Directory Lab vulnerable to attacks

### Running Vulnerable AD Script

Right-click on the <u>Start menu</u> and select **`Windows PowerShell (Admin)`**.

![dc-91|300](images/building-home-lab-part-7/dc-91.png)

Run the following command:

```powershell
# Allow Execution of Scripts
Set-ExecutionPolicy -ExecutionPolicy Bypass -Force
```

![dc-121|500](images/building-home-lab-part-7/dc-121.png)

```powershell
# Download and Execute Script
[System.Net.WebClient]::new().DownloadString('https://raw.githubusercontent.com/WaterExecution/vulnerable-AD-plus/master/vulnadplus.ps1') -replace 'change\.me', 'ad.lab' | Invoke-Expression
```

> [!WARNING]
> Replace **`ad.lab`** with the name you have used for your Active Directory Domain before running the above command.  

The above command constants of the following steps:
**`[System.Net.WebClient]::new().DownloadString()`**: Downloads the Script  
**`-replace`**: Change string present in the script  
**`Invoke-Expression`**: Execute the Script

![dc-122|600](images/building-home-lab-part-7/dc-122.png)

Once the script reaches the end. It will wait for 30 seconds and then restart the system.

![dc-123|600](images/building-home-lab-part-7/dc-123.png)

### Group Policy Configuration

After the system restarts open the <u>Start menu</u> and click on "<u>Windows Administrative Tools</u>" then choose **`Group Policy Management`**.

![dc-81|400](images/building-home-lab-part-7/dc-81.png)

Expand "<u>Forest</u>" and then expand "<u>Domains</u>".

![dc-102|400](images/building-home-lab-part-7/dc-102.png)

#### Disable Windows Defender and Firewall

Right-click on the <u>domain name</u>. Select "<u>Create a GPO in the domain and link here</u>".

![dc-82|500](images/building-home-lab-part-7/dc-82.png)

Give the GPO the <u>name</u> **`Disable Protections`**.

![dc-83|400](images/building-home-lab-part-7/dc-83.png)

Expand the d<u>omain name</u>. Right-click on "<u>Disable Protections</u>" and choose **`Edit`**.

![dc-84|600](images/building-home-lab-part-7/dc-84.png)

This will open the <u>Group Policy Management Editor</u>. From the sidebar go to the following folder: **`Computer Configuration -> Policies -> Administrative Templates -> Windows Components -> Windows Defender Antivirus`**.

![dc-85|600](images/building-home-lab-part-7/dc-85.png)

Select "<u>Windows Defender Antivirus</u>". From the right side select "<u>Turn off Windows Defender Antivirus</u>" and click on **`Edit policy setting`**.

![dc-86|600](images/building-home-lab-part-7/dc-86.png)

Set it to **`Enabled`**. Click on **`Apply`** then **`OK`** to save the changes.

![dc-87|600](images/building-home-lab-part-7/dc-87.png)

Double-click on **`Real-time Protection`**.

![dc-104|600](images/building-home-lab-part-7/dc-104.png)

Select "<u>Turn off real-time protection</u>" and then click on "<u>Edit policy settings</u>"

![dc-105|600](images/building-home-lab-part-7/dc-105.png)

Set it to **`Enabled`**. Click on **`Apply`** then **`OK`** to save the changes.

![dc-106|500](images/building-home-lab-part-7/dc-106.png)

Expand the sidebar folders to the following: **`Computer Configuration -> Policies -> Administrative Templates -> Network -> Network Connections -> Windows Defender Firewall -> Domain Profile`**. 

Select "<u>Windows Defender Firewall: Protect all network connections</u>". Click on "Edit policy settings".

![dc-88|600](images/building-home-lab-part-7/dc-88.png)

Set it to **`Disabled`**. Click on **`Apply`** then **`OK`** to save the changes. 

![dc-89|600](images/building-home-lab-part-7/dc-89.png)

Close Group Policy Management Editor. From the sidebar of Group Policy Management right-click on "<u>Disable Protections</u>" and choose "<u>Enforced</u>". 

![dc-90|600](images/building-home-lab-part-7/dc-90.png)

#### Enable Remote Login for Local Admins

Right-click on the <u>domain</u> name. Select "<u>Create a GPO in the domain and link here</u>".

![dc-124|360](images/building-home-lab-part-7/dc-124.png)

Give the GPO the name **`Local Admin Remote Login`**.

![dc-125|400](images/building-home-lab-part-7/dc-125.png)

Right-click on "<u>Local Admin Remote Login</u>" and choose **`Edit`**.

![dc-126|340](images/building-home-lab-part-7/dc-126.png)

Using the sidebar descend into **`Computer Configuration -> Preferences -> Windows Settings -> Registry`**. Then, right-click **`Registry`** and choose **`New -> Registry Item`**.

![dc-127|400](images/building-home-lab-part-7/dc-127.png)

For the Hive field select **`HKEY_LOCAL_MACHINE`**. To fill the value in the "<u>Key Path</u>" field click on the **`...`** button.

![dc-128|400](images/building-home-lab-part-7/dc-128.png)

In the window that opens up navigate to the following directory: **`SOFTWARE\Microsoft\Windows\CurrentVersion\Policies\System`**

![dc-129|420](images/building-home-lab-part-7/dc-129.png)

Enter the following for the remaining fields:  
Value name: **`LocalAccountTokenFilterPolicy`**  
Value type: **`REG_DWORD`**  
Value data: **`1`**

Click on **`Apply`** then **`OK`**. Close Group Policy Management Editor.

![dc-130|400](images/building-home-lab-part-7/dc-130.png)

#### Enable WinRM Server

Right-click on the <u>domain</u> name. Select "<u>Create a GPO in the domain and link here</u>".

![dc-124|360](images/building-home-lab-part-7/dc-124.png)

Give the GPO the name **`Enable WinRM Server`**.

![dc-131|400](images/building-home-lab-part-7/dc-131.png)

Right-click on "<u>Enable WinRM Server</u>" and choose **`Edit`**.

![dc-132|340](images/building-home-lab-part-7/dc-132.png)

Using the sidebar go to the following folder: **`Computer Configuration -> Policies -> Administrative Templates -> Windows Components -> Windows Remote Management (WinRM) -> WinRM Service`**.

![dc-133|600](images/building-home-lab-part-7/dc-133.png)

Select "<u>Allow remote server management through WinRM</u>" and then click on "<u>Edit policy settings</u>".

![dc-134|560](images/building-home-lab-part-7/dc-134.png)

Set the policy to **`Enabled`**. In the <u>IPv4 filter</u> field enter **`*`**. Click on **`Apply`** then **`OK`**.

![dc-135|500](images/building-home-lab-part-7/dc-135.png)

Select "<u>Allow Basic authentication</u>" and click on "<u>Edit policy settings</u>".

![dc-136|560](images/building-home-lab-part-7/dc-136.png)

Set the policy to **`Enabled`**. Click on **`Apply`** and then **`OK`**.

![dc-137|500](images/building-home-lab-part-7/dc-137.png)

Select "<u>Allow unencrypted traffic</u>" and click on "<u>Edit policy settings</u>".

![dc-138|560](images/building-home-lab-part-7/dc-138.png)

Set the policy to **`Enabled`**. Click on **`Apply`** then **`OK`**.

![dc-139|500](images/building-home-lab-part-7/dc-139.png)

In the sidebar navigate to: **`Computer Configuration -> Preferences -> Control Panel Settings`**. Right-click on <u>Services</u> and select **`New -> Service`**.

![dc-140|560](images/building-home-lab-part-7/dc-140.png)

Select <u>Startup</u> to **`Automatic`**. Use the **`...`** button to select the <u>Server name</u>.

![dc-141|400](images/building-home-lab-part-7/dc-141.png)

Select "<u>Windows Remote Management (WS-Management)</u>" and click on **`Select`**.

![dc-142|420](images/building-home-lab-part-7/dc-142.png)

For <u>Service action</u> select **`Start service`**. Click on **`Apply`** then **`OK`**.

![dc-143|400](images/building-home-lab-part-7/dc-143.png)

Using the sidebar navigate to the following location: **`Computer Configuration -> Policies -> Administrative Templates -> Windows Components -> Windows Remote Shell`**

Select "<u>Allow Remote Shell Access</u>" and click on "<u>Edit policy setting</u>".

![dc-144|600](images/building-home-lab-part-7/dc-144.png)

Set the policy to **`Enabled`**. Click on **`Apply`** then **`OK`**. Close the Group Policy Management Editor.

![dc-145|500](images/building-home-lab-part-7/dc-145.png)

#### Enable RDP (Remote Desktop Protocol)

Right-click on the <u>domain</u> name. Select "<u>Create a GPO in the domain and link here</u>".

![dc-124|360](images/building-home-lab-part-7/dc-124.png)

Give the GPO the name **`Enable RDP`**.

![dc-146|400](images/building-home-lab-part-7/dc-146.png)

Right-click on "<u>Enable RDP</u>" and select **`Edit`**.

![dc-147|340](images/building-home-lab-part-7/dc-147.png)

Using the sidebar navigate to the following folder: **`Computer Configuration -> Policies -> Administrative Templates -> Windows Components -> Remote Desktop Services -> Remote Desktop Session Host -> Connections`**.

Select "<u>Allow users to connect remotely using Remote Desktop Services</u>" and click on "<u>Edit policy settings</u>".

![dc-148|600](images/building-home-lab-part-7/dc-148.png)

Set the policy to **`Enabled`**. Click on **`Apply`** then **`OK`**. Close Group Policy Management Editor.

![dc-149|500](images/building-home-lab-part-7/dc-149.png)

#### Enable RPC (Remote Procedure Call)

Right-click on the <u>domain</u> name. Select "<u>Create a GPO in the domain and link here</u>".

![dc-124|360](images/building-home-lab-part-7/dc-124.png)

Give the GPO the name **`Enable RPC`**.

![dc-150|400](images/building-home-lab-part-7/dc-150.png)

Right-click on "<u>Enable RPC</u>" and select **`Edit`**.

![dc-151|340](images/building-home-lab-part-7/dc-151.png)

Using the sidebar navigate to the following folder: **`Computer Configuration -> Administrative Templates -> System -> Remote Procedure Call`**.

Select "<u>Enable RPC Endpoint Mapper Client Authentication</u>" and click on "<u>Edit policy settings</u>".

![dc-152|600](images/building-home-lab-part-7/dc-152.png)

Set the policy to **`Enabled`**. Click on **`Apply`** then **`OK`**. Close Group Policy Management Editor.

![dc-153|500](images/building-home-lab-part-7/dc-153.png)

#### Enforce the Domain Policies

Right-click on the <u>Start menu</u> and select **`Windows PowerShell (Admin)`**.

![dc-91|300](images/building-home-lab-part-7/dc-91.png)

In the terminal enter the following:

```powershell
gpupdate /force
```

![dc-92|440](images/building-home-lab-part-7/dc-92.png)

Now whenever a new device joins our AD environment the Group Policies that apply to all the devices will automatically be applied to them. With this, we have completed the Domain Controller setup.

> [!INFO]
> For the rest of the module the DC VM should be left powered on. To use the AD lab DC should be the first VM that is launched.

## Windows 10 Enterprise VM1 Setup

Select Windows 10 Enterprise VM1 from the sidebar then click on **`Start`**.

![user-45|540](images/building-home-lab-part-7/user-45.png)

### OS Installation

Click on **`Next`**.

![user-1|540](images/building-home-lab-part-7/user-1.png)

Click on **`Install now`**.

![user-2|540](images/building-home-lab-part-7/user-2.png)

<u>Accept</u> the agreement and then click on **`Next`**.

![user-3|540](images/building-home-lab-part-7/user-3.png)

Select "<u>Custom: Install Windows only (advanced)</u>".

![user-4|540](images/building-home-lab-part-7/user-4.png)

Select **`Disk 0`** and then click on **`Next`**.

![user-5|540](images/building-home-lab-part-7/user-5.png)

The VM will reboot multiple times during the installation.

![user-6|540](images/building-home-lab-part-7/user-6.png)

Select your **`Region`** and **`Keyboard Layout`**.

![user-7|540](images/building-home-lab-part-7/user-7.png)

![user-8|540](images/building-home-lab-part-7/user-8.png)

Click on **`Skip`**.

![user-9|540](images/building-home-lab-part-7/user-9.png)

Select "<u>Domain join instead</u>". This will allow us to configure a local account.

![user-10|540](images/building-home-lab-part-7/user-10.png)

Enter a <u>username</u> and click on **`Next`**. 

![user-11|540](images/building-home-lab-part-7/user-11.png)

> [!INFO]
> You can provide any username in this step but to avoid confusion I would recommend using the <u>First Name</u> of one of the non-admin users that was created in AD. In my case the two AD users are John Doe and Jane Doe. For this VM I have choose John, when i configure the 2nd VM I will use Jane.

Enter a <u>password</u> and click on **`Next`**.

This password can be different from the password that was configured in Active Directory.

![user-12|540](images/building-home-lab-part-7/user-12.png)

Configure the "<u>Security Questions</u>" for the user. Remember to note down these details in a secure location.

![user-13|540](images/building-home-lab-part-7/user-13.png)

Disable all the features that are shown. Then click on **`Accept`**.

![user-14|540](images/building-home-lab-part-7/user-14.png)

Select **`Not now`**.

![user-15|540](images/building-home-lab-part-7/user-15.png)

Once on the desktop a prompt to allow internet access should show up click on **`Yes`**.

![user-16|540](images/building-home-lab-part-7/user-16.png)

### Guest Additions Installation

Similar to the Windows 2019 Server VM we need to install <u>Guest Additions</u> to enable Fullscreen mode. From the VM toolbar select **`Devices -> Remove disk for virtual drive`**. This will remove the Windows 10 image.

![user-17|500](images/building-home-lab-part-7/user-17.png)

Click on **`Devices -> Insert Guest Additions CD image`**.

![user-18|380](images/building-home-lab-part-7/user-18.png)

Open <u>File Explorer</u>. Once the disk has loaded from the sidebar select the disk drive. Double-click **`VBoxWindowsAdditions`** to start the installer. 

![user-19|540](images/building-home-lab-part-7/user-19.png)

Click **`Next`**.

![user-20|400](images/building-home-lab-part-7/user-20.png)

Click **`Next`**.

![user-21|400](images/building-home-lab-part-7/user-21.png)

Click on **`Install`** to start the installation.

![user-22|400](images/building-home-lab-part-7/user-22.png)

Select "<u>Reboot now</u>" and then click on **`Finish`**. The VM will reboot.

![user-23|400](images/building-home-lab-part-7/user-23.png)

Login into the system. 

![user-24|540](images/building-home-lab-part-7/user-24.png)

From the toolbar select **`Optical Devices -> Remove disk from virtual drive`** to remove the <u>Guest Additions</u> image.

![user-25|400](images/building-home-lab-part-7/user-25.png)

Use the shortcut **`Right Ctrl+F`** to enter <u>Fullscreen mode</u>. Use the same key to exit Fullscreen. The VM should automatically scale to fit the window size. 

### Adding VM1 to Domain

Now we can add this device to the AD domain and log in as an AD user.

Click on the <u>Search Bar</u> and search for "<u>This PC</u>". Right-click on it and select **`Properties`**.

![user-26|500](images/building-home-lab-part-7/user-26.png)

Click on **`Advanced system settings`**.

![user-27|540](images/building-home-lab-part-7/user-27.png)

Select the "<u>Computer Name</u>" tab and click on **`Change`**.

![user-28|360](images/building-home-lab-part-7/user-28.png)

In the <u>Computer name</u> field enter a name that can be used to easily identify this VM. In the <u>Member of</u> section select **`Domain`** and enter the name of the AD domain (in my case **`ad.lab`**). Then click on **`More`**.

![user-29|360](images/building-home-lab-part-7/user-29.png)

In the "<u>Primary DNS suffix of this computer</u>" field enter the <u>domain name</u>. Click on **`OK`**.

![user-30|360](images/building-home-lab-part-7/user-30.png)

Click on **`OK`**.

![user-31|360](images/building-home-lab-part-7/user-31.png)

Now a popup should appear. Enter the <u>login name</u> and <u>password</u> of the Domain Admin and click on **`OK`**.

![user-32|300](images/building-home-lab-part-7/user-32.png)

The device will be added to the AD environment. Click on **`OK`**.

![user-33|260](images/building-home-lab-part-7/user-33.png)

The device needs to be rebooted to apply the domain-specific settings. Click on **`OK`** to continue.

![user-34|300](images/building-home-lab-part-7/user-34.png)

Click on "<u>Restart Now</u>".

![user-35|300](images/building-home-lab-part-7/user-35.png)

Once on the login screen. Click on "<u>Other user</u>". Enter the <u>login name</u> and <u>password</u> of the AD user that will use this device and press **`Enter`**. 

![user-36|600](images/building-home-lab-part-7/user-36.jpg)

Now we are logged into the system as the AD user. To confirm this we can open PowerShell and run **`whoami`**.

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

Login using the AD credentials of the second AD user.

![user-42|600](images/building-home-lab-part-7/user-42.jpg)

![user-43|540](images/building-home-lab-part-7/user-43.png)

## Appendix

With this, we have completed the setup of the Active Directory lab. To wrap up, in this module we set up 3 VMs. The 1st VM (Windows Server 2019) was configured to be the Domain Controller and the other 2 VMs (Windows 10 Enterprise) were configured as client devices. Additionally, on the DC VM, we enabled DHCP, set up DNS Forwarder, enabled AD Certificate Services and configured Policies to be applied to all devices that are part of the AD environment.

You can delete the Windows Server 2019 ISO file if you do not want to store it for future use. Do not delete the Windows 10 Enterprise ISO just yet as we will require it to setup FlareVM.  

### DNS & DHCP Verification

To verify that the client VMs are indeed connected to the AD environment you can open **`DHCP Manager`** and compare the IP address shown with the IP address that has been assigned to the VM.

![misc-1|600](images/building-home-lab-part-7/misc-1.png)

Similarly, we can use **`DNS Manager`** to confirm that new DNS entries have been added for the client devices.

![misc-2|600](images/building-home-lab-part-7/misc-2.png)

### Taking VM Snapshots

> [!INFO]
> Snapshots can be taken with the VM in a running state but sometimes doing so can cause the VM to behave erratically. So I recommend "Powering off" all the VM before taking its Snapshot. 

Select the <u>Windows Server 2019 VM</u>. Click on the "<u>Hamburger menu</u>" and select **`Snapshots`** from the dropdown menu.

![misc-3|540](images/building-home-lab-part-7/misc-3.png)

Click on **`Take`** from the toolbar.

![misc-8|540](images/building-home-lab-part-7/misc-8.png)

Give the snapshot a descriptive <u>name</u> and click on **`OK`**.

![misc-4|400](images/building-home-lab-part-7/misc-4.png)

This will create a new Snapshot from the VM.

![misc-5|540](images/building-home-lab-part-7/misc-5.png)

Select the <u>Windows 10 Enterprise VM1</u> from the sidebar and follow the above steps to create a Snapshot.

![misc-6|540](images/building-home-lab-part-7/misc-6.png)

Follow the same steps to create Snapshot for <u>Windows 10 Enterprise VM2</u>.

![misc-7|540](images/building-home-lab-part-7/misc-7.png)

Right-click on the hamburger menu and select "<u>Details</u>" to return to the VM configuration page.

### Alternative AD Setup

Many other features and services can enabled on the DC. Refer to the below links for variations on the installation process.

- [How to Setup a Basic Home Lab Running Active Directory - YouTube](https://www.youtube.com/watch?v=MHsI8hJmggI)
- [How to Build an Active Directory Hacking Lab - YouTube](https://www.youtube.com/watch?v=xftEuVQ7kY0)

### Hacking AD Lab

There any numerous attacks that can be performed against an AD environment. Refer to the below links to see some of the commonly used hacks.

* [Hack Your VirtualBox AD Lab](https://benheater.com/hack-your-virtualbox-ad-lab/)
* [Active Directory Methodology - HackTricks](https://book.hacktricks.xyz/windows-hardening/active-directory-methodology)

In the next module, we will begin the setup of the Malware Analysis Lab.