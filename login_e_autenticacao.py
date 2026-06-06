import json
with open('dados.json', 'r', encoding='utf-8') as arquivo:
    dados = json.load(arquivo)

def login():
    usuario = input("Digite seu nome de usuário: ")
    usuario = usuario.strip()
    senha = input("Digite sua senha: ")
    senha = senha.strip()
    resultado = autenticar(usuario, senha)

    if resultado:
        return resultado
    
    else:
        print("Credenciais inválidas.")

def autenticar(usuario, senha):
    for usuario_cadastrado in dados:
        if usuario_cadastrado['usuario'] == usuario and usuario_cadastrado['senha'] == senha:
            return usuario_cadastrado
        
    return None
    
def cadastrar_usuario():
    while True:
        usuario = input("Digite um nome de usuário ou 'sair' para cancelar: ")
        usuario = usuario.strip()
        if usuario.lower() == 'sair':
            print("Cadastro cancelado.")
            return
        senha = input("Digite uma senha: ")
        senha = senha.strip()
        if not usuario or not senha:
            print("Usuário e senha não podem ser vazios. Por favor, tente novamente.")
            continue
        usuario_existe = False
        for usuario_cadastrado in dados:
            if usuario_cadastrado['usuario'] == usuario:
                print("Usuário já existe. Por favor, escolha outro nome de usuário.")
                usuario_existe = True
                break

        if usuario_existe:
            continue
        
        else:
            usuario_cadastrado = {
                'usuario': usuario,
                'senha': senha,
                'saldo': 0.0,
                'extrato': [],
                'tipo': 'cliente'
            }
            dados.append(usuario_cadastrado)
            print("Usuário cadastrado com sucesso!")
            with open('dados.json', 'w', encoding='utf-8') as arquivo:
                json.dump(dados, arquivo, ensure_ascii=False, indent=4)
            return
        