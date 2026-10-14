# Desafio

"""

Ler o nome de um aluno
Ler o número da turma
Ler as 3 notas
Calcular média
Caso seja menor que 70, esta reprovado
Deve mostra a soma das notas, a média das notas
Deve mostra se reprovou ou não

""" 

nome = input("\nCaro estudante, Insira o seu nome: ")
turma = int(input("\nInsira o número de sua turma: "))
nota = int(input("\nInsira o sua 1ª nota: "))
notb = int(input("\nInsira o sua 2ª nota: "))
notc = int(input("\nInsira o sua 3ª nota: "))

med = ((nota+notb+notc)/3)

if med >= 70:
    print(f"\nParabens {nome}, Você foi aprovado(a) com a média de {med} pontos!!!\n")
    print(f"Identificação:\nEstudante: {nome};\nTurma: {turma};")
    print(f"\nPontuação:\n1ª nota: {nota};\n2ª nota: {notb};\n3ª nota: {notc};\nSoma: {nota+notb+notc};\nMédia: {med};\n\nStatus: Aprovado(a)\n")

else: #elif med < 70:
    print(f"\nQue pena {nome}, Você reprovou com a média de {med} pontos\n")
    print(f"Identificação:\nEstudante: {nome};\nTurma: {turma};")
    print(f"\nPontuação:\n1ª nota: {nota};\n2ª nota: {notb};\n3ª nota: {notc};\nSoma: {nota+notb+notc};\nMédia: {med};\n\nStatus: Reprovado(a)\n")