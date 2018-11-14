def func_somar(a, b, c):
    #print(a, b, c)
    soma = 0
    for i in range(b,c+1):
        #print(i)
        if i % a == 0:
            soma = soma + i
    return soma

print("Digite o valor inicial")
ini = int(input())
print("Digite o valor final")
fim = int(input())
print("Digite o divisor")
div = int(input())
resultado = func_somar(div,ini,fim)
print("A soma e", resultado)