amaiorqtdpessoas =0
odiadamaiorqtd = 0

amenorqtdpessoas = 0
odiadamenorqtd=0
somaeventogrande=0
contaeventogrande=0
contaeventopequeno = 0
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
    if numpessoas >= 1000:
        somaeventogrande = somaeventogrande + vallocacao
        contaeventogrande = contaeventogrande  + 1
    else:
        contaeventopequeno = contaeventopequeno + 1
#aqui nao da mais
print("A maior qtd de pessoas e", amaiorqtdpessoas)
print("no dia ", odiadamaiorqtd)
print("A menor qtd de pessoas e", amenorqtdpessoas)
print("no dia", odiadamenorqtd)

print("O numero de eventos com mais de 1000 pessoas e", contaeventogrande)
print("O numero de eventos com menos de 1000 pessoas e", contaeventopequeno)
if contaeventogrande > 0:
    media = somaeventogrande / contaeventogrande
    print("A media do valor dos eventos com mais de 1000 pessoas e")
    print(media)