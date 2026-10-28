#SECTION - Bibliotecas
import os

#SECTION - Limpa tela
def limpar():
    os.system("cls" if os.name == "nt" else "clear")

#SECTION - Função Retorno
def greetings(nome):
    return f"\n{nome}, seja bem vindo!"

#SECTION - Algoritmo principal

limpar()

nome = input("Informe seu nome: ").strip().title()

print(greetings(nome))