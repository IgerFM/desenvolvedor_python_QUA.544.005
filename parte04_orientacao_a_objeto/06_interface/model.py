#SECTION - Bibliotecas
from abc import ABC, abstractmethod

#NOTE - 4º Pilar Programação Orientada ao Objeto - Abstração
#NOTE - Uma classe abstrata não pode ser instanciada na main
#NOTE - É uma Super Classe
#NOTE - A INTERFACE NÃO TEM CONSTRUTOR
#SECTION - SC - Interface
class IConta(ABC): #NOTE - Deve ser definida com "I" e a primeira letra da classe em Maiusculo maiusculos
    @abstractmethod #NOTE - Transforma a subclasse em Abstrata
    def consultar(self):
        pass
    
    @abstractmethod
    def depositar(self,valor):
        pass
    
    @abstractmethod
    def sacar(self,valor):
        pass

#SECTION - C - Pessoa
class Conta(IConta):
    def __init__(self,titular,cpf,agencia,n_conta,saldo):
        self.__titular = titular
        self.__cpf = cpf
        self.__agencia = agencia
        self.__n_conta = n_conta
        self.__saldo = saldo
    
    #SECTION - Set && Get Titular
    @property
    def titular(self):
        return self.__titular
    @titular.setter
    def titular(self,titular):
        self.__titular = titular

    #SECTION - Set && Get CPF
    @property
    def cpf(self):
        return self.__cpf
    @cpf.setter
    def cpf(self,cpf):
        self.__cpf = cpf

    #SECTION - Set && Get Agencia
    @property
    def agencia(self):
        return self.__agencia
    @agencia.setter
    def agencia(self,agencia):
        self.__agencia = agencia

    #SECTION - Set && Get N_Conta
    @property
    def n_conta(self):
        return self.__n_conta
    @n_conta.setter
    def n_conta(self,n_conta):
        self.__n_conta = n_conta

    #SECTION - Set && Get Saldo
    @property
    def saldo(self):
        return self.__saldo
    @saldo.setter
    def saldo(self,saldo):
        self.__saldo = saldo

    #SECTION - Metodos Interface
    def consultar(self):
        print(f"\n{"-"*20} Dados da Conta {"-"*20}\n")
        print(f"Nome do Titular: {self.titular};")
        print(f"CPF: {self.cpf};")
        print(f"Agência: {self.agencia};")
        print(f"Conta: {self.n_conta};")
        print(f"Saldo: R$ {self.saldo:.2f}.")
        
    def depositar(self,valor):
        self.saldo += valor #NOTE - Decremento: Saldo - Valor
        return f"{"-"*20} Saldo Atual da Conta {"-"*20}\n\nSaldo: R$ {self.__saldo:.2f}.\n\n"
        
    def sacar(self,valor):
        self.saldo -= valor #NOTE - Decremento: Saldo - Valor
        return f"{"-"*20} Saldo Atual da Conta {"-"*20}\n\nSaldo: R$ {self.__saldo:.2f}.\n\n"
        