from scapy.all import ARP, sniff

def process_packet(packet):
    if packet.haslayer(ARP):
        arp = packet[ARP]
        if arp.op == 2:
            if arp.psrc == "192.168.28.1" and arp.hwsrc != "08:00:27:75:7c:51":
                print("Possível ataque ARP detectado!")
                print(f"ARP original: 192.168.28.1 is-at 08:00:27:75:7c:51")
                print(f"ARP detectado: {arp.psrc} is-at {arp.hwsrc}")

sniff(iface="enp0s8", prn=process_packet, store=0)
