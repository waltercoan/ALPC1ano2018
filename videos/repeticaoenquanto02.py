'''Faça um algoritmo que leia um número
inteiro e calcule o seu fatorial. Se o
número for negativo, informe que o valor
é inválido. Sabemos que o fatorial de um
número n, representado por n!, é dado por:
n * (n-1) * (n-2) * ... * 1, para n > 0 e n! = 1 para n = 0
'''
print("Digite o número base")
base = int(input())
if base < 0:
    print("Número inválido")
else:
    if base == 0:
        print("0! = 1")
    else:
        conta = base
        fat = 1
        while conta >= 1:
            print(conta)
            fat = fat * conta
            conta = conta - 1
        print("%d! = %d" % (base, fat))