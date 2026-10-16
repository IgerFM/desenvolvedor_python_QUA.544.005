#TODO - 
import os
"""

Criar um programa que receba apenas um nome e idade, e insira a lista de filmes do cinema, as salas e as classificações indicativas

O usuario escolhe a sala do filme e se ele tiver a idade necessaria, o programa imprimira o ingresso e encerrara

Caso contrario ele impede o usuario de escolher aquele filme e volta ao catalogo de filmes para que o mesmo possa escolher novamente

"""
"""
A ODISSEIA ||| SALA 07 14
CARROS ||| SALA 05 L
COYOTE VS ACME ||| SALA 03 6
SPACE JAM (1996) ||| SALA 09 L
STREET FIGHTER ||| SALA 03 ||| SALA 04 ||| SALA 05 ||| SALA 09 14
TOY STORY 5 ||| SALA 05 6
VINGADORES - ULTIMATO ENCORE ||| SALA 01 DUB 14
"""
fl = ["A odisseia","Carros","Coyote VS Acme","Space Jam (1996)","Street Fighter","Toy Story 5","Vingadores Ultimato - Encore"] #5 filmes em cartaz
"""
od = ["A Odisseia","Sala 07",14]
ca = ["Carros","Sala 05",0]
co = ["Coyote VS Acme","Sala 03",6]
sj = ["Space Jam (1996)","Sala 09",0]
sf = ["Street Fighter","Sala 03,04,05,09",14]
ts = ["Toy Story 5","Sala 05",6]
vu = ["Vingadores Ultimato - Encore","Sala 01",14]
"""
# apresentação (do programa)
os.system("cls" if os.name == "nt" else "clean")

print("\n\nBem vindo ao site de ingressos da Kinoplex, venha conhecer o nosso catalogo:\n")
print(f"\nA Odisseia --------------------- Classificação 14 Anos\nSala 07")
print(f"\nCarros ------------------------- Classificação Livre\nSala 05")
print(f"\nCoyote VS Acme ----------------- Classificação 06 Anos\nSala 03")
print(f"\nSpace Jam (1996) --------------- Classificação Livre\nSala 09")
print(f"\nStreet Fighter ----------------- Classificação 14 Anos\nSala 03 --- Sala 04 --- Sala 05 --- Sala 09")
print(f"\nToy Story 5 -------------------- Classificação 06 Anos\nSala 05")
print(f"\nVingadores Ultimato - Encore --- Classificação 14 Anos\nSala 01")

#identificação (nome, idade)

nom = input("\nQual o seu nome: ").strip().title()
ida = int(input("Qual a sua idade: "))
x = 0

#lista(apresentação e seleção)
try:
    
    while True:
        print(f'Muito bem {nom}, digite "sim" para escolher qual filme você gostaria de assistir\n')
        input(f"\nA Odisseia --------------------- Classificação 14 Anos\nSala 07\n\n")
        print("ingresso" break if x != "sim")
        input(f"\nCarros ------------------------- Classificação Livre\nSala 05\n\n")
        print("ingresso" if x != "sim")
        input(f"\nCoyote VS Acme ----------------- Classificação 06 Anos\nSala 03\n\n")
        print("ingresso" if x != "sim")
        input(f"\nSpace Jam (1996) --------------- Classificação Livre\nSala 09\n\n")
        print("ingresso" if x != "sim")
        input(f"\nStreet Fighter ----------------- Classificação 14 Anos\nSala 03 --- Sala 04 --- Sala 05 --- Sala 09\n\n")
        print("ingresso" if x != "sim")
        input(f"\nToy Story 5 -------------------- Classificação 06 Anos\nSala 05\n\n")
        print("ingresso" if x != "sim")
        input(f"\nVingadores Ultimato - Encore --- Classificação 14 Anos\nSala 01\n\n")
        print("ingresso" if x != "sim")
        pass

except Exception as e:
    print("Algo deu errado")
finally:
    print("Programa finalizado")


#impressão ou repetição



"""
sl = ["Sala 0","Sala 1","Sala 2","Sala 3","Sala 4","Sala 5","Sala 6","Sala 7","Sala 8","Sala 9","Sala 10","Sala 11"]

print(f"{fl[1]} esta em cartaz nas salas:\n{sl[7]} {sl[9]} {sl[9]} {sl[9]}")
print(f"{fl[2]} esta em cartaz nas salas:\n{sl[9]} {sl[9]} {sl[9]}")
print(f"{fl[3]} esta em cartaz nas salas:\n{sl[9]}")
print(f"{fl[4]} esta em cartaz nas salas:\n{sl[9]} {sl[9]} {sl[9]}")
print(f"{fl[5]} esta em cartaz nas salas:\n{sl[9]} {sl[9]}")"""

