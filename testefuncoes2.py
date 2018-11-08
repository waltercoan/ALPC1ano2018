#escopo GLOBAL
numero = 1

def alteraNumero():
    #escopo LOCAL
    #global numero
    numero = 3

numero = 2
alteraNumero()
print("O valor e", numero)
