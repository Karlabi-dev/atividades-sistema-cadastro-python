usuarios = []


def adicionar_usuario():
    nome = input("Digite o nome: ")
    idade = int(input("Digite a idade: "))
    email = input("Digite o e-mail: ")

    usuario = {
        "nome": nome,
        "idade": idade,
        "email": email
    }

    usuarios.append(usuario)
    print("\nUsuário cadastrado com sucesso!")


def listar_usuarios():
    if len(usuarios) == 0:
        print("\nNenhum usuário cadastrado.")
        return

    print("\n--- USUÁRIOS CADASTRADOS ---")

    for i, usuario in enumerate(usuarios, start=1):
        print(f"\nUsuário {i}")
        print(f"Nome: {usuario['nome']}")
        print(f"Idade: {usuario['idade']}")
        print(f"E-mail: {usuario['email']}")


def remover_usuario():
    if len(usuarios) == 0:
        print("\nNenhum usuário cadastrado.")
        return

    listar_usuarios()
    numero = int(input("\nDigite o número do usuário que deseja remover: "))

    if 1 <= numero <= len(usuarios):
        usuario_removido = usuarios.pop(numero - 1)
        print(f"\nUsuário {usuario_removido['nome']} removido com sucesso!")
    else:
        print("\nNúmero de usuário inválido.")


while True:
    print("\n===== SISTEMA DE CADASTRO =====")
    print("1 - Adicionar usuário")
    print("2 - Listar usuários")
    print("3 - Remover usuário")
    print("4 - Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        adicionar_usuario()
    elif opcao == "2":
        listar_usuarios()
    elif opcao == "3":
        remover_usuario()
    elif opcao == "4":
        print("\nSistema encerrado.")
        break
    else:
        print("\nOpção inválida!")
