#declaração de variaveis

nome = input("\nDigite o seu Nome: ").strip().title()
idade = int(input("\nDigite a sua Idade: "))

#.strip() serve para rirar espaços soltos no final, como (esta )
#.title() serve para deixar iniciais pelo 

"""
Sem o Operador Ternario

if idade >= 18: 
    print("\É maior de idade")


elif idade < 18: 
    print("\nÉ menor de idade\n")

else: : 
    print("\nOpção invalida\n")

"""

#Com o Operador Ternario
print(f"{nome} {"É maior de idade" if idade >= 18 else "É menor de idade"}")
