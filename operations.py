import json
with open('dados.json', 'r', encoding='utf-8') as arquivo:
    dados = json.load(arquivo)

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
                usuario_logado['extrato'].append(f"Depósito: R${valor_deposito:.2f}")
                with open('dados.json', 'w', encoding='utf-8') as arquivo:
                    json.dump(dados, arquivo, ensure_ascii=False, indent=4)
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
                usuario_logado['extrato'].append(f"Saque: R${valor_saque:.2f}")
                with open('dados.json', 'w', encoding='utf-8') as arquivo:
                    json.dump(dados, arquivo, ensure_ascii=False, indent=4)
                return
            
        except ValueError:
            print("Valor inválido. Por favor, digite um número válido.")
            continue

def ver_extrato(usuario_logado):
    if not usuario_logado['extrato']:
        print("Nenhuma transação realizada.")

    else:
        print("Extrato:")
        for transacao in usuario_logado['extrato']:
            print(transacao)
            
    return

def transferir(usuario_logado):
    while True:
        usuario_destino = input("Digite o nome de usuário do destinatário ou x para sair da tela de transferência: ")
        if usuario_destino.lower() == "x":
            print("Voltando a tela principal...")
            return
        
        usuario_destino = usuario_destino.strip()
        if usuario_destino == "":
            print("Nome de usuário inválido. Por favor, digite um nome de usuário válido.")
            continue

        if usuario_destino == usuario_logado['usuario']:
            print("Não é possível transferir para si mesmo. Por favor, digite um nome de usuário diferente.")
            continue

        destinatario_encontrado = None

        for usuario_cadastrado in dados:

            if usuario_cadastrado['usuario'] == usuario_destino:
                destinatario_encontrado = usuario_cadastrado
                break
        
        if not destinatario_encontrado:
            print("Usuário destinatário não encontrado. Por favor, digite um nome de usuário válido.")
            continue
        
        elif destinatario_encontrado:
            while True:
                valor_transferencia = input("Digite o valor a ser transferido ou x para sair da tela de transferência: ")
                if valor_transferencia.lower() == "x":
                    print("Voltando a tela principal...")
                    return
                
                try:
                    valor_transferencia = float(valor_transferencia)
                    if valor_transferencia <= 0:
                        print("Valor inválido. Por favor, digite um valor positivo.")
                        continue
                    
                    elif valor_transferencia > usuario_logado['saldo']:
                        print("Saldo insuficiente. Por favor, digite um valor menor ou igual ao seu saldo atual.")
                        continue
                    
                    else:
                        usuario_logado['saldo'] -= valor_transferencia
                        destinatario_encontrado['saldo'] += valor_transferencia
                        print(f"Transferência de R${valor_transferencia:.2f} para {destinatario_encontrado['usuario']} realizada com sucesso!")
                        usuario_logado['extrato'].append(f"Transferência para {destinatario_encontrado['usuario']}: R${valor_transferencia:.2f}")
                        destinatario_encontrado['extrato'].append(f"Transferência recebida de {usuario_logado['usuario']}: R${valor_transferencia:.2f}")
                        with open('dados.json', 'w', encoding='utf-8') as arquivo:
                            json.dump(dados, arquivo, ensure_ascii=False, indent=4)
                        return
                    
                except ValueError:
                    print("Valor inválido. Por favor, digite um número válido.")
                    continue