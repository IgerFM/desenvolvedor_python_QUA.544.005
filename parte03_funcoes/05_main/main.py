#SECTION - Bibliotecas
import os
import math

#SECTION - Limpa tela
def limp():

    os.system("cls" if os.name == "nt" else "clear")

#SECTION - Calcular raiz
def raiz(n):

    return math.sqrt(n)

#SECTION - Algoritmo Principal
def main():

    limp()
    n = int(input("Informe um número que gostaria de calcular a raiz: "))   
    print(f"A raiz de {n} é de: {raiz(n)}.")

#SECTION - Algoritimo de seguraça para impedir que o codiso principal seja importao inconsequentimente
if __name__ == "__main__":

    main()
