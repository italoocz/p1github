peso = float(input("Digite quantos quilos de peixe João pegou: "))
print(f'O seu peso foi de {peso} kilos.')
excesso = 0
multa = 0

if peso <= 50:
    print("O peso está adequado")
    print("Não pagará multa")
else:
    excesso = peso - 50
    multa = excesso * 4
    print(f'O peso ultrapassou {excesso} kilos')
    print(f'Vai pagar uma multa de R$ {multa}')