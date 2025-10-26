n1 = float(input('Digite a nota da sua primeira avaliação: '))
n2 = float(input('Digite a nota da sua segunda avaliação: '))
n3 = float(input('Digite a nota da sua terceira avaliação: '))
n4 = float(input('Digite a nota da sua quarta avaliação: '))

media = (n1 + n2 + n3 + n4) / 4

print(f'A sua média foi de: {media:.2f}')

if media >= 7:
    print('Você está aprovado e passou de ano!')
    print('Parabens!!')
if media < 6.99:
    print('Você está reprovado :(')
    print('Se esforce mais...')