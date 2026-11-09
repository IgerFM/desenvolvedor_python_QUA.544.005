#SECTION - Bibliotecas
import os
from model import Empresa, Departamento

#SECTION - Limpa tela
def limpar():
    os.system("cls" if os.name == "nt" else "clear")

#SECTION - Body
def main():
    #SECTION - Intanciamento
    departamento = Departamento(nome="")
    empresa = Empresa(razao_social="",nome_fantasia="",cnpj="",departamento=departamento)

    limpar()
    print(f"{"-"*20}Insira os dados da empresa: {"-"*20}")
    empresa.razao_social = input("Insira o seu razao_social: ").strip()
    empresa.nome_fantasia = input("Insira o seu nome_fantasia: ").strip()
    empresa.cnpj = input("Insira o seu cnpj: ").strip()
    empresa.departamento = input("Insira o seu departamento: ").strip()

    limpar()
    print(empresa.detalhes())

    #TODO - 
    pass

#SECTION - Runner
if __name__ == "__main__":
    main()