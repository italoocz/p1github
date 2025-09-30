compra = float(input('Digite o valor da compra: '))
estado = input('Digite a sigla do seu estado: ')

if estado == 'PB':
    if compra > 500:
        cpf = int(input('Digite seu cpf: '))
    else:
        print('Nao precisa de cpf')

if estado == 'RN':
    if compra > 700:
        cpf = int(input('Digite seu cpf'))
    else:
        print('Nao precisa do cpf')