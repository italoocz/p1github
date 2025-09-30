altura = float(input('Digita o valor da sua altura: '))

PesoHomem = (72.7 * altura) - 58
PesoMulher = (62.1 * altura) -44.7

print(f'Se for homem, seu peso ideal para sua altura é: {PesoHomem:.2f} kilos')
print(f'Se for mulher, seu peso ideal para sua altura é: {PesoMulher:.2f} kilos')