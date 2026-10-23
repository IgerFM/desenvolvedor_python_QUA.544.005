#TODO - Atividade 01 da parte 02

"""
Crie um programa que faça o seguinte:
- Cadastre novos usuarios (nome, email, telefone, cpf)
- Lista usuarios
- Altera dados de usuarios
- Exclui usuario
- Grava os dados de todos os usuarios em .json
- Abre .json e lista os usuarios cadastrados lá
"""
import os
import json

usuarios = []

# Limpa tela
os.system("cls" if os.name == "nt" else "clear")

while True:

    #menu
    print("Opção 01 - Cadastro de Novo Usuario")
    print("Opção 02 - Listar o Cadastro dos Usuarios")
    print("Opção 03 - Alterar o Cadastro de um Usuario")
    print("Opção 04 - Excluir o Cadastro de um Usuario")    
    print("Opção 05 - Gravar os Dados Referentes ao Cadastro dos Usuarios")
    print("Opção 06 - Abrir Arquivo com os Cadastros dos Usuarios")
    print("Opção 07 - Encerrar Programa")
    menu = input("")

    match menu:
        # Cadastro 
        case "1":
            usuario = {}
            
            usuario['nome'] = input("Insira o seu Nome Completo: ").strip().title()
            usuario['email'] = input("Insira o seu Email: ").strip().lower()
            usuario['telefone'] = input("Insira o seu Telefone: ").strip().lower()
            usuario['cpf'] = input("Insira o seu CPF: ").strip().lower()

            usuarios.append(usuario)

            print(f"\nMuito bem {usuarios.get('nome')}!\n\nO seu cadastro foi bem succedido")

        #TODO -  Impressão de todos 
        case "2":
            choskey = input("Qual Usuario voçê gostaria de alterar")
            if choskey:
                #TODO - if else para conferir se usuarios esta vazio
                    pass
            else:
                #TODO - 
                    pass

        ##TODO -  Alteração de dados 
        case "3":
            choskey = input("Qual Usuario voçê gostaria de alterar")
            if choskey:
                #TODO - if else para conferir se usuarios esta vazio
                    pass
            else:
                #TODO - 
                    pass

        ##TODO -  Exclusão 
        case "4":
            choskey = input("Qual Usuario voçê gostaria de alterar")
            if choskey:
                #TODO - if else para conferir se usuarios esta vazio
                    pass
            else:
                #TODO - 
                    pass
            
        ##TODO -  Gravação do .json 
        case "5":
            with open(f"parte02/atv01/{usuarios}.json","w",encoding="uts-8") as f:
                json.dump(usuarios, f)
            #TODO - 
            pass

        ##TODO -  Leitura do .json 
        case "6":

            choice = input("Qual arquivo gostaria de ler? ")

            if choice:
                #TODO - if else para conferir se o arquivo existe
                    pass
            else:
                #TODO - 
                    pass

        # Fim
        case "7":
            print("Programa encerrado com sucesso")            
            break
        # Error
        case _:
            print("Opção invalida")
            

