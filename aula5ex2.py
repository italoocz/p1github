compra = float(input('Digite o toal da compra: '))
valorFrete = 60


if compra > 100:
    compra = compra - valorFrete
else:
    compra = compra + valorFrete

print(f'O valor total da compra + frete foi de: R$ {compra}')