#SECTION - Bibliotecas
from datetime import date
import pyautogui as auto #!SECTION

#SECTION - Main
def main():
    hoje = date.today().strftime("%Y/%m/%d")

    auto.PAUSE = 1
    auto.hotkey("win","r")
    auto.write("cmd")
    auto.press("enter")
    auto.write("cd C:/Users/ALUNO/igorvrs/workspaces/python/desenvolvedor_python_qua.544.005")
    auto.press("enter")
    auto.write("git add .")
    auto.press("enter")
    auto.write(f'git commit -m "{hoje} | Auto-Commit (PC Senai)"')
    auto.press("enter")
    auto.write("git push origin main")
    auto.press("enter")
    auto.write("exit")
    auto.press("enter")
#!SECTION

#SECTION - Runner
if __name__ == "__main__":
    main()
#!SECTION
#SECTION - Notes

#NOTE - Este.exe sera limitado, ele apenas dara o git add . e o git commit para este repositorio

#NOTE - Iremos aprender como gerar um .exe

#!SECTION