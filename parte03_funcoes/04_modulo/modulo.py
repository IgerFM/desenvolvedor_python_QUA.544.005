#SECTION - Bibliotecas
import os
import math

#SECTION - Limpa tela
def limp():
    os.system("cls" if os.name == "nt" else "clear")

#SECTION - Calcular a área de um quadrado
def arquad(b, h):
    return b*h

#SECTION - Calcula a átea de um circulo
def arcir(r):
    return math.pi*(r**2)

#SECTION - Calcula o comprimento do circulo
def comcir(r):
    return 2*math.pi*r