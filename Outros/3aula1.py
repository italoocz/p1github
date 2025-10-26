# in ---
# email = input('Digite um email válido: ')

# if "@" in email:
#     print('Email válido, pois possui o @')
# else:
#     print('Email inválido, falta um @')

# not in ---

email = input('Digite um email válido: ')

while "@" not in email:
    print('Email inválido, falta um @')
    email = input('Digite um email válido: ')

senha = input('Digite sua senha: ')

while "*" not in senha:
    print('Senha inválida, tente novamente')
    senha = input('Digite sua senha: ')