#SECTION - Bibliotecas
import os
from model import Pessoa

#SECTION - Limpa tela
def limpar(): 
    os.system("cls" if os.name == "nt" else "clear")

#SECTION - Body
def main ():
    usuario = Pessoa(nome="",idade=0,altura=0.0)
    
    limpar()

    usuario.nome = input("Informe o nome: ").strip().title()
    usuario.idade = int(input("Informe a sua idade: "))
    usuario.altura = float(input("Informe a sua idade: ").replace(",","."))

    limpar()

    #STUB - print(usuario)
    #STUB - print(f"A idade de {usuario.nome} é {len(usuario)} anos e mede {float(usuario)}m.")
    print(usuario)
    del(usuario) #NOTE - Estou apagando o objeto
    try:
        print(usuario)
    except Exception as e:
        print(e)

#SECTION - Runner
if __name__ == "__main__":
    main()