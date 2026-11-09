#SECTION - Biblioteca
import os
from model import Endereco, Pessoa

#SECTION - Limpa tela
def limp():
    os.system("cls" if os.name == "nt" else "clear")

#SECTION - Body
def main():
    #SECTION - Instanciamento
    endereco = Endereco(cep="",uf="",cidade="",bairro="",logradouro="",complemento="",numero="")
    usuario = Pessoa(nome="",cpf="",email="",telefone="",endereco=endereco)

    limp()
    usuario.nome = input("Qual o seu nome: ").strip().title()
    usuario.cpf = input("Qual o seu cpf: ").strip().title()
    usuario.email = input("Qual o seu email: ").strip()
    usuario.telefone = input("Qual o seu telefone: ").strip()
    usuario.endereco = input("Qual o seu endereço: ").strip()

    
    endereco.cep = input("Qual o seu cep: ").strip().title()
    endereco.uf = input("Qual o seu uf: ").strip().upper()
    endereco.cidade = input("Qual o seu cidade: ").strip().title()
    endereco.bairro = input("Qual o seu bairro: ").strip().title()
    endereco.logradouro = input("Qual o seu logradouro: ").strip()
    endereco.complemento = input("Qual o seu complemento: ").strip()
    endereco.numero = input("Qual o seu numero: ").strip()

    usuario.exibir_dados() #FIXME - 

#SECTION - Runner
if __name__ == "__main__":
    main()