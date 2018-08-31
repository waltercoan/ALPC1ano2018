import random
numeros = [9,8,7,5,3]
#numeros = [0] * 10
#for i in range(10):
#    numeros[i] = int(random.random() * 100000)

for i in range(0,len(numeros)-1):
    #print(numeros[i])
    for j in range(i+1,len(numeros)):
        #print("\t", numeros[j])
        if numeros[i] > numeros[j]:
            aux = numeros[i]
            numeros[i] = numeros[j]
            numeros[j] = aux
            #numeros[i],numeros[j] = numeros[j],numeros[i]
print(numeros)
