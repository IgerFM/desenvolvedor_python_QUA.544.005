#SECTION - Bibliotecas
import os

#NOTE - A lambda serve resumidamente como uma abreviatura para usar as funções
#NOTE - A lambda funciona como o operador ternario

#SECTION - Lambdas
limpar = lambda: os.system("cls" if os.name == "nt" else "clear")
artri = lambda b,h: (b*h)/2

#SECTION - Função Principal
def main():
    limpar()
    b = float(input("Informe a base: ").replace(",","."))
    h = float(input("Informe a altura: ").replace(",","."))    
    limpar()
    print(f"A sua area é de: {artri(b,h)}.")

#SECTION - Algoritmo de Segurança
if __name__ == "__main__":
    main()
