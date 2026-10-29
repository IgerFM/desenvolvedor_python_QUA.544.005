#SECTION - Bibliotecas
import os
from mod import planeta , limp

#SECTION - Função Principal
def main():

    limp()
    p = float(input("Insira o seu peso: ").strip())
    world = input("Insira um planeta do Sistema Solar: ").strip().lower()
    limp()
    print(planeta(world , p))

#SECTION - Algoritmo de Segurança
if __name__ == "__main__":
    main()

#FIXME - Parte 03 Atividade 01
"""
#NOTE - Crie um programa que calcule o peso de uma pessoa em um planeta do sistema solar escolhido por ela
#NOTE - Pesquisar pela aceleração da gravidade em cada planeta;
#NOTE - Inclua a blua na lista de Planetas;
"""