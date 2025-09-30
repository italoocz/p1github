tamanho = float(input('Digite em metros quadrados a área a ser pintada: '))

litro = tamanho / 3

lata = 18
valor = 80

qntLatas = litro / lata
ValorLata = qntLatas * 80

if litro%lata != 0:
    qntLatas += 1
    print(f'A quantidade de latas necessárias é de: {qntLatas} latas de tinta')
    print(f'O preço total das latas será de: {qntLatas * valor}')