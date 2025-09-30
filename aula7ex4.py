numero = int(input('Digite um número inteiro menor que 1000: '))
centenas = 0

if numero < 1000:
    centenas = numero // 100 
    numero = numero - centenas * 100
    print(f'{centenas} centenas')
    if numero >= 10:
        dezenas = numero // 10
        numero = numero - dezenas * 10
        print(f'{dezenas} dezenas')

    if numero > 0:
        print(f'{numero} unidades')