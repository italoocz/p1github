idade = int(input('Digite sua idade: '))

if idade >= 18:
    print('É obrigado a votar')
elif idade >= 16 and idade < 18:
    print('Voto é facultativo')
else:
    print('Não pode voltar')