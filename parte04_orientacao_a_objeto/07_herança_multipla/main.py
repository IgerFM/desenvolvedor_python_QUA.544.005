#SECTION - Bibliotecas
import os
from model import CarroAviao

#SECTION - Limpa Tela
def limp():
    os.system("cls" if os.name == "nt" else "clear")


#SECTION - Body
def main():

    aviarro = CarroAviao(
    cambio = True,
    estepe = False,
    porta_malas = False,
    volante = True,
    retrovisor = True,
    buzina = True,
    escapamento = True,
    asa = True,
    turbina = True,
    aerofolio = True,
    calda = True,
    manche = True,
    caixa_preta = True,
    transponder = True
    )

    limp()
    print(f"Câmbio: {aviarro.cambio}")
    print(f"Estepe: {aviarro.estepe}")
    print(f"Porta Malas: {aviarro.porta_malas}")
    print(f"Volante: {aviarro.volante}")
    print(f"Retrovisor: {aviarro.retrovisor}")
    print(f"Buzina: {aviarro.buzina}")
    print(f"Escapamento: {aviarro.escapamento}")
    print(f"Asa: {aviarro.asa}")
    print(f"Turbina: {aviarro.turbina}")
    print(f"Aerofolio: {aviarro.aerofolio}")
    print(f"Calda: {aviarro.calda}")
    print(f"Manche: {aviarro.manche}")
    print(f"Caixa Preta: {aviarro.caixa_preta}")
    print(f"Transponder: {aviarro.transponder}")
    

    #TODO - 
    pass

#SECTION - Rodar
if __name__ == "__main__":
    main()