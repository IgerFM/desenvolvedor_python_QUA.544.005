# Criar um algoritimo que leia 2 numeros
# Mostre no final qual número é o maior


"""

---ENTRADA---
Leia um número 
Leia outro número

---PROCESSAMENTO---
Verifica quem é o maior

---SAIDA---
Mostra o maior

"""
print("\nInsira 2 números e eu direi qual número deles é maior que o outro")

numa = int(input("\nInsira o número 1: "))
numb = int(input("\nInsira o número 2: "))

if numa > numb:
    print(f'\nO número 1 "{numa}" que é o maior número\n')

elif numa < numb:
    print(f'\nO número 2 "{numb}" que é o maior número\n')

else: #elif numa == numb:
    print(f'\nO número 1 "{numa}" e o número 2 "{numb}" são iguais\n')