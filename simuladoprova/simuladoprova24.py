n1 = float(input('Digite um numero: '))
n2 = float(input('Digite outro numero: '))
operação = input('Qual operação deseja ealizar <A/S/D/M>: ')

if operação == 'A':
    adicao = n1 + n2
    if adicao % 2 == 0:
        print('Par')
    else:
        print('impar')
    if adicao >= 0:
        print('Positivo')
    else:
        print('Negativo')
    if adicao % 1 == 0:
        print('inteiro')
    else:
        print('Decimal')
