print("Digite o numero da tabuada")
base = int(input())

cont = 0
while cont <= 10:
    resul = base * cont
    print("%d x %d = %d" % (base,cont,resul))
    cont = cont + 1
