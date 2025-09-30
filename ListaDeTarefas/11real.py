int1 = int(input('Digite um numero inteiro: '))
int2 = int(input('Digite outro numero inteiro: '))
real = float(input('Digite um numero real: '))

# a
dobro = int1 * 2
metade = int2 / 2
a = dobro + metade

# b
triplo = int1 * 3
b = triplo + real

# c
c = real ** 3

print(f'o dobro do primeiro com metade do segundo é: {a:.2f}')
print(f'a soma do triplo do primeiro com o terceiro é: {b:.2f}')
print(f'o terceiro elevado ao cubo é: {c:.2f}')