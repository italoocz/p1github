salario = int(input('Digite seu salário: '))
salarioLiquido = salario
percentual = 0
valorAumento = 0

if  salario > 0 and salario <= 280:
    percentual = 20
elif salario > 280


valorAumento = salario * percentual / 100
salarioLiquido = salarioLiquido + valorAumento

print(f'Salário inicial: {salario}')
...