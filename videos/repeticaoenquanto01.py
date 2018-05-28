'''Faça um algoritmo que calcule a multiplicação de
dois números inteiros sem utilizar o operador “*”.
Em vez disso, utilize apenas o operador de adição “+”.
Para implementar esse algoritmo, devemos lembrar que
qualquer multiplicação pode ser expressa por meio de somas.
Por exemplo, o resultado da expressão 6 * 3 é o mesmo
que 6 + 6 + 6 ou 3 + 3 + 3 + 3 + 3 + 3. Ou seja,
soma-se um elemento com ele próprio o número de vezes
do segundo elemento.'''
print("Digite o primeiro numero")
num1 = int(input())
print("Digite o segundo numero")
num2 = int(input())
conta = 0
soma = 0
while conta < num2:
    print(conta)
    soma = soma + num1
    conta = conta + 1
print("O resultado da multiplicação e", soma)