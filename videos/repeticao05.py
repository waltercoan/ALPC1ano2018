'''
Faça um programa que leia cinco pares
de valores (a,b), todos inteiros e
positivos, um de cada vez. Mostre os
números inteiros pares de a até b (inclusive).
'''

contapares = 0
while contapares < 5:
    print("Digite o valor de A")
    a = int(input())
    print("Digite o valor de B")
    b = int(input())

    conta = a
    while conta <= b:
        if conta % 2 == 0:
            print(conta)
        conta = conta + 1
    contapares = contapares + 1