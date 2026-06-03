from banco import dados

def login():
    usuario = input("Digite seu nome de usuário: ")
    usuario = usuario.strip()
    senha = input("Digite sua senha: ")
    senha = senha.strip()
    resultado = autenticar(usuario, senha)

    if resultado:
        print (f"Bem vindo, {resultado['usuario']}!")
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
        usuario = input("Digite um nome de usuário: ")
        usuario = usuario.strip()
        senha = input("Digite uma senha: ")
        senha = senha.strip()
        for usuario_cadastrado in dados:
            if usuario_cadastrado['usuario'] == usuario:
                print("Usuário já existe. Por favor, escolha outro nome de usuário.")
                continue
        usuario_cadastrado = {
            'usuario': usuario,
            'senha': senha,
            'saldo': 0.0
        }
        dados.append(usuario_cadastrado)
        print("Usuário cadastrado com sucesso!")
        return