'''
Cada espectador de um cinema respondeu a um questionário
no qual constava sua idade e a sua opinião em relação
ao filme: ótimo – 3, bom – 2, regular – 1. Faça um
programa que receba a idade e a opinião de 15 espectadores
e que calcule e mostre:
- a média das idades das pessoas que responderam ótimo
- a quantidade de pessoas que respondeu regular
- a percentagem de pessoas que respondeu bom entre
todos os espectadores analisados
'''
somaidade = 0
contaotimos=0
contaregular = 0
contabom = 0
for i in range(15):
    print("Digite sua idade")
    idade = int(input())
    print("Digite sua avaliação 3 ótimo 2 bom 1 regular")
    avaliacao = int(input())
    if avaliacao == 3:
        contaotimos = contaotimos + 1
        somaidade = somaidade + idade

    if avaliacao == 1:
        contaregular = contaregular + 1

    if avaliacao == 2:
        contabom = contabom + 1

if contaotimos > 0:
    media = somaidade / contaotimos
    print("A média da idade das pessoas que responderam otimo e", media)

print("O número de avaliações regulares e ", contaregular)

perc = (contabom * 100) / 15
print("O perc de respostas BOM foi ", perc)
# 15       - 100%
# contabom - perc