# tratamento de exceção

"""
-------------------- Esta é a forma correta de fazer um place hoader --------------------
try:
    pass
except Exception as e:
    print("ERROR 101")
"""

#

try:
    nome = input("\nInforme o seu nome: ").strip().title()
    idade = int(input("\nInforme a sua idade: "))

    print(f"\nNome de Usuario: {nome};")
    print(f"\nIdade do Usuario: {idade} anos.")

# Dentro do except Exception, o Exception tem que necessariamente ter o "E" maiusculo
except Exception as e: 
    print(f"\nERROR {e}")

finally:
    print("\nPrograma finalizado com sucesso")

"""
 -------------------- Comandos para a extensão "comment anchor" --------------------
# TODO
# FIXME
# NOTE
# REVIEW

"""