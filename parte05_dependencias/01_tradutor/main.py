#SECTION - Bibliotecas 
import os
from translate import Translator #ANCHOR - Biblioteca externa
#!SECTION

#SECTION - Limpa Tela
def limpar():
    os.system("cls" if os.name == "nt" else "clear") #!SECTION


#SECTION - Tradutor
def traduzir(texto):
    tradutor = Translator(to_lang="pt")
    return tradutor.translate(texto) #!SECTION

#SECTION - Body
def main():
    limpar()
    texto = input("Oque gostaria de traduzir? ")
    print(f"\nTexto traduzido: \n{traduzir(texto)}")
#!SECTION

#SECTION - Runner
if __name__ == "__main__":
    main() #!SECTION

""" #SECTION - Anotações aula de hoje

#NOTE - A partir desta parte 05, a .venv deve ser criada dentro da pasta de CADA programa.

#NOTE - Fazemos isso para evitar que as bibliotecas não sejam instaladas dentro do python em si

#NOTE - A .venv isola as dependencias de cada projeto que serão aplicadas e trabalhadas a partir de agora.

#NOTE - As dependencias dão a incrementada que deixa o python mais potente

#NOTE - Estamos "Aprimorando" o comando import, ou seja, quando chamarmos biblioteca x, existe a chance do python não ter essa biblioteca baixada previamente

#NOTE - Caso não esteja baixada previamente, devemos procurar ela no site "https://pypi.org/" onde existe uma grande chance de acharmos o que queremos e é certeiro de acharmos a biblioteca expecifica que queremos

#NOTE - A partir da aula de hoje provavelmente TODOS os programas terão que instalar alguma biblioteca

#NOTE - Para instalar alguma biblioteca, devemos usar um gerenciador de pacotes, para este caso é o o pip

#NOTE - DEVEMOS RODAR O CODIGO "PIP" DENTRO DA PASTA QUE TIVER A .VENV, CASO CONTRARIO, A BIBLIOTECA SERA INSTALADO DIRETAMENTE NO PYTHON

#NOTE - Neste codigo iremos digitar no cmd o seguinte codigo "pip install deep_translator"

#NOTE - Para desinstalar, devemos digitar no cmd "pip uninstall deep_translator"

#NOTE - Para saber o que esta instalado na .venv, deve se executar o comando no cmd "pip freeze"

#NOTE - Para salvar as bibliotecas de um projeto x, devemos executar no cmd "pip freeze > requirements.txt"

""" #!SECTION
""" #SECTION - Algoritmo Defeituoso por conta da biblioteca - Biblioteca desinstalada
#SECTION - Bibliotecas 
import os
from deep_translator import GoogleTranslator #ANCHOR - Biblioteca externa (Desinstalada)
#!SECTION

#SECTION - Limpa Tela
def limpar():
    os.system("cls" if os.name == "nt" else "clear") #!SECTION


#SECTION - Tradutor
def traduzir(texto):
    tradutor = GoogleTranslator(source="auto",target="pt")
    return tradutor.translate(texto) #!SECTION

#SECTION - Body
def main():
    limpar()
    texto = input("Oque gostaria de traduzir? ")
    print(f"\nTexto traduzido: \n{traduzir(texto)}")
#!SECTION

#SECTION - Runner
if __name__ == "__main__":
    main() #!SECTION

""" #!SECTION
