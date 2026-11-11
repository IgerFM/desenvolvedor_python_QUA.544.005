#SECTION - Bibliotecas
import os
import random
from model import ContaCorrente,ContaPolpanca,Pessoa

#SECTION - Limpa tela
def limpar():
    os.system("cls" if os.name == "nt" else "clear")

#SECTION - Operações
def operacoes(agencia,conta,usuario): #TODO - Função operações esta incompleta
    if conta == "1":
        conta = ContaCorrente(
            agencia=agencia,
            n_conta=f"{random.randint(10000,99999)}-1",
            tipo_conta="Conta Corrente",
            saldo=0.0,
            titular=usuario,
            taxa=0.01
        )

    else:
        conta = ContaPolpanca(
            agencia=agencia,
            n_conta=f"{random.randint(10000,99999)}-2",
            tipo_conta="Conta Polpança",
            saldo=0.0,
            titular=usuario,
            juros=0.1
        )


    while True:
        print("Opção 00 - Sair do Programa;")
        print("Opção 01 - Consultar dados da conta;")
        print("Opção 02 - Depositar Dinheiro;")
        print("Opção 03 - Sacar Dinheiro;")
        menu = input("Opção desejada: ").strip()
        limpar()

        match menu:
            case "0":
                break

            case "1":
                conta.consultar()
                continue

            case "2":
                valor = float(input(f"Quanto gostaria de depositar: R$ ").replace(",","."))
                saldo = conta.depositar(valor)
                limpar()
                print(f"Deposito efetuado com sucesso,.\nSaldo atual: R${saldo:.2f}")
                continue

            case "3":
                valor = float(input(f"Quanto gostaria de depositar: R$ ").replace(",","."))
                if valor < conta.saldo:
                    saldo = conta.sacar(valor)
                    limpar()
                    print(f"Saque efetuado com sucesso,.\nSaldo atual: R${saldo:.2f}")
                else:
                    print("Não foi possivel efetuar o saque")
                continue

            case _:
                print("Opção invalida!!!")
                continue

#SECTION - Body
def main():
    #SECTION - Intanciamento
    usuario = Pessoa(nome="",cpf="")

    limpar()
    usuario.nome = input("Insira o seu nome: ").strip().title()
    usuario.cpf = input("Insira o seu cpf: ").strip()
    limpar()

    print("Opção 01 - Criar Conta Corrente;")
    print("Opção 02 - Criar Conta Polpança;")
    conta = input("Informe o tipo de conta que- deseja cria: ").strip()
    limpar()

    if conta == "1" or conta == "2":
        operacoes("1234-1",conta,usuario)

    else:
        print("Tipo de conta invalida!!!")


#SECTION - Runner
if __name__ == "__main__":
    #try:
        main()
        print("Programa encerrado com sucesso!")
    #except Exception as e:
        #print(e)