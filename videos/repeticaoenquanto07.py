'''Faça um programa que receba a idade de 15 pessoas
e que calcule e mostre:
- A quantidade de pessoas em cada faixa etária
- A percentagem de pessoas em cada uma das faixas
etárias, com relação ao total de pessoas,
de acordo com a tabela abaixo:
Faixa Etária	Idade
1	            Até 15 anos
2	            De 16 a 30 anos
3	            De 31 a 45 anos
4	            De 46 a 60 anos
5	            Acima de 61 anos
'''

conta = 0
qtdf1=0
qtdf2=0
qtdf3=0
qtdf4=0
qtdf5=0
while conta < 15:
    print("Pessoa: ", conta + 1)
    print("Digite a idade:")
    idade = int(input())
    if idade <= 15:
        print("Faixa 1")
        qtdf1 = qtdf1 + 1
    else:
        if idade >= 16 and idade <= 30:
            print("Faixa 2")
            qtdf2 = qtdf2 + 1
        else:
            if idade >= 31 and idade <= 45:
                print("Faixa 3")
                qtdf3 = qtdf3 + 1
            else:
                if idade >= 46 and idade <= 60:
                    print("Faixa 4")
                    qtdf4 = qtdf4 + 1
                else:
                    print("Faixa 5")
                    qtdf5 = qtdf5 + 1
    conta = conta + 1
percf1 = (qtdf1 * 100) / 15
percf2 = (qtdf2 * 100) / 15
percf3 = (qtdf3 * 100) / 15
percf4 = (qtdf4 * 100) / 15
percf5 = (qtdf5 * 100) / 15
print("Qtd faixa 1: ", qtdf1, " com perc de ",percf1)
print("Qtd faixa 2: ", qtdf2, " com perc de ",percf2)
print("Qtd faixa 3: ", qtdf3, " com perc de ",percf3)
print("Qtd faixa 4: ", qtdf4, " com perc de ",percf4)
print("Qtd faixa 5: ", qtdf5, " com perc de ",percf5)

'''
15    - 100%
qtdf1 - x
'''