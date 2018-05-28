'''
Faça um programa que leia dez conjuntos
de dois valores, o primeiro representando
o número do aluno e o segundo representando
a sua altura em centímetros. Encontre o
aluno mais alto e o mais baixo. Mostre o
número do aluno mais alto e o número do
mais baixo, junto com suas alturas.
'''
conta = 0
maioraltura = 0
menoraltura = 0
numerodomaior=0
numerodomenor=0
while conta < 10:
    print("Aluno ", conta+1)
    print("Digite o número do aluno")
    numero = int(input())
    print("Digite a altura em centímetros")
    altura = int(input())

    if altura > maioraltura:
        maioraltura = altura
        numerodomaior = numero

    if conta == 0:
        menoraltura = altura
        numerodomenor = numero
    else:
        if altura < menoraltura:
            menoraltura = altura
            numerodomenor = numero

    conta = conta + 1
print("A maior altura é", maioraltura, " matrícula" , numerodomaior)
print("A menor altura é", menoraltura, " matrícula" , numerodomenor)