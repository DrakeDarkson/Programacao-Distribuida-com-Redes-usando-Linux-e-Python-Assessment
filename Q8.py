from scapy.all import *
import threading

def capturar_pacotes(interface):
    print(f"Iniciando captura de pacotes na interface: {interface}")
    sniff(iface=interface, prn=analisar_pacote, store=0)

def analisar_pacote(pacote):
    print(f"\nPacote Capturado: {pacote.summary()}")
    
    if pacote.haslayer(IP):
        ip_origem = pacote[IP].src
        ip_destino = pacote[IP].dst
        print(f"IP de Origem: {ip_origem} -> IP de Destino: {ip_destino}")
        
    if pacote.haslayer(TCP):
        print(f"Porta de Origem: {pacote[TCP].sport} -> Porta de Destino: {pacote[TCP].dport}")

    if pacote.haslayer(IP):
        pacote[IP].src = "192.168.1.100"
        print("Alterando IP de origem para 192.168.1.100")
        send(pacote)

def injetar_pacote():
    pacote = IP(dst="8.8.8.8")/ICMP()
    print("Injetando pacote ICMP para 8.8.8.8")
    send(pacote)

if __name__ == "__main__":
    captura_thread = threading.Thread(target=capturar_pacotes, args=("enp0s3",))
    captura_thread.start()

    injetar_pacote()

    captura_thread.join()
