#!/bin/bash

# Firewall Response Script
# Usage: sudo ./firewall_response.sh <IP_ADDRESS>

if [ "$#" -ne 1 ]; then
    echo "Usage: sudo $0 <IP_ADDRESS>"
    exit 1
fi

IP="$1"

echo "[+] Blocking source IP: $IP"

iptables -A INPUT -s "$IP" -j DROP

echo "[+] Firewall rule added successfully."
echo "[+] Current matching rule:"

iptables -L INPUT -n --line-numbers | grep "$IP"