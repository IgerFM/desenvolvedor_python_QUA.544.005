usuario = {
    'nome': "Alex Machado", 
    'idade': 41, 
    'email': "alex@gmail.com", 
    'telefone': "(61) 9 8765-4321", 
    'endereço': "Campo da Esperança", 
}


print("")
n = 1
for chave, valor in usuario.items():
    print(f"(0{n})ª {chave}: {valor}")
    n = n+1

choskey = input("\nInforme qual chave gostaria de excluir: ")
del usuario[choskey] #NOTE - jeito certo de excluir uma chave expecifica

print("")
n = 1
for chave, valor in usuario.items():
    print(f"({n})ª {chave}: {valor}")
    n = n+1