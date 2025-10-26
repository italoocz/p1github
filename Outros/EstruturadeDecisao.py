lado1 = float(input('Digite um lado do triagulo: '))
lado2 = float(input('Digite o segundo lado do triagulo: '))
lado3 = float(input('Digite o terceiro lado do triagulo: '))

if lado1 == lado2 == lado3:
    print('Triangulo equilátero.')
elif (lado1 == lado2 and lado1 != lado3) or (lado3 == lado2 and lado3 != lado1) or (lado1 == lado3 and lado1 != lado2):
    print('Triangulo Isórceles.')
elif lado1 != lado2 != lado3:
    print('Triangulo Escaleno.')
else:
    print('Numeros inválidos, tente novamente...')