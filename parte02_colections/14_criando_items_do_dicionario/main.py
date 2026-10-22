import os

usuarios = [

]   

os.system("cls" if os.name == "nt" else "clear")

while True: #for usuario in usuarios:

    print(f"Digite 01 - Para Cadastrar Novo Usuário; ")
    print(f"Digite 02 - Para Listar os Usuários; ")
    print(f"Digite 03 - Para Encerrar o Programa; ")
    #print(f"Digite 04 - Para Excluir Usuário; ")
    menu = input("Qual opção prefere? ")

    os.system("cls" if os.name == "nt" else "clear")

    match menu:
        
        case "1":

            usuario = {}

            usuario['nome'] = input("Informe o nome: ").strip().title()
            usuario['telefone'] = int(input("Informe a Idade: "))
            usuario['email'] = input("Informe o email: ").strip().lower()
            usuario['cpf'] = input("informe o CPF: ").strip()

            usuarios.append(usuario)

            print(f"{usuario.get('nome')}")
            continue

        case "2":
            for usuario in usuarios:
                for chave, valor in usuario.items():
                    print(f"{chave.capitalize()}: {valor}")
                print(f"{'-'*80}")
            continue
        case "3":
            print("\nPrograma encerrado com sucesso.\n")
            break
        case _:
            print("\nOpção invalida.\n")