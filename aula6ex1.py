ano = int(input('Digite o ano do seu nascimento: '))
acompanhada = input('você está acompanhada? (y/n) ')

idade = 2025 - ano

if idade >= 18 or acompanhada == 'y':
    print('Você pode entrar na festa.')
else:
    print('Você não pode entrar na festa.')