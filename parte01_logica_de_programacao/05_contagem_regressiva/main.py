import os
# A biblioteca os serve para mexer no terminal
import time
# A biblioteca time reduz a velocidade do codigo

os.system("cls")

n = int(input("\nInforme um número inteiro: "))

while n >= 0:
    os.system("cls")
    print(f"\n{n}...\n")
    time.sleep(1)
    n -= 1

#Kabbom?
#Yes Ricko, Kaboom
os.system("cls")
print(f"\n{'♨︎'*20}  BOOM {'♨︎'*20}\n")
