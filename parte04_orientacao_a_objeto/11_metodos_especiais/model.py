#SECTION - C - Pessoa
class Pessoa:
    def __init__(self,nome,idade,altura):
        self.__nome = nome
        self.__idade = idade
        self.__altura = altura

    #SECTION - M - String
    #NOTE - Este metodo retorna uma string
    def __str__(self):
        #STUB - return f"Objeto {self.nome} criado com sucesso!"
        return f"Nome: = {self.nome}\nIdade: = {len(self)}\nAltura: = {float(self)}"

    #SECTION - M - Int
    #NOTE - Este metodo retorna um int (Inteiro)
    def __len__(self):
        return self.idade

    #SECTION - M - Float
    #NOTE - Este metodo retorna um float
    def __float__(self):
        return self.altura

    #SECTION - M - Destrutor
    def __del__(self):
         print(f"Objeto {self.nome} destruido com sucesso!")
