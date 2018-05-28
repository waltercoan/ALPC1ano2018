'''
Faça um programa que receba duas notas de seis alunos,
calcule e mostre:
- Média aritmética das duas notas de cada aluno;
- A mensagem que esta na tabela a seguir:
+--------------------+--------------+
|Média Aritmética    |   Mensagem   |
+--------------------+--------------+
|     até 3.0        |   Reprovado  |
|  entre 3.0 e 7.0   |   Exame      |
|    Acima de 7.0    |   Aprovado   |
+--------------------+--------------+
Ao final:
- O total de alunos aprovados;
- O total de alunos em exame;
- O total de alunos reprovados;
- A média da classe.
'''

conta = 0
qtdaprovados=0
qtdexame=0
qtdreprovados=0
somamedias = 0
while conta < 6:
    print("Aluno:", conta + 1)
    print("Digite a primeira nota")
    n1 = float(input())
    print("Digite a segunda nota")
    n2 = float(input())
    media = (n1 + n2) / 2
    print("Média: ", media)
    somamedias = somamedias + media
    if media < 3:
        print("Reprovado")
        qtdreprovados = qtdreprovados + 1
    else:
        if media >= 3 and media < 7:
            print("Exame")
            qtdexame = qtdexame + 1
        else:
            print("Aprovado")
            qtdaprovados = qtdaprovados + 1
    conta = conta + 1
print("Qtd aprovados é", qtdaprovados)
print("Qtd em exame é", qtdexame)
print("Qtd reprovados é", qtdreprovados)
mediasala = somamedias / 6
print("A média da sala é ", mediasala)