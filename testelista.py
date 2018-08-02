#idade = 20
#print(idade)

lista = [0] * 7

lista[0] = 10
lista[5] = 100
lista[6] = 1000

print(lista[0])
print(lista)

nomes = ["zezinho","luizinho","huguinho"]

print(nomes[1])
#lenght - tamanho maximo de uma lista
print(len(nomes))

nomes.append("tio patinhas")
print(nomes)
print(len(nomes))

lista += [20,30,40,50]
print(lista)
lista.insert(1,500) #inserir novo
print(lista)
lista[1] = 2222 #alterar existente
print(lista)

naocopia = lista
copia = lista[:]
print(copia)
print(lista)
naocopia[0] = 1111
print(lista)
lista[0] = 666
print(naocopia)
print(copia)




