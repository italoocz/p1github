soma = 0
soma1 = int(input('Digite um numero: '))
while soma1 != -1:
    if soma1 < 21 or soma1 > 70:
        total = soma = soma1
    soma1 = int(input('Digite um numero: '))
print(f'A soma dos números é: {total}')