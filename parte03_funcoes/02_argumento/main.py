import os

#SECTION - Saudações
def greetings(nome):
    print(f"\nOlá {nome}, seja bem-vindo!")

def clean():
    os.system("cls" if os.name == "nt" else "clear")

#SECTION - Algoritimo principal
clean()
nome = input("\nInforme o seu nome: ").strip().title()
greetings(nome)