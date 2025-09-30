# 7. Faça um Programa que leia três números e mostre o maior e o menor deles.

n1 = float(input('Digite sua primeiro numero: '))
n2 = float(input('Digite sua segundo numero: '))
n3 = float(input('Digite sua terceiro numero: '))

if n1 > n2 and n1 > n3:
    print('O primeiro numero é o maior')
elif n2 > n1 and n2 > n3:
    print('O segundo numero é o maior')
elif n3 > n1 and n3 > n2:
    print('O terceiro numero é o maior')

if n1 < n2 and n1 < n3:
    print('O menor numero é o primeiro')
elif n2 < n1 and n2 < n3:
    print('O segundo numero é o menor')
elif n3 < n1 and n3 < n2:
    print('O terceiro numero é o menor')

else:
    print('Numeros inválidos')
