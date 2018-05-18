print("Digite o primeiro numero")
num1 = int(input())
print("Digite o segundo numero")
num2 = int(input())

cont = 0
soma = 0
while cont < num1:
    print(num2," + ",end="")
    #isso e um acumulador
    soma = soma + num2
    #isso e um contador
    cont = cont + 1

print("Resultado", soma)
