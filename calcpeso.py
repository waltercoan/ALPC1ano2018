print("Digite a sua altura")
altura = float(input())
print("Digite o sexo (m/f)")
sexo = input()

if sexo == "m":
    #caminho do SIM
    peso = (72.7 * altura) - 58
    #aqui1
else:
    #caminho do NAO
    peso = (62.1 * altura) - 44.7
    #aqui2
print("Seu peso ideal e", peso)

