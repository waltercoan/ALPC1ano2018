'''
Calcule e apresente a PROGRESSÃO GEOMÉTRICA dos 200 próximos
números de 1 considerando o quociente 4.
'''

#conta = 0
#while conta < 10:
#    print("Funcionou...")
#    conta = conta + 1

#for i in range(10):
#    print(i,"Tb Funciona...")

num = 1
for i in range(200):
    num = num * 4

print("Resultado", num)