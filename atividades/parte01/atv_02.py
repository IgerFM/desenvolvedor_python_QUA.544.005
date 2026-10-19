import os
import time
"""

Criar um programa que receba apenas um nome e idade, e insira a lista de filmes do cinema, as salas e as classificações indicativas

O usuario escolhe a sala do filme e se ele tiver a idade necessaria, o programa imprimira o ingresso e encerrara

Caso contrario ele impede o usuario de escolher aquele filme e volta ao catalogo de filmes para que o mesmo possa escolher novamente

Não sei como, mas o professor disse que conseguiu resolver em 30 linhas

"""
""" Catalogo dos filme que participam
A ODISSEIA ||| SALA 07 ||| Classificação Indicativa 14
CARROS ||| SALA 05 ||| Classificação Indicativa L
COYOTE VS ACME ||| SALA 03 ||| SALA 08 ||| SALA 11 ||| Classificação Indicativa 06
SPACE JAM (1996) ||| SALA 09 ||| SALA 10 ||| Classificação Indicativa L
STREET FIGHTER ||| SALA 03 ||| SALA 04 ||| SALA 05 ||| SALA 09 ||| Classificação Indicativa 14
TOY STORY 5 ||| SALA 05 ||| Classificação Indicativa 06
VINGADORES - ULTIMATO ENCORE ||| SALA 01 ||| SALA 02 ||| SALA 06 ||| Classificação Indicativa 14
"""

# apresentação (do programa)
os.system("cls" if os.name == "nt" else "clean")

print("\n\nBem vindo ao site de ingressos da Kinoplex, por favor, se apresente para apresentarmos o nosso catalogo:\n")

#identificação (nome, idade)

nom = input("Qual o seu nome: ").strip().title()
ida = int(input("Qual a sua idade: "))
# Para definir uma variavel vazia, deve utilizar var = None

#lista(apresentação e seleção)
try:
    #Estrutura de desição para escolher o filme
    while True:
        
        print(f'\nOlá {nom}, venha conhecer o nosso catalogo:')
        print(f"\n(01) A Odisseia --------------------- Classificação 14 Anos\nSala 07")
        time.sleep(1)
        print(f"\n(02) Carros ------------------------- Classificação Livre\nSala 05")
        time.sleep(1)
        print(f"\n(03) Coyote VS Acme ----------------- Classificação 06 Anos\nSala 03 --- Sala 08 --- Sala 11")
        time.sleep(1)
        print(f"\n(04) Space Jam (1996) --------------- Classificação Livre\nSala 09 --- Sala 10")
        time.sleep(1)
        print(f"\n(05) Street Fighter ----------------- Classificação 14 Anos\nSala 03 --- Sala 04 --- Sala 05 --- Sala 09")
        time.sleep(1)
        print(f"\n(06) Toy Story 5 -------------------- Classificação 06 Anos\nSala 05")
        time.sleep(1)
        print(f"\n(07) Vingadores Ultimato - Encore --- Classificação 14 Anos\nSala 01 --- Sala 02 --- Sala 06")
        time.sleep(1)
        fd = int(input(f'\n\nMuito bem {nom}, digite o numero do filme do qual você gostaria de assistir: '))
        
        
        #Estrutura de desição para escolher a sala + Barreira de idade + Impressão de ingresso
        match fd:
        
            case 1:
                if ida >= 14:
                    while True:
                        sala = int(input("Muito bem, dentre as salas (07), em qual você gostaria de assistir: "))
                        match sala:
                            case 7:
                                time.sleep(1.5)
                                print(f"\n\nIngresso Kinolex\n\nComprador: {nom}\nFilme: A Odisseia\nSala: 07\n\nAgradeçemos por comprar o seu ingresso na Kinoplex, tenha uma otima sessão\n\n")
                                break
                            case _:
                                print("\n\nEste filme não esta disponivel nesta sala\n\n")
                                time.sleep(2)
                    break
                else:
                    print("\n\nIdade isuficiente, escolha outro filme do catalogo\n")
                    time.sleep(2)

            case 2:
                if ida >= 0:
                    while True:
                        sala = int(input("Muito bem, dentre as salas (05), em qual você gostaria de assistir: "))
                        match sala:
                            case 5:
                                time.sleep(1.5)
                                print(f"\n\nIngresso Kinolex\n\nComprador: {nom}\nFilme: Carros\nSala: 05\n\nAgradeçemos por comprar o seu ingresso na Kinoplex, tenha uma otima sessão\n\n")
                                break
                            case _:
                                print("\n\nEste filme não esta disponivel nesta sala\n\n")
                                time.sleep(2)
                    break
                else:
                    print("\n\nIdade isuficiente, escolha outro filme do catalogo\n")
                    time.sleep(2)

            case 3:
                if ida >= 6:
                    while True:    
                        sala = int(input("Muito bem, dentre as salas (03, 08, 11), em qual você gostaria de assistir: "))
                        match sala:
                            case 3:
                                time.sleep(1.5)
                                print(f"\n\nIngresso Kinolex\n\nComprador: {nom}\nFilme: Coyote vs Acme\nSala: 03\n\nAgradeçemos por comprar o seu ingresso na Kinoplex, tenha uma otima sessão\n\n")
                                break
                            case 8:
                                time.sleep(1.5)
                                print(f"\n\nIngresso Kinolex\n\nComprador: {nom}\nFilme: Coyote vs Acme\nSala: 08\n\nAgradeçemos por comprar o seu ingresso na Kinoplex, tenha uma otima sessão\n\n")
                                break
                            case 11:
                                time.sleep(1.5)
                                print(f"\n\nIngresso Kinolex\n\nComprador: {nom}\nFilme: Coyote vs Acme\nSala: 11\n\nAgradeçemos por comprar o seu ingresso na Kinoplex, tenha uma otima sessão\n\n")
                                break
                            case _:
                                print("\n\nEste filme não esta disponivel nesta sala\n\n")
                                time.sleep(2)
                    break
                else:
                    print("\n\nIdade isuficiente, escolha outro filme do catalogo\n")
                    time.sleep(2)

            case 4:
                if ida >= 0:
                    while True:    
                        sala = int(input("Muito bem, dentre as salas (09, 10), em qual você gostaria de assistir: "))
                        match sala:
                            case 9:
                                time.sleep(1.5)
                                print(f"\n\nIngresso Kinolex\n\nComprador: {nom}\nFilme: Space Jam (1996)\nSala: 09\n\nAgradeçemos por comprar o seu ingresso na Kinoplex, tenha uma otima sessão\n\n")
                                break
                            case 10:
                                time.sleep(1.5)
                                print(f"\n\nIngresso Kinolex\n\nComprador: {nom}\nFilme: Space Jam (1996)\nSala: 10\n\nAgradeçemos por comprar o seu ingresso na Kinoplex, tenha uma otima sessão\n\n")
                                break
                            case _:
                                print("\n\nEste filme não esta disponivel nesta sala\n\n")
                                time.sleep(2)
                    break
                else:
                    print("\n\nIdade isuficiente, escolha outro filme do catalogo\n")
                    time.sleep(2)

            case 5:
                if ida >= 14:
                    while True:    
                        sala = int(input("Muito bem, dentre as salas (03, 04, 05, 09), em qual você gostaria de assistir: "))
                        match sala:
                            case 3:
                                time.sleep(1.5)
                                print(f"\n\nIngresso Kinolex\n\nComprador: {nom}\nFilme: Street Fighter\nSala: 03\n\nAgradeçemos por comprar o seu ingresso na Kinoplex, tenha uma otima sessão\n\n")
                                break
                            case 4:
                                time.sleep(1.5)
                                print(f"\n\nIngresso Kinolex\n\nComprador: {nom}\nFilme: Street Fighter\nSala: 04\n\nAgradeçemos por comprar o seu ingresso na Kinoplex, tenha uma otima sessão\n\n")
                                break
                            case 5:
                                time.sleep(1.5)
                                print(f"\n\nIngresso Kinolex\n\nComprador: {nom}\nFilme: Street Fighter\nSala: 05\n\nAgradeçemos por comprar o seu ingresso na Kinoplex, tenha uma otima sessão\n\n")
                                break
                            case 9:
                                time.sleep(1.5)
                                print(f"\n\nIngresso Kinolex\n\nComprador: {nom}\nFilme: Street Fighter\nSala: 09\n\nAgradeçemos por comprar o seu ingresso na Kinoplex, tenha uma otima sessão\n\n")
                                break
                            case _:
                                print("\n\nEste filme não esta disponivel nesta sala\n\n")
                                time.sleep(2)
                    break
                else:
                    print("\n\nIdade isuficiente, escolha outro filme do catalogo\n")
                    time.sleep(2)

            case 6:
                if ida >= 6:
                    while True:
                        sala = int(input("Muito bem, dentre as salas (05), em qual você gostaria de assistir: "))
                        match sala:
                            case 5:
                                time.sleep(1.5)
                                print(f"\n\nIngresso Kinolex\n\nComprador: {nom}\nFilme: Toy Story 5\nSala: 05\n\nAgradeçemos por comprar o seu ingresso na Kinoplex, tenha uma otima sessão\n\n")
                                break
                            case _:
                                print("\n\nEste filme não esta disponivel nesta sala\n\n")
                                time.sleep(2)
                    break
                else:
                    print("\n\nIdade isuficiente, escolha outro filme do catalogo\n")
                    time.sleep(2)

            case 7:
                if ida >= 14:
                    while True:
                        sala = int(input("Muito bem, dentre as salas (01, 02, 06), em qual você gostaria de assistir: "))
                        match sala:
                            case 1:
                                time.sleep(1.5)
                                print(f"\n\nIngresso Kinolex\n\nComprador: {nom}\nFilme: Vingadores: Ultimato - Encore\nSala: 01\n\nAgradeçemos por comprar o seu ingresso na Kinoplex, tenha uma otima sessão\n\n")
                                break
                            case 2:
                                time.sleep(1.5)
                                print(f"\n\nIngresso Kinolex\n\nComprador: {nom}\nFilme: Vingadores: Ultimato - Encore\nSala: 02\n\nAgradeçemos por comprar o seu ingresso na Kinoplex, tenha uma otima sessão\n\n")
                                break
                            case 6:
                                time.sleep(1.5)
                                print(f"\n\nIngresso Kinolex\n\nComprador: {nom}\nFilme: Vingadores: Ultimato - Encore\nSala: 06\n\nAgradeçemos por comprar o seu ingresso na Kinoplex, tenha uma otima sessão\n\n")
                                break
                            case _:
                                print("\n\nEste filme não esta disponivel nesta sala\n\n")
                                time.sleep(2)
                    break
                else:
                    print("\n\nIdade isuficiente, escolha outro filme do catalogo\n")
                    time.sleep(2)
                os.system("cls" if os.name == 'nt' else 'clear')
                    
            case _:
                print("Este filme não existe")
                time.sleep(2)
                os.system('cls' if os.name == 'nt' else 'clear')

except Exception as e:
    print(f"Algo deu errado {e}")
finally:
    print("Programa finalizado")

""" Como o professor fez:

while True:
    print("sala 1 - filme tananan")
    print("sala 2 - filme tananan")
    print("sala 3 - filme tananan")
    print("sala 4 - filme tananan")
    print("sala 5 - filme tananan")
    print("sala 6 - filme tananan")
    sala = input("sala desejada").strip()
    match sala:
        case "1":
            idade_minima = x
        case "2":
            idade_minima = x
        case "3":
            idade_minima = x
        case "4":
            idade_minima = x
        case "4":
            idade_minima = x
        case "5":
            idade_minima = x
        case "6":
            idade_minima = x
        case "_":
            print("a sala não existe")
            idade_minima = idade + 1
    if idade >= idade_minima
        print("ingresso")
    else:
        print("ingresso negado")
"""