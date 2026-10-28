#SECTION - Bibliotecas
import os
import math

#SECTION - Limpa tela
def limp():

    os.system("cls" if os.name == "nt" else "clear")

#SECTION - Função de Segundo Grau  
def eq_segura(a,b,c): #NOTE - Bhaskara no python

    delta = (b**2)-(4*a*c)
    if delta > 0:
        x1 = (-b+(math.sqrt(delta)))/(2*a)
        x2 = (-b-(math.sqrt(delta)))/(2*a)
        #NOTE - O "yield" funciona como o return porem tem a diferença que ele não quebra o codigo, ele retorna um valor e depois retorna o outro
        yield x1 
        yield x2

    elif delta == 0:
        x = -b/(2*a)
        yield x

    else:
        yield "Não existem Raizes Reais"