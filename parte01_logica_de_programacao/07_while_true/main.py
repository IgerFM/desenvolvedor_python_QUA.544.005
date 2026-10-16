# O programa deve receber varios dados de alunos
import os

# Limpar a tela windows
os.system("cls" if os.name == "nt" else "clear")

print("\n\nBem vindo(a) ao sistema de averiguação de nota: ")

while True:

    try:
# Receber nome
        aluno = input("\n\nInforme o nome do aluno: ").strip().title()
# Receber nota (de 0 a 10 com numeros quebrados)            
        nota = float(input("Informe a nota do aluno entre 0 a 10: ").replace(",","."))
        if nota >= 0 and nota <= 10:
            if nota >= 7:
                 print(f"\n{aluno} esta aprovado")
            elif nota >= 5:
                 print(f"\n{aluno} esta de recuperação")
            else:
                 print(f"\n{aluno} esta reprovado")
            
        else:
            print("\nNota inválida.")
            
# Avisar se passou ou não
    except Exception as e:
        print(f"\nNão foi possivel calcular a nota\n\nError: {e}")

    continuar = input("\nDeseja inserir outra nota?\n\nDigite 'Sim' para prosseguir, ou qualquer outro valor para encerrar: ").strip().lower()

    if continuar == "sim": #No caso de string, tambem funcionaria (if continuar is "sim":)
        os.system("cls" if os.name == "nt" else "clear")
        continue
    # Para diferente é !=

    else:
        break