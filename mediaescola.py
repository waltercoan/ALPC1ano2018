print("Digite o numero de turmas da escola")
numturmas = int(input())
print("Digite o numero de alunos")
numalunos = int(input())
somamedturma = 0
contaturma = 0
while contaturma < numturmas:
    print("Turma: ", contaturma + 1)
    contaaluno = 0
    somamedalunos = 0
    while contaaluno < numalunos:
        print("Digite a media do aluno")
        mediaaluno = float(input())
        somamedalunos = somamedalunos + mediaaluno
        contaaluno = contaaluno + 1
    mediaturma = somamedalunos / numalunos
    print("A media da turma e", mediaturma)
    somamedturma = somamedturma + mediaturma
    contaturma = contaturma + 1
mediaescola = somamedturma / numturmas
print("A media da escola e ", mediaescola)
