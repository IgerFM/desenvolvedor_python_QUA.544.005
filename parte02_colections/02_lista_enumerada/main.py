# lista de nomes
nomes = ['João', 'Maria', 'José', 'Alex', 'Fernanda', 'Epaminondas']
# Diferente do C, no python pode se misturar coisas diferentes dentro da array

#lista numerada
for n, nome in enumerate(nomes, start=1):
    print(f'\n{n}º nome: {nome}')
