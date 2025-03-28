import pcapy
from scapy.all import Ether, IP, UDP, sendp
import time

def listar_interfaces():
    interfaces = pcapy.findalldevs()
    print("Interfaces disponíveis:")
    for i, iface in enumerate(interfaces):
        print(f"{i + 1}. {iface}")
    return interfaces

def capturar_pacotes(interface):
    cap = pcapy.open_live(interface, 65536, 1, 0)
    print(f"Capturando pacotes na interface: {interface}...")
    
    while True:
        header, packet = cap.next()
        if header:
            print(f"Pacote capturado! Tamanho: {header.getlen()} bytes")

def injetar_pacote(interface):
    print(f"Injetando pacote na interface: {interface}")

    pacote = Ether()/IP(dst="192.168.1.1")/UDP(dport=53)/b"Teste de pacote"
    sendp(pacote, iface=interface, verbose=True)
    print("Pacote injetado, aguardando captura...")

if __name__ == "__main__":
    interfaces = listar_interfaces()
    if interfaces:
        interface = interfaces[0]
        injetar_pacote(interface)
        time.sleep(2)
        capturar_pacotes(interface)
    else:
        print("Nenhuma interface disponível.")
