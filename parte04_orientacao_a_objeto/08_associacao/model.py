#SECTION - C - Endereço
class Endereco:
    def __init__(self,cep,uf,cidade,bairro,logradouro,complemento,numero):
        self.__cep = cep
        self.__uf = uf
        self.__cidade = cidade
        self.__bairro = bairro
        self.__logradouro = logradouro
        self.__complemento = complemento
        self.__numero = numero

    #NOTE - Tem o objetivo de criar um atributo, assim como float e string, assim existindo o tipo "Endereço"

    #SECTION - S&G - cep
    @property
    def cep(self):
        return self.__cep
    @cep.setter
    def cep(self,cep):
        self.__cep = cep

    #SECTION - S&G - uf
    @property
    def uf(self):
        return self.__uf
    @uf.setter
    def uf(self,uf):
        self.__uf = uf

    #SECTION - S&G - cidade
    @property
    def cidade(self):
        return self.__cidade
    @cidade.setter
    def cidade(self,cidade):
        self.__cidade = cidade

    #SECTION - S&G - bairro
    @property
    def bairro(self):
        return self.__bairro
    @bairro.setter
    def bairro(self,bairro):
        self.__bairro = bairro

    #SECTION - S&G - logradouro
    @property
    def logradouro(self):
        return self.__logradouro
    @logradouro.setter
    def logradouro(self,logradouro):
        self.__logradouro = logradouro

    #SECTION - S&G - complemento
    @property
    def complemento(self):
        return self.__complemento
    @complemento.setter
    def complemento(self,complemento):
        self.__complemento = complemento

    #SECTION - S&G - numero
    @property
    def numero(self):
        return self.__numero
    @numero.setter
    def numero(self,numero):
        self.__numero = numero

    #SECTION - M -
    def obter_endereco(self):
        return f"cep: {self.__cep}\nuf: {self.__uf}\ncidade: {self.__cidade}\nbairro: {self.__bairro}\nlogradouro: {self.__logradouro}\ncomplemento: {self.__complemento}\nnumero: {self.__numero}"


#SECTION - C - Pessoa   
class Pessoa:
    def __init__(self,nome,cpf,email,telefone,endereco):
        self.__nome = nome
        self.__cpf = cpf
        self.__email = email
        self.__telefone = telefone
        self.__endereco = endereco

    #SECTION - S&G - nome
    @property
    def nome(self):
        return self.__nome
    @nome.setter
    def nome(self,nome):
        self.__nome = nome

    #SECTION - S&G - cpf
    @property
    def cpf(self):
        return self.__cpf
    @cpf.setter
    def cpf(self,cpf):
        self.__cpf = cpf

    #SECTION - S&G - email
    @property
    def email(self):
        return self.__email
    @email.setter
    def email(self,email):
        self.__email = email

    #SECTION - S&G - telefone
    @property
    def telefone(self):
        return self.__telefone
    @telefone.setter
    def telefone(self,telefone):
        self.__telefone = telefone

    #SECTION - S&G - endereco
    @property
    def endereco(self):
        return self.__endereco
    @endereco.setter
    def endereco(self,endereco):
        self.__endereco = endereco

    #SECTION - M
    def exibir_dados(self):
        print(f"\nnome: {self.__nome}\ncpf: {self.__cpf}\nemail: {self.__email}\ntelefone: {self.__telefone}\nendereco: {self.__endereco.obter_endereco()}")
        #NOTE - Estou associando a classe Endereco com o self.__endereco por meior do metodo, assim transformando Endereco em um tipo tipo string