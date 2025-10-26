senha = input('Digite sua senha: ')

while len(senha) < 8:
    print('Senha inválida, digite novamente!')
    senha = input('Digite sua senha: ')

    if (senha == 'admin'):
        break