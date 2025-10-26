usuarios = []
produtos = []
admin = [['admin', '12345']]

while True:
    print("\n===== MENU PRINCIPAL =====")
    print('Bem vindo ao PetShop')
    print('1 - Fazer login')
    print('2 - Cadastrar usuário')
    print('0 - Sair\n')
    opcao = input('Escolha a opção: ')

    if opcao == '0':
        print('Encerrando o programa...')
        break

    elif opcao == '1':
        usuario = input('Usuario: ')
        senha = input('Senha: ')
        logado = 0
        for i in admin:
            if(i[0] == usuario and i[1] == senha):
                logado = 1

        if logado == 1:
            print('\nBem vindo ao acesso exclusivo!\n')
            print('1 - Cadastrar produto / serviço')
            print('2 - Alterar um produto / serviço')
            print('3 - Deletar um produto / serviço')
            print('4 - Listar produtos')
            print('5 - Listar serviços')
            print('0 - Voltar\n')
            opcaoADM = input('Escolha a opção: ')
            
    

        elif logado == 0:
            print('\nBem vindo cliente!\n')
            print('1 - Comprar produtos')
            print('2 - Agendamentos')
            print('0 - Voltar\n')
            opcaoCliente = input('Escolha a opção: ')




    elif opcao == 2:
        print('\nCadastro de Usuário.\n')
        nome = input('Digite seu nome:')
        data = int(input('Digite sua data de nascimento [00/00/0000]: '))
        nomePet = input('Qual o nome do seu Pet?: ')
        sexoPet = input('Qual o sexo do seu Pet? <f/m> : ')
        idadePet = int(input('Digite quantos anos tem seu Pet: '))
        quilosPet = float(input('Digite quantos quilos tem seu Pet: '))