#SECTION - Bibliotecas
import os
from model import PessoaFisica, PessoaJuridica

#SECTION - Limpa Tela
def limpar():
    os.system("cls" if os.name == "nt" else "clear")

#NOTE - 2º Pilar da orientação ao objeto - Polimorfismo
#NOTE - Faz com que um unico metodo se comporte diferente entre 2 utilizações
#NOTE - 

#SECTION - Algoritmo Principal
def main():

    #SECTION - Instancia das classes
    usuario = PessoaFisica(nome="",cpf="",email="",telefone="",endereco="")
    empresa = PessoaJuridica(cnpj="",razao_social="",nome_fantasia="",email="",telefone="",endereco="")

    #SECTION - Informa os dados do usuario
    print(f"{'-' * 20} Informe os dados do Usuario {'-' * 20}")
    usuario.cpf = input("Informe o seu CPF: ").strip()
    usuario.nome = input("Informe o seu Nome: ").strip().title()
    usuario.email = input("Informe o seu Email: ").strip().lower()
    usuario.telefone = input("Informe o seu Telefone: ").strip()
    usuario.endereco = input("Informe o seu Endereço: ").strip()

    #SECTION - Informa os dados da Empresa
    print(f"{'-' * 20} Informe os dados da Empresa {'-' * 20}")
    empresa.cnpj = input("Informe o seu CNPJ: ").strip()
    empresa.nome_fantasia = input("Informe o sua Nome Fantasia: ").strip().title()
    empresa.razao_social = input("Informe o sua Razão Social: ").strip().title()
    empresa.email = input("Informe o seu Email: ").strip().lower()
    empresa.telefone = input("Informe o seu Telefone: ").strip()
    empresa.endereco = input("Informe o seu Endereço: ").strip()

    #SECTION - Imprime os dados da Pessoa
    limpar()
    usuario.exibir_dados()
    empresa.exibir_dados()

#SECTION - Roda Programa
if __name__ == "__main__":
    main()