vendas = [[0] * 4 for i in range(5)]

for lin in range(5):
    print("Vendedor: ", lin+1)
    for col in range(4):
        print("Semana: ", col+1)
        print("\tDigite o valor de venda")
        vendas[lin][col] = float(input())
#O total de vendas do mês de cada vendedor

#total = vendas[0][0] + vendas[0][1] + \
#        vendas[0][2] + vendas[0][3]
#
#total = vendas[1][0] + vendas[1][1] + \
#        vendas[1][2] + vendas[1][3]
total = 0
#sentido linha -> colunas
for lin in range(5):
    for col in range(4):
        total = total + vendas[lin][col]
    print("O total do vendedor",lin+1," e ", total)
    total = 0

#b.	O total de vendas de cada semana (todos os vendedores juntos)
total = 0
#sentido colunas -> linha
for col in range(4):
    for lin in range(5):
        total = total + vendas[lin][col]
    print("O total da semana", col+1, " e ", total)
    total = 0

totalgeral = 0
for lin in range(5):
    for col in range(4):
        totalgeral += vendas[lin][col]
print("O total geral e",  totalgeral)



