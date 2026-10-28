#SECTION - Bibliotecas
import os

#SECTION - Limpa tela
def limp():
    os.system("cls" if os.name == "nt" else "clear")

#STUB - 
def eq_priga(a, b):
    return -b / a #NOTE - Jeito certo de calcular equação de primeiro grau dentro de um codigo