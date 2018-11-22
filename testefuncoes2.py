#global
numero = 1

def alteraNumero():
    #LOCAL
    global numero
    numero = 3
    #FALECEU!!!

numero = 2
alteraNumero()
print("O valor e", numero)
