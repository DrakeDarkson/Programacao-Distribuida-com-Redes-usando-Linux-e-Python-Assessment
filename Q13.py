import dns.resolver

def consulta_dns(dominio):
    print(f"Consultando informações DNS para {dominio}\n")

    registros = ["A", "MX", "NS", "TXT"]

    for reg in registros:
        try:
            resposta = dns.resolver.resolve(dominio, reg)
            for rdata in resposta:
                print(f"{reg}: {rdata}")
        except dns.resolver.NoAnswer:
            print(f"{reg}: Nenhuma resposta")
        except dns.resolver.NXDOMAIN:
            print("Domínio não encontrado")
            return
        except dns.resolver.LifetimeTimeout:
            print("Tempo limite excedido")

def enumera_subdominios(dominio):
    print(f"\nEnumerando subdomínios para {dominio}\n")

    subdominios_comuns = ["www", "mail", "ftp", "blog", "api", "dev", "test"]
    
    for sub in subdominios_comuns:
        subdominio = f"{sub}.{dominio}"
        try:
            resposta = dns.resolver.resolve(subdominio, "A")
            for rdata in resposta:
                print(f"Subdomínio encontrado: {subdominio} -> {rdata}")
        except (dns.resolver.NoAnswer, dns.resolver.NXDOMAIN, dns.resolver.LifetimeTimeout):
            pass

if __name__ == "__main__":
    dominio_alvo = "exemplo.com"
    consulta_dns(dominio_alvo)
    enumera_subdominios(dominio_alvo)
