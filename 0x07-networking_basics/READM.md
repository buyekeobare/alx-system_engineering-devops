# 0x07.Networking Basic #0

## Learning objectives

> 1. OSI MODEL
> 2. What is LAN
> 3. What is WAN
> 4. What is the Internet
> 5. TCP/UDP

## OSI MODEL

> The OSI (Open Systems Interconnection) model is a conceptual framework that characterizes the communication functions of a telecommunication system without regard to their underlying internal structure and technology. It standardardizes the functions of a telecommunication system or computing system into seven distint layers.

> The model is a guide for understanding how different network protocols and technologies interact to enable communication between networked devices. 

> Each layer in the OSI model has a specific set of functions and responsibilities. They are organized from the lowest to the highest level, with each layer building upon the services provided by the layers below it.

### These layers include (from lowest to highest):

> - Physical Layer
> - Data link Layer
> - Network Layer
> - Tranport Layer
> - Session Layer
> - Presentation Layer
> - Application Layer

## LAN

> LAN is Local Area Network. It is a computer network that interconnects computers, printers, servers, e.t.c within a limited area, such as a home, laboratory, school or campus or office building. 

> A LAN is designed to facilitate communication and resource sharing between devices in close proximity.

## WAN

> WAN is Wide Area Network. It is a telecommunications network that extends over a large geographic area, transmitting data over long distances, and between different networks.

> WANS are designed to facilitate communication between widely distributed locations. 

> The main difference between LANs and WANs is that LANs are confined to a limited area, while WANs cover a wide geographic region, such as cities, countries, or even continents. LANs connect local devices together, WANs connect LANs and other types of networks together so that users and computers in one location can communicate with users and computers in other locations.

## What is the Internet?

> The Internet is a global system of interconnected computer networks that uses the Internet protocol suite TCP/IP to communicate between networks and devices. It is a network of netwroks that consists of millions of private, public, academic, business, and government networks that are linked together using various technologies. It allows users to share and access information, communicate with others, and engage in various online activities like browsing websites, sending emails, and streaming videos.

## What is an IP address

> An IP (Internet Protocol) address is a unique numerical label assigned to each device connected to a computer network. In simple terms, is to devices connected to a network what postal address is to houses. It serves as an identifier for that device, allowing it to communicate with other devices over the Internet. IP addresses are used to route data packets between different devices and networks. 

### There are two main versions of IP addresses in use today: IPv4 and IPv6.

- IPv4 (Internet Protocol version 4): This IP is the most widely used version of IP addresses. It has four sets of numbers, separated by periods (e.g., 192.168.0.1). Each set can range from 0 to 255, providing a total of approximately 4.3 billion unique addresses. However, the availability of IPv4 address is becoming limited due to the growing number of connected devices to the Internet.

- IPv6 (Internet Protocol version 6): IPv6 was developed to address the limitations of IPv4 and provide a larger address space. It has eight groups of four hexadecimal digits, separated by colons (e.g., 2001:0db8:85a3:0000:0000:8a2e:0370:7334). This gives room to a significantly larger number of unique addresses, ensuring that the increasing number of devices can be connected to the Internet.

## TCP/UDP

> TCP (Transmission Control Protocol) and UDP (User Datagram Protocol) are two transport layer protocols used for data transmission over IP networks.

> TCP is a connection-oriented protocol that provides reliable, ordered, and error-checked delivery of data packets. It establishes a connection between the sender and receiver before transmitting data and ensures that packets are delivered in the correct order. TCP also performs flow control and congestion control to manage the rate of data transmission.

> UDP is a connectionless protocol that provides a simple method for sending data packets without establishing a direct connection. Unlike TCP, UDP does not guarantee reliable delivery or packet ordering. It is often used for applications where speed and efficiency are more important than reliability, such as real-time streaming and online gaming.

> The main difference between TCP and UDP lies in their reliability and connection management. TCP is reliable and ensures that data is delivered in the correct order without errors. It establishes a connection, performs error checking, and retransmits lost packets. UDP, on the other hand, does not provide reliability mechanisms. It does not establish a connection and does not guarantee ordered or error-free delivery of packets. UDP is faster and more lightweight than TCP but sacrifices reliability.

## What is a localhost?

> Localhost is a hostname that refers to the current device or computer that you are using. It is used to access the network services running on the same device. When you access "localhost" in a web browser or use it in network communications, you are referring to the device you are currently using. It is often used for testing and development purposes.

## What is a subnet?

> A subnet (short for subnetwork) is a division of an IP network into smaller, logically separate networks. It helps in managing and organizing IP addresses within a larger network. By creating subnets, network administrators can control network traffic, improve security, and efficiently allocate IP addresses. Each subnet has its own range of IP addresses and can be treated as an independent network within the larger network infrastructure.

## Port

> In networking, a port is a communication endpoint associated with a specific process or service on a device. It is identified by a unique number ranging from 0 to 65535. Ports allow multiple applications to use the same IP address on a device by distinguishing between different services. For example, web servers typically use port 80 for HTTP and port 443 for HTTPS.

## Tool/protocol to check device connectivity

> A commonly used tool/protocol to check if a device is connected to a network is the ICMP (Internet Control Message Protocol) Echo Request/Echo Reply, which is commonly known as "ping." By sending an ICMP Echo Request packet to a device's IP address, you can determine if the device is reachable and responsive. If the device is connected and functioning properly, it will send an ICMP Echo Reply packet back to the sender.
