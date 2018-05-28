'''
Em um campeonato de futebol existem cinco
times e cada time possui onze jogadores.
Faça um programa que receba a idade, o
peso e a altura de cada um dos jogadores,
calcule e mostre:
- a quantidade de jogadores com idade
inferior a 18 anos;
- a média das idades dos jogadores de
cada time;
- a média das alturas de todos os jogadores
do campeonato;
- a percentagem de jogadores com mais de
80 quilos entre todos os jogadores
do campeonato.
'''

contatime = 0
contamenor=0
somaaltura=0
contagordinhos=0
while contatime < 5:
    print("Time ", contatime + 1)
    contajogador = 0
    somaidade = 0
    while contajogador < 11:
        print("Jogador ", contajogador+1)
        print("Digite a idade")
        idade = int(input())
        somaidade = somaidade + idade
        if idade < 18:
            contamenor = contamenor + 1
        print("Digite o peso")
        peso = float(input())
        if peso > 80:
            contagordinhos = contagordinhos + 1
        print("Digite a altura")
        altura = float(input())
        somaaltura = somaaltura + altura
        contajogador = contajogador + 1
    mediaidadetime = somaidade / 11
    print("Média idade time é", mediaidadetime)
    contatime = contatime + 1


print("A qtd de jogadores com menos de 18 anos e ", contamenor)
mediaaltura = somaaltura / 55
print("A média das alturas de todos os jogadores é", mediaaltura)
percgordinhos = (contagordinhos * 100) / 55
print("O perc de jog com peso superior a 80 é", percgordinhos)

'''
55  -  100
cg  -  x
'''