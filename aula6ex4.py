n1 = float(input('Digite um numero: '))
n2 = float(input('Digite outro numero: '))

if n1 > n2:
    print('O primeiro numero é maior.')
    if n1 > 0 or n1 == 0:
        print('O resultado é positivo ou neutro')
    else:
        print('Resultado negativo')

if n1 < n2:
    print('O segundo numero é maior.')
    if n2 > 0 or n2 == 0:
        print(f'O resultado é positivo ou neutro')
    else:
        print('Resultado negativo')