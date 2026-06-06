from login_e_autenticacao import login, cadastrar_usuario
from operations import ver_saldo, depositar, sacar, ver_extrato, transferir
import json

def menu_usuario(usuario_logado):
    print(f"Bem-vindo, {usuario_logado['usuario']}!")
    while True:
        opcao_usuario = input("Escolha o que deseja fazer: 1.Ver sado 2.Depositar 3.Sacar 4.Ver extrato 5.Transferir 6.Sair: ")
        if opcao_usuario == "1":
            ver_saldo(usuario_logado)
            continue

        elif opcao_usuario == "2":
            depositar(usuario_logado)
            continue

        elif opcao_usuario == "3":
            sacar(usuario_logado)
            continue

        elif opcao_usuario == "4":
            ver_extrato(usuario_logado)
            continue

        elif opcao_usuario == "5":
            transferir(usuario_logado)
            continue

        elif opcao_usuario == "6":
            print("Obrigado por usar nosso sistema!")
            break

        else:
            print("Opção inválida. Por favor, escolha uma opção válida.")
            continue

def menu_admin(usuario_logado):
    print(f"Bem vindo a area administrativa, {usuario_logado['usuario']}!")
    while True:
        with open('dados.json', 'r', encoding='utf-8') as arquivo:
            dados = json.load(arquivo)
        opcao_admin = input("Escolha o que deseja fazer: 1.Ver usuários 2.Quantidade de usuários 3.Saldo total do banco 4.Relatório gerencial 5.Menu de usuário 6.Sair: ")
        if opcao_admin == "1":
            print("Lista de usuários cadastrados:")
            for usuario in dados:
                if usuario['tipo'] == 'cliente':
                    print(f"Usuário: {usuario['usuario']}, Saldo: R${usuario['saldo']:.2f}")

        elif opcao_admin == "2":
            usuarios = 0
            for usuario in dados:
                if usuario['tipo'] == 'cliente':
                    usuarios += 1
            print(f"Quantidade de usuários cadastrados: {usuarios}")

        elif opcao_admin == "3":
            saldo_total = 0.0
            for usuario in dados:
                if usuario['tipo'] == 'cliente':
                    saldo_total += usuario['saldo']
            print(f"Saldo total do banco: R${saldo_total:.2f}")

        elif opcao_admin == "4":
            usuarios = 0
            saldo_total = 0.0
            for usuario in dados:
                if usuario['tipo'] == 'cliente':
                    usuarios += 1
                    saldo_total += usuario['saldo']

            print(f"Relatório gerencial:\n"
                  f"Quantidade de usuários cadastrados: {usuarios}\n"
                  f"Saldo total do banco: R${saldo_total:.2f}")

        elif opcao_admin == "5":
            menu_usuario(usuario_logado)
            continue
        
        elif opcao_admin == "6":
            print("Obrigado por usar nosso sistema!")
            break

def main():
    print("Inicindo sistema...")
    while True:
        opcao_inicial = input("Escolha uma opção: 1.Login 2.Cadastrar 3.Sair: ")
        if opcao_inicial == "1":
            usuario_logado = login()
            if usuario_logado:
                if usuario_logado['tipo'] == 'admin':
                    menu_admin(usuario_logado)
                else:
                    menu_usuario(usuario_logado)
                    continue

        elif opcao_inicial == "2":
            cadastrar_usuario()
            continue

        elif opcao_inicial == "3":
            print("Encerrando sistema...")
            break

        else:
            print("Opção inválida. Por favor, escolha uma opção válida.")
            continue
