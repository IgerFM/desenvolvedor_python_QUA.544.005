# Desafio

"""

    Deve Elaborar um programa que leia um número, que verifique se o número é par ou ímpar e mostre a mensagem na tela, se "é par", ou "É impar"

"""

# Passo 1: Entender o problema
# Passo 2: 

num = int(input("\nEscolha um número e eu direi se ele é impar ou par: "))

res = (num%2)

if res == 0:
    print("\nO seu número é par\n")

else:
    print("\nO seu número é impar\n")


"""

Para igualar numeros, devo usar ==
Para falar que e diferente, devo usar +-

"""
