#SECTION - Bibliotecas
import os

#SECTION - Lambdas
limp = lambda: os.system("cls" if os.name == "nt" else "clear")
pg = lambda x: x*2


#SECTION - Função Principal
def main():

    #SECTION - Lista
    numeros = [1,2,3,4,5,6,7,8,9]
    
    limp()
    print(numeros)

    #NOTE - A função "list" gera uma nova lista com os parametros entre os ()
    #NOTE - A função aplicar a função dentro dentro da lista da seguinte forma "map(função , lista)"
    numeros_pg = list(map(pg, numeros))
    print(numeros_pg)

#SECTION - Algoritmo de Segurança
if __name__ == "__main__":
    main()