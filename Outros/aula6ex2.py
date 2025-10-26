faltas = int(input('Digite o numero de faltas no bimestre: '))
media = int(input('Digite a sua média: '))

if media >= 7 and faltas < 10:
    print('Aprovado')
else:
    print('Reprovado')
    