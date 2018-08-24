x = [0] * 10
y = [0] * 10
uniao = [0] * 20

diff = [0] * 10

print("Conjunto X")
for i in range(10):
    print("Digite um numero")
    x[i] = int(input())

print("Conjunto Y")
for i in range(10):
    print("Digite um numero")
    y[i] = int(input())

#UNIAO
#a união de X com Y
# (todos os elementos de X
# e os elementos de Y que não estejam em X)
for i in range(10):
    uniao[i] = x[i]

proxlivre = 10
for i in range(10):
    print("y -> ",y[i])
    achei = False
    for j in range(10):
        print("\tx -> ", x[j])
        if y[i] == x[j]:
            print("Deu ruim: duplicado")
            achei = True
            break
    if not achei:
        uniao[proxlivre] = y[i]
        proxlivre = proxlivre  + 1
print(uniao)

print("Algoritmo diferenca")
##a diferença entre X e Y (todos os elementos de
# X que não existam em Y)
for i in range(10):
    print(x[i])
