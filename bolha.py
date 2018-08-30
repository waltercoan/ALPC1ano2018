import random
numeros = [0] * 100000
for i in range(100000):
    numeros[i] = int(random.random() * 100000)

for i in range(0,len(numeros)-1):
    #print(numeros[i])
    for j in range(i+1,len(numeros)):
        #print("\t", numeros[j])
        if numeros[i] > numeros[j]:
            aux = numeros[i]
            numeros[i] = numeros[j]
            numeros[j] = aux

print(numeros)