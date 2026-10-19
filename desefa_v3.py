import time
from datetime import datetime

TENTATIVAS_MAX = 3
TEMPO_BLOQUEIO = 300

tentativas_falhas = {}
ips_bloqueados = {}

def registrar_log(ip, status):
    agora = datetime.now().strftime("%d/%m/%y %H:%M:%S")
    mensagem = f"[{agora}] IP: {ip} | STATUS: {status}\n"

    with open("ataques.log", "a") as arquivo:
        arquivo.write(mensagem)

    print(f"LOG: {mensagem.strip()}")

def verificar_bloqueados(ip):
    if ip in ips_bloqueados:
        tempo_passado = time.time() - ips_bloqueados [ip]
        if tempo_passado < TEMPO_BLOQUEIO:
            restante = int (TEMPO_BLOQUEIO - tempo_passado)
            print(f"IP {ip} bloqueado! Faltam {restante}s")
            return True
        else:
            del ips_bloqueados[ip]
            tentativas_falhas [ip] = 0
            print(f"IP {ip} liberado automaticamente")
            registrar_log(ip, "LIBERADO_AUTOMATICO")
            return False
    return False

def login(ip, senha_correta=False):
    if verificar_bloqueados(ip):
        registrar_log(ip, "TENTATIVAS_BLOQUEADOS")
        return False
    if senha_correta:
        tentativas_falhas[ip] = 0
        print(f"Login ok para {ip}")
        registrar_log(ip, "LOGIN_SUCESSO")
        return True
    else:
        if ip not in tentativas_falhas:
            tentativas_falhas[ip] = 0
        tentativas_falhas[ip] += 1

        print(f"Falha {tentativas_falhas[ip]}/{TENTATIVAS_MAX} para {ip}")
        registrar_log(ip, f"FALHA_{tentativas_falhas[ip]}")

        if tentativas_falhas[ip] >= TENTATIVAS_MAX:
            ips_bloqueados[ip] = time.time()
            print(f"!!! IP {ip} BVLOQUEADO por {TEMPO_BLOQUEIO}s")
            registrar_log(ip, "BLOQUEADO")
        return False
print("=== TESTE SISTEMA DEFESA V3.0 ===")
login("192.168.0.10")
login("192.168.0.10")
login("192.168.0.10")
login("192.168.0.10")


