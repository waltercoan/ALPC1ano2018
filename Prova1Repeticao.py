amaiorqtd=0
linhamaiorqtd=0
linhamenorqtd=0
somalinha = 0
amenorqtd = 0
somamatutino=0
somavespertino=0
somanoturno=0
valortotal = 0
for linha in range(4):
    print("Linha ", (linha + 1 ))
    somalinha = 0
    for horario in range(2):
        print("Horario ", (horario + 1))
        print("Digite o codigo da linha")
        codigo = int(input())
        print("Digite o horário de saida")
        saida = int(input())
        print("Digite a qtd de passagens vendidas")
        qtd = int(input())
        somalinha = somalinha + qtd

        if saida >= 7 and saida <=12:
            somamatutino = somamatutino + qtd
        else:
            if saida > 12 and saida <= 19:
                somavespertino = somavespertino + qtd
            else:
                if saida >19 and saida <= 23:
                    somanoturno = somanoturno + qtd

        if codigo == 1 or codigo == 3:
            if saida < 14:
                valor = 45
            else:
                valor = 75
        else:
            if saida > 9 and saida < 16:
                valor = 120
            else:
                valor  = 80
        valortotal = valortotal + ( qtd * valor)
        print("O valor da passagem e ", valor)
    if somalinha > amaiorqtd:
        amaiorqtd = somalinha
        linhamaiorqtd = linha
    if linha == 0:
        amenorqtd = somalinha
        linhamenorqtd = linha
    else:
        if somalinha < amenorqtd:
            amenorqtd = somalinha
            linhamenorqtd = linha

print("Na linha", linhamaiorqtd)
print("houve a maior qtd de passageiros com ", amaiorqtd)
print("Na linha", linhamenorqtd)
print("houve a menor qtd de passageiros com ", amenorqtd)
print("A soma das vendas no horario matutino e ", somamatutino)
print("A soma das vendas no horario vespertino e ", somavespertino)
print("A soma das vendas no horario noturno e ", somanoturno)
print("O valor total é ", valortotal)