# 1. Faça um Programa que peça dois números e imprima o maior deles.

n1 = int(input('Digite um número: '))
n2 = int(input('Digite outro número: '))

if n1 > n2:
    print(f'O {n1} é maior que o número {n2}.')
elif n1 < n2:
    print(f'O {n2} é maior que o número {n1}.')
else:
    print('Número incorreto, tente novamente.')