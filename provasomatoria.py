gaba = [0] * 10
qtdaprov = 0
print("Digite as respostas do gabarito")
for i in range(10):
    print("Questao ", (i+1), " digite resposta")
    gaba[i] = int(input())

for a in range(15):
    print("Aluno: ", (a+1))
    print("Digite o codigo")
    codigo = int(input())
    nota = 0
    for q in range(10):
        print("Digite a resposta da questao ", (q+1))
        resposta = int(input())
        if gaba[q] == resposta:
            nota = nota + 1
    print("Numero do aluno", codigo)
    print("Nota do aluno: ", nota)
    if nota >= 6:
        qtdaprov = qtdaprov + 1

perc = (qtdaprov * 100) / 15
print("O perc de aprovados e", perc)


