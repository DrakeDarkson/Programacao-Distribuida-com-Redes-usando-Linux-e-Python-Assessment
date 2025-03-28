import requests
import time

ALVO = "http://google.com"
WORDLIST = ["admin", "login", "dashboard", "config", "backup", "database", "test", "dev", "api", "hidden"]
METODOS = ["GET", "POST"]
TIMEOUT = 5

def fuzzing_web(alvo, wordlist, metodos):
    print(f"Iniciando fuzzing em {alvo}\n")
    resultados = []

    for palavra in wordlist:
        for metodo in metodos:
            url = f"{alvo}/{palavra}"
            try:
                resposta = requests.request(metodo, url, timeout=TIMEOUT)
                status = resposta.status_code
                tamanho_resposta = len(resposta.text)

                if status in [200, 301, 302, 403, 500]:
                    resultado = f"[{metodo}] {url} -> Status: {status}, Tamanho: {tamanho_resposta} bytes"
                    print(resultado)
                    resultados.append(resultado)

            except requests.exceptions.RequestException as e:
                print(f"[-] Erro ao acessar {url}: {e}")

            time.sleep(0.5)

    with open("fuzzing_resultados.txt", "w") as f:
        f.write("\n".join(resultados))

    print("\n🔹 Fuzzing concluído! Resultados salvos em 'fuzzing_resultados.txt'.")

if __name__ == "__main__":
    fuzzing_web(ALVO, WORDLIST, METODOS)
