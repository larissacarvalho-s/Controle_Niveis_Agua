
# ============================================
# Projeto: Controle de Níveis de Água
# Curso: Técnico em Desenvolvimento de Sistemas
# Agenda 11 - Bibliotecas
# ============================================

from colorama import Fore, Style, init

# Inicializa a biblioteca Colorama (garante compatibilidade no terminal Windows e Linux)
init(autoreset=True)

# 1. Lista com os níveis e as situações do reservatório
niveis_agua = [
    "Nível 1 - Muito baixo (CRÍTICO)",
    "Nível 2 - Baixo",
    "Nível 3 - Médio",
    "Nível 4 - Alto",
    "Nível 5 - Muito alto (ALERTA)"
]

# 2. Função que define a cor de cada nível do reservatório
def definir_cor(nivel):
    if nivel == 1:
        return Fore.RED
    elif nivel == 2:
        return Fore.YELLOW
    elif nivel == 3:
        return Fore.GREEN
    elif nivel == 4:
        return Fore.CYAN
    elif nivel == 5:
        return Fore.BLUE
    else:
        return Fore.WHITE

# 3. Função principal para simular o monitoramento e exibir os dados no terminal
print("===================================")
print("   CONTROLE DE NÍVEIS DE ÁGUA")
print("===================================\n")

# Simulação dos níveis do reservatório
for nivel in range(1, 6):
    cor = definir_cor(nivel)
    mensagem = niveis_agua[nivel - 1]

    print(cor + mensagem + Style.RESET_ALL)

print("\nMonitoramento finalizado.")
