from scapy.all import *

def escanear_porta(ip, porta):
    pacote = IP(dst=ip)/TCP(dport=porta, flags="S")
    resposta = sr1(pacote, timeout=1, verbose=0)

    if resposta is None:
        print(f"Porta {porta} no {ip} está FILTRADA (sem resposta).")
    elif resposta.haslayer(TCP):
        if resposta[TCP].flags == 0x12:
            print(f"Porta {porta} no {ip} está ABERTA.")
            send(IP(dst=ip)/TCP(dport=porta, flags="R"), verbose=0)
        elif resposta[TCP].flags == 0x14:
            print(f"Porta {porta} no {ip} está FECHADA.")
    else:
        print(f"Resposta inesperada para a porta {porta} no {ip}.")

def escanear_portas(ip, portas):
    for porta in portas:
        escanear_porta(ip, porta)

if __name__ == "__main__":
    ip_destino = input("Digite o IP de destino: ")
    portas = [21, 22, 23, 80, 443, 8080]
    print(f"Iniciando escaneamento de portas no host {ip_destino}...")
    escanear_portas(ip_destino, portas)
