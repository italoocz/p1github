usuarios = []
PetsCadastrados = []
Produtos = ['Tapetes Higiênicos', 'Areia para Gatos', 'Brinquedos Interativos','Camas Confortáveis', 'Comedouros e Bebedouros Automáticos','Coleiras e Guias', 'Ração de Qualidade', 'Shampoos e Produtos de Higiene', 'Antipulgas e Carrapaticidas', 'Roupinhas e Acessórios', 'Casinhas e Tocas', 'Snacks e Petiscos', 'Caixas de Transporte', 'Fonte de Água para Gatos', 'Kit de Escovação Dental']
PrecosProdutos = ['50,00', '70,00', '85,00', '200,00','60,00','30,00','100,00','40,00','250,00','50,00','80,00','150,00','50,00','100,00', '40,00']
Servicos = ['Banho Simples', 'Tosa Higiênica', 'Tosa Completa', 'Banho + Tosa Completa (Pacote)', 'Hidratação de Pelos', 'Desembolo de Pelos', 'Escovação de Dentes', 'Corte de Unhas (Avulso)']
PrecosServicos = [] # falta colocar
admin = [['admin', '12345']]

while True:
    print("\n===== Au Au Fofura =====")
    print('Bem vindo ao PetShop')
    print('1 - Fazer login')
    print('2 - Cadastrar usuário')
    print('3 - Cadastro de Pet')
    print('4 - Listar Usuários e Pets')
    print('0 - Sair\n')
    opcao = input('Escolha a opção: ')

    if opcao == '0': # Sair do Programa
        print('Encerrando o programa...')
        break

    elif opcao == '1': # login
        usuario = input('Usuario: ')
        senha = input('Senha: ')
        logado = 0
        for i in admin:
            if i[0] == usuario and i[1] == senha:
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
            if opcaoADM == '0':
                print('\nVoltando...\n')
            elif opcaoADM == '1':
                CadProduto = input('Deseja cadastrar produto ou serviço?: ')
                while CadProduto not in ['produto', 'serviço']:
                    print('Valor inválido ')
                    CadProduto = input('Oque deseja cadastrar? (produto ou serviço): ')
                if CadProduto == 'produto':
                    NovoProduto = input('Digite o nome do novo produto: ')
                    NovoPrecoProd = input('Digite o novo preço do produto: ')
                    Produtos.append(NovoProduto)
                    PrecosProdutos.append(NovoPrecoProd)
                    print('Produto e preço cadastrados com sucesso!')
                else:
                    NovoServico = input('Digite o nome do novo serviço: ')
                    NovoPrecoServ = input('Digite o novo preço do serviço: ')
                    Servicos.append(NovoServico)
                    PrecosServicos.append(NovoPrecoServ)
                    print('Serviço e preço cadastrados com sucesso!')


            
    

        if logado == 0:
            print('\nBem vindo cliente!\n')
            print('1 - Comprar produtos')
            print('2 - Agendamentos')
            print('0 - Voltar\n')
            opcaoCliente = input('Escolha a opção: ')
            if opcaoCliente == '0':
                print('\nVoltando...\n')
            elif opcaoCliente == '1': # Comprando Produtos
                for indice in range(len(Produtos)):
                    print(f'Código {indice} - {Produtos[indice]} R$ {PrecosProdutos[indice]}')

                indice = int(input('Digite o indice que deseja comprar: '))






    elif opcao == '2': # Cadastro de usuário
        print('\nCadastro de Usuário.\n')
        nome = input('Digite seu nome:')
        idade = int(input('Digite sua data de nascimento [00/00/0000]: '))
        nacionalidade = input('Onde você nasceu?: ')
        usuarios.append([nome, idade, nacionalidade])

    elif opcao == '3': # Cadastro de Pet
        print('\nCadastro de Pet:\n')
        nomePet = input('Qual o nome do seu Pet?: ')
        sexoPet = input('Qual o sexo do seu Pet? <f/m> : ')
        while sexoPet not in ['m', 'M', 'f', 'F']:
            print('Valor inválido ')
            sexoPet = input('Digite < f ou m >: ')
        if sexoPet == 'm' or sexoPet == 'M':
            sexoPet = 'Masculino'
        else:
            sexoPet = 'Feminino'
        idadePet = int((input('Digite quantos anos tem seu Pet: ')))
        while idadePet > 30 or idadePet < 0:
            print('Idade negativa ou inválida!')
            idadePet = int((input('Digite quantos anos tem seu Pet: ')))
        quilosPet = float(input('Digite quantos quilos tem seu Pet: '))
        while quilosPet > 155 or quilosPet < 0:
            print('Peso negativo ou inválio!')
            quilosPet = float(input('Digite quantos quilos tem seu Pet: '))
        PetsCadastrados.append([nomePet, sexoPet, idadePet, quilosPet])

    elif opcao == '4': # Listar Usuários e Pets
        print('\nLista de usuários e pets\n')
        for list in usuarios:
            print(f'Nome: {list[0]} | Idade: {list[1]} | Nacionalidade: {list[2]}')
        print('\nPets Cadastrados:\n')
        for pets in PetsCadastrados:
            print(f'Nome do pet: {pets[0]} | Sexo: {pets[1]} | Idade: {pets[2]} Anos | Peso: {pets[3]} Quilos')

    
    else:
        print('\nPrograma falhou, escolha a opção correta!\n')