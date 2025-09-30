numero = int(input('Digite um numero inteiro: '))

if numero > 50:
    maior = numero * 2
    print(f'Seu numero é: {maior}')
else:
    desconto = numero * 12 / 100
    numero = numero - desconto
    print(f'Seu numero é: {numero}')