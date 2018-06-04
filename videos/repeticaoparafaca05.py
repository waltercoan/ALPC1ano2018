'''
Uma radio necessita realizar alguns cálculos
referente ao número de minutos de musicas e de propagandas
que são vinculadas. Considere que a radio fica 744 horas
por mês no ar. Solicite POR SEMANA o número horas da
programação em que foram vinculadas músicas e o numero
de horas em que foram vinculadas apenas propagandas.
Calcule e mostre:
a. A semana em que houve o a maior quantidade de horas
de propagandas vinculadas.
b. A semana em que houve a menor quantidade de horas
de musicas vinculadas.
c. O total de horas de propagandas vinculadas.
d. O total de horas de musicas vinculadas.
e. O percentual que o total de horas de propagandas
representa do numero total de horas que a rádio fica no ar
'''
totalhoras = 744
maiorqtdpropaganda=0
semanamaiorqtdprop=0

menorqtdmusica = 0
semanamenorqtdmusica=0

totprop = 0
totmusica = 0
for semana in range(4):
    print("Semana: ", (semana+1))
    print("Digite o número de horas de música")
    numhmusica = float(input())
    print("Digite o número de horas de propaganda")
    numhprop = float(input())
    if numhprop > maiorqtdpropaganda:
        maiorqtdpropaganda = numhprop
        semanamaiorqtdprop = semana

    if semana == 0:
        menorqtdmusica = numhmusica
        semanamenorqtdmusica = semana
    else:
        if numhmusica < menorqtdmusica:
            menorqtdmusica = numhmusica
            semanamenorqtdmusica = semana

    totprop = totprop + numhprop
    totmusica = totmusica + numhmusica


print("Na semana ", semanamaiorqtdprop, " ocorreu o maior num de horas de propaganda com ", maiorqtdpropaganda)
print("Na semana ", semanamenorqtdmusica, " ocorreu a menor qtd de horas de música com" , menorqtdmusica)
print("O número total de horas de propaganda é", totprop)
print("O número total de horas de música é", totmusica)
perc = (totprop * 100) / totalhoras
print("O perc de propaganda é" , perc)

# totalhoras - 100%
# totprop    - perc