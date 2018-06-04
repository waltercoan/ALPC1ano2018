'''
Implemente um programa para controlar o número de
crianças em uma creche. Para isso solicite o número
de turmas, e para CADA TURMA solicite o número da
sala, o numero de alunos matriculados e sexo de
cada uma das crianças (M – Masculino, F – Feminino).
Calcule e apresente em tela:
a. Número total de crianças na creche.
b. Média de alunos considerando todas as salas.
c. O numero da sala com o maior número de meninos.
d. O numero da sala com o menor número de meninas.
'''
totalunos = 0
maiornummeninos = 0
salamaiornum = 0
menornummeninas=0
salamenornum = 0

print("Digite o número de turmas")
numtotturmas = int(input())
for contaturma in range(numtotturmas):
    print("Turma: ", (contaturma+1))
    print("Digite o número da sala")
    numsala = int(input())
    print("Digite o número de alunos")
    numtotalunos = int(input())
    totalunos = totalunos + numtotalunos
    contameninos = 0
    contameninas = 0
    for contaaluno in range(numtotalunos):
        print("Aluno: ", (contaaluno + 1))
        print("Digite o sexo M-masculino F-feminino")
        sexo = input()
        if sexo == "m" or sexo == "M":
            contameninos = contameninos + 1
        else:
            contameninas = contameninas + 1
    if contameninos > maiornummeninos:
        maiornummeninos = contameninos
        salamaiornum = numsala

    if contaturma == 0:
        menornummeninas = contameninas
        salamenornum = numsala
    else:
        if contameninas < menornummeninas:
            menornummeninas = contameninas
            salamenornum = numsala

print("O número total de alunos e ", totalunos)
media = totalunos / numtotturmas
print("A média de alunos por turma é ", media)

print("A sala ", salamaiornum, " possui o maior número de meninos com ", maiornummeninos)
print("A sala ", salamenornum, " possui o menor número de meninas com ", menornummeninas)