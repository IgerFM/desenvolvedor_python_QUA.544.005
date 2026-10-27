#FIXME - Atividade 01 da parte 02

"""
Crie um programa que faça o seguinte:
- Cadastre novos usuarios (nome, email, telefone, cpf)
- Lista usuarios
- Altera dados de usuarios
- Exclui usuario
- Grava os dados de todos os usuarios em .json
- Abre .json e lista os usuarios cadastrados lá
"""

#SECTION - Bibliotecas
import os
import json
import time

#SECTION - Listas
usuarios = []

os.system("cls" if os.name == "nt" else "clear") # Limpa tela

while True:

    #SECTION - Botões Menu
    print("Opção 01 - Cadastro de Novo Usuario")
    print("Opção 02 - Listar o Cadastro dos Usuarios")
    print("Opção 03 - Alterar o Cadastro de um Usuario")
    print("Opção 04 - Excluir o Cadastro de um Usuario")    
    print("Opção 05 - Gravar e Exportar os Dados Referentes ao Cadastro dos Usuarios")
    print("Opção 06 - Abrir Arquivo com os Cadastros dos Usuarios")
    print("Opção 07 - Encerrar Programa")
    menu = input("\nSelecione o que gostaria de executar agora: ").strip()
    print("")

    #SECTION - Menu
    match menu:
         
        #SECTION - Cadastro 
        case "1":

            usuario = {}
            
            usuario['nome'] = input("Insira o seu Nome Completo: ").strip().title()
            usuario['email'] = input("Insira o seu Email: ").strip().lower()
            usuario['telefone'] = input("Insira o seu Telefone: ").strip().lower()
            usuario['cpf'] = input("Insira o seu CPF: ").strip().lower()

            usuarios.append(usuario)

            print(f"\nMuito bem {usuario.get('nome')}!\n\nO seu cadastro foi bem sucedido\n")
            continue

        #SECTION - Impressão de todos 
        case "2":
            
            n = 1 #NOTE - Jeito de listar usuarios que eu testei
            for usuario in usuarios:
                print(f"\n{"-"*40} Usuario {n} {"-"*40}\n")
                for chave, valor in usuario.items():
                    print(f"{chave}: {valor}")
                    time.sleep(.25)
                n += 1
            print("")
            continue

        #SECTION -  Alteração de dados 
        case "3":

            #NOTE - Jeito mais efetivo que o professor recomendou e eu pessoalmente adorei
            for n, usuario in enumerate(usuarios, start=1): 
                print(f"\n{"-"*40} Usuario {n} {"-"*40}\n")
                for chave, valor in usuario.items():
                    print(f"{chave}: {valor}")
                    time.sleep(.25)
            print("")
            try:
                """ #FIXME - #NOTE - Jeito mais efetivo que o professor recomendou e eu estou em duvida em como não pensei em testar isso
                chosus = int(input("\nQual Usuario voçê gostaria de alterar: ").strip())
                choskey = input("\nQual chave voçê gostaria de alterar: ").strip()
                usuarios[chosus][choskey] = input(f"Qual {choskey} gostaria de colocar")
                """
                chosus = int(input("\nQual Usuario voçê gostaria de alterar: ").strip())
                for n, usuario in enumerate(usuarios, start=1): 
                    if chosus == n:
                        choskey = input("\nQual chave voçê gostaria de alterar: ").strip()
                        if choskey:
                            usuario[choskey] = input(f"\nQual {choskey} gostaria de colocar: ")
                            continue
                        else:
                            print("\nChave Invalida\n")
                            continue
            except Exception as e:
                print(f"ERROR {e}")
                continue

        #SECTION -  Exclusão 
        case "4":   

            for n, usuario in enumerate(usuarios, start=1): 
                print(f"\n{"-"*40} Usuario {n} {"-"*40}\n")
                for chave, valor in usuario.items():
                    print(f"{chave}: {valor}")
                    time.sleep(.25)
            print("")
            try:
                chosus = int(input("\nQual Usuario voçê gostaria de excluir: ").strip())
                for n, usuario in enumerate(usuarios, start=1): 
                    if chosus == n:
                        del(usuarios[chosus-1])
                        print(f"\nUsuario {chosus} excluido com sucesso\n")
                        continue
            except Exception as e:
                print(f"ERROR {e}")
                continue
            
        #SECTION - Gravação do .json 
        case "5":

            for n, usuario in enumerate(usuarios, start=1): 
                print(f"\n{"-"*40} Usuario {n} {"-"*40}\n")
                for chave, valor in usuario.items():
                    print(f"{chave}: {valor}")
                    time.sleep(.25)
            print("")
            tobecon = input("\nGostaria de salvar os dados? (s/n)\n").lower()
            if tobecon == "s":
                newfile = input("\nQual o nome do arquivo que você gostaria de salvar os dados: ")
                with open(f"atv01/{newfile}.json","w",encoding="utf-8") as f:
                    json.dump(usuarios, f)
                print("\nO arquivo foi salvo com sucesso!!!\n")
                continue
            else:
                print("\nO arquivo não foi alterado\n")
                continue

        #SECTION - Leitura do .json 
        case "6":

            try:
                opefi = input("Qual arquivo gostaria de ler? ")
                with open(f"atv01/{opefi}.json","r",encoding="utf-8") as f:
                    usuarios = json.load(f)
                for n, usuario in enumerate(usuarios, start=1): 
                    print(f"\n{"-"*40} Usuario {n} {"-"*40}\n")
                    for chave, valor in usuario.items():
                        print(f"{chave}: {valor}")
                        time.sleep(.25)
                print("")
                continue
            except Exception as e:
                print(f"\nNão foi possivel achar o arquivo\n")
                continue

        #SECTION - Fim
        case "7":

            print("\nPrograma encerrado com sucesso\n")            
            break

        #SECTION - Error
        case _:

            print("\nOpção invalida\n")
            continue