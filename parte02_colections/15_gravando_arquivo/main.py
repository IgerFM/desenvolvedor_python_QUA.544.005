# Criar um programa que gera, grava e modifica uma arquivo de texto
#NOTE - Este metodo cria um arquivo .txt na pasta do projeto como esta pasta "15_gravando_arquivo"
import os

# Limpaterm
os.system("cls" if os.name == "nt" else "clear")
while True:
    print("Digite 01 - Para gravar no arquivo")
    print("Digite 02 - Para abrir e ler o arquivo")
    print("Digite 03 - Para sair do programa")
    menu = input("O que gostaria de fazer? ")
    os.system("cls" if os.name == "nt" else "clear")
    match menu:
        case "1":
            # O usuario informa o texto que quer gravar
            newtxt = input("\nDigite o seu texto: ")
            newfile = input("\nDigite o nome do novo arquivo: ").strip().lower()#.replace("\" as " ")

            #NOTE - o "w" indica que deve ser gravado
            #NOTE - o 'encoding="utf-8"' serve para indicar o padrão das letras, evitando que sejam trocadas
            #NOTE -  o "15_gravando_arquivo/{newfile}.txt" funciona apenas es eu estiver na parte02_collections, se eu estiver na "desenvolvedor_phyton", eu devo colocar "parte02_colections/15_gravando_arquivo/{newfile}.md"
            with open(f"15_gravando_arquivo/{newfile}.txt","w",encoding="utf-8") as f: 
                f.write(newtxt)
            continue
        case "2":

            #NOTE - Este lê o arquivo dentro do programa

            #TODO - achar uma solução melhor para listar itens da pasta
            #os.system("cd 15_gravando_arquivo")
            #os.system("dir")
            opefi = input("Qual arquivo .txt gostaria de abrir? ").strip()
            #NOTE - With open() é uma condicional para um arquivo aberto
            #NOTE - O "r" serve para ler o arquivo
            with open(f"15_gravando_arquivo/{opefi}.txt","r",encoding="utf-8") as f:
                texto = f.read()
            print(f"\n\n{texto}\n\n")
            continue

        case "3":
            print("Programa Encerrado com sucesso")
            break
        case _:
            print("Opção Invalida")