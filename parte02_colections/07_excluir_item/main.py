# O usuario informa e exclui itens da lista

lista = [
    'Abacate', 
    'Banana', 
    'Maçã', 
    'Uva', 
    'Pera', 
    'Ameixa', 
    'Laranja', 
    'Limão', 
    'Morango', 
    'Melancia', 
    'Goiaba', 
    'Maracuja', 
    'Pera', 
    'Cupuaçu', 
    'Bacuri', 
    'Manga' 
]

while True:
    for n, fruta in enumerate(lista):
        print(f'{n+1}ª Fruta: {fruta}')
        
    #break
    print('01 - Excluir Fruta')
    print('02 - Encerrar programa')
    menu = input('Opção desejada: ')

    match menu:
        case '1':
            indice = int(input('\nInforme o indice a ser excluidor: '))
            del(lista[indice-1]) # Exclui o item selecionado dentro da lista
            print('\nFruta excluida com sucesso!\n')
            continue
        case '2':
            break
        case _:
            print('Opção invalida')
            continue