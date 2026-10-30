#NOTE - É imperativo a classe começar com letra maiuscula
#NOTE - Caso a classe tenha um espaço, ela deve ser escrita junta como em "PessoaFisica"
#SECTION - Classes
class Pessoa: 
    #SECTION - Construtor
    #NOTE - O primeiro item da classe deve ser o construtor
    #NOTE - Dentro do construtor deve ser escrito como "__init__(self,atributo1,atributo2)"
    def __init__(self,nome,idade,email,cpf):
        #SECTION - Atributos
        self.nome = nome
        self.idade = idade
        self.email =  email
        self.cpf = cpf

    #SECTION - Impressão de dados V2
    def exibicionista(self):
        print(f"\n\nNome: {self.nome}.")
        print(f"Idade: {self.idade} Anos old.")
        print(f"Email: {self.email}.")
        print(f"CPF: {self.cpf}.")
        print(f"\n\nPrograma encerrado com sucesso")

#SECTION - Algoritmo Principal
def main():
    #FIXME - Instanciar a Classe
    usuario = Pessoa(nome="",idade=0,email="",cpf="")

    #SECTION - Inserção dos valores dos atributos
    usuario.nome = input("\n\nInsira o seu Nome: ").strip().title()
    usuario.idade = int(input("Insira o seu Idade: ").strip())
    usuario.email = input("Insira o seu Email: ").strip().lower()
    usuario.cpf = input("Insira o seu CPF: ").strip()

    """
    #STUB - Impressão dos atributos
    print(f"\n\nNome: {usuario.nome}.")
    print(f"Idade: {usuario.idade} Anos old.")
    print(f"Email: {usuario.email}.")
    print(f"CPF: {usuario.cpf}.")
    print(f"\n\nPrograma encerrado com sucesso")"""

    #SECTION - Impressão de atributos V2
    usuario.exibicionista()

#SECTION - Player
if __name__ == "__main__":
    main()
