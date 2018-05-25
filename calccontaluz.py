print("Digite o salario minimo")
salmin = float(input())
valkw = salmin / 8
print("O valor do KW e ", valkw)
repete = True
somafaturamento = 0
contador=0
while repete:
    print("Digite o consumo em KW")
    qtdkw = float(input())
    if qtdkw == 0:
        repete = False
    print("Digite o tipo 1-Residencia 2-Comercial 3- Ind")
    tipo = int(input())
    valordaconta = valkw * qtdkw
    if  tipo == 1:
        valordaconta = valordaconta + (valordaconta * 0.05)
    else:
        if tipo == 2:
            valordaconta = valordaconta + (valordaconta * 0.10)
        else:
            valordaconta = valordaconta + (valordaconta * 0.15)
    print("O valor da conta e R$", valordaconta)
    if valordaconta >= 500 and valordaconta <= 1000:
        contador = contador + 1
    somafaturamento = somafaturamento + valordaconta
print("O faturamento total e ", somafaturamento)
print("O num de consumidores com conta entre 500 e mil e", contador)


