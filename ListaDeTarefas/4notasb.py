print('Digite a nota das 4 avaliações do seu bimestre..')

av1 = int(input('nota 1: '))
av2 = int(input('nota 2: '))
av3 = int(input('nota 3: '))
av4 = int(input('nota 4: '))

media = (av1 + av2 + av3 + av4) / 4

print(f'A sua média é de: {media:.2f}')