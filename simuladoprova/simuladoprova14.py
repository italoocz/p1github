# 14. Faça um programa que lê as duas notas parciais obtidas por um aluno numa disciplina ao longo de um semestre, e calcule
# a sua média. A atribuição de conceitos obedece à tabela abaixo:
# Média de Aproveitamento Conceito
# Entre 9.0 e 10.0 A
# Entre 7.5 e 9.0 B
# Entre 6.0 e 7.5 C
# Entre 4.0 e 6.0 D
# Entre 4.0 e zero E


# O algoritmo deve mostrar na tela as notas, a média, o conceito correspondente e a mensagem “APROVADO” se o
# conceito for A, B ou C ou “REPROVADO” se o conceito for D ou E.

n1 = float(input('Digite sua primeira nota em Calculo I: '))
n2 = float(input('Digite sua segunda nota em Calculo I: '))

media = (n1 + n2) / 2

print(f'Sua primeira nota foi: {n1}')
print(f'Sua segunda nota foi: {n2}')
print(f'Sua média é: {media}')

if media >= 9 and media <= 10:
    print('A')
    print('APROVADO')
elif media >= 7.5 and media <= 9:
    print('B')
    print('APROVADO')
elif media >= 6 and media <= 7.5:
    print('C')
    print('APROVADO')
elif media >= 4 and media <= 6:
    print('D')
    print('REPROVADO')
elif media < 4:
    print('E')
    print('REPROVADO')
else:
    print('Valor inválido, tente novamente.')

