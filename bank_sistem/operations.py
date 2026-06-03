def ver_saldo(usuario_logado):
    print(f"Saldo atual: R${usuario_logado['saldo']:.2f}")
    return

def depositar(usuario_logado):
    while True:
        valor_deposito = input("Digite o valor a ser depositado ou x para sair da tela de depósito: ")
        if valor_deposito.lower() == "x":
            print("Voltando a tela principal...")
            return
        try:
            valor_deposito = float(valor_deposito)
            if valor_deposito <= 0:
                print("Valor inválido. Por favor, digite um valor positivo.")
                continue
            
            else:
                usuario_logado['saldo'] += valor_deposito
                print(f"Depósito de R${valor_deposito:.2f} realizado com sucesso!")
                return
            
        except ValueError:
            print("Valor inválido. Por favor, digite um número válido.")
            continue

def sacar(usuario_logado):
    while True:
        valor_saque = input("Digite o valor a ser sacado ou x para sair da tela de saque: ")
        if valor_saque.lower() == "x":
            print("Voltando a tela principal...")
            return
        try:
            valor_saque = float(valor_saque)
            if valor_saque <= 0:
                print("Valor inválido. Por favor, digite um valor positivo.")
                continue
            
            elif valor_saque > usuario_logado['saldo']:
                print("Saldo insuficiente. Por favor, digite um valor menor ou igual ao seu saldo atual.")
                continue
            
            else:
                usuario_logado['saldo'] -= valor_saque
                print(f"Saque de R${valor_saque:.2f} realizado com sucesso!")
                return
            
        except ValueError:
            print("Valor inválido. Por favor, digite um número válido.")
            continue