# Lista de usuarios
# Deve exibir os dados de cada usuario

usuarios = [
    {
        'nome': "Alex Machado", 
        'idade': 41, 
        'email': "alex@gmail.com", 
    }, 
    {
        'nome': "Joana de Silva", 
        'idade': 18, 
        'email': "joana@hotmail.com", 
    }, 
    {
        'nome': "Karolyne de Souza", 
        'idade': 21, 
        'email': "karol@yahoo.com.ber", 
    }

]

for usuario in usuarios:
    print("")
    for chave, valor in usuario.items():
        print(f"{chave.capitalize()}: {valor}")
    print(f"\n{'-'*80}")