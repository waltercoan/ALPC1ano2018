'''Faça um programa que apresente os resultados
de uma tabuada de um número qualquer, a qual
deve ser impressa no seguinte formato:
Considerando como exemplo o fornecimento do
número 2 para o número qualquer, temos
a seguinte situação:
2 x 1 = 2
2 x 2 = 4
2 x 3 = 6
...
2 x 10 = 20
'''
print("Digite o número base")
base = int(input())
conta = 1
resul = 0
while conta <= 10:
    resul = base * conta
    print("%d x %d = %d" % (base, conta, resul))
    conta = conta + 1
