pipoca = input('Qual tamanho da pipoca? <P/M/G>: ')
refri = input('A compra inclui refrigerante <S/N>: ')
pipocaP = 5
pipocaM = 8
pipocaG = 10
refrigerante = 5
if pipoca == 'P':
    pipoca = pipocaP
elif pipoca == 'M':
    pipoca = pipocaM
elif pipoca == 'G':
    pipoca = pipocaG
if refri == 'S':
    totalcompra = pipoca + refrigerante
    desconto = totalcompra * 0.10
    totalcompradesc = totalcompra - desconto
else:
    totalcompra = pipoca + refrigerante
    desconto = 0
    totalcompradesc = totalcompra - desconto

print(f'Valor antes do desconto: {totalcompra}')
print(f'O valor do desconto é de: {desconto}')
print(f'O valor final é de : {totalcompra - desconto}')