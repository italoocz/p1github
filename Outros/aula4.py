# preço de um produto
# dar um desconto em x %

PrecoProduto = float(input("Digite o valor: "))
percentualdesconto = int(input("Figite o seu desconto em %: "))

valorDesconto = PrecoProduto * percentualdesconto / 100

print(f'O preço do produto é: {PrecoProduto}')
print(f'O percentual desconto é: {percentualdesconto}')
print(f'O valor do desconto é: {valorDesconto}')
print(f'O preço final do produto é: {PrecoProduto - valorDesconto}')