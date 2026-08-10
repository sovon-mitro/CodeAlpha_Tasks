# Network-Based Intrusion Detection System Using Suricata

![Platform](https://img.shields.io/badge/Platform-Kali%20Linux-blue)
![IDS](https://img.shields.io/badge/IDS-Suricata-orange)
![Virtualization](https://img.shields.io/badge/Virtualization-VirtualBox-green)
![License](https://img.shields.io/badge/License-MIT-yellow)

## Overview

This project implements a **Network-Based Intrusion Detection System (NIDS)** using **Suricata** in an isolated VirtualBox laboratory environment.

The system uses two Kali Linux virtual machines:

- One machine acts as the **attacker/test system**.
- The second machine acts as the **IDS monitoring system**.

Suricata monitors network traffic, applies custom detection rules, generates security alerts, and records detected events. A firewall-based response mechanism using `iptables` is also demonstrated to block a suspicious source IP.

---

## Objectives

The project was developed to:

- Deploy a network-based intrusion detection system.
- Monitor network traffic continuously.
- Configure custom Suricata detection rules.
- Detect suspicious ICMP traffic.
- Generate and analyze IDS alerts.
- Record security events in Suricata logs.
- Implement a firewall-based response mechanism.
- Validate the detection and response process in an isolated environment.

---

## Architecture

```text
┌─────────────────────────────┐
│       Kali Attacker         │
│       192.168.139.128       │
└──────────────┬──────────────┘
               │
               │ ICMP Traffic
               ▼
┌─────────────────────────────┐
│          Kali IDS           │
│       192.168.139.130       │
│                             │
│         Suricata            │
│      Detection Engine       │
└──────────────┬──────────────┘
               │
               ▼
         IDS Alert
               │
               ▼
          iptables
       Firewall Response
Technologies
Technology	Purpose
Kali Linux	IDS and attacker/test environments
Suricata 8.0.6	Network intrusion detection
VirtualBox	Virtualized laboratory
iptables	Firewall-based response
ICMP/Ping	Traffic generation and testing
JSON Logging	Structured security event logging
Lab Configuration
IDS Machine
Operating System: Kali Linux
IP Address: 192.168.139.130
Role: Network Intrusion Detection System
Attacker/Test Machine
Operating System: Kali Linux
IP Address: 192.168.139.128
Role: Traffic Generation / Security Testing

Both systems were connected through an isolated VirtualBox network.

Project Structure
Network-Intrusion-Detection/
│
├── README.md
├── LICENSE
├── .gitignore
│
├── rules/
│   └── local.rules
│
├── scripts/
│   └── firewall_response.sh
│
├── screenshots/
│   ├── 01-normal-connectivity.png
│   ├── 02-suricata-alert.png
│   ├── 03-firewall-block.png
│   ├── 04-blocked-ping.png
│   └── 05-connectivity-restored.png
│
└── report/
    └── IDS_Report.md
Suricata Configuration
Configuration Validation

Before starting the IDS, the Suricata configuration was tested using:

sudo suricata -T -c /etc/suricata/suricata.yaml

A successful configuration produced:

Configuration provided was successfully loaded.
Custom Detection Rule

The project uses a custom Suricata rule located in:

rules/local.rules

Rule:

alert icmp any any -> $HOME_NET any (msg:"LOCAL ICMP Traffic Detected"; sid:1000001; rev:1;)
Rule Breakdown
Field	Description
alert	Generates a security alert
icmp	Monitors ICMP traffic
any	Accepts any source
$HOME_NET	Protected network
msg	Alert description
sid	Unique rule identifier
rev	Rule revision
Running the IDS

Start Suricata using the network interface connected to the laboratory network:

sudo suricata -c /etc/suricata/suricata.yaml -i <interface> -l /var/log/suricata

Replace <interface> with the appropriate network interface.

The interface can be identified using:

ip -br addr
Testing
1. Verify Connectivity

From the attacker machine:

ping 192.168.139.130

Successful replies confirm connectivity between the two virtual machines.

2. Generate Test Traffic

ICMP traffic was generated using:

ping 192.168.139.130

Suricata monitors the traffic and applies the custom ICMP detection rule.

3. Verify the Alert

Suricata records human-readable alerts in:

/var/log/suricata/fast.log

The expected alert is:

LOCAL ICMP Traffic Detected

Example command:

sudo tail -n 20 /var/log/suricata/fast.log
4. Structured Security Events

Suricata also generates structured event information in:

/var/log/suricata/eve.json

Example:

sudo tail -n 5 /var/log/suricata/eve.json

The JSON event format can be used for further analysis or integration with SIEM systems.

Firewall Response

A controlled firewall response was demonstrated using iptables.

To block the attacker/test machine:

sudo iptables -A INPUT -s 192.168.139.128 -j DROP

The rule blocks incoming traffic from:

192.168.139.128

After applying the firewall rule, connectivity from the attacker machine was interrupted.

Restoring Connectivity

The firewall rule can be removed using:

sudo iptables -D INPUT -s 192.168.139.128 -j DROP

Connectivity can then be verified again:

ping 192.168.139.130
Response Workflow
Network Traffic
      │
      ▼
   Suricata
      │
      ▼
Detection Rule
      │
      ▼
   IDS Alert
      │
      ▼
Security Response
      │
      ▼
   iptables
      │
      ▼
Source IP Blocked
Evidence

The project includes screenshots demonstrating the implementation:

1. Normal Connectivity

Demonstrates successful communication between the attacker and IDS machines.

2. Suricata Detection

Demonstrates Suricata detecting ICMP traffic and generating:

LOCAL ICMP Traffic Detected
3. Firewall Response

Demonstrates the firewall rule used to block the test source IP.

4. Blocked Traffic

Demonstrates that communication was interrupted after the firewall rule was applied.

5. Restored Connectivity

Demonstrates successful communication after removing the firewall rule.

Results

The project successfully demonstrated:

Network-based IDS deployment.
Continuous network traffic monitoring.
Custom Suricata rule configuration.
ICMP traffic detection.
Security alert generation.
Security event logging.
Firewall-based response.
Source IP blocking.
Restoration of network connectivity.
Limitations

This project is an educational implementation conducted in an isolated virtual laboratory.

The current detection rule focuses specifically on ICMP traffic. The firewall response was manually initiated during controlled testing rather than automatically triggered by Suricata.

It should therefore be considered a foundational IDS implementation rather than a complete enterprise intrusion detection and automated response platform.

Future Improvements

Potential improvements include:

Additional Suricata signatures.
Port-scan detection.
Brute-force attack detection.
HTTP attack detection.
DNS anomaly detection.
Automated firewall response.
Real-time dashboards.
SIEM integration.
Centralized log management.
Threat intelligence integration.
Machine-learning-based anomaly detection.
Security Disclaimer

This project was developed and tested in an isolated virtual laboratory using systems controlled by the project author.

It is intended for educational and defensive cybersecurity purposes only.

Do not use the techniques demonstrated in this project against systems or networks without appropriate authorization.

Author

Sovon Mitro

Computer Science and Engineering

This project was developed as part of a cybersecurity internship project.


