lista = [""] * 20
comprado = [""] * 20
opcao = 0
proxlivre = 0
while(opcao != 9):
    print("MENU")
    print("1 - incluir")
    print("2 - alterar")
    print("3 - remover")
    print("4 - marcar como comprado")
    print("9 - sair")
    print("Digite a opcao desejada")
    opcao = int(input())
    if opcao == 1:
        if proxlivre >= 20:
            print("Lista cheia")
        else:
            print("Digite o nome do item")
            nomeitem = input()
            achei = False
            for i in range(20):
                if lista[i] == nomeitem:
                    print("Item duplicado")
                    achei = True
                    break
            #if achei == False:
            if not achei:
                lista[proxlivre] = nomeitem
                proxlivre = proxlivre + 1

    if opcao == 2:
        for i in range(20):
            print("[",i,"] - ", lista[i])
        print("Digite o numero do item para altera")
        posicao = int(input())
        print("Digite o novo valor")
        novonome = input()
        lista[posicao] = novonome
        print(lista)

    if opcao == 3:
        for i in range(20):
            print("[",i,"] - ", lista[i])
        print("Digite o numero do item para remover")
        posicao = int(input())
        lista[posicao] = ""
        print(lista)

    if opcao == 4:
        for i in range(20):
            print("[", i, "] - ", lista[i], " - ", comprado[i])
        print("Digite o numero do item para marcar comprado?")
        posicao = int(input())
        comprado[posicao] = "SIM"
#aqui2