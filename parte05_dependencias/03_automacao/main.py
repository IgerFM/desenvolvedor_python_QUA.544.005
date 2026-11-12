#SECTION - Bibliotecas
import pyautogui as auto #!SECTION

#SECTION - Main
def main():
    auto.PAUSE = 0.75
    auto.press("win")
    auto.write("firefox")
    auto.press("enter")
    auto.write("https://github.com/dev-alexmachado/desenvolvedor_python_qua.544.005/tree/main")
    auto.press("enter")
    auto.sleep(2)
    auto.hotkey("ctrl","t")
    auto.write("https://www.sistemafibra.org.br/senai")
    auto.press("enter")
    auto.sleep(2)
    auto.hotkey("ctrl","shift","p")
    auto.sleep(2)
    auto.write("metropoles.com")
    auto.press("enter")

#!SECTION
#SECTION - Runner
if __name__ == "__main__":
    main() #!SECTION

#SECTION - Notas

#NOTE - A pyautogui é uma biblioteca poderosa que controla o mouse e teclado

#NOTE - Ja o selene, serve para automatizar em web como o pyautogui, porem a diferença é que ele so fuynciona em web (Se eu entendi certo)

#!SECTION