#SECTION - Bibliotecas
import os
from model import Pessoa

#SECTION - Lambda
def limpa():
    os.system("cls" if os.name == "nt" else "clear")

#SECTION - Algoritmo Principal
def main():
    limpa()
    usuario = Pessoa(nome="",idade=0,email="")
    usuario.nome = input("Insira o seu nome: ").strip().title()
    usuario.idade = int(input("Insira a sua idade: ").strip())
    usuario.email = input("Insira o seu email: ").strip().lower()

    limpa()
    print(usuario.comprimentador())

#SECTION - Player
if __name__ == "__main__":
    main()
