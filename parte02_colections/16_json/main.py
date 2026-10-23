#bibliotecas
#NOTE - JSON = (JavaScript Object Notation) ou (Objeto de Notação JavaScript
#NOTE - O tipo de arquivo JSON conversa MUITO bem com o Python, mesmo sendo um arquivo do JavaScript

import os
import json

usuarios = []
os.system("cls" if os.name == "nt" else "clean") 

# abri, ler e sair

while True:
    print("Opção 01 - Cadastrar novo usuário")
    print("Opção 02 - Criar ou Gravar o arquivo JSON")    
    print("Opção 03 - Ler o arquivo JSON")
    print("Opção 04 - Sair do programa")    
    menu = input("Qual a opção desejada: ")
    match menu:
        case "1":
            # Novo Dicionario
            
            usuario = {}

            # insersão dos dados no dicionario

            usuario['nome'] = input("Insira o seu Nome: ").strip().title()
            usuario['idade'] = int(input("Insira a sua Idade: ").strip())
            usuario['email'] = input("Insira o seu Email: ").strip().lower()
            usuario['cpf'] = input("Insira o seu CPF: ").strip()
            usuario['telefone'] = input("Insira o seu Telefone: ").strip()

            # O .append() adiciona algo dentro da lista

            usuarios.append(usuario)

            os.system("cls" if os.name == "nt" else "clean") 

            # mensagem de confirmação
            print(f"{usuario.get('nome')} cadastrado com sucesso")

        case "2":
            for usuario in usuarios:
                for chave, valor in usuario.items():
                    print(f"{chave.capitalize()}: {valor}")
                print(f"{"-"*40}")

            tobecon = input("Deseja gravar os dados? (s/n): ").lower()
                #NOTE - O json. é de arquivos .json, ja o f. é de arquivos .txt
            if tobecon == "s":
                os.system("cls" if os.name == "nt" else "clear")                        
                newfile = input("Qual o nome do arquivo que voce gostaria de salvar os usuarios: ")
                with open(f"16_json/{newfile}.json","w",encoding="utf-8") as f:
                    json.dump(usuarios,f)
                print("Arquivos salvos com sucesso")
                continue
            else: 
                os.system("cls" if os.name == "nt" else "clear")                            
                print("O arquivo original não foi alterado")
                continue
        case "3":
            os.system("cls" if os.name == "nt" else "clear")
            try:
                opefi = input("Qual arquivo gostaria de abrir: ")
                with open(f"16_json/{opefi}.json","r",encoding="utf-8") as f:
                    usuarios = json.load(f)
                for usuario in usuarios:
                    for chave, valor in usuario.items():
                        print(f"{chave.capitalize()}: {valor}")
                    print(f"{"-"*40}")
            except Exception as e:
                print(f"\nNão foi possivel abrir o arquivo. \nERROR: {e}")
            #TODO - 
            pass
        case "4":
            print("Programa encerrado")
            break
        case _:
            print("Opção invalida")