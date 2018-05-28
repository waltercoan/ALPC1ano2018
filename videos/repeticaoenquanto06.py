'''
Faça um programa que receba o valor do salário
mínimo e uma lista contendo a quantidade de
quilowatts gasta por consumidor e o tipo do
consumidor (1-Residencial, 2-Comercial, 3-Industrial).
Calcule e mostre:
- O valor de cada quilowatt, sabendo que o
quilowatt custa 1/8 do salário mínimo;
- O valor a ser pago por cada consumidor
(conta final mais acréscimos), considerando
que o acréscimo é o mesmo da tabela a seguir:
+-------+-------------------------------------+
| Tipo	| % de acréscimo sobre o valor gasto  |
+-------+-------------------------------------+
|1	    | 5                                   |
|2	    | 10                                  |
|3	    | 15                                  |
+-------+-------------------------------------+
- O faturamento geral da empresa
- a quantidade de consumidores que pagam
entre R$ 500,00 e R$ 1000,00

Termine a entrada de dados quando a quantidade
de quilowatts digitada for igual a zero.
'''
print("Digite o valor do salário mínimo")
valsal = float(input())
valkw = valsal / 8
print("O valor do KW é", valkw)

repete = True
somaprecobase = 0
qtdconsumidor = 0
while repete:
    print("Digite a qtd de KW consumida")
    qtdkw = float(input())
    if qtdkw == 0:
        repete = False
    print("Digite o tipo: 1-Residencial/2-Comercial/3-Industrial")
    tipo = int(input())
    precobase = valkw * qtdkw
    if tipo == 1:
        precobase = precobase + (precobase * 5 / 100)
    else:
        if tipo == 2:
            precobase = precobase + (precobase * 10 / 100)
        else:
            precobase = precobase + (precobase * 15 / 100)
    print("O preço a ser pago é", precobase)
    somaprecobase = somaprecobase + precobase
    if precobase >= 500 and precobase <= 1000:
        qtdconsumidor = qtdconsumidor + 1
print("O faturamento da empresa é", somaprecobase)
print("A qtd de clientes com conta entre 500 e 1000 é", qtdconsumidor)

