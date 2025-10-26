hackton = int(input('Informa o número de participantes do time: '))
ingresso = 44

if hackton >= 5:
    total = hackton * ingresso
    desconto = total * 0.10
    valorF = total - desconto
else:
    valorF = hackton * ingresso

print(f'O número de participantes é de: {hackton}')
print(f'O valor total é de : R$ {valorF}')