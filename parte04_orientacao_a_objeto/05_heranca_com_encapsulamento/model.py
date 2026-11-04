#SECTION - SuperClasse
class Pessoa:
    def __init__(self,telefone,email):
        self.__telefone = telefone
        self.__email = email

    #SECTION - Set & Get Telefone
    @property
    def telefone(self):
        return self.__telefone
    @telefone.setter
    def telefone(self,telefone):
        self.__telefone = telefone

    #SECTION - Set & Get Email
    @property
    def email(self):
        return self.__email
    @email.setter
    def email(self,email):
        self.__email = email


#SECTION - Classe Pessoa Fisica
class PessoaFisica(Pessoa):
    def __init__(self,nome,cpf,telefone,email):
        self.__nome = nome
        self.__cpf = cpf
        super().__init__(telefone=telefone,email=email)

    #SECTION - Set & Get Nome
    @property
    def nome(self):
        return self.__nome
    @nome.setter
    def nome(self,nome):
        self.__nome = nome

    #SECTION - Set & Get CPF
    @property
    def cpf(self):
        return self.__cpf
    @cpf.setter
    def cpf(self,cpf):
        self.__cpf = cpf


        
#SECTION - Classe Pessoa Juridica
class PessoaJuridica(Pessoa):
    def __init__(self,nome_fantasia,razao_social,cnpj,telefone,email):
        self.__nome_fantasia = nome_fantasia
        self.__razao_social = razao_social
        self.__cnpj = cnpj
        super().__init__(telefone=telefone,email=email)

    #SECTION - Set & Get Nome_fantasia
    @property
    def nome_fantasia(self):
        return self.__nome_fantasia
    @nome_fantasia.setter
    def nome_fantasia(self,nome_fantasia):
        self.__nome_fantasia = nome_fantasia

    #SECTION - Set & Get Razão Social
    @property
    def razao_social(self):
        return self.__razao_social
    @razao_social.setter
    def razao_social(self,razao_social):
        self.__razao_social = razao_social

    #SECTION - Set & Get CNPJ
    @property
    def cnpj(self):
        return self.__cnpj
    @cnpj.setter
    def cnpj(self,cnpj):
        self.__cnpj = cnpj


        