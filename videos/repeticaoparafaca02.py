'''
Faça um programa que receba a idade, a altura e o
peso de 25 pessoas. Calcule e mostre:
- a quantidade de pessoas com idade superior
a 50 anos
- a média das alturas das pessoas com idade
entre 10 e 20 anos;
- a percentagem de pessoas com peso inferior
a 40 quilos entre todas as pessoas analisadas.
'''
contapessoas = 0
contamenoridade = 0
somaalturamenoridade=0
contapeso=0
for i in range(25):
    print("Pessoa: ", (i+1))
    print("Digite a idade")
    idade = int(input())
    print("Digite a altura")
    altura = float(input())
    print("Digite o peso")
    peso = float(input())
    if idade > 50:
        contapessoas = contapessoas + 1
    if idade >= 10 and idade <= 20:
        contamenoridade = contamenoridade + 1
        somaalturamenoridade = somaalturamenoridade + altura
    if peso <= 40:
        contapeso = contapeso + 1
print("O número de pessoas com mais de 50 anos e", contapessoas)
if contamenoridade > 0:
    media = somaalturamenoridade / contamenoridade
    print("A média da altura das pessoas entre 10 e 20 anos e", media)
if contapeso > 0:
    perc = (contapeso * 100) / 25
    print("O perc de pessoas com menos de 40 kg é", perc)

# 25        - 100%
# contapeso - perc