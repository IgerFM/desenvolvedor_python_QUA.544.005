#SECTION - Bibliotecas
from mod import limp
from mod import eq_priga

#SECTION - Algoritmo Principal
def main():
    limp()
    a = float(input("Informe o valor de 'x': ").replace(",","."))
    b = float(input("Informe o valor de 'y': ").replace(",",".")) 
    x = eq_priga(a,b)
    limp()
    print(f"O valor de x é {x}.")

#SECTION - Algoritmo de segurançã
if __name__ == "__main__":
    main()