#SECTION - Bibliotecas
import os
import random
from model import Conta

#SECTION - Limpa Tela
def limp():
    os.system("cls" if os.name == "nt" else "clear")

#SECTION - Main
def main():
    #SECTION - Instanciamento
    cc = Conta(titular="",
               cpf="",
               agencia="1305-1",
               n_conta=f"{random.randint(10000,99999)}-1",
               saldo=0.0
               )
    #TODO - Terminar amanhã
    pass

#SECTION - Rodador
if __name__ == "__main__":
    main()