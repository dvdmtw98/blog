---
title: "Building Your Own Home Lab: Part 4 - pfSense Firewall Configuration"
description: A step-by-step guide to build your very own Cybersecurity Home Lab using VirtualBox
date: 2024-01-06 18:30:00 -0600
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
image: images/building-home-lab-part-4/building-home-lab-part-4-banner.png
---

Banner Background by <a href="https://www.freepik.com/free-vector/gradient-white-color-background-abstract-modern_34010189.htm#query=simple%20backgrounds&position=28&from_view=search&track=ais&uuid=96e36b2e-64b3-42e2-8fd8-4fd18a6e1d5d">logturnal</a> on Freepik  
Hacker Image by <a href="https://www.freepik.com/free-vector/hacker-operating-laptop-cartoon-icon-illustration-technology-icon-concept-isolated-flat-cartoon-style_11602236.htm#page=2&query=hacker&position=28&from_view=search&track=sph&uuid=070b0d8a-d045-434d-9a51-f239e46d5f17">catalyststuff</a> on Freepik

## pfSense General Configuration

### Web Portal Setup

On the Kali Linux VM, open the web browser and navigate to `http://10.0.0.1`. 

You will get an Warning saving that the site could be Dangerous. This warning is shown since we are accessing a site that uses a self-signed certificate. Click on Advanced and then click on Accept the Risk and Continue.

![pfsense-26|500](images/building-home-lab-part-4/pfsense-26.png)

This will open the pfSense Web UI login page. Enter the default username and pasword.

Username: `admin`  
Password: `pfsense`

![pfsense-27|580](images/building-home-lab-part-4/pfsense-27.png)

Click next to start the onboarding process.

![pfsense-28|580](images/building-home-lab-part-4/pfsense-28.png)

Click Next again.

![pfsense-29|580](images/building-home-lab-part-4/pfsense-29.png)

In the General Information section. Enter a Hostname and Domain. This can be any name you chose. The hostname will be used to access the pfSense VM on the network. Uncheck the Override DNS option and then click Next.

![pfsense-30|580](images/building-home-lab-part-4/pfsense-30.png)

Select the Timezone that is correct for your region and then click Next. 

![pfsense-31|580](images/building-home-lab-part-4/pfsense-31.png)

Scroll to the bottom of the page and look for the RFC1918 Networks section. Uncheck the Block RFC1918 Private Networks option. We need to disable this option as our WAN interface is also an private interface that is managed by VirtualBox. 

![pfsense-32|580](images/building-home-lab-part-4/pfsense-32.png)

Click on Next.

![pfsense-33|580](images/building-home-lab-part-4/pfsense-33.png)

Enter the new password that will be used to access the pfSense Web UI. Remember to note down the new password.

![pfsense-34|580](images/building-home-lab-part-4/pfsense-34.png)

Click on Next to reload pfSense and apply the changes.

![pfsense-35|580](images/building-home-lab-part-4/pfsense-35.png)

Click on Next.

![pfsense-36|580](images/building-home-lab-part-4/pfsense-36.png)

Once the onboarding is complete we will be able to access the pfSense dashboard.

![pfsense-37|580](images/building-home-lab-part-4/pfsense-37.png)

### Interface Renaming

Click on Interfaces from the navigation bar and select OPT1.

![pfsense-38|580](images/building-home-lab-part-4/pfsense-38.png)

In the Description field enter `CYBER_RANGE`. Scroll to the bottom and click on Save. 

![pfsense-39|580](images/building-home-lab-part-4/pfsense-39.png)

At the top of the page a new popup will appear. Click on Apply Changes.

![pfsense-40|580](images/building-home-lab-part-4/pfsense-40.png)

In the navigation bar click on Interfaces and select OPT2. 

![pfsense-41|580](images/building-home-lab-part-4/pfsense-41.png)

In the Description field enter `AD_LAB`. Scroll to the bottom of the page and click on Save. An popup will appear at the top of the page click on Apply Changes.

![pfsense-42|580](images/building-home-lab-part-4/pfsense-42.png)

### DNS Resolver Configuration

From the navigation bar select Services and then click on DNS Resolver.

![pfsense-43|580](images/building-home-lab-part-4/pfsense-43.png)

Scroll to the bottom of the page and look for the highlighted options and enable them. No need to hit on save just yet. Scroll to the top of the page.

![pfsense-44|580](images/building-home-lab-part-4/pfsense-44.png)

Click on Advanced Settings.

![pfsense-45|580](images/building-home-lab-part-4/pfsense-45.png)

Scroll down to the Advanced Resolver Options section and enable the highlighted options. Scroll to the end and click on Save.

![pfsense-46|580](images/building-home-lab-part-4/pfsense-46.png)

A popup will appear at the top of the page. Click on Apply Changes.

![pfsense-47|580](images/building-home-lab-part-4/pfsense-47.png)

### Advanced Configuration

From the navigation bar select System and then click on Advanced.

![pfsense-48|580](images/building-home-lab-part-4/pfsense-48.png)
Click on the Networking Tab.

![pfsense-49|580](images/building-home-lab-part-4/pfsense-49.png)

Scroll to the end in the Network Interfaces section enable the highlighted option. This option should improve the performance of the pfSense VM. Click on Save.

![pfsense-50|580](images/building-home-lab-part-4/pfsense-50.png)

An popup will appear telling that pfSense needs to be rebooted. Click on Ok.

![pfsense-51|360](images/building-home-lab-part-4/pfsense-51.png)

The following page will be shown while pfSense reboots and applies the changes.

![pfsense-52|580](images/building-home-lab-part-4/pfsense-52.png)

Once the reboot is complete we will be asked to login again. Use the new password to access the Dashboard.

![pfsense-27|580](images/building-home-lab-part-4/pfsense-27.png)

## Kali Linux Static IP Assignment

From the navigation bar select Status and then click on DHCP Leases.

![pfsense-53|580](images/building-home-lab-part-4/pfsense-53.png)

In the Leases section we should see the Kali Linux VM with its current IP address. Click on the highlighted `+` icon to assign a static IP to the VM. The static IP will make it easier for us to apply firewall rules where certain interfaces should be able to reach the Kali VM. 

![pfsense-54|580](images/building-home-lab-part-4/pfsense-54.png)

In the IP Address input enter `10.0.0.2`. Scroll to the bottom and click on Save.

![pfsense-55|580](images/building-home-lab-part-4/pfsense-55.png)

A popup will show up at the top of the page. Click on Apply Changes.

![pfsense-56|580](images/building-home-lab-part-4/pfsense-56.png)

### Refresh Kali Linux IP Address

Open a terminal on the Kali VM. We can see the following command to see out current address.

```bash
ip a l eth0
```

We want the VM to release the current IP address and use the static IP that was reserved. This can be due using the following command:

```bash
sudo ip l set eth0 down && sudo ip l set eth0 up
```

Enter password when prompted. To confirm that the VM is using the static IP run the following command:

```bash
ip a l eth0
```

![pfsense-57|580](images/building-home-lab-part-4/pfsense-57.png)

## pfSense Firewall Configuration

From the navigation bar select Firewall and then click on Rules.

![pfsense-58|580](images/building-home-lab-part-4/pfsense-58.png)

### LAN Rules

Click on the LAN tab. The LAN tab will contain some predefined rules.

![pfsense-59|580](images/building-home-lab-part-4/pfsense-59.png)

Click on the "Add rule to top" button to create a new rule. 

![pfsense-60|400](images/building-home-lab-part-4/pfsense-60.png)

Change the following options:  
Action: `Block`  
Address Family: `Ipv4+IPv6`  
Protocol: `Any`  
Source: `LAN subnets`  
Destination: `WAN subnets`  
Description: `Block access to services on WAN interface`

Scroll to the bottom and click on Save.

![pfsense-61|580](images/building-home-lab-part-4/pfsense-61.png)

A popup will appear at the top of the page. Click on Apply Changes.

![pfsense-62|580](images/building-home-lab-part-4/pfsense-62.png)

The final LAN rules should look as follows. The order of the rules are important. If the order is not correct. Drag the rules around till it matches the below image.

![pfsense-63|580](images/building-home-lab-part-4/pfsense-63.png)

### CYBER_RANGE Rules

Before creating the rules for CYBER_RANGE we need to create a Alias. From the navigation bar select Firewall and click on Aliases.

![pfsense-64|580](images/building-home-lab-part-4/pfsense-64.png)

In the IP tab click on Add to create a new alias.

![pfsense-65|580](images/building-home-lab-part-4/pfsense-65.png)

Enter the following details:  
Name: `RFC1918`  
Description: `Private I{v4 Address Space`  
Type: `Network(s)`  
Network 1: `10.0.0.0/8`  
Network 2: `172.16.0.0/12`  
Network 3: `192.168.0.0/16`  
Network 4: `169.254.0.0/16`  
Network 5: `127.0.0.0/8`

Click on Save to create alias.

![pfsense-66|580](images/building-home-lab-part-4/pfsense-66.png)

A popup will show up at the top click on Apply Changes.

![pfsense-67|580](images/building-home-lab-part-4/pfsense-67.png)

The final result should be as follows:

![pfsense-68|580](images/building-home-lab-part-4/pfsense-68.png)

From the navigation bar select Firewall and then click on Rules. Select the CYBER_RANGE tab.

![pfsense-69|580](images/building-home-lab-part-4/pfsense-69.png)

Use the "Add rule to end" button for all the rules.

![pfsense-71|400](images/building-home-lab-part-4/pfsense-71.png)

Configure the rule as follows:
Address Family: `IPv4+IPv6`  
Protocol: `Any`  
Source: `CYBER_RANGE subnets`  
Destination: `CYBER_RANGE address`  
Description: `Allow traffic to all devices on the CYBER_RANGE network`

Scroll to the bottom and click on save.

![pfsense-70|580](images/building-home-lab-part-4/pfsense-70.png)

A popup will appear at the top to save the changes, no need to click on that just yet. Click on the "Add rule to end" button to create a new rule.

The rule has the following details:  
Protocol: `Any`  
Source: `CYBER_RANGE subnets`  
Destination: `Address or Alias - 10.0.0.2`  
Description: `Allow traffic to Kali Linux VM`

Scroll to the bottom and click on Save.

![pfsense-72|580](images/building-home-lab-part-4/pfsense-72.png)

Click on the "Add rule to end" button to create a new rule.

Create a rule with the following settings:  
Protocol: `Any`  
Source: `CYBER_RANGE subnets`  
Destination: `Address or Alias - RFC1918` (Select Invert match)  
Description: `Allow to any non-private IPv4 Address`

Scroll to the bottom and click on Save. 

![pfsense-73|580](images/building-home-lab-part-4/pfsense-73.png)

Click on the "Add rule to end" button to create a new rule.

Create a rule with the following settings:  
Action: `Block`  
Address Family: `IPv4+IPv6`  
Protocol: `Any`  
Source: `CYBER_RANGE subnets`  
Description: `Block access to everything`

Scroll to the bottom and click on Save.

![pfsense-74|580](images/building-home-lab-part-4/pfsense-74.png)

Click on the Apply Changes button in the popup at the top of the screen.

![pfsense-75|580](images/building-home-lab-part-4/pfsense-75.png)

The final rules should look as follows:

![pfsense-76|580](images/building-home-lab-part-4/pfsense-76.png)

### AD_LAB Rules

Click on the `AD_LAB` tab. Use the "Add rule to end" button to create new rules.

![pfsense-77|580](images/building-home-lab-part-4/pfsense-77.png)

Create a rule with the following settings:  
Action: `Block`  
Address Family: `IPv4+IPv6`  
Protocol: `Any`  
Source: `AD_LAB subnets`  
Destination: `WAN subnets`  
Description: `Block access to services on WAN interface`

Scroll to the bottom and click on Save.

![pfsense-78|580](images/building-home-lab-part-4/pfsense-78.png)

A popup will appear at the top to save the changes, no need to click on that just yet. Click on the "Add rule to end" button to create a new rule.

The rule has the following details:  
Action: `Block`  
Address Family: `IPv4+IPv6`  
Protocol: `Any`  
Source: `AD_LAB subnets`  
Destination: `CYBER_RANGE subnets`  
Description: `Block traffic to CYBER_RANGE interface`

Scroll to the bottom and click on Save.

![pfsense-79|580](images/building-home-lab-part-4/pfsense-79.png)

Click on the "Add rule to end" button to create a new rule.

The rule has the following details:  
Address Family: `IPv4+IPv6`  
Protocol: `Any`  
Source: `AD_LAB subnets`  
Description: `Allow traffic to all other subnets and Internet`

Scroll to the bottom and click on Save.

![pfsense-80|580](images/building-home-lab-part-4/pfsense-80.png)

Click on the Apply Changes button in the popup at the top of the screen.

![pfsense-81|580](images/building-home-lab-part-4/pfsense-81.png)

The final rules should look as follows:

![pfsense-82|580](images/building-home-lab-part-4/pfsense-82.png)

I would recommend restarting the pfSense VM at this point before proceeding to the next module. 

In the next module we will add some vulnerable VMs to the CYBER_RANGE interface and try to attack it using Kali Linux.
