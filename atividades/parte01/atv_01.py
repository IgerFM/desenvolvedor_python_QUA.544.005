#TODO - Atividade 01
import os
"""

Criar um programa que receba um nome, a massa eem kg e a altura em metros do usuario, e com isso, calcule IMC (indice de massa corporal) e finalize informando se o proprio esta (magro, gordo ou no peso ideal) levando em consideraçao o IMC ja calculado

"""

os.system ("cls" if os.name == "nt" else ("clean"))

try:

   
    print("\nBem vindo a calculadora do seu IMC (Indice de Massa Corporal)\n")
    # Pegar nome
    nom = input("Antes de começarmos, Digite o seu nome: ").strip().title()
    # Falar sobre o IMC
    print(f"\nMuito bom {nom}, agora dependendo de qual resultado da razão que der entre o seu peso divido pelo quadrado da sua altura, o seu indice sera dado com base na tabela abaixo")
    print(f"Menor que 18,5 {'-' * 18} Magreza")
    print(f"Entre 18,5 e 24,9 {'-' * 15} Normal")
    print(f"Entre 25 e 29,9 {'-' * 17} Sobrepeso")
    print(f"Entre 30 e 34,9 {'-' * 17} Obesidade grau |")
    print(f"Entre 35 e 39,9 {'-' * 17} Obesidade grau ||")
    print(f"Maior que 40 {'-' * 20} Obesidade grau |||\n")
    

    # Pegar peso
    pes = float(input("Digite o seu peso em 'Kg' (Kilogramas): ").replace(",","."))
    # Pegar altura
    alt = float(input("Digite a sua altura em 'm' (Metros): ").replace(",","."))
    # Calcular IMC
    imc = (pes/(alt*alt))
    # Informar o estado atual do individuo
    print(f"\nO seu IMC é atualmente de {imc:.2f}\n") 
    # :.2f Serve para definir que so deve escrever em até 2 algarismos apos o .
    if imc < 18.5:
        print(f"E atualmente {nom} esta em um estado de Magreza\n\nSe cuide, pois não é saudavel permanecer neste estado")

    elif imc >= 18.5 and imc <= 24.9:
        print(f"E atualmente {nom} esta em um estado Normal\n\nParabens!!! Continue saudavel assim")

    elif imc >= 25 and imc <= 29.9:
        print(f"E atualmente {nom} esta em um estado de Sobrepeso\n\nSe cuide, pois não é saudavel permanecer neste estado")

    elif imc >= 30 and imc <= 34.9:
        print(f"E atualmente {nom} esta em um estado de Obesidade grau |\n\nSe cuide, pois não é saudavel permanecer neste estado")

    elif imc >= 35 and imc <= 40:
        print(f"E atualmente {nom} esta em um estado de Obesidade grau ||\n\nSe cuide, pois não é saudavel permanecer neste estado")

    elif imc > 40:
        print(f"E atualmente {nom} esta em um estado de Obesidade grau |||\n\nSe cuide, pois não é saudavel permanecer neste estado")

    else:
        print("Algo deu errado")

except Exception as e:
    print(f"Algo deu errado\n\nError: {e}")

"""
Uma forma diferente de fazer isso seria

if imc < 18.5
elif imc < 25
elif imc < 30
elif imc < 35
elif imc < 40
elif imc >= 40
else

E isso se deve pois ele vai verificando em sequencia, onde se o ele so imprimira 1 condição e imprimira a primeira que atender ao problema
"""