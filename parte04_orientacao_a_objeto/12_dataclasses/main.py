#SECTION - Bibliotecas
import os
from model import Pessoa

#SECTION - Limpa Tela
def limpar():
    os.system("cls" if os.name == "nt" else "clear")

#SECTION - Body
def main():
    usuario = Pessoa(nome="",cpf="",email="",idade=0,altura=0.0)

    usuario.nome = input("Insira o seu nome: ").strip().title()
    usuario.cpf = input("Insira o seu cpf: ").strip()
    usuario.email = input("Insira o seu email: ").strip().lower()
    usuario.idade = int(input("Insira a sua idade: "))
    usuario.altura = float(input("Insira a sua altura: ").replace(",","."))
     
    print(f"o seu nome é: {usuario.nome}")
    print(f"o seu cpf é: {usuario.cpf}")
    print(f"o seu email é: {usuario.email}")
    print(f"a sua idade é: {usuario.idade}")
    print(f"a sua altura é: {usuario.altura}")

#SECTION - Runner
if __name__ == "__main__":
    main()