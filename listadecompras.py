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
        print("Digite o nome do item")
        nomeitem = input()
        lista[proxlivre] = nomeitem
        proxlivre = proxlivre + 1

    if opcao == 2:
        for i in range(20):
            print("[",i,"] - ", lista[i])
        print("Digite o numero do item para altera")
        posicao = int(input())

    if opcao == 4:
        for i in range(20):
            print("[", i, "] - ", lista[i], " - ", comprado[i])
#aqui2