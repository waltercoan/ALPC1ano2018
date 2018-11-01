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


