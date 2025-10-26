# fruta1 = 'banana'
# fruta2 = 'abacaxi'
# fruta3 = 'maça'
# fruta4 = 'mamao'

# print(fruta2)

# fruta = input('Qual fruta deseja adicionar na cesta?: ')
# cestaFrutas = ['Banana', 'Abacaxi', 'Maça', 'Mamão', fruta]

# print(cestaFrutas[2])

# cestaFrutas = ['Banana', 'Abacaxi', 'Maça', 'Mamão']

# for i in range(4):
#     print('Indice', cestaFrutas[i])

# times = ['Flamengo','Vasco', 'Corinthians', 'Real madrid']

# for posicao in range(4):
#     if(posicao == 1):
#         print(f'Posição: {posicao} time: {times[posicao]}')

times = ['Flamengo','Vasco', 'Corinthians', 'Real madrid']

for posicao in range(4):
    if posicao % 2 == 0:
        print(f'Posição: {posicao} time: {times[posicao]}')

# for t in times:
#     print(t)