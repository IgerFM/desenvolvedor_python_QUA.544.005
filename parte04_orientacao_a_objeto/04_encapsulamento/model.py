class Pessoa:

    def __init__(self,nome,idade,cpf,telefone,email):
        #self.nome = nome #NOTE - Definindo como Public
        #self._idade = idade #NOTE - Definindo como Protected
        #self.__cpf = cpf #NOTE - Definindo como Private

        self.__nome = nome
        self.__idade = idade 
        self.__cpf = cpf
        self.__telefone = telefone
        self.__email = email

    #FIXME - Metodos de acesso
    #NOTE - Define, executa, atribui vcalores a uma classe
    #NOTE - set define e get resgata
    #NOTE - É diferente do java
    #NOTE - É imperativo o get e o set ficarem juntos, não posso algomerar para fins de organização varios get's e varios set's
    
    #SECTION - Nome
    @property #NOTE - Serve para definir o metodo get
    def nome(self):
        return self.__nome
    @nome.setter #NOTE - Serve para definir o metodo set
    def nome(self,nome):
        self.__nome = nome

    #SECTION - Idade
    @property 
    def idade(self):
        return self.__idade
    @idade.setter 
    def idade(self,idade):
        self.__idade = idade

    #SECTION - CPF 
    @property 
    def cpf(self):
        return self.__cpf
    @cpf.setter 
    def cpf(self,cpf):
        self.__cpf = cpf

    #SECTION - Telefone 
    @property 
    def telefone(self):
        return self.__telefone
    @telefone.setter 
    def telefone(self,telefone):
        self.__telefone = telefone

    #SECTION - Email 
    @property 
    def email(self):
        return self.__email
    @email.setter 
    def email(self,email):
        self.__email = email