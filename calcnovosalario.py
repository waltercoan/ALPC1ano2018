print("Digite o numero de horas trabalhadas")
numhorastrab = float(input())
print("Valor do salário mínimo")
valsalmin = float(input())
print("Digite o número de horas extras")
numhorasex = float(input())

valhora = valsalmin / 8
print("O valor da hora trabalhada e", valhora)
valhoraex = valsalmin / 4
print("O valor da hora extra e", valhoraex)
valsalbruto = numhorastrab * valhora
print("O valor do salário bruto e", valsalbruto)
valhorasextotal = numhorasex * valhoraex
print("O valor pago pelas horas extras e", valhorasextotal)
salreceber = valsalbruto + valhorasextotal
print("O salário a receber e", salreceber)
