# teclado

nome = input("Digite o seu nome: \n")
  idade = int(input("Digite a sua idade: \n"))

# processamento

if idade >= 18:
    print(f"{nome}[aaa] é maior de idade\n")
    r = (f"{nome} é maior de idade\n")


else: 
    print(f"{nome} é menor de idade\n")
    r = (f"{nome} é menor de idade\n")

# imprimir

print(f"{r}\n")
print("Programa encerrado com sucesso...\n")

"""
(f "texto{variavel}") ERRADO
(f"texto{variavel}") CERTO
"""
