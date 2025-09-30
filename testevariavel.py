produto = 100
desconto = 10
valordesconto = produto * desconto / 100
precoFinal = produto - valordesconto


print(f' O produto custa R$ {produto}')
print(f'O valor do desconto é: {desconto}%')
print(f'O valor do desconto bruto é: R$ {valordesconto}')
print(f'O valor do produto final é: R$ {precoFinal}')