while True:
    opcao = input('Sistema CalcPython \n\n1 - Somar\n2 - Subtrair\n3 - Multiplicar\n4 - Dividir\n0 - Sair\n\nDigite sua opção: ')
    if opcao == '0':
        print('Programa encerrado.')
        break
    elif opcao == '1':
        numeros = int(input('Digite quantos números deseja somar: '))
        soma = 0
        for n in range(numeros):
            valor = float(input('Digite o valor: '))
            soma += valor
        print(f'O valor da soma é {soma}')
        break
    elif opcao == '2':
        numeros = int(input('Digite quantos números deseja subtrair: '))
        sub = 0
        for n in range(numeros):
            valor = float(input('Digite o valor: '))
            if (n == 0):
                sub = valor
            else:
                sub -= valor
        print(f'O valor da soma é {sub}')
        break
    elif opcao == '3':
        numeros = int(input('Digite quantos números deseja multiplicar: '))
        multi = 1
        for n in range(numeros):
            valor = float(input('Digite o valor: '))
            multi *= valor
        print(f'O valor da soma é {multi}')
        break
    elif opcao == '4':
        numeros = int(input('Digite quantos números deseja dividir: '))
        div = 0
        for n in range(numeros):
            valor = float(input('Digite o valor: '))
            if (n == 0):
                div = valor
            else:
                div /= valor
        print(f'O valor da soma é {div}')
        break