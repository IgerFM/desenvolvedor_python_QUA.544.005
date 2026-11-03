#SECTION - Bibliotecas
import os
from model import Pessoa

#SECTION - Limpa Tela
def limpar():
    os.system("cls" if os.name == "nt" else "clear")

#NOTE - A partir de agora, TODOS os programas futuros que tem orientação ao objeto devem ter encapsulamento
#NOTE - Ele faz com que alguns dados fiquem escondidos do programa livre ao publico, ele "Omite" algumas informações não necessarias no momento
#NOTE - Torna os dados mais burocraticos de acessar
#SECTION - Algoritmo Principal
def main():

    #SECTION - Instanciamento
    usuario = Pessoa(nome="",idade="",cpf="",telefone="",email="")

    usuario.nome = input("Insira o seu Nome: ").strip().title()
    usuario.idade = int(input("Insira o seu idade: ").strip())
    usuario.cpf = input("Insira o seu cpf: ").strip()
    usuario.telefone = input("Insira o seu telefone: ").strip()
    usuario.email = input("Insira o seu email: ").strip().lower()

    print(f"\n\nNome: {usuario.nome}")
    print(f"idade: {usuario.idade}")
    print(f"cpf: {usuario.cpf}")
    print(f"telefone: {usuario.telefone}")
    print(f"email: {usuario.email}")
    """usuario.nome = input("Insira o seu Nome: ").strip()
    print(f"Nome: {usuario.nome}")"""
                        
#SECTION - Rodador
if __name__ == "__main__":
    main()
