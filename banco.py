contas = [0] * 10
saldos = [0] * 10

for i in range(10):
    repete = True
    while(repete):
        print("Digite o numero da conta")
        novaconta = int(input())
        achei = False
        for j in range(10):
            if novaconta == contas[j]:
                print("Conta duplicada")
                achei = True
                repete = True
                break
        if not achei:
            repete = False
    contas[i] = novaconta
    print("Digite o saldo da conta")
    saldos[i] = float(input())



opcao = 0
while(opcao != 9):
    print("Menu")
    print("1 Efetuar deposito")
    print("2 Efetuar saque")
    print("3 Listar saldos ativos")
    print("4 Conta com maior saldo")
    print("5 Conta com menor saldo")
    print("9 Sair")
    print("Digite a opcao desejada")
    opcao = int(input())

    if opcao == 4:
        omaiorvalor = 0
        contamaiorsaldo = 0
        for i in range(10):
            if saldos[i] > omaiorvalor:
                omaiorvalor     = saldos[i]
                contamaiorsaldo = contas[i]
        print("A conta ", contamaiorsaldo)
        print("O maior saldo e R$", omaiorvalor)

    if opcao == 5:
        #omenorsaldo = saldos[0]
        omenorsaldo = 0
        contamenorsaldo = 0
        for i in range(10):
            if i == 0:
                omenorsaldo     = saldos[i]
                contamenorsaldo = contas[i]
            else:
                if saldos[i] < omenorsaldo:
                    omenorsaldo     = saldos[i]
                    contamenorsaldo = contas[i]
        print("A conta ", contamenorsaldo)
        print("O menor saldo e R$", omenorsaldo)

    if opcao == 1:
        print("DEPOSITO")
        print("Digite o numero da conta")
        contadep = int(input())
        achei = False
        for i in range(10):
            if contadep == contas[i]:
                print("Digite o valor do deposito")
                valdep = float(input())
                saldos[i] = saldos[i] + valdep
                print("Deposito realizado com sucesso")
                achei = True
                break
        if not achei:
            print("Conta inválida...")

    if opcao == 2:
        print("SAQUE")
        print("Digite o numero da conta")
        contasaq = int(input())
        achei = False
        for i in range(10):
            if contasaq == contas[i]:
                achei = True
                print("Digite o valor do saque")
                valsaq = float(input())
                if saldos[i] >= valsaq:
                    saldos[i] = saldos[i] - valsaq
                    print("Saque realizado com sucesso")
                else:
                    print("Saldo insuficiente")
                break
        if not achei:
            print("Conta inválida...")

    if opcao == 3:
        print("Listagem de Ativos")
        for i in range(10):
            print(contas[i], " -> R$ ", saldos[i])
