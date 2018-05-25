print("Digite o valor inicial")
ini = int(input())
print("Digite o valor final")
fim = int(input())

conta = ini
soma = 0
while conta <= fim:
    print(conta)
    if conta % 2 == 1:
        soma = soma + conta
    conta = conta + 1
print("A soma dos impares e", soma)
