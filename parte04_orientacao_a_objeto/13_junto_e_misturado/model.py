#SECTION - Bibliotecas
from abc import ABC,abstractmethod
from dataclasses import dataclass

#SECTION - I - IConta
class IConta(ABC):
    
    #SECTION - AM - consultar
    @abstractmethod
    def consultar(self):
        pass
    
    #SECTION - AM - depositar
    @abstractmethod
    def depositar(self):
        pass
    
    #SECTION - AM - sacar
    @abstractmethod
    def sacar(self):
        pass

#SECTION - DC - Pessoa
@dataclass
class Pessoa:
    nome: str
    cpf: str

    def __str__(self):
        return f"Nome: {self.nome}\nCPF: {self.cpf}."

    def __del__(self):
        print(f"O objeto {self.nome} foi destruido com sucesso")

#SECTION - DC - Conta
@dataclass
class Conta(IConta):
    agencia: str
    n_conta: str
    saldo: float
    titular: Pessoa

    #SECTION - SM - string
    def __str__(self):
        #return f"\n{'-'*20}Dados do Titular da conta{'-'*20}\n\ntitular: {self.titular}\n{'-'*20}Dados da conta{'-'*20}\n\nagencia: {self.titular}\nn_conta: {self.titular}\nsaldo: {float(self):.2f}\n"
        return f"Conta n.{self.n_conta} criada com sucesso!"
    
    #SECTION - SM - float
    def __float__(self):
        return self.saldo

    
    #SECTION - M - __del__
    def __del__(self):
        print("A conta foi destruida com sucesso")
    
    #SECTION - M - consultar
    def consultar(self):
        print(f"{'-'*20} Titular da Conta {'-'*20}")
        print(self.titular)
        print(f"{'-'*20} Dados da Conta {'-'*20}")
        print(f"Agencia: {self.agencia}")
        print(f"Número da Conta: {self.n_conta}")
        print(f"Saldo: R${float(self):.2f}")
        print(self)
    
    #SECTION - M - depositar
    def depositar(self,valor):
        self.saldo += valor
        return self.saldo
    
    #SECTION - M - sacar
    def sacar(self,valor):
        self.saldo -= valor
        return self.saldo

#SECTION - DC - Conta Corrente
class ContaCorrente(Conta):
    taxa: float

    def sacar(self,valor,taxa):
        valor += taxa
        return super().sacar(valor)

#SECTION - DC - Conta Polpança
class ContaPolpanca(Conta):
    juros: float

    def depositar(self,valor,juros):
        valor += (juros/100)
        return super().depositar(valor)