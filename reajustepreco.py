print("Digite o preço atual")
precoatual = float(input())
print("Digite o valor de venda medio")
valvendmedio = float(input())

if valvendmedio < 500 or precoatual < 30:
    reajuste = precoatual + ((precoatual * 12)/100)
else:
    if (valvendmedio >= 500 and valvendmedio < 1600) or \
            (precoatual >= 30 and precoatual < 80):
        reajuste = precoatual + ((precoatual * 15)/100)
    else:
        if valvendmedio >= 1600 or precoatual >= 80:
            reajuste = precoatual - ((precoatual * 25)/100)

print("O novo preco e",  reajuste)
