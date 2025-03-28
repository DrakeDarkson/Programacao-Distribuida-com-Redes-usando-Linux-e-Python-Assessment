from scapy.all import sniff

def packet_callback(packet):
    print(packet.summary())

print("Capturando pacotes...")
sniff(prn=packet_callback, store=False)
