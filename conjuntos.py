x = [0] * 10
y = [0] * 10
uniao = [0] * 20



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
diff = [0] * 10
proxlivre = 0
for i in range(10):
    print(x[i])
    achei = False
    for j in range(10):
        print(y[j])
        if x[i] == y[j]:
            achei = True
            break
    if not achei:
        diff[proxlivre] = x[i]
        proxlivre = proxlivre + 1
print("Diferença ", diff)
#a soma entre X e Y (soma de cada elemento
# de X com o elemento de mesma posição em Y)
soma = [0] * 10
for i in range(10):
    soma[i] = x[i] + y[i]
print("Soma",  soma)
#d.	produto entre X e Y (multiplicação
# de cada elemento de X com o elemento de mesma posição em Y)
prod = [0] * 10
for i in range(10):
    prod[i] = x[i] * y[i]
print("Produto", prod)
#a interseção entre X e Y (apenas os
# elementos que aparecem nos dois vetores)
inter = [0] * 10
proxlivre = 0
for i in range(10):
    print(x[i])
    for j in range(10):
        print(y[j])
        if x[i] == y[j]:
            inter[proxlivre] = x[i]
            proxlivre += 1
            break
print("Interseção", inter)

