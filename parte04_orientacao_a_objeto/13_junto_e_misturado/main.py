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
            saldo=0.0,
            titular=usuario,
            taxa=0.01
        )

    else:
        conta = ContaPolpanca(
            agencia=agencia,
            n_conta=f"{random.randint(10000,99999)}-2",
            saldo=0.0,
            titular=usuario,
            juros=0.01
        )


    while True:
        print("Opção 00 - Sair do Programa;")
        print("Opção 01 - Consultar dados da conta;")
        print("Opção 02 - Depositar Dinheiro;")
        print("Opção 03 - Sacar Dinheiro;")
        menu = input("Opção desejada: ").strip()
        match menu:
            case "0":
                break
            case "1":
                #TODO - 
                pass
            case "2":
                #TODO - 
                pass
            case "3":
                #TODO - 
                pass
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
    conta = input("Informe o tipo de conta quee deseja cria: ").strip()
    limpar()

    if conta == "1" or conta == "2":
        operacoes("1234-1",conta,usuario)

    else:
        print("Tipo de conta invalida!!!")


#SECTION - Runner
if __name__ == "__main__":
    try:
        main()
        print("Programa encerrado com sucesso!")
    except Exception as e:
        print(f"ERROR {e}")