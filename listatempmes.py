temp = [0] * 12
meses = ["Jan", "Fev", "Mar", "Abr", "Mai", "Jun",
         "Jul", "Ago", "Set", "Out", "Nov", "Dez"]
maiortemp = 0
mesmaiortemp = 0

menortemp = 0
mesmenortemp=0
for i in range(12):
    print("Digite a temp do mes ", meses[i])
    temp[i] = float(input())

for i in range(12):
    if maiortemp < temp[i]:
        maiortemp = temp[i]
        mesmaiortemp = i
    if i == 0:
        menortemp = temp[i]
        mesmenortemp = i
    else:
        if menortemp > temp[i]:
            menortemp = temp[i]
            mesmenortemp = i
print("A maior temp do ano foi", maiortemp, "no mes", meses[mesmaiortemp])
print("A menor temp do ano foi", menortemp, "no mes", meses[mesmenortemp])