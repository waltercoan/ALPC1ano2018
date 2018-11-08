tabuada = lambda x,y: x * y

print(tabuada(7,6))
eusoumaisumavariavelsimples = tabuada
print(eusoumaisumavariavelsimples(5,7))

def gerartabuada(num, regra):
    for i in range(11):
        print("%d x %d = %d" % (num, i, regra(i,num)))

gerartabuada(7,tabuada)
