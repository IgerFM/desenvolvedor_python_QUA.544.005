# App to do
import os

tarefas = []

os.system('cls' if os.name == 'nt' else 'clear')

while True:

    print('O que gostaria de fazer agora?\n')
    print('Digite (01) - Para Inserir um novo item')
    print('Digite (02) - Para Mostrar a lista e Encerrar o programa')   
    menu = input('\nOpção desejada: ').strip()

    match menu:
        case '1':
            new_task = input('Insira a nova tarefa: ')
            tarefas.append(new_task) # Insere o item digitado na lista
            continue
        case '2':
            os.system('cls' if os.name == 'nt' else 'clear')
            for n, tarefa in enumerate(tarefas, start=1):
                print(f'\n{n}ª Tarefa: {tarefa}\n')
            break
        case _:
            os.system('cls' if os.name == 'nt' else 'clear')
            print('\n\nOpção invalida\n\n')