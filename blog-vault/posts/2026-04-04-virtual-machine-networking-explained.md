---
title: Virtual Machine Networking Modes Explained
description: Stop guessing. Learn how NAT, Bridged, Host-Only, and Internal actually work.
date: 2026-04-04 21:20:00 +0530
categories:
  - Networking
  - Virtualization
tags:
  - networking
  - virtualization
  - virtual-machine
  - home-lab
  - technology
published: true
media_subpath: /assets/
---

![[virtual-machine-networking-banner.png|640]]
_Banner Background by [rawpixel.com](https://www.freepik.com/free-photo/business-network-background-connecting-dots-technology-design_21629645.htm) on Freepik_

When you create a virtual machine, one of the first settings you have to configure is the networking mode. The problem is options like NAT, Bridged, and Host-Only do not make it obvious what they do. With no easy way of telling what they actually mean, choosing the right mode becomes more complex than it needs to be.

At its core, this is not a networking problem. It's a **connectivity** problem. Each network mode simply determines where the VM sits, who it can communicate with, and who can initiate that communication. In this article, I will break down the network types and explain how NAT, Bridged, Host-Only, and Internal compare with each other.

## How Virtual Networking Works

A virtual machine (VM) is just a computer running inside another computer. It has its own processor, memory, storage, and IP address. Virtual machines are not directly connected to physical hardware. A layer sits between the VM and the physical world. This layer is the hypervisor, the software that runs and manages your VMs. 

For networking, the hypervisor builds a virtual network of switches, and routers (NAT engines) that direct traffic exactly where it needs to go. Instead of plugging into a physical network, your VM connects to the virtual network. Depending on the network mode, a VM may get an IP from your real network, a private virtual network, or no IP at all.

Every network mode basically answers four questions:
- Can the VM access the internet?
- Can the VM and host communicate with each other?
- Can VMs communicate with each other?
- Can the VM and devices on LAN communicate with each other?

All network modes are just different combinations of these four. Let's see how each mode answers these questions.

## Networking Modes

<iframe width="560" height="315" src="https://www.youtube-nocookie.com/embed/Fhdxk4bmJCs?si=XLeObuTHiTQb3kgm" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>

### NAT (Network Address Translation)

NAT is the default networking mode in most commercial virtualization software. It’s popular because in this mode your VM gets internet access with no extra setup.

![[nat-diagram.png|640]]
_NAT_

#### How It Works

The hypervisor creates a virtual router (also called NAT engine). The router has two interfaces:
- A public (outside) interface that connects to your host machine's network stack.
- A private (inside) interface that connects to the VM.

The VM gets a private IP address from the NAT engine, which usually includes a DHCP service. When the VM sends traffic to the internet, the NAT engine replaces the VM’s private IP in the traffic with the host’s IP. The host then forwards this traffic to the internet through its network connection. To the outside world, all traffic appears to come from your host. 

#### NAT vs. NAT Network

NAT mode creates a separate virtual network for each VM. Each VM sits behind its own NAT engine (virtual router). This means the VMs cannot communicate with each other.

NAT Network extends this by creating a shared virtual network. All VMs are connected using a virtual switch. This allows the VMs to communicate with each other while still having internet access.

![[nat-network-diagram.png|640]]
_NAT Network_

> [!IMPORTANT] Product Difference
> - VMware does not have a basic NAT mode like VirtualBox. 
> - The NAT mode in VMware is equivalent to the NAT Network mode in VirtualBox. This means that in VMware, VMs that use NAT mode can communicate with each other.

In simple terms:
- NAT → one VM per private network (isolated)
- NAT Network → multiple VMs on the same private network

#### What This Means in Practice

- The VM can access the internet through the host.
- The VM can initiate communication with the host.
- Devices on your physical network cannot initiate connections to the VM.
- VMs on the same host cannot talk to each other in basic NAT mode (they can in NAT Network).

| Feature                  | VirtualBox NAT             | VirtualBox NAT Network     | VMware NAT                 |
| ------------------------ | -------------------------- | -------------------------- | -------------------------- |
| Internet access from VM  | Yes                        | Yes                        | Yes                        |
| VM can reach Host        | Yes                        | Yes                        | Yes                        |
| Host can reach VM        | No (needs port forwarding) | No (needs port forwarding) | No (needs port forwarding) |
| VM can reach LAN devices | Yes                        | Yes                        | Yes                        |
| LAN devices can reach VM | No (needs port forwarding) | No (needs port forwarding) | No (needs port forwarding) |
| VM ↔ VM communication    | No                         | Yes                        | Yes                        |

#### Accessing the VM from Outside

Because the VM is behind NAT, you cannot directly connect to it from another machine on your network. To allow inbound access, such as connecting via SSH or running a web server, you must configure port forwarding on the NAT engine. This tells the hypervisor to forward traffic from a specific port on your host to a port on the VM.

> [!INFO] Port Forwarding  
> - Port forwarding is a networking technique that redirects incoming traffic from one IP address and port to another. It allows external devices to access services running inside a private network.
> - In the context of virtual machines, port forwarding maps a port on the host to a port on the VM. This allows external systems to reach services running inside the VM, even though it is behind NAT.

#### When to Use NAT

Use NAT when you simply need the VM to reach the internet and don't need other devices to reach the VM. It's ideal for:
- Downloading software or updates inside the VM.
- Testing web browsers or command‑line tools.
- Any task where the VM acts only as a client, not a server.

### Limitations

- **Inbound access requires extra configuration.** Devices on your physical network cannot reach the VM unless you set up port forwarding.
- **VM‑to‑VM communication is blocked** (in basic NAT mode). If you need multiple VMs to talk to each other, you must use NAT Network (VirtualBox) or a different mode.
- **Limited visibility.** The VM is hidden behind the host, so network troubleshooting (e.g., ping from other devices) is not possible without port forwarding.

### Bridged

Bridged mode makes your VM act like a real machine on your physical network. Instead of being hidden behind NAT, the VM connects directly to the same network as your host.

![[bridged-diagram.png|540]]
_Bridged_

#### How It Works

The hypervisor creates a virtual bridge between the VM’s virtual network interface and your host’s physical network adapter. The VM effectively shares the host’s network connection, but appears as a separate device on the network.

When you enable Bridged mode:
- The VM sends and receives traffic directly through the host’s NIC.
- It requests an IP address from the same DHCP server that assigns IPs to your physical devices.
- From the perspective of your router and other devices on the network, the VM is just another device.

#### What This Means in Practice

- The VM can access the internet (via your physical router).
- The VM can communicate with the host using the host’s IP on the physical network.
- Other devices on your physical network can reach the VM directly, using its IP address.
- VMs on the same host can communicate with each other, just like devices on a normal network.

| Feature                  | Bridged |
| ------------------------ | ------- |
| Internet access from VM  | Yes     |
| VM can reach Host        | Yes     |
| Host can reach VM        | Yes     |
| VM can reach LAN devices | Yes     |
| LAN devices can reach VM | Yes     |
| VM ↔ VM communication    | Yes     |

#### Accessing the VM from Outside

Because the VM gets its own IP on your physical network, you can connect to it from any device on that network using its IP address. No port forwarding is needed (within the local network). However, if you need to access the VM from the internet, you must configure port forwarding on your physical router.

#### When to Use Bridged

Use Bridged mode when you want the VM to behave like a real device on your physical network. It’s ideal for:
- Running network services (web server, SSH, file sharing, etc.) that need to be accessible by other devices.
- Testing applications in a real network environment.
- Situations where you need the VM to have its own IP and be fully reachable.

#### Limitations

- **Less isolation.** The VM is directly exposed to your physical network, which can increase security risks if the VM is vulnerable or misconfigured.
- **Network changes affect connectivity.** If you move the host between networks (e.g., switching Wi‑Fi), the VM may need to obtain a new IP address or be reconfigured.
- **May not work on some networks.** Bridged mode may not work on some laptop Wi-Fi cards, enterprise networks and VPNs due to restrictions that limit the number of devices and MAC addresses per connection.

### Host‑Only

Host‑Only mode creates a private network that is completely isolated from your physical network. The only devices that can communicate on this network are your host and the VMs attached to the network. There is no internet access, and outside devices cannot reach the VMs.

![[host-only-diagram.png|640]]
_Host-Only_

#### How It Works

The hypervisor creates a virtual switch. Connected to this switch are:
- A virtual network adapter from the host machine.
- The virtual network interfaces of VMs that are configured to use Host‑Only mode.

All devices on this virtual switch share the same private IP range. The host gets an IP on this network through its virtual adapter, and each VM gets its own IP from a DHCP server provided by the hypervisor.

The host has two network interfaces: a physical NIC connected to the internet and a virtual NIC connected to the Host-Only network. There is no routing between these two networks, so traffic from the Host-Only network cannot reach the internet. Because the virtual switch is not connected to a router, traffic never leaves the isolated network.

#### What This Means in Practice

- The VM has no internet access.
- The VM can communicate with the host (using the host’s virtual adapter IP).
- VMs connected to the same Host‑Only network can communicate with each other.
- Devices on your physical network cannot reach the VM, and the VM cannot reach them.

| Feature                  | Host‑Only |
| ------------------------ | --------- |
| Internet access from VM  | No        |
| VM can reach Host        | Yes       |
| Host can reach VM        | Yes       |
| VM can reach LAN devices | No        |
| LAN devices can reach VM | No        |
| VM ↔ VM communication    | Yes       |

#### Accessing the VM from Outside

There is no direct way to access a Host‑Only VM from your physical network or the internet, because the virtual switch is isolated. If you need occasional outbound access, you can temporarily add a second network adapter to the VM (e.g., NAT or Bridged) and disable it when you’re done.

#### When to Use Host‑Only

Use Host‑Only when you need a completely isolated environment where the VM should not have internet access but still needs to communicate with the host or other VMs. It’s ideal for:
- Setting up local development environments.
- Isolated labs where you want to control everything without external interference.
- Learning and experimentation where internet access is undesirable.

#### Limitations

- **No internet connectivity**. Software updates or package installations must be done through other means (e.g., shared folders, ISO files, or temporarily switching network modes).
- **Isolation from physical network**. You cannot access the VM from other devices on your network.
- **Creates separate host adapter**. The host gains an additional virtual IP, which can be confusing to new users.

### Internal

Internal mode takes isolation one step further than Host‑Only. It creates a private network where only VMs can communicate with each other. This network is equivalent to a standalone switch that is not connected to any router, DHCP service, or external network.

![[internal-diagram.png|640]]
_Internal_

#### How It Works

The hypervisor creates a virtual switch. Any VMs configured to use Internal mode are connected to this switch. Unlike Host‑Only, no virtual network adapter is created on the host. This means:
- The host cannot communicate with VMs on the Internal network.
- The Internal network is completely separate from the host’s physical interfaces.

All VMs attached to the same internal network share the same private IP range. IP addresses must usually be configured manually, or provided by a DHCP server running inside the network. Because the virtual switch is not connected to any router or physical adapter, traffic never leaves the isolated environment.

> [!IMPORTANT] Product Difference
> - In VMware, internal/isolated networks are created using LAN Segments.
> - VMware does not provide a built-in DHCP service for LAN Segment. The user must set up a VM to provide DHCP functionality.

#### What This Means in Practice

- VMs have no internet access.
- The VM cannot communicate with the host.
- VMs connected to the same internal network can communicate with each other.
- Devices on your physical network cannot reach the VMs, and the VMs cannot reach them.

| Feature                  | Internal / LAN Segment |
| ------------------------ | ---------------------- |
| Internet access from VM  | No                     |
| VM can reach Host        | No                     |
| Host can reach VM        | No                     |
| VM can reach LAN devices | No                     |
| LAN devices can reach VM | No                     |
| VM ↔ VM communication    | Yes                    |

#### Accessing the VM from Outside

There is no direct way to access VMs on an internal network from your physical network or the internet, because the virtual switch is isolated. If you need outbound access (e.g., to install updates), you can temporarily add a second network adapter (e.g., NAT or Bridged) and remove it when you’re done.

#### When to Use Internal

Use Internal mode when you need a completely isolated, self‑contained network where VMs interact only with each other. It’s ideal for:
- Malware analysis or security testing.
- Simulating real network environments with multiple machines.
- Experimenting with network services without any risk of affecting the host or physical network.

#### Limitations

- **No host access.** You cannot connect to the host from the VMs without adding a second adapter.
- **No internet access.** Software installation or updates require alternative methods (shared folders, ISO files, or a temporary second adapter).
- **DHCP may be unavailable.** In some hypervisors (e.g., VMware), you must configure static IPs or run your own DHCP server.

## Quick Comparison

| Mode                                         | Internet | VM → Host | Host → VM                  | VM → LAN | LAN → VM                   | VM ↔ VM |
| -------------------------------------------- | -------- | --------- | -------------------------- | -------- | -------------------------- | ------- |
| NAT (VirtualBox)                             | Yes      | Yes       | No (needs port forwarding) | Yes      | No (needs port forwarding) | No      |
| NAT Network (VirtualBox) / <br>NAT (VMware)  | Yes      | Yes       | No (needs port forwarding) | Yes      | No (needs port forwarding) | Yes     |
| Bridged                                      | Yes      | Yes       | Yes                        | Yes      | Yes                        | Yes     |
| Host‑Only                                    | No       | Yes       | Yes                        | No       | No                         | Yes     |
| Internal (VirtualBox) / LAN Segment (VMware) | No       | No        | No                         | No       | No                         | Yes     |

One Line Summary:
- NAT → VM hides behind host
- Bridged → VM is another machine on the network
- Host-Only → VM talks only to the host and other VMs
- Internal → VM talks only to other VMs

## Conclusion

Virtual machine networking looks complicated because of the names, but the idea behind it is simple. Each mode decides where your VM sits and who it can communicate with. 

Once you understand that, the rest becomes predictable. You don’t need to memorize settings. Just ask the four questions from the beginning. All networking modes are just different combinations of those four questions. Answer those, and the right networking mode becomes obvious.

## References

- [VirtualBox Network Settings: All You Need to Know](https://www.nakivo.com/blog/virtualbox-network-setting-guide/)
- [VirtualBox Networks: In Pictures](https://forums.virtualbox.org/viewtopic.php?t=96608)
- [Different Networking Options in VMware](https://superuser.com/questions/725218/in-vmware-what-are-the-differences-between-the-network-connection-options)
- [VMware Network Modes: A Concise Guide](https://www.linkedin.com/pulse/vmware-network-modes-concise-guide-ssh-access-from-raspberry-zhu-4mijc)
