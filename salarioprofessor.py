print("Digite o valor da hora aula")
valhora = float(input())
print("Digite o numero de horas trab no mes")
numhoras = float(input())
print("Digite o perc de desconto inss")
percinss = float(input())
salbruto = valhora * numhoras
print("O valor do sal bruto e:", salbruto)
valimposto = (salbruto * percinss) / 100
print("O valor do imposto e: ", valimposto)
salliq = salbruto - valimposto
print("O salario liquido do professor e %.2f" % salliq)
