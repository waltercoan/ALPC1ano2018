def calcmedia(nota1, nota2, nota3, letra):
    media = 0
    if letra == 'A' or letra == 'a':
        #calcular media aritmetica
        media = (nota1 + nota2 + nota3) / 3
    else:
        #calcular media ponderada
        media = ((nota1 * 5) + (nota2 * 3) + (nota3  * 2)) / 10
    return media

print("Digite a nota 1")
n1 = int(input())
print("Digite a nota 2")
n2 = int(input())
print("Digite a nota 3")
n3 = int(input())
l = input("Digite A para aritmetica ou P para ponderada")
resultado = calcmedia(n1,n2,n3,l)
print(resultado)