#SECTION - Bibliotecas
from mod import eq_segura, limp

#SECTION - Algoritmo Principal
def main():
    limp()

    #SECTION - Entrada de dados
    a = float(input("Informe o valor de a: ").replace(",","."))
    b = float(input("Informe o valor de b: ").replace(",","."))
    c = float(input("Informe o valor de c: ").replace(",","."))
    
    limp()

    #SECTION - Verificação se os dados são 
    if a != 0:
        result = eq_segura(a,b,c)
        print("O resultado da sua equação é:")
        
        for x in result:
            print(f"x = {x}")
        
    else:
        print("Valores informados não são equação de 2º grau")


#SECTION - Algoritmo de Segurança
if __name__ == "__main__":
    main()