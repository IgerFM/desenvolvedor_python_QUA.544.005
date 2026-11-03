class Pessoa:
    def __init__(self,email,endereco,telefone):
        self.email = email
        self.endereco = endereco
        self.telefone = telefone

    #SECTION - Metodo da Super Classe    
    def exibir_dados(self):
        print(f"Email: {self.email}")
        print(f"Telefone: {self.telefone}")
        print(f"Endereço: {self.endereco}")
        

class PessoaFisica(Pessoa):
    def __init__(self,nome,cpf,email,telefone,endereco):
        self.nome = nome
        self.cpf = cpf
        super().__init__(email=email,telefone=telefone,endereco=endereco)

    #SECTION - Metodo da Classe Pessoa 
    def exibir_dados(self):
        print(f"{'-' * 20} Dados do Usuario {'-' * 20}")
        print(f"Nome: {self.nome}")
        print(f"CPF: {self.cpf}")
        super().exibir_dados()

class PessoaJuridica(Pessoa):
    def __init__(self,nome_fantasia,razao_social,cnpj,email,telefone,endereco):
        self.nome_fantasia = nome_fantasia
        self.razao_social = razao_social
        self.cnpj = cnpj
        super().__init__(email=email,telefone=telefone,endereco=endereco)

    #SECTION - Metodo da Classe Empresa 
    def exibir_dados(self):
        print(f"{'-' * 20} Dados da Empresa {'-' * 20}")
        print(f"Nome Fantasia: {self.nome_fantasia}")
        print(f"Razão Social: {self.razao_social}")
        print(f"Cnpj: {self.cnpj}")
        super().exibir_dados()
        