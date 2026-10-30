#SECTION - Bibliotecas
import os
import time
import math

#SECTION - Lambdas
limp = lambda: os.system("cls" if os.name == "nt" else "clear")

#SECTION - Sequencia de Fibonacci falha que eu produzi
"""def sefibo(n):
    p1 = (1/(math.sqrt(5))) * (((1+math.sqrt(5))/2) ** n)
    p2 = (1/(math.sqrt(5))) * (((1-math.sqrt(5))/2) ** n)
    return p1 - p2"""

#SECTION - Sequencia de Fibonacci - funcional que o professor fez
#def fibonnaci(n):
    #return n if n <= 1 else fibonnaci(n-1) + fibonnaci (n-2)

#SECTION - Função Principal
def main():
    limp()
    n = int(input("Insira um número inteiro: ").strip())
    #print(fibonnaci(n))
    #print(sefibo(n))
    
    """
    while True:
        print(f"{sefibo(n):.2f}")
        n += 1
        time.sleep(2)""" #NOTE - Algoritmo falho


#SECTION - Algoritmo de Segurança
if __name__ == "__main__":
    main()

#FIXME - Parte 03 Atividade 02
"""
#NOTE - Crie um programa em que o usuário número inteiro e o programa retorne a sequencia de Fibonacci
"""