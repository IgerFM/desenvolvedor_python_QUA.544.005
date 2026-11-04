#SECTION - Bibliotecas
import os
from model import PessoaFisica, PessoaJuridica

#SECTION - Limpa Tela
def limpar():
    os.system("cls" if os.name == "nt" else "clear")

#SECTION - Body
def main():

    #SECTION - Instanciamento
    usuario = PessoaFisica(nome="",cpf="",telefone="",email="",)
    #NOTE - Outra forma de instanciamento:
    empresa = PessoaJuridica(nome_fantasia="",razao_social="",cnpj="",telefone="",email="")
    limpar()
    
    #SECTION - Entrada usuario
    print(f"{"-"*20} Insira os Dados do Usuario {"-"*20}")
    usuario.nome = input("Informe o seu Nome: ").strip().title()
    usuario.cpf = input("Informe o seu CPF: ").strip()
    usuario.telefone = input("Informe o seu Telefone: ").strip()
    usuario.email = input("Informe o seu Email: ").strip().lower()
    
    #SECTION - Entrada empresa
    print(f"{"-"*20} Insira os Dados da Empresa {"-"*20}")
    empresa.nome_fantasia = input("Informe o seu Nome Fantasia: ").strip().title()
    empresa.razao_social = input("Informe a sua Razão Social: ").strip()
    empresa.cnpj = input("Informe o seu CNPJ: ").strip()
    empresa.telefone = input("Informe o seu Telefone: ").strip()
    empresa.email = input("Informe o seu Email: ").strip().lower()
    limpar()
    
    #SECTION - Saida usuario
    print(f"{"-"*20} Dados do Usuario {"-"*20}")
    print(f"O seu Nome é: {usuario.nome}")
    print(f"O seu CPF é: {usuario.cpf}")
    print(f"O seu Telefone é: {usuario.telefone}")
    print(f"O seu Email é: {usuario.email}")
    
    #SECTION - Saida empresa
    print(f"{"-"*20} Dados da Empresa {"-"*20}")
    print(f"O seu Nome Fantasia é: {empresa.nome_fantasia}")
    print(f"A sua Razão Social é: {empresa.razao_social}")
    print(f"O seu CNPJ é: {empresa.cnpj}")
    print(f"O seu Telefone é: {empresa.telefone}")
    print(f"O seu Email é: {empresa.email}")

#SECTION - Rodador
if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(e)