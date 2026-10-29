import os

def limpar():
    os.system("cls")

def fatorial(n):
    return 1 if n == 1 else n*fatorial(n-1)

def main():
    limpar()
    n = int(input("Digite o seu número inteiro: "))
    try:
        print(f"O fatorial de {n}! vale: {fatorial(n)}")

    except Exception as e:
        print(f"ERROR {e}")

if __name__ == "__main__":
    main()