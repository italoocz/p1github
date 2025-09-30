n = int(input('Digite um numero: '))

if n % 2 == 0:
    print('Par')
else:
    print('Impar')

continua = input('Deseja executar o programa novamente? (S/N)')
while continua == 'S':
    n = int(input('Digite um numero: '))
    if n < 0:
        print('Entrada inválida!')
    elif n > 0 and n % 2 == 0:
        print(f'O numero {n} é Par')
    elif n > 0 and n % 2 != 0:
        print(f'O numero {n} é Impar')
    continua = input('Deseja executar o programa novamente? (S/N)')
print('Programa encerrado!')