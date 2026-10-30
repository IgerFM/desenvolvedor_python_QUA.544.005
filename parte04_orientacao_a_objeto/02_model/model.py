#SECTION - Classe de usuário
class Pessoa:
    def __init__(self,nome,idade,email):
        self.nome = nome
        self.idade = idade
        self.email = email

    def comprimentador(self):
        return f"Olá, o meu nome é {self.nome}, tenho {self.idade} anos e o meu email é {self.email}."
