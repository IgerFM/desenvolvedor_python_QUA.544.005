ds = int(input("Digite um numero de 1 a 7 e direi qual dia da semana pertence esse número: "))

match ds:
    case 1:
        print("\nDomingo\n")

    case 2:
        print("\nSegunda\n")

    case 3:
        print("\nTerça\n")

    case 4:
        print("\nQuarta\n")

    case 5:
        print("\nQuinta\n")

    case 6:
        print("\nSexta\n")

    case 7:
        print("\nSabado\n")

    case _:
        print("\nEste dia é inválido\n")
