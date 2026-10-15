#
x = float(input("\nFale um número: ").replace(",","."))
y = float(input("\nFale um número: ").replace(",","."))

print(f"\n{'-'*20} Seguindo o seguinte menu: {'-'*20}\n")
print("1 - Soma")
print("2 - Subtração")
print("3 - Multiplicação")
print("4 - Divisão")

menu = input(f"\n{'-'*20} Qual operação que fazer {'-'*20}\n\n").strip()

match menu:

    case "1":
        print(f"\nA sua operação de soma resultou em {x + y}")
    case "2":
        print(f"\nA sua operação de subtação resultou em {x - y}")
    case "3":
        print(f"\nA sua operação de multiplicação resultou em {x * y}")
    case "4":
        print(f"\nA sua operação de divisão resultou em {x / y}")
    case _:
        print(f"\nA sua operação de inválida")