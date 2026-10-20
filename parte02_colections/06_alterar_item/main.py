import os

nomes = [
    'Alex',
    'Charlotte',
    'Scarlet',
    'Jonh',
    'Jason',
    'Michael',
    'Connor'
]

os.system('cls' if os.name == 'nt' else 'clear')

#for n, nome in enumerate(nomes): # jeito certo de usar for variavel n (n = quantidade) , variavel que recebe a variavel dessa posição
#    print(f"Indice {n + 1}: {nome}")

while True:
    
    for n, nome in enumerate(nomes): # jeito certo de usar for variavel n (n = quantidade) , variavel que recebe a variavel dessa posição
        print(f"Indice {n + 1}: {nome}")
    print('Opção 1 - alterar item da lista: ')
    print('Opção 2 - Encerrar programa')    
    menu = int(input('Opção Desejada: '))

    match menu:
        case 1:
            indice = int(input('Informe o indice que deseja alterar: '))
            nomes[indice-1] = input('Informe o novo nome: ')
            print('Item alterado')
            os.system('cls' if os.name == 'nt' else 'clear')
        case 2:
            os.system('cls' if os.name == 'nt' else 'clear')
            for n, nome in enumerate(nomes): # jeito certo de usar for variavel n (n = quantidade) , variavel que recebe a variavel dessa posição
                print(f"Indice {n + 1}: {nome}")
            break
        case _:
            print('Opção invalida')