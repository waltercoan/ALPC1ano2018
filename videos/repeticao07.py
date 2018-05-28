'''
Foi feita uma estatística em cinco cidades brasileiras
para coletar dados sobre acidentes de trânsito.
Foram obtidos os seguintes dados:
a) nome da cidade;
b) número de veículos de passeio;
c) número de acidentes de trânsito com vítimas
Deseja-se saber:
a) qual o maior e o menor índice de acidentes de
trânsito e a que cidades pertencem;
b) qual a média de veículos nas cinco cidades juntas;
c) qual a média de acidentes de trânsito nas cidades
com menos de 2.000 veículos de passeio.
'''

contacidade = 0
maiornumero = 0
nomemaiornumero=""
menornumero = 0
nomemenornumero = ""
somaveic = 0
somaacidentes=0
contaacidades=0
while contacidade < 5:
    print("Cidade: ", contacidade+1)
    print("Digite o nome da cidade")
    nome = input()
    print("Digite o número de veículos de passeio")
    numveic = int(input())
    print("Digite o número de acidentes")
    numacidentes = int(input())

    if numacidentes > maiornumero:
        maiornumero = numacidentes
        nomemaiornumero = nome

    if contacidade == 0:
        menornumero = numacidentes
        nomemenornumero = nome
    else:
        if numacidentes < menornumero:
            menornumero = numacidentes
            nomemenornumero = nome

    somaveic = somaveic + numveic

    if numveic < 2000:
        somaacidentes = somaacidentes + numacidentes
        contaacidades = contaacidades + 1

    contacidade = contacidade + 1
print("A cidade ", nomemaiornumero, " teve o maior número de acidentes com ", maiornumero)
print("A cidade ", nomemenornumero, " teve o menor número de acidentes com ", menornumero)

media = somaveic / 5
print("A média de veículos das cinco cidades é", media)

mediaacides = somaacidentes / contaacidades
print("A media de acidentes em cidades com menos de 2000 carros é",mediaacides)