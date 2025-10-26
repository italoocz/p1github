usuario = input('Digite o nome do usuario: ')
senha = input('Digite sua senha: ')

if usuario == 'admin' and senha == 'mk123456':
    print('Usuário logado com sucesso!')
else:
    print('Senha ou usuário inválidos, tente novamente...')