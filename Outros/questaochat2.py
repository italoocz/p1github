carroHora = 3
carroMinuto = 47
valor_hora = 7
valor_bloco = 1.5

pagar = carroHora // 1
blocos = carroMinuto // 10
if carroMinuto % 10 != 0:
    blocos += 1

print(f'ele pagará {pagar} horas cheias')
print(f'ele vai pagar {blocos:.2f} blocos adicionais')
print(f'o valor total será de: R$ {pagar*valor_hora + valor_bloco*blocos}')