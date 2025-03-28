import nmap
import asyncio

def scan_sync(host, ports):
    """
    Realiza uma varredura síncrona nas portas especificadas.
    """
    nm = nmap.PortScanner()
    print(f"Escaneando {host} de forma síncrona...")
    nm.scan(host, ports, arguments="-T4")
    
    for host in nm.all_hosts():
        print(f"\nHost: {host} ({nm[host].hostname()})")
        print(f"Status: {nm[host].state()}")
        for proto in nm[host].all_protocols():
            print(f"\nProtocolo: {proto}")
            ports = nm[host][proto].keys()
            for port in sorted(ports):
                print(f"Porta {port}: {nm[host][proto][port]['state']}")

async def scan_async(host, ports):
    """
    Realiza uma varredura assíncrona nas portas especificadas.
    """
    loop = asyncio.get_event_loop()
    nm = nmap.PortScannerAsync()
    
    def callback_result(host, scan_result):
        print(f"\n[ASSÍNCRONO] Resultados para {host}:")
        for proto in scan_result.get(host, {}).get('tcp', {}):
            state = scan_result[host]['tcp'][proto]['state']
            print(f"Porta {proto}: {state}")

    print(f"\nEscaneando {host} de forma assíncrona...")
    nm.scan(host, ports, arguments="-T4", callback=callback_result)

    while nm.still_scanning():
        await asyncio.sleep(1)

async def main():
    target_host = "scanme.nmap.org"
    target_ports = "22,80,443"

    scan_sync(target_host, target_ports)

    await scan_async(target_host, target_ports)

if __name__ == "__main__":
    asyncio.run(main())
