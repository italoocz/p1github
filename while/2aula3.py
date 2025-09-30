# peça numeros e vai somando até o usuario digitar -1
# quanto o usuario digitar -1 imprima o valor total da soma de todos os numeros digitados
soma = 0
numero = int(input('Digite um numero: '))
while numero != -1:
    soma += numero
    numero = int(input('Digite um numero: '))

print('Fim do calculo')
print(f'Valor da soma {soma}')