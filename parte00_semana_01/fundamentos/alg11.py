#algoritimo onde lê 3 notas e da a media delas

nota = int(input("\nDigite a sua nota a: "))
notb = int(input("Digite a sua nota b: "))
notc = int(input("Digite a sua nota c: "))

med = ((nota + notb + notc)/ 3)

print (f"\nParabens (ou não), a sua media é de {med}\nOnde a soma das suas notas é de {nota+notb+notc}")
print (f"\nParabens (ou não), a sua media é de " +str(med))


"""
+str(var) transforma o valor de float para string

print("texto"+(numero)) ERRADO
print("texto"+str(numero)) CERTO
"""