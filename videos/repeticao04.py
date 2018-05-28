'''
Um funcionário de uma empresa recebe aumento salarial
anualmente. Sabe-se que:
a) esse funcionário foi contratado em 1995, com salário
inicial de R$ 1.000,00;
b) em 1996 recebeu aumento de 1,5% sobre seu salário inicial;
c) a partir de 1997 (inclusive), os aumentos salariais
sempre corresponderam ao dobro do percentual do ano anterior.
Faça um programa que determine o salário atual desse funcionário.
'''
contaano = 1995
salario = 0
percaumento = 0
while contaano <= 2018:
    if contaano == 1995:
        salario = 1000
    if contaano == 1996:
        percaumento = 1.5
    if contaano >= 1997:
        percaumento = percaumento * 2
    salario = salario + (salario * percaumento / 100)

    print("Ano: ", contaano, " salário ",  salario)
    contaano = contaano + 1