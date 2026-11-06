#SECTION - Bibliotecas
import os
import time
import random
from model import Conta

#SECTION - Limpa Tela
def limp():
    os.system("cls" if os.name == "nt" else "clear")

#SECTION - Main
def main():
    #SECTION - Instanciamento
    cc = Conta(
        titular="",
        cpf="",
        agencia="1305-1",
        n_conta=f"{random.randint(10000,99999)}-1",
        saldo=0.0
        )

    limp()

    cc.titular = input("Digite o nome do titular da conta: ").strip().title()
    cc.cpf = input("Digite o CPF do titular da conta: ").strip()

    limp()
    while True:
        print(f"{'-'*20}🐍KOBRANK🐍{'-'*20}")
        print("Opção 00 - Encerrar Programa;")
        print("Opção 01 - Consultar Saldo;")
        print("Opção 02 - Depositar Saldo;")
        print("Opção 03 - Sacar Saldo;")
        menu = input("Qual opção gostaria de executar? ")
        limp()
        match menu:
            case "0":
                break
            case "1":
                cc.consultar()
                pass
            case "2":
                valor = float(input("Informe o valor que deseja depositar: R$ ").replace(",","."))
                saldo = cc.depositar(valor)
                limp()
                print(f"O deposito foi efetuado.\n\n")
                time.sleep(2)
                print(f"{saldo}")
                continue
            case "3":
                valor = float(input("Informe o valor que deseja sacar: R$ ").replace(",","."))
                if valor <= cc.saldo:
                    saldo =cc.sacar(valor)
                    limp()
                    print(f"Saque efetuado com sucesso.\n\n")
                    time.sleep(2)
                    print(f"{saldo}")
                else:
                    print("Não foi possivel efetivar o saque:")
                continue
            case _:
                print("Opção Invalida")
                continue

#SECTION - Rodador
if __name__ == "__main__":
        main()