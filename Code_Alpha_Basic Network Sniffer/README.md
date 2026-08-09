# SPECTRA

## Systematic Packet Examination & Communication Traffic Research Analyzer

SPECTRA is a basic network packet sniffer and analyzer developed using Python and Scapy.

The purpose of this project is to capture network traffic, identify common network protocols, display information about communicating hosts, and allow individual packets to be inspected.

This project was developed to understand the basics of network traffic, packet structure, protocols, ports, and payload data.

---

## Table of Contents

- [Overview](#overview)
- [Features](#features)
- [How It Works](#how-it-works)
- [Technologies Used](#technologies-used)
- [Project Structure](#project-structure)
- [Requirements](#requirements)
- [Installation](#installation)
- [Windows Packet Capture Setup](#windows-packet-capture-setup)
- [Running the Program](#running-the-program)
- [Using the Protocol Filter](#using-the-protocol-filter)
- [Using the IP Filter](#using-the-ip-filter)
- [Understanding the Output](#understanding-the-output)
- [Packet Capture](#packet-capture)
- [Packet Statistics](#packet-statistics)
- [Packet Inspection](#packet-inspection)
- [Payload Analysis](#payload-analysis)
- [Example Workflow](#example-workflow)
- [How the Code Works](#how-the-code-works)
- [Why TCP, UDP and ICMP Matter](#why-tcp-udp-and-icmp-matter)
- [Understanding Ports](#understanding-ports)
- [Learning Outcomes](#learning-outcomes)
- [Limitations](#limitations)
- [Future Improvements](#future-improvements)
- [Security and Privacy Considerations](#security-and-privacy-considerations)
- [Disclaimer](#disclaimer)
- [Author](#author)

---

## Overview

Network communication is divided into packets that travel between devices.

Each packet contains different layers of information. Depending on the protocol being used, a packet can contain information such as:

- Source IP address
- Destination IP address
- Source port
- Destination port
- Protocol information
- Payload data

SPECTRA captures these packets and extracts useful information so that it can be viewed directly from the terminal.

The program currently focuses on:

- IP
- TCP
- UDP
- ICMP
- Raw payload data

---

## Features

### Packet Capture

Captures network packets in real time using Scapy.

### Protocol Detection

Identifies:

- TCP
- UDP
- ICMP
- Other IP protocols

### IP Information

Displays:

- Source IP
- Destination IP

### Port Information

For TCP and UDP packets, the program displays:

- Source port
- Destination port

### Protocol Filtering

The user can choose to capture:

- All supported traffic
- TCP traffic
- UDP traffic
- ICMP traffic

### IP Filtering

The user can provide a specific IP address to monitor traffic involving that address.

### Packet Statistics

After stopping the capture, SPECTRA displays:

- Total packets
- IP packets
- TCP packets
- UDP packets
- ICMP packets
- Other IP packets

### Packet Inspection

Captured packets can be selected by packet number for more detailed analysis.

### Payload Analysis

If a packet contains a Raw payload, SPECTRA displays:

- Payload size
- Hexadecimal representation
- ASCII representation

---

## How It Works

The basic workflow of SPECTRA is:

```text
Start Program
     |
     v
Select Protocol Filter
     |
     v
Select IP Filter
     |
     v
Start Packet Capture
     |
     v
Receive Packet
     |
     v
Check IP Layer
     |
     v
Identify Protocol
     |
     +---- TCP
     |
     +---- UDP
     |
     +---- ICMP
     |
     +---- Other
     |
     v
Apply Filters
     |
     v
Display Packet
     |
     v
Store Packet
     |
     v
CTRL+C
     |
     v
Display Statistics
     |
     v
Inspect Individual Packets
```

When a packet is captured, the program first checks whether it contains an IP layer.

It then determines whether the packet uses TCP, UDP, ICMP, or another IP protocol.

After identifying the protocol, the selected filters are applied.

Packets that match the filters are displayed in the terminal and stored so that they can be inspected after the capture is stopped.

---

## Technologies Used

### Python

Python is used as the main programming language for the project.

### Scapy

Scapy is used to capture and inspect network packets.

Scapy provides access to packet layers and allows information such as IP addresses, ports, protocols, and payloads to be extracted.

---

## Project Structure

The project contains three main files:

```text
SPECTRA/
|
|-- network_sniffer.py
|-- requirements.txt
|-- README.md
```

### network_sniffer.py

Contains the main packet capture, filtering, analysis, and inspection code.

### requirements.txt

Contains the Python libraries required by the project.

### README.md

Contains the project documentation and usage instructions.

---

## Requirements

Before running SPECTRA, make sure the following are available:

- Python 3
- Scapy
- A network interface capable of capturing traffic
- Administrator privileges on Windows may be required

Packet capture permissions depend on the operating system and network configuration.

---

## Installation

### 1. Install Python

Download and install Python 3 from the official Python website:

https://www.python.org/

After installation, verify that Python is available:

```bash
python --version
```

On some systems, use:

```bash
python3 --version
```

### 2. Download the Project

Download or clone the SPECTRA repository.

Using Git:

```bash
git clone https://github.com/sovon-mitro/CodeAlpha_Tasks/tree/main/Code_Alpha_Basic%20Network%20Sniffer
```

Then enter the project directory:

```bash
cd Code_Alpha_Basic Network Sniffer
```

### 3. Install the Required Library

Install Scapy using:

```bash
pip install scapy
```

Or install the dependency listed in `requirements.txt`:

```bash
pip install -r requirements.txt
```

---

## Windows Packet Capture Setup

On Windows, Scapy may require Npcap to capture packets correctly.

Npcap can be downloaded from:

https://npcap.com/

During installation, enabling the option to install Npcap in WinPcap API-compatible mode can be useful for compatibility with applications that rely on the older WinPcap interface.

After installing Npcap, restart the computer if required.

Run the terminal or command prompt with Administrator privileges if packet capture does not work with normal permissions.

---

## Running the Program

Open a terminal in the SPECTRA project directory.

Run:

```bash
python network_sniffer.py
```

On systems where Python is accessed using `python3`:

```bash
python3 network_sniffer.py
```

The program will display the SPECTRA header and ask for filtering options.

Example:

```text
SPECTRA

Systematic Packet Examination & Communication Traffic Research Analyzer

Protocol filter [ALL/TCP/UDP/ICMP]:
```

---

## Using the Protocol Filter

The program asks:

```text
Protocol filter [ALL/TCP/UDP/ICMP]:
```

You can enter:

```text
ALL
```

to capture all supported IP traffic.

You can also enter:

```text
TCP
```

to display TCP packets.

Or:

```text
UDP
```

to display UDP packets.

Or:

```text
ICMP
```

to display ICMP packets.

The filter is not case-sensitive.

For example:

```text
udp
```

will be treated as:

```text
UDP
```

If an invalid protocol is entered, SPECTRA automatically uses `ALL`.

---

## Using the IP Filter

After selecting the protocol, the program asks:

```text
IP filter [ALL]:
```

Entering:

```text
ALL
```

allows packets involving any IP address to be displayed.

To monitor traffic involving a specific IP address, enter the address.

Example:

```text
192.168.0.196
```

The packet will be displayed if that IP address is either:

- The source IP
- The destination IP

---

## Understanding the Output

During packet capture, SPECTRA displays packets in a table.

Example:

```text
No.   Time      Source IP         Destination IP    Protocol  S.Port   D.Port
1     02:15:31  192.168.0.196     142.250.x.x       UDP       60304    443
2     02:15:31  142.250.x.x       192.168.0.196     UDP       443      60304
```

### No.

The packet number assigned by SPECTRA.

### Time

The time when SPECTRA processed the packet.

### Source IP

The IP address that sent the packet.

### Destination IP

The IP address receiving the packet.

### Protocol

The protocol detected in the packet.

Possible values include:

```text
TCP
UDP
ICMP
OTHER
```

### S.Port

The source port.

This is available for TCP and UDP packets.

### D.Port

The destination port.

This is also available for TCP and UDP packets.

---

## Packet Capture

SPECTRA continuously captures packets until the user stops the program.

The terminal displays:

```text
Capturing packets...
Press CTRL+C to stop.
```

Press:

```text
CTRL+C
```

to stop the capture.

The program then moves to the statistics and packet inspection sections.

---

## Packet Statistics

After packet capture is stopped, SPECTRA displays a summary of the captured traffic.

Example:

```text
+------------------------------------------+
|              SNIFFER SUMMARY             |
+------------------------------------------+
|  Total packets : 52                      |
|  IP packets    : 43                      |
|  TCP packets   : 0                       |
|  UDP packets   : 43                      |
|  ICMP packets  : 0                       |
|  Other packets : 0                       |
+------------------------------------------+
```

The statistics provide a quick overview of the traffic observed during the capture session.

### Total packets

The total number of packets received by the packet processing function.

### IP packets

The number of captured packets containing an IP layer.

### TCP packets

The number of IP packets identified as TCP.

### UDP packets

The number of IP packets identified as UDP.

### ICMP packets

The number of IP packets identified as ICMP.

### Other packets

IP packets that do not match TCP, UDP, or ICMP.

---

## Packet Inspection

After the capture is stopped, SPECTRA allows individual captured packets to be inspected.

The program asks:

```text
Enter packet number to inspect (or Q to quit):
```

For example:

```text
15
```

The program searches for packet number 15 and displays its information.

Example:

```text
+--------------------------------------------------+
|                 PACKET DETAILS                   |
+--------------------------------------------------+
| Packet Number    : 15                            |
| Time             : 02:15:42                     |
| Source IP        : 192.168.0.196                |
| Destination IP   : 142.250.x.x                  |
| Protocol         : UDP                           |
| Source Port      : 60304                         |
| Destination Port : 443                           |
```

The user can continue inspecting packets or enter:

```text
Q
```

to exit.

---

## Payload Analysis

Some packets contain a Raw layer containing payload data.

When a Raw payload is available, SPECTRA displays its size.

Example:

```text
Payload Size : 1250 bytes
```

The program then displays the payload in two formats.

### Hexadecimal

Example:

```text
4e 0a f1 d7 a4 10 ac d4 b6 41 a2 1c 4c 2a ed e9
```

Hexadecimal representation allows the raw bytes of the payload to be examined.

### ASCII

The program also attempts to display printable bytes as normal characters.

Example:

```text
N........A..L*..l...J......
```

Bytes that are not printable are represented using:

```text
.
```

Only the first 500 bytes are displayed to prevent extremely large payloads from filling the terminal.

---

## Example Workflow

A typical SPECTRA session can be performed as follows.

### Step 1 — Start the program

```bash
python network_sniffer.py
```

### Step 2 — Select a protocol

Example:

```text
Protocol filter [ALL/TCP/UDP/ICMP]: UDP
```

### Step 3 — Select an IP filter

For all IP addresses:

```text
IP filter [ALL]: ALL
```

Or specify an IP:

```text
IP filter [ALL]: 192.168.0.196
```

### Step 4 — Capture packets

The program begins displaying matching packets.

```text
Capturing packets...
Press CTRL+C to stop.
```

### Step 5 — Stop the capture

Press:

```text
CTRL+C
```

### Step 6 — Review statistics

SPECTRA displays the number of packets captured and their protocol distribution.

### Step 7 — Inspect a packet

Enter a packet number:

```text
Enter packet number to inspect (or Q to quit): 15
```

### Step 8 — Examine the packet

Review:

- Source IP
- Destination IP
- Protocol
- Source port
- Destination port
- Payload size
- Payload data

### Step 9 — Exit

Enter:

```text
Q
```

to finish the program.

---

## How the Code Works

The program uses Scapy's `sniff()` function to capture packets.

The packet processing function is:

```python
def process_packet(packet):
```

Scapy sends every captured packet to this function.

The program first checks whether the packet contains an IP layer:

```python
if not packet.haslayer(IP):
    return
```

Packets without an IP layer are ignored for the main analysis.

The program then extracts:

```python
source_ip = packet[IP].src
destination_ip = packet[IP].dst
```

The protocol is identified by checking the packet layers.

For TCP:

```python
if packet.haslayer(TCP):
```

For UDP:

```python
elif packet.haslayer(UDP):
```

For ICMP:

```python
elif packet.haslayer(ICMP):
```

If none of these protocols are detected, the packet is classified as:

```text
OTHER
```

The selected protocol and IP filters are then applied.

Packets that match the filters are stored in the `captured_packets` list.

The basic packet information is also printed to the terminal.

---

## Why TCP, UDP and ICMP Matter

### TCP

TCP is a connection-oriented protocol.

It provides mechanisms for reliable data delivery and is commonly used by applications such as web services, file transfers, and other network communications.

### UDP

UDP is a connectionless protocol.

It does not provide the same delivery guarantees as TCP, but it has lower overhead and is useful for applications where speed and low latency are important.

### ICMP

ICMP is mainly used for network diagnostics and control messages.

A common example is the ICMP traffic generated by the `ping` command.

---

## Understanding Ports

A port identifies a particular communication endpoint associated with a network service or application.

For example:

```text
Source IP       : 192.168.0.196
Source Port     : 60304

Destination IP  : 142.250.x.x
Destination Port: 443
```

Here, the IP addresses identify the two hosts while the ports identify the communication endpoints.

Port `443` is commonly associated with HTTPS traffic.

However, the presence of a port number alone does not guarantee what application or protocol is actually being used.

---

## Learning Outcomes

This project was developed to gain practical experience with basic network traffic analysis.

Through this project, I learned about:

- Network packet structure
- IP addressing
- Source and destination addresses
- TCP communication
- UDP communication
- ICMP traffic
- Network ports
- Packet payloads
- Packet filtering
- Packet statistics
- Network traffic monitoring
- Python packet processing
- Scapy packet capture

The project also provided practical experience in observing network traffic generated by normal applications and services.

---

## Limitations

SPECTRA is a basic educational network sniffer and is not intended to replace professional packet analysis tools.

Current limitations include:

- The program mainly focuses on IP traffic.
- It does not decode every network protocol.
- It does not reconstruct complete TCP or UDP conversations.
- Encrypted traffic cannot normally be understood simply by displaying its payload.
- It does not currently export packets to PCAP files.
- It does not provide a graphical user interface.
- It does not provide advanced protocol dissections.
- Packet capture capabilities depend on the operating system and network interface.
- Administrator/root privileges may be required.

---

## Future Improvements

Possible future improvements include:

- DNS packet analysis
- HTTP packet analysis
- TCP flag analysis
- MAC address display
- PCAP file export
- Advanced protocol detection
- Packet search functionality
- Traffic statistics by destination
- Real-time traffic graphs
- Graphical user interface
- Connection tracking
- More advanced packet filtering

These features can be added in future versions as the project develops.

---

## Security and Privacy Considerations

Network packets may contain sensitive information depending on the type of traffic being captured.

For this reason, packet capture should only be performed on networks and systems where the user has permission to monitor the traffic.

Encrypted traffic may still appear as captured packets, but the contents are generally not readable without the appropriate decryption context.

The payload displayed by SPECTRA should therefore be treated as potentially sensitive data.

---

## Disclaimer

SPECTRA was created for educational purposes and network security learning.

Only capture and analyze network traffic on systems and networks that you own or have explicit permission to monitor.

Do not use this tool to intercept or analyze traffic from networks or devices without authorization.

The author is not responsible for misuse of this software.

---

## Author

Sovon Mitro

Developed as a Python and network security learning project.

**Project:** SPECTRA  
**Purpose:** Basic Network Packet Capture and Analysis  
**Language:** Python  
**Library:** Scapy
