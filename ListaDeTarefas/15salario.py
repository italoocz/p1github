ValorHora = float(input('Digite quanto você ganha por hora: '))
Horas = int(input('Digite quantas horas você trabalha por mês: '))

salario = ValorHora * Horas

impostoR = salario * 0.11
inss = salario * 0.08
sindicato = salario * 0.05

liquido = salario - impostoR - inss - sindicato

print(f'+ Seu salário bruto foi de: R$ {salario:.2f}')
print(f'- Você pagou R$ {impostoR:.2f} ao imposto de renda')
print(f'- Você pagou R$ {inss:.2f} ao inss')
print(f'- Você pagou R$ {sindicato:.2f} para o sindicato')
print(f'+ O seu salario com os descontos foi de: R$ {liquido:.2f}')