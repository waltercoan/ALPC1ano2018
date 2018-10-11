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

    tab[linha-1][coluna-1] = jogador

    if jogador == "x":
        jogador = "o"
    else:
        jogador = "x"
    pass