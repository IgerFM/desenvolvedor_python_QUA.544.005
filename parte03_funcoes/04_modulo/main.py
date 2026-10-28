#SECTION - Bibliotecas
import modulo

#SECTION - Algoritmo principal
modulo.limp()
while True:
    print("\nOpção 01 - Calcula a Área do Quadriltero")
    print("Opção 02 - Calcula a Área do Circulo")
    print("Opção 03 - Calcula a Comprimento do Circulo")
    print("Opção 04 - Sair do Programa")
    menu = input("\nOpção desejada: ").strip()
    modulo.limp()

    match menu:

        case "1":

            b = float(input("Informe a base: ").replace(",","."))
            h = float(input("informe a altura: ").replace(",","."))
            a = modulo.arquad(b, h)
            print(f"A área do seu quadrilátero é: {a}")
            continue

        case "2":

            r = float(input("Informe o raio: ").replace(",","."))
            a = modulo.arcir(r)
            print(f"A área do seu circulo é: {a}")
            continue

        case "3":

            r = float(input("Informe o raio: ").replace(",","."))
            c = modulo.comcir(r)
            print(f"O comprimento do seu circulo é: {c}")

        case "4":

            print("Programa Encerrado com Sucesso")
            break

        case _:

            print("Opção invalida")
            continue