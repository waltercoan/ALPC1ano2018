'''Faça um algoritmo que calcule a média
de todas as turmas de uma escola. Considere
como entradas o número de turmas e o número
de alunos de cada turma. A média de cada
turma deve ser apresentada, além da média
geral, que será o resultado da média
das turmas.'''
print("Digite o número de turmas")
numturmas = int(input())
print("Digite o número de alunos por turma")
numalunos = int(input())

somamedturmas=0
contaturma = 0
while contaturma < numturmas:
    contaaluno = 0
    somamedalunos = 0
    while contaaluno < numalunos:
        print("Digite a média do aluno")
        mediaaluno = float(input())
        somamedalunos = somamedalunos + mediaaluno
        contaaluno = contaaluno + 1
    mediaturma = somamedalunos / numalunos
    print("A media da turma e", mediaturma)
    somamedturmas = somamedturmas + mediaturma
    contaturma = contaturma + 1
mediaescola = somamedturmas / numturmas
print("A média da escola e:", mediaescola)