# 2. Faça um Programa que peça um valor e mostre na tela se o valor é positivo ou negativo.

numero = float(input('Digite um valor: '))

if numero > 0:
    print(f'o valor {numero} é positivo')
elif numero < 0:
    print(f'o valor {numero} é negativo')