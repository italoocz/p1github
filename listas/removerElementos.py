bruxos = ["Harry Potter", "Hermione", "Ronie Wesly", "Sirius Black", "Snape"]
# print('Lista antes de remover...')
# print(bruxos)

# print('Lista depois de remover...')
# bruxos.remove('Snape')
# print(bruxos)

# for b in bruxos:
#     print(f'Nome do bruxo {b}')

# bruxos.remove(input('Digite o nome do bruxo que deseja remover: '))

# for b in bruxos:
#     print(f'Nome do bruxo {b}')

for i in range(len(bruxos)):
    print(f'Codigo: {i} | Nome: {bruxos[i]}')

indice = int(input('Digite o indice para remover: '))

bruxos.remove(bruxos[indice])

for i in range(len(bruxos)):
    print(f'Codigo: {i} | Nome: {bruxos[i]}')