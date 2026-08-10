# Network-Based Intrusion Detection System
## Technical Project Report

---

## 1. Introduction

This project implements a Network-Based Intrusion Detection System (NIDS) using Suricata in an isolated virtualized laboratory environment.

The system was developed using two Kali Linux virtual machines running under VirtualBox. One virtual machine was used as the attacker/test system, while the second virtual machine operated as the Intrusion Detection System.

The IDS monitors network traffic, applies custom detection rules, generates security alerts, and provides a firewall-based response mechanism using `iptables`.

---

## 2. Project Objectives

The main objectives of this project were to:

- Deploy a network-based intrusion detection system.
- Monitor network traffic continuously.
- Configure custom Suricata detection rules.
- Detect suspicious network activity.
- Generate and analyze security alerts.
- Record detected events in Suricata logs.
- Implement a defensive response mechanism.
- Validate the detection and response process in an isolated laboratory.

---

## 3. Laboratory Environment

The project was implemented using the following environment:

| Component | Configuration |
|---|---|
| Virtualization Platform | VirtualBox |
| IDS Operating System | Kali Linux |
| Attacker Operating System | Kali Linux |
| IDS IP Address | `192.168.139.130` |
| Attacker IP Address | `192.168.139.128` |
| IDS Software | Suricata 8.0.6 |
| Firewall | iptables |
| Detection Protocol | ICMP |

The two virtual machines were connected through an isolated virtual network.

---

## 4. Network Architecture

The laboratory consisted of an attacker machine and an IDS machine.


┌─────────────────────────────┐
│       Kali Attacker         │
│       192.168.139.128       │
└──────────────┬──────────────┘
               │
               │ ICMP Traffic
               │
               ▼
┌─────────────────────────────┐
│          Kali IDS           │
│       192.168.139.130       │
│                             │
│         Suricata            │
│       Detection Engine      │
└──────────────┬──────────────┘
               │
               ▼
       Security Alert
               │
               ▼
          iptables
       Firewall Response
5. Suricata Deployment

Suricata was installed and configured on the Kali Linux IDS machine.

The configuration was validated using:

sudo suricata -T -c /etc/suricata/suricata.yaml

The configuration test successfully completed with:

Configuration provided was successfully loaded.

Suricata was then executed in live monitoring mode using the appropriate network interface.

Example:

sudo suricata -c /etc/suricata/suricata.yaml -i <interface> -l /var/log/suricata

The -i option specifies the network interface to monitor, while -l specifies the logging directory.

6. Custom Detection Rule

A custom Suricata rule was created in:

rules/local.rules

The rule used in the project was:

alert icmp any any -> $HOME_NET any (msg:"LOCAL ICMP Traffic Detected"; sid:1000001; rev:1;)
Rule Components
Component	Purpose
alert	Generates an IDS alert
icmp	Detects ICMP traffic
any	Allows any source address/port
$HOME_NET	Represents the protected network
msg	Defines the alert message
sid	Unique rule identifier
rev	Rule revision

This rule was designed to detect ICMP traffic directed toward the protected network.

7. Network Connectivity Testing

Before testing the IDS, connectivity between the two virtual machines was verified.

The attacker machine used:

192.168.139.128

The IDS machine used:

192.168.139.130

The following command was executed from the attacker machine:

ping 192.168.139.130

Successful replies confirmed that the two virtual machines could communicate across the virtual network.

8. Intrusion Detection Testing

After confirming network connectivity, ICMP traffic was generated from the attacker machine.

Command:

ping 192.168.139.130

Suricata continuously monitored the network interface.

The configured rule detected the ICMP traffic and generated the following alert:

LOCAL ICMP Traffic Detected

This confirmed that the custom Suricata detection rule was functioning correctly.

9. Alert Logging

Suricata records detected security events in its logging system.

The primary logs used during testing were:

/var/log/suricata/fast.log
/var/log/suricata/eve.json
fast.log

Provides human-readable security alerts and was used to verify the custom ICMP detection.

eve.json

Provides structured JSON-based event information that can be used for further analysis, automation, or integration with SIEM platforms.

10. Firewall-Based Response

A response mechanism was implemented using the Linux iptables firewall.

After detecting the test traffic, the source IP address of the attacker machine was blocked using:

sudo iptables -A INPUT -s 192.168.139.128 -j DROP

This firewall rule blocks incoming traffic originating from:

192.168.139.128

After applying the rule, communication between the attacker and IDS was interrupted.

This demonstrated how an IDS detection can be followed by a defensive firewall response.

11. Restoring Connectivity

After completing the controlled test, the firewall rule was removed:

sudo iptables -D INPUT -s 192.168.139.128 -j DROP

Connectivity was then tested again using:

ping 192.168.139.130

Normal communication was restored successfully.

12. Detection and Response Workflow

The complete demonstrated workflow was:

          Network Traffic
                │
                ▼
       ┌─────────────────┐
       │     Suricata    │
       │   IDS Engine    │
       └────────┬────────┘
                │
                ▼
        Custom Rule Match
                │
                ▼
          IDS Alert
                │
                ▼
       Security Analysis
                │
                ▼
      ┌──────────────────┐
      │     iptables     │
      │ Firewall Response│
      └────────┬─────────┘
               │
               ▼
       Source IP Blocked
13. Results

The implementation successfully demonstrated the following:

Successful deployment of Suricata as a network-based IDS.
Successful validation of the Suricata configuration.
Continuous monitoring of network traffic.
Successful creation and loading of a custom detection rule.
Successful detection of ICMP traffic.
Successful generation of Suricata alerts.
Successful logging of security events.
Successful firewall-based blocking of the test source IP.
Successful restoration of connectivity after removing the firewall rule.
14. Evidence

The repository contains screenshots documenting the major stages of the implementation.

Suggested evidence includes:

Network connectivity between the attacker and IDS.
Suricata detecting ICMP traffic.
Suricata alert appearing in the log.
Firewall rule being applied.
Attacker traffic being blocked.
Firewall rule being removed.
Network connectivity being restored.
15. Limitations

This project was developed as an educational cybersecurity laboratory.

The demonstrated Suricata detection rule specifically focuses on ICMP traffic. The firewall response was manually initiated as part of the controlled testing process rather than being automatically triggered by Suricata.

The project therefore represents a foundational IDS implementation rather than a complete enterprise SOC or automated incident-response platform.

16. Future Improvements

The system can be extended with:

Additional Suricata detection signatures.
Port-scan detection.
Brute-force detection.
HTTP attack detection.
DNS anomaly detection.
Automated alert-to-firewall response.
Real-time dashboards.
SIEM integration.
Centralized security logging.
Automated incident-response workflows.
Threat intelligence integration.
Machine-learning-based anomaly detection.
17. Security Considerations

All testing was performed within an isolated virtual laboratory using systems controlled by the project author.

The project is intended for educational and defensive cybersecurity purposes.

The firewall response should only be applied to authorized systems and controlled laboratory environments unless appropriate authorization has been obtained.

18. Conclusion

The project successfully demonstrated the fundamental operation of a Network-Based Intrusion Detection System using Suricata.

A virtualized laboratory was created using two Kali Linux machines. Network traffic was monitored by Suricata, a custom ICMP detection rule generated security alerts, and detected traffic was recorded in Suricata logs.

A firewall-based response mechanism using iptables was also demonstrated by blocking the source IP address and subsequently restoring connectivity.

Overall, the project provided practical experience in network monitoring, IDS configuration, security alert analysis, and defensive incident response.