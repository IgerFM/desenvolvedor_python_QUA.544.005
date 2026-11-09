#SECTION - Bibliotecas
from model import Carro

#SECTION - Body
def main():
    #SECTION - Intanciamento
    carro = Carro(fabricante="",modelo="",ano=0,cor="",potencia=600)

    print(f"{"-"*20}Dados do veiculo{"-"*20}")
    carro.fabricante = input("Informe o fabricante: ").strip()
    carro.modelo = input("Informe o modelo: ").strip()
    carro.ano = int(input("Informe o ano: "))
    carro.cor = input("Informe o cor: ").strip()

    print(carro.exibir_detalhes())
    
#SECTION - Runner
if __name__ == "__main__":
    main()