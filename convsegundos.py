def conversor(totseg):
    horas = int(totseg / 3600)
    sobra = totseg - (horas * 3600)
    minutos = int(sobra / 60)
    segundos = sobra - (minutos * 60)
    #print(horas, minutos, segundos)
    print("%dh: %dm: %ds" % (horas, minutos, segundos))


print("Digite a quantidade de segundos")
qtdtotalseg = int(input())
conversor(qtdtotalseg)