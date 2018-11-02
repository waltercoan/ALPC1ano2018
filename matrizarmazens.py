mat = [[0] * 3 for i in range(5)]

for lin in range(4):
    for col in range(3):
        print("Arm: ", lin+1, "Prod: ", col+1)
        print("Digite a quantidade")
        mat[lin][col] = float(input())

for col in range(3):
    print("Prod: ", col+1)
    print("Digite o valor")
    mat[4][col] = float(input())
#a.	A quantidade de itens  armazenas em cada armazém
totalarm=0
for lin in range(4):
    for col in range(3):
        totalarm += mat[lin][col]
    print("Arm: ", lin, " valor total ", totalarm)
    totalarm = 0

#b.	Qual o armazém possui maior estoque do produto 2;
omaior = 0
armazemmaior = 0
for lin in range(4):
    if omaior < mat[lin][1]:
        omaior = mat[lin][1]
        armazemmaior = lin + 1

print("No armazem ", armazemmaior, \
      "tem a maior qtd de ", omaior)

#c.	Qual o armazém possui menor estoque

totalarm = 0
omenor = 0
oarmmenor = 0
for lin in range(4):
    for col in range(3):
        totalarm += mat[lin][col]
        #totalarm = totalarm + mat[lin][col]
    if lin == 0:
        omenor = totalarm
        oarmmenor = lin + 1
    else:
        if omenor > totalarm:
            omenor = totalarm
            oarmmenor = lin + 1
    totalarm = 0
print("O Armazem ", oarmmenor)
print("possui a menor quantidade de", omenor)

#d.	Qual o custo total de cada produto

somaqtd=0
for col in range(3):
    for lin in range(4):
        somaqtd += mat[lin][col]
    custototal = somaqtd * mat[4][col]
    print("Produto ", col, " custo total ", custototal)
    somaqtd = 0

#e.	Qual o custo total de cada armazém
somacustoarm=0
for lin in range(4):
    for col in range(3):
        somacustoarm = somacustoarm + (mat[lin][col] * mat[4][col])
    print("Armazem ", lin+1 , " custo total de ", somacustoarm)
    somacustoarm = 0