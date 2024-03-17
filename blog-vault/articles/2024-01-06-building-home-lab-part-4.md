---
categories:
  - Security
  - Home Lab
date: 2024-01-06 09:10:00 -0600
description: A step-by-step guide for building your very own Cybersecurity Home Lab using VirtualBox
img_path: /assets/
published: true
tags:
  - security
  - home-lab
  - virtualbox
  - networking
  - pfsense
title: "Building a Virtual Security Home Lab: Part 4 - pfSense Firewall Configuration"
---

![banner-image|640](images/building-home-lab-part-4/building-home-lab-part-4-banner.png)

Banner Background by [logturnal](https://www.freepik.com/free-vector/gradient-white-color-background-abstract-modern_34010189.htm) on Freepik  
Hacker Image by [catalyststuff](https://www.freepik.com/free-vector/hacker-operating-laptop-cartoon-icon-illustration-technology-icon-concept-isolated-flat-cartoon-style_11602236.htm) on Freepik

In this module, we will finish the pending pfSense setup. After that, we will define firewall rules for the subnets we defined for our home lab. 

## pfSense General Configuration

### Web Portal Setup

On the Kali Linux VM, open the web browser and navigate to **`https://10.0.0.1`**. 

You will get the following message <u>Warning: Potential Security Risk Ahead</u>. This warning can be ignored. We get this warning because the URL that we are trying to access does not use the secure HTTP (HTTPS). Click on **`Advanced`** and then click on **`Accept the Risk and Continue`**.

![pfsense-26|500](images/building-home-lab-part-4/pfsense-26.png)

This will open the pfSense Web UI login page. Login using the default credentials.  
Username: **`admin`**  
Password: **`pfsense`**

![pfsense-27|600](images/building-home-lab-part-4/pfsense-27.png)

Click on **`Next`**.

![pfsense-28|600](images/building-home-lab-part-4/pfsense-28.png)

Click **`Next`** again.

![pfsense-29|600](images/building-home-lab-part-4/pfsense-29.png)

In the **`General Information`** section. Provide a <u>Hostname</u> and <u>Domain</u> name. This can be any name you choose. The <u>hostname</u> can be used to identify the pfSense VM on the network. Uncheck the <u>Override DNS</u> option and then click **`Next`**.

![pfsense-30|600](images/building-home-lab-part-4/pfsense-30.png)

Select your <u>Timezone</u> and then click **`Next`**. 

![pfsense-31|600](images/building-home-lab-part-4/pfsense-31.png)

Scroll to the bottom of the page and look for the **`RFC1918 Networks`** section. Uncheck the <u>Block RFC1918 Private Networks</u> option. 

![pfsense-32|600](images/building-home-lab-part-4/pfsense-32.png)

> [!INFO]
> We disable this option because our WAN interface is not an real WAN interface. It uses an private IP address instead of an public IP address which would be used by a real WAN interface to connect to the Internet.  
> Our WAN interface uses a private IP address to send data packets to the host system which then sends the data packets to the router present in the network.

Don't change any value on this page. Click on **`Next`**.

![pfsense-33|600](images/building-home-lab-part-4/pfsense-33.png)

Enter a new password for the admin user. Store the password in a secure place.

![pfsense-34|600](images/building-home-lab-part-4/pfsense-34.png)

Click on **`Reload`** to apply the changes.

![pfsense-35|600](images/building-home-lab-part-4/pfsense-35.png)

Click on **`Finish`**.

![pfsense-36|600](images/building-home-lab-part-4/pfsense-36.png)

Once the onboarding is complete we will be able to access the pfSense dashboard.

![pfsense-37|600](images/building-home-lab-part-4/pfsense-37.png)

### Interface Renaming

From the navigation bar select **`Interfaces -> OPT1`**.

![pfsense-38|600](images/building-home-lab-part-4/pfsense-38.png)

In the <u>Description</u> field enter **`CYBER_RANGE`**. Scroll to the bottom and click on **`Save`**. 

![pfsense-39|600](images/building-home-lab-part-4/pfsense-39.png)

At the top of the page, a new popup will appear. Click on **`Apply Changes`**.

![pfsense-40|600](images/building-home-lab-part-4/pfsense-40.png)

From the navigation bar select **`Interfaces -> OPT2`**. 

![pfsense-41|600](images/building-home-lab-part-4/pfsense-41.png)

In the <u>Description</u> field enter **`AD_LAB`**. Scroll to the bottom of the page and click on **`Save`**. A popup will appear at the top of the page click on **`Apply Changes`**.

![pfsense-42|600](images/building-home-lab-part-4/pfsense-42.png)

### DNS Resolver Configuration

From the navigation bar select **`Services -> DNS Resolver`**.

![pfsense-43|600](images/building-home-lab-part-4/pfsense-43.png)

Scroll to the bottom of the page, look for the highlighted options and enable them. No need to save just yet. Scroll to the top of the page.

![pfsense-44|600](images/building-home-lab-part-4/pfsense-44.png)

Click on **`Advanced Settings`**.

![pfsense-45|600](images/building-home-lab-part-4/pfsense-45.png)

Scroll down to the **`Advanced Resolver Options`** section and enable the highlighted options. Scroll to the end and click on **`Save`**.

![pfsense-46|600](images/building-home-lab-part-4/pfsense-46.png)

A popup will appear at the top of the page. Click on **`Apply Changes`**.

![pfsense-47|600](images/building-home-lab-part-4/pfsense-47.png)

### Advanced Configuration

From the navigation bar select **`System -> Advanced`**.

![pfsense-48|600](images/building-home-lab-part-4/pfsense-48.png)

Go to the **`Networking`** tab

![pfsense-49|600](images/building-home-lab-part-4/pfsense-49.png)

Scroll to the end in the **`Network Interfaces`** section and enable the highlighted option. This option should improve the performance of pfSense. Click on **`Save`**.

![pfsense-50|600](images/building-home-lab-part-4/pfsense-50.png)

A popup will appear click on **`OK`** to reboot pfSense.

![pfsense-51|360](images/building-home-lab-part-4/pfsense-51.png)

The following page will be shown while pfSense applies the changes.

![pfsense-52|600](images/building-home-lab-part-4/pfsense-52.png)

Once the reboot is complete we will be asked to log in again. Use the new password to access the Dashboard.

![pfsense-27|600](images/building-home-lab-part-4/pfsense-27.png)

## Kali Linux Static IP Assignment

From the navigation bar select **`Status -> DHCP Leases`**.

![pfsense-53|600](images/building-home-lab-part-4/pfsense-53.png)

In the **`Leases`** section, we should see the Kali Linux VM with its current IP address. Click on the highlighted **`+`** icon to assign a static IP to Kali Linux. The static IP will make it easier for us to apply firewall rules to interfaces that should only be able to reach the Kali VM. 

![pfsense-54|600](images/building-home-lab-part-4/pfsense-54.png)

In the <u>IP Address</u> input enter **`10.0.0.2`**. Scroll to the bottom and click on **`Save`**.

![pfsense-55|600](images/building-home-lab-part-4/pfsense-55.png)

A popup will show up at the top of the page. Click on **`Apply Changes`**.

![pfsense-56|600](images/building-home-lab-part-4/pfsense-56.png)

### Refresh Kali Linux IP Address

Open a terminal on the VM. Use the following command to see the current IP address.

```bash
ip a l eth0
```

We want the VM to release the current IP address and use the static IP that was reserved. This can be achieved using the following command:

```bash
sudo ip l set eth0 down && sudo ip l set eth0 up
```

Enter password when prompted. To confirm that the VM is using the static IP run the following command:

```bash
ip a l eth0
```

![pfsense-57|600](images/building-home-lab-part-4/pfsense-57.png)

## pfSense Firewall Configuration

From the navigation bar select **`Firewall -> Rules`**.

![pfsense-58|600](images/building-home-lab-part-4/pfsense-58.png)

### LAN Rules

Go to the **`LAN`** tab. The LAN tab will have some predefined rules.

![pfsense-59|600](images/building-home-lab-part-4/pfsense-59.png)

Click on the "<u>Add rule to top</u>" button to create a new rule. 

![pfsense-60|400](images/building-home-lab-part-4/pfsense-60.png)

Change the following options:  
Action: **`Block`**  
Address Family: **`Ipv4+IPv6`**  
Protocol: **`Any`**  
Source: **`LAN subnets`**  
Destination: **`WAN subnets`**  
Description: **`Block access to services on WAN interface`**

Scroll to the bottom and click on **`Save`**.

![pfsense-61|600](images/building-home-lab-part-4/pfsense-61.png)

A popup will appear at the top of the page. Click on **`Apply Changes`**.

![pfsense-62|600](images/building-home-lab-part-4/pfsense-62.png)

The final LAN rules should look as follows.

![pfsense-63|600](images/building-home-lab-part-4/pfsense-63.png)

The order of the rules is important. If the order is not correct. Drag the rules around till it matches the above image.

### CYBER_RANGE Rules

Before creating the rules for **`CYBER_RANGE`** we need to create a <u>Alias</u>. From the navigation bar select **`Firewall -> Aliases`**.

![pfsense-64|600](images/building-home-lab-part-4/pfsense-64.png)

In the <u>IP</u> tab click on **`Add`** to create a new alias.

![pfsense-65|600](images/building-home-lab-part-4/pfsense-65.png)

Enter the following details:  
Name: **`RFC1918`**  
Description: **`Private IPv4 Address Space`**  
Type: **`Network(s)`**  
Network 1: **`10.0.0.0/8`**  
Network 2: **`172.16.0.0/12`**  
Network 3: **`192.168.0.0/16`**  
Network 4: **`169.254.0.0/16`**  
Network 5: **`127.0.0.0/8`**

Click on **`Save`** to create an alias.

![pfsense-66|600](images/building-home-lab-part-4/pfsense-66.png)

A popup will show up at the top click on **`Apply Changes`**.

![pfsense-67|600](images/building-home-lab-part-4/pfsense-67.png)

The final result should be as follows:

![pfsense-68|600](images/building-home-lab-part-4/pfsense-68.png)

From the navigation bar select **`Firewall -> Rules`**. Select the **`CYBER_RANGE`** tab.

![pfsense-69|600](images/building-home-lab-part-4/pfsense-69.png)

Use the "<u>Add rule to end</u>" button for all the rules.

![pfsense-71|400](images/building-home-lab-part-4/pfsense-71.png)

Configure the rule as follows:
Address Family: **`IPv4+IPv6`**  
Protocol: **`Any`**  
Source: **`CYBER_RANGE subnets`**  
Destination: **`CYBER_RANGE address`**  
Description: **`Allow traffic to all devices on the CYBER_RANGE network`**

Scroll to the bottom and click on **`Save`**.

![pfsense-70|600](images/building-home-lab-part-4/pfsense-70.png)

A popup will appear at the top to save the changes, no need to click on that just yet. Click on the "<u>Add rule to end</u>" button to create a new rule.

The rule has the following details:  
Protocol: **`Any`**  
Source: **`CYBER_RANGE subnets`**  
Destination: **`Address or Alias - 10.0.0.2`**  
Description: **`Allow traffic to Kali Linux VM`**

Scroll to the bottom and click on **`Save`**.

![pfsense-72|600](images/building-home-lab-part-4/pfsense-72.png)

Click on the "<u>Add rule to end</u>" button to create a new rule.

Create a rule with the following settings:  
Protocol: **`Any`**  
Source: **`CYBER_RANGE subnets`**  
Destination: **`Address or Alias - RFC1918`** (Select Invert match)  
Description: **`Allow to any non-private IPv4 Address`**

Scroll to the bottom and click on **`Save`**. 

![pfsense-73|600](images/building-home-lab-part-4/pfsense-73.png)

Click on the "<u>Add rule to end</u>" button to create a new rule.

Create a rule with the following settings:  
Action: **`Block`**  
Address Family: **`IPv4+IPv6`**  
Protocol: **`Any`**  
Source: **`CYBER_RANGE subnets`**  
Description: **`Block access to everything`**

Scroll to the bottom and click on **`Save`**.

![pfsense-74|600](images/building-home-lab-part-4/pfsense-74.png)

Click on the **`Apply Changes`** button in the popup at the top of the screen.

![pfsense-75|600](images/building-home-lab-part-4/pfsense-75.png)

The final rules should look as follows:

![pfsense-76|600](images/building-home-lab-part-4/pfsense-76.png)

### AD_LAB Rules

Click on the **`AD_LAB`** tab. Use the "<u>Add rule to end</u>" button to create new rules.

![pfsense-77|600](images/building-home-lab-part-4/pfsense-77.png)

Create a rule with the following settings:  
Action: **`Block`**  
Address Family: **`IPv4+IPv6`**  
Protocol: **`Any`**  
Source: **`AD_LAB subnets`**  
Destination: **`WAN subnets`**  
Description: **`Block access to services on WAN interface`**

Scroll to the bottom and click on **`Save`**.

![pfsense-78|600](images/building-home-lab-part-4/pfsense-78.png)

A popup will appear at the top to save the changes, no need to click on that just yet. Click on the "<u>Add rule to end</u>" button to create a new rule.

The rule has the following details:  
Action: **`Block`**  
Address Family: **`IPv4+IPv6`**  
Protocol: **`Any`**  
Source: **`AD_LAB subnets`**  
Destination: **`CYBER_RANGE subnets`**  
Description: **`Block traffic to CYBER_RANGE interface`**

Scroll to the bottom and click on **`Save`**.

![pfsense-79|600](images/building-home-lab-part-4/pfsense-79.png)

Click on the "<u>Add rule to end</u>" button to create a new rule.

The rule has the following details:  
Address Family: **`IPv4+IPv6`**  
Protocol: **`Any`**  
Source: **`AD_LAB subnets`**  
Description: **`Allow traffic to all other subnets and Internet`**

Scroll to the bottom and click on **`Save`**.

![pfsense-80|600](images/building-home-lab-part-4/pfsense-80.png)

Click on the **`Apply Changes`** button in the popup at the top of the screen.

![pfsense-81|600](images/building-home-lab-part-4/pfsense-81.png)

The final rules should look as follows:

![pfsense-82|600](images/building-home-lab-part-4/pfsense-82.png)

## pfSense Reboot

Now we need to restart pfSense to persist the firewall rules. From the navigation bar select **`Diagnostics -> Reboot`**.

![pfsense-118|600](images/building-home-lab-part-4/pfsense-118.png)

Click on **`Submit`**.

![pfsense-119|600](images/building-home-lab-part-4/pfsense-119.png)

Once pfSense boots up you will be redirected to the login page.

In the next module, we will add some vulnerable VMs to the **`CYBER_RANGE`** interface and then we will test our connectivity to them from the Kali Linux VM.

[Part 5 - Cyber Range Setup](https://blog.davidvarghese.dev/posts/building-home-lab-part-5/)