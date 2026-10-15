"""
São 3 tipos para estrutoras de decisão
Servem pra mais de 1 condicional
and = e
or = ou
not = não
"""

# Ao se trabalhar com nome, é bem inportante utilizar o .stripe() .title() como no exemplo abaixo
nome = input("\nInsira a seu nome: ").strip().title()
idade = int(input("\nInsira a sua idade: "))
# .replace(",",".")) serve para transformar uma , em . dentro de um float para evitar falha no programa
altura = float(input("\nInsira a sua altura: ").replace(",","."))

# verificar a altura e idade do pagante

if idade >= 12 and altura >= 1.35:
    print(f"\nAcesso liberado para {nome}")

#elif idade < 12:
#    print(f"\nAcesso negado para {nome} por conta de idade insuficiente")
#elif altura < 1.35:
#    print(f"\nAcesso negado para {nome} por conta de altura insuficiente")
#elif idade < 12 and altura < 1.35:
#    print(f"\nAcesso negado para {nome} por conta de idade e altura insuficiente")

else:
    print(f"\nAcesso negado para {nome}")
