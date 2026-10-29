#SECTION - Bibliotecas
import os

#SECTION - Lambdas
limp = lambda: os.system("cls" if os.name == "nt" else "clear")

#SECTION - Sequencia de Fibonacci
#def sefibo(x):
def main():
    limp()
    x = int(input("Insira um número inteiro: ").strip())
    n1 = x
    n2 = x
    n3 = x
    for fi, n1, n2 , n3 in x:
        print(n1)
        print(n2)
        n3 == n2
        n2 == n1+n2
        n1 == n3
        fi += 1

#SECTION - Função Principal
    #sefibo(x)

#SECTION - Algoritmo de Segurança
if __name__ == "__main__":
    main()

#FIXME - Parte 03 Atividade 02
"""
#NOTE - Crie um programa em que o usuário número inteiro e o programa retorne a sequencia de Fibonacci
"""