# ----- > operadores lógicos < -----

# and ( As operações precisam ser verdadeiras )
# or ( Pode só uma ser verdadeira )

n1 = int(input('Digite um numero: '))
n2 = int(input('Digite outro numero: '))

operacao = input('Digite (somar ou +) para somar os numeros: ')
resultado = 0

if operacao == 'somar' or operacao == ' + ':
    resultado = n1 + n2
else:
    
    resultado = n1 * n2

print(f'O resultado é {resultado}')