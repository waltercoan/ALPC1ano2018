print("Digite o preço atual")
preco = float(input())

if preco < 50:
    novopreco = ((preco * 5)/100) + preco
    #aqui1
else:
    if preco < 100:
        novopreco = ((preco * 10) / 100) + preco
        #aqui2
    else:
        novopreco = ((preco * 15)/100) + preco
        #aqui3
print("O novo preco e", novopreco)

if novopreco <= 80:
    print("Preço barato")
else:
    if novopreco > 80 and novopreco <= 120:
        print("Preço Normal")
    else:
        if novopreco > 120 and novopreco <= 200:
            print("Preço caro")
        else:
            print("Preço meu deus como esta caro")
