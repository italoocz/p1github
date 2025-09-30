litro = float(input('Quantos litros você abasteceu?: '))
tipo = input('Qual o tipo de combustivel, <A/G>: ')

gasolina = 2.5
alcool = 1.9

if tipo == 'A':
    valorT = (litro * alcool)
    if litro <= 20:
        porcentagem = valorT * 0.03
        desconto = valorT - porcentagem
    elif litro > 20:
        porcentagem = valorT * 0.05
        desconto = valorT - porcentagem

if tipo == 'G':
    valorT = (litro * gasolina)
    if litro <= 20:
        porcentagem = valorT * 0.04
        desconto = valorT - porcentagem
    elif litro > 20:
        porcentagem = valorT * 0.06
        desconto = valorT - porcentagem

print(f'Com {litro} litros de combustivel, você irá pagar R$ {desconto:.2f}')