#SECTION - Bibliotecas
import os
import pyjokes
from translate import Translator

#SECTION - Limpa Tela
def limpar():
    os.system("cls")

#SECTION - Gerador de Piadas
def gerador_piadas():
    tradutor = Translator(to_lang="pt")
    piadas = pyjokes.get_joke()
    return f"{piadas}\n\n{tradutor.translate(piadas)}\n\n"

#SECTION - Body
def main():
    while True:
        print("Opção 00 - Sair do Programa; ")
        print("Opção 01 - Gerar piada aleatória; ")
        menu = input("Opção desejada: ").strip()
        limpar()
        match menu:
            case "0":
                break
            case "1":
                print(gerador_piadas())
                continue
            case _:
                print("Opção invalida")
                continue

#SECTION - Runner
if __name__ == "__main__":
    main()
#NOTE - Para instalar mais de 1 biblioteca ao mesmo tempo, digite no cmd "pip install pyjokes translate" onde as bibliotecas estão separadas pelo espaço