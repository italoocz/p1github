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

