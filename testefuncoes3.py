
def conta(numero):
    print(numero)
    if numero < 10:
        conta(numero + 1)

conta(0)