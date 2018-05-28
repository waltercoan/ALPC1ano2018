'''Faça um algoritmo que calcule a
soma de todos os números ímpares
dentro de uma faixa de valores
determinada pelo usuário. Um número
é ímpar quando sua divisão por 2 não
é exata, ou seja, o resto resultante
da divisão inteira pelo número 2 tem
valor 1. Utilize a palavra resto como
operador que calcula o resto da divisão
de um numero por outro.'''
print("Digite o número inicial")
ini = int(input())
print("Digite o número final")
fim = int(input())
conta = ini
somaimpar = 0
while conta <= fim:
    print(conta)
    if conta % 2 == 1:
        print("Impar")
        somaimpar = somaimpar + conta
    conta = conta + 1
print("A soma dos num impares e", somaimpar)