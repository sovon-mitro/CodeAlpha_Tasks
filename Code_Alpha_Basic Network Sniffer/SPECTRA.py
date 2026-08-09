from scapy.all import sniff, IP, TCP, UDP, ICMP, Raw
from datetime import datetime


# Packet counters
total_packets = 0
ip_packets = 0
tcp_packets = 0
udp_packets = 0
icmp_packets = 0
other_packets = 0

# Store packets so we can inspect them after capture
captured_packets = []


print()
print("+" + "-" * 71 + "+")
print("|" + "SPECTRA".center(71) + "|")
print("|" + "Systematic Packet Examination & Communication Traffic Research Analyzer".center(58) + "|")
print("+" + "-" * 71 + "+")
print()


# Ask the user which protocol they want to capture
protocol_filter = input(
    "Protocol filter [ALL/TCP/UDP/ICMP]: "
).strip().upper()

if protocol_filter not in ["ALL", "TCP", "UDP", "ICMP"]:
    print("Invalid protocol. Using ALL.")
    protocol_filter = "ALL"


# Ask whether the user wants to monitor a specific IP
ip_filter = input("IP filter [ALL]: ").strip()

if not ip_filter:
    ip_filter = "ALL"


print("\nActive filters:")
print("  Protocol :", protocol_filter)
print("  IP       :", ip_filter)

print("\nCapturing packets...")
print("Press CTRL+C to stop.\n")


# This function runs whenever Scapy captures a packet
def process_packet(packet):

    global total_packets
    global ip_packets
    global tcp_packets
    global udp_packets
    global icmp_packets
    global other_packets

    total_packets += 1

    # Ignore packets that do not contain an IP layer
    if not packet.haslayer(IP):
        return

    ip_packets += 1

    source_ip = packet[IP].src
    destination_ip = packet[IP].dst

    # Record the time when the packet is processed
    timestamp = datetime.now().strftime("%H:%M:%S")


    # Check which protocol the packet uses
    if packet.haslayer(TCP):

        protocol = "TCP"
        source_port = packet[TCP].sport
        destination_port = packet[TCP].dport

        tcp_packets += 1

    elif packet.haslayer(UDP):

        protocol = "UDP"
        source_port = packet[UDP].sport
        destination_port = packet[UDP].dport

        udp_packets += 1

    elif packet.haslayer(ICMP):

        protocol = "ICMP"
        source_port = "-"
        destination_port = "-"

        icmp_packets += 1

    else:

        protocol = "OTHER"
        source_port = "-"
        destination_port = "-"

        other_packets += 1


    # Ignore the packet if it does not match the protocol filter
    if protocol_filter != "ALL":

        if protocol != protocol_filter:
            return


    # Ignore the packet if it does not match the IP filter
    if ip_filter != "ALL":

        if source_ip != ip_filter and destination_ip != ip_filter:
            return


    # Give the packet a number based on the packets that
    # passed the filters
    packet_number = len(captured_packets) + 1


    # Save the packet and its basic information
    captured_packets.append({
        "number": packet_number,
        "packet": packet,
        "time": timestamp,
        "source_ip": source_ip,
        "destination_ip": destination_ip,
        "protocol": protocol,
        "source_port": source_port,
        "destination_port": destination_port
    })


    # Display the packet in the terminal
    print(
        f"{packet_number:<6}"
        f"{timestamp:<10}"
        f"{source_ip:<18}"
        f"{destination_ip:<18}"
        f"{protocol:<9}"
        f"{str(source_port):<9}"
        f"{str(destination_port):<9}"
    )


# Print the table headings
print(
    f"{'No.':<6}"
    f"{'Time':<10}"
    f"{'Source IP':<18}"
    f"{'Destination IP':<18}"
    f"{'Protocol':<9}"
    f"{'S.Port':<9}"
    f"{'D.Port':<9}"
)

print("-" * 78)


# Start capturing packets.
# prn calls process_packet() for every captured packet.
# store=False prevents Scapy from keeping another copy of packets.
try:

    sniff(
        prn=process_packet,
        store=False
    )

except KeyboardInterrupt:

    # CTRL+C stops sniffing and allows the program
    # to continue to the statistics section.
    print("\n\nPacket capture stopped.")


# Display packet statistics
print()
print("+" + "-" * 42 + "+")
print("|" + "SNIFFER SUMMARY".center(42) + "|")
print("+" + "-" * 42 + "+")

print(f"|  Total packets : {total_packets:<22}|")
print(f"|  IP packets    : {ip_packets:<22}|")
print(f"|  TCP packets   : {tcp_packets:<22}|")
print(f"|  UDP packets   : {udp_packets:<22}|")
print(f"|  ICMP packets  : {icmp_packets:<22}|")
print(f"|  Other packets : {other_packets:<22}|")

print("+" + "-" * 42 + "+")


# Let the user inspect individual packets
if not captured_packets:

    print("\nNo packets matched your filters.")

else:

    print(
        f"\n{len(captured_packets)} "
        "packets are available for inspection."
    )

    while True:

        choice = input(
            "\nEnter packet number to inspect "
            "(or Q to quit): "
        ).strip()


        if choice.upper() == "Q":

            print("\nProgram finished.")
            break


        # Check that the user entered a number
        if not choice.isdigit():

            print("Please enter a valid packet number.")
            continue


        packet_number = int(choice)


        # Check whether the packet number exists
        if packet_number < 1 or packet_number > len(captured_packets):

            print("Packet number not found.")
            continue


        # Get the selected packet
        selected = captured_packets[packet_number - 1]
        packet = selected["packet"]


        # Display the selected packet's information
        print()
        print("+" + "-" * 50 + "+")
        print("|" + "PACKET DETAILS".center(50) + "|")
        print("+" + "-" * 50 + "+")

        print(f"| Packet Number    : {selected['number']:<25}|")
        print(f"| Time             : {selected['time']:<25}|")
        print(f"| Source IP        : {selected['source_ip']:<25}|")
        print(f"| Destination IP   : {selected['destination_ip']:<25}|")
        print(f"| Protocol         : {selected['protocol']:<25}|")
        print(f"| Source Port      : {str(selected['source_port']):<25}|")
        print(f"| Destination Port : {str(selected['destination_port']):<25}|")


        # Check whether the packet contains a Raw payload
        if packet.haslayer(Raw):

            payload = packet[Raw].load

            print(f"| Payload Size     : {len(payload)} bytes")


            # Convert the payload into hexadecimal
            payload_hex = " ".join(
                f"{byte:02x}"
                for byte in payload[:500]
            )

            print("+" + "-" * 50 + "+")
            print("Payload (Hex):")
            print(payload_hex)


            # Convert printable bytes into normal characters.
            # Non-printable bytes are replaced with dots.
            payload_ascii = "".join(
                chr(byte) if 32 <= byte <= 126 else "."
                for byte in payload[:500]
            )

            print()
            print("Payload (ASCII):")
            print(payload_ascii)

        else:

            print("| Payload          : None")
            print("+" + "-" * 50 + "+")

        print()