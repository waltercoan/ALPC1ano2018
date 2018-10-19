mat = [[0] * 5 for i in range(3)]
contador = 0
for lin in range(3):
    for col in range(5):
        mat[lin][col] = int(input("Digite um numero"))

for lin in range(3):
    for col in range(5):
        print(mat[lin][col],end=" ")
    print()

for lin in range(3):
    for col in range(5):
        if mat[lin][col] >= 15 and mat[lin][col] <= 20:
            contador += 1
print("O numero de elementos entre 15 e 20 e", contador)