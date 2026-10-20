cidades = [
    'Taguatinga',
    'Plano Piloto',
    'Santa Maria',
    #'Ceilândia',
    'Gama',
    'Samambaia',
    'Taguatinga',
    'Planaltina',
    'Plano Piloto',
    'Brazlândia',
    'Plano Piloto'
]

# O usuarioi informa o item pesquisado
item = input("\n\nInforme uma cidade de brasilia: ").strip().title()

print(f'\n{item} foi encontrado, {cidades.count(item)} vezes na lista')