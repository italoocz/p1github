nota1 = float(input('Digite sua primeira nota: '))
nota2 = float(input('Digite sua segunda nota: '))

media = (nota1 + nota2) / 2

print(f'Sua média é: {media:.2f}')

if media >= 7 and media < 9.99:
    print('Aprovado')
elif media < 7:
    print('Reprovado')
elif media == 10:
    print('Aprovado com distinção, parabens!')
else:
    print('Valor inválido, tente novamnte.')