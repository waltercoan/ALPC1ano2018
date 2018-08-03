listaA = [0] * 10
listaB = [0] * 10
#listaR = []
listaR = [0] * 20
for i in range(10):
    print("Digite um numero")
    listaA[i] = int(input())

for i in range(10):
    print("Digite um numero")
    listaB[i] = int(input())
proxlivre=0
for i in range(10):
    listaR[proxlivre] = listaA[i]
    proxlivre = proxlivre + 1
    listaR[proxlivre] = listaB[i]
    proxlivre = proxlivre + 1

#for i in range(10):
#    listaR.append(listaA[i])
#    listaR.append(listaB[i])

print(listaA)
print(listaB)
print(listaR)