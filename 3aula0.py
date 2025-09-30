contador = int(input('Digite o número de notas que você quer calcular: '))
auxiliar = contador
soma = 0

while contador > 0:
    nota = float(input('Digite a nota: '))
    print(f'Nota {nota}')
    soma = soma + nota
    contador -= 1

print(f'Todas as notas juntas você tem {soma} pontos')
media = soma / auxiliar
print(f'A sua média é de {media}')