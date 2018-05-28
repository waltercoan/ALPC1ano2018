'''
Tem-se um conjunto de dados contendo a altura e o sexo
(M ou F) de 10 pessoas. Faça um programa que calcule e mostre:
a) a maior e a menor altura do grupo;
b) a média de altura das mulheres;
c) o número de homens;
d) o sexo da pessoa mais alta.
'''

conta = 0
maioraltura=0
menoraltura=0
somaalturam=0
contarmulheres=0
contahomens=0
sexomaioraltura = ""
while conta < 10:
    print("Pessoa ", conta + 1)
    print("Digite a altura")
    altura = float(input())
    print("Digite o sexo M/F")
    sexo = input()

    if altura > maioraltura:
        maioraltura = altura
        sexomaioraltura = sexo

    if conta == 0:
        menoraltura = altura
    else:
        if altura < menoraltura:
            menoraltura = altura

    if sexo == "f" or sexo == "F":
        somaalturam = somaalturam + altura
        contarmulheres = contarmulheres + 1

    if sexo == "m" or sexo == "M":
        contahomens = contahomens + 1
    conta = conta + 1
print("A maior altura é", maioraltura)
print("A menor altura é", menoraltura)

mediaaltmulheres = somaalturam / contarmulheres
print("A media da altura das mulheres é", mediaaltmulheres)

print("O número de homens é ", contahomens)

print("O sexo da pessoa mais alta é", sexomaioraltura)