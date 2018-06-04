'''
O cardápio de uma lanchonete é o seguinte
Produto	        Cód	Preço
Cachorro Quente	100	R$ 1,20
Bauru Simples	101	R$ 1,30
Bauru com Ovo	102	R$ 1,50
Hambúrguer	    103	R$ 1,20
Cheeseburguer	104	R$ 1,30
Refrigerante	105	R$ 1,00
Faça um programa que leia o código dos itens
pedidos e as quantidades desejadas (valide as entradas).
Calcule e mostre o valor a ser pago por item
(preço * quantidade) e o total geral do pedido.
Considere que o cliente deve informar quando o
pedido deve ser encerrado.
'''

continua = True
totalgeral = 0
while continua:
    print("Menu")
    print("100 - Cachorro quente - 1.2")
    print("101 - Bauru Simples - 1.3")
    print("102 - Bauru com ovo - 1.5")
    print("103 - Hamburguer - 1.2")
    print("104 - Cheeseburguer - 1.3")
    print("105 - Refrigerante - 1.0")
    print("Digite o código do produto")
    cod = int(input())
    print("Digite a quantidade")
    qtd = int(input())
    print("Deseja mais algum produto s/n")
    continua = (input() == "s")
    preco = 0
    if cod == 100:
        preco = 1.2
    else:
        if cod == 101:
            preco = 1.3
        else:
            if cod == 102:
                preco = 1.5
            else:
                if cod == 103:
                    preco = 1.2
                else:
                    if cod == 104:
                        preco = 1.3
                    else:
                        preco = 1
    print("Preço unitário ", preco)
    precoitem = preco * qtd
    print("O preço por item é", precoitem)
    totalgeral = totalgeral + precoitem

    pass

print("O preço total da conta e", totalgeral)
