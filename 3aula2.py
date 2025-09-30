senha = input('Digite a senha (minimo 8 caracteres): ')

tamanho = len(senha) # length
while tamanho < 8 and tamanho > 16 or ('*' not in senha):
    print(f'o tamanho do texto é: {tamanho}')
    print('Senha com caracteres insuficientes, ou sem *')
    senha = input('Digite a senha (minimo 8 caracteres): ')
    tamanho = len(senha)
if tamanho >= 8 and tamanho <= 16 and "*" in senha:
    print(f'o tamanho do texto é: {tamanho}')
    print('Senha válida')
