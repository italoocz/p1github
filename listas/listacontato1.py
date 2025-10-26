# nomes = ['Ana', 'João', "Gabriel", 'Lais']

# nomes[2] = "José"

# print(nomes[2])

nomes = ['Ana', 'João', "Gabriel", 'Lais']

for indice in range(len(nomes)):
    print(f'Código: {indice} | Nome {nomes[indice]}')

opcao = int(input('Qual o nome você quer editar? (Digite o indice): '))
while indice < 0 or indice >= len(nomes):
    print('Indice negativo ou maior que o tamanho da lista')
    opcao = int(input('Qual o nome você quer editar? (Digite o indice): '))
    
novoNome = input('Digite um novo nome: ')

nomes[indice] = novoNome

for indice in range(len(nomes)):
    print(f'Código: {indice} | Nome {nomes[indice]}')
