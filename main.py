from login_e_autenticacao import login, cadastrar_usuario
from operations import ver_saldo, depositar, sacar

def menu_usuario(usuario_logado):
    print(f"Bem-vindo, {usuario_logado['usuario']}!")
    while True:
        opcao_usuario = input("Escolha o que deseja fazer: 1.Ver sado 2.Depositar 3.Sacar 4.Sair: ")
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
            print("Obrigado por usar nosso sistema!")
            break

        else:
            print("Opção inválida. Por favor, escolha uma opção válida.")
            continue

def main():
    print("Inicindo sistema...")
    while True:
        opcao_inicial = input("Escolha uma opção: 1.Login 2.Cadastrar 3.Sair: ")
        if opcao_inicial == "1":
            usuario_logado = login()
            if usuario_logado:
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

main()