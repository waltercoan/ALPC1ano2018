print("Digite o numero de turmas")
numturmas = int(input())

totalunos = 0
amaiorqtdmeninos = 0
salamaiorqtdmeninos=0
amenorqtdmeninas = 0
salamenorqtdmeninas=0
for t in range(numturmas):
    print("Turma: ", t+1)
    print("Digite o numero da sala")
    numsala = int(input())
    print("Digite o numero de alunos matriculados")
    numalunos = int(input())
    #acumulador
    totalunos = totalunos + numalunos
    contameninos = 0
    contameninas = 0
    for a in range(numalunos):
        print("Aluno: ", a+1)
        print("Digite o sexo (M/F)")
        sexo = input()
        if sexo == "m" or sexo == "M":
            contameninos = contameninos + 1
        else:
            contameninas = contameninas + 1
    print("Numero de meninos e", contameninos)
    print("Numero de meninas e", contameninas)
    if contameninos > amaiorqtdmeninos:
        amaiorqtdmeninos = contameninos
        salamaiorqtdmeninos = numsala

    if t == 0:
        amenorqtdmeninas = contameninas
        salamenorqtdmeninas= numsala
    else:
        if contameninas < amenorqtdmeninas:
            amenorqtdmeninas = contameninas
            salamenorqtdmeninas = numsala

print("O numero total de alunos e", totalunos)
media = totalunos / numturmas
print("A media de alunos por turma e", media)
print("A maior qtd de meninos e", amaiorqtdmeninos)
print("na sala ", salamaiorqtdmeninos)
print("A menor qtd de meninas e", amenorqtdmeninas)
print("na sala", salamenorqtdmeninas)