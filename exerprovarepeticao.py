amaiorqtdpessoas =0
odiadamaiorqtd = 0

amenorqtdpessoas = 0
odiadamenorqtd=0
for contadia in range(8):
    print("Digite o numero do dia")
    numdia = int(input())
    print("Digite o numero de pessoas")
    numpessoas = int(input())

    if numpessoas <= 1000:
        vallocacao = 4500
    else:
        vallocacao = numpessoas * 5
    print("O valor da locacao e", vallocacao)

    if numpessoas > amaiorqtdpessoas:
        amaiorqtdpessoas = numpessoas
        odiadamaiorqtd = numdia

    if contadia == 0:
        amenorqtdpessoas = numpessoas
        odiadamenorqtd = numdia
    else:
        if numpessoas < amenorqtdpessoas:
            amenorqtdpessoas = numpessoas
            odiadamenorqtd = numdia
    #aqui OHHH

#aqui nao da mais
print("A maior qtd de pessoas e", amaiorqtdpessoas)
print("no dia ", odiadamaiorqtd)
print("A menor qtd de pessoas e", amenorqtdpessoas)
print("no dia", odiadamenorqtd)