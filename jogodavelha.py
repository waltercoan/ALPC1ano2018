tab = [[" "] * 3 for i in range(3)]

repete = True
jogador = "x"
while(repete):
    for lin in range(3):
        print("|",end="")
        for col in range(3):
            print(tab[lin][col],end="|")
        print()
        print("-------")
    print("Jogador: ", jogador)
    print("Digite o numero da linha")
    linha = int(input())
    print("Digite o numero da coluna")
    coluna = int(input())

    if tab[linha-1][coluna-1] == " ":
        tab[linha-1][coluna-1] = jogador
        if jogador == "x":
            jogador = "o"
        else:
            jogador = "x"
    else:
        print("Jogada inválida")

    for lin in range(3):
        if tab[lin][0] == tab[lin][1] and \
                tab[lin][1] == tab[lin][2] and tab[lin][2] != " ":
            print("Voce venceu: ", tab[lin][0])
            repete = False
            break
    for col in range(3):
        if tab[0][col] == tab[1][col] and \
            tab[1][col] == tab[2][col] and tab[2][col] != " ":
            print("Voce venceu: ", tab[0][col])
            repete = False
            break
    if (tab[0][0] == tab[1][1] and tab[1][1] == tab[2][2] and tab[2][2] != " ") or \
        (tab[0][2] == tab[1][1] and tab[1][1] == tab[2][0] and tab[2][0] != " "):
        print("Voce venceu: ", tab[1][1])
        repete = False

    pass
for lin in range(3):
    print("|",end="")
    for col in range(3):
        print(tab[lin][col],end="|")
    print()
    print("-------")