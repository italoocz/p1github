# Faça um programa que leia e valide as seguintes informações: 
# a. Nome: maior que 3 caracteres; 
# b. Idade: entre 0 e 150; 
# c. Salário: maior que zero; 
# d. Sexo: 'f' ou 'm'; 
# e. Estado Civil: 's', 'c', 'v', 'd'; 

# Nome: maior que 3 caracteres
while True:
    nome = input("Digite seu nome: ")
    if len(nome) > 3:
        break
    else:
        print("O nome deve ter mais de 3 caracteres.")

# Idade: entre 0 e 150
while True:

        idade = int(input("Digite sua idade: "))
        if 0 <= idade <= 150:
            break
        else:
            print("Idade deve estar entre 0 e 150.")


# Salário: maior que zero
while True:

        salario = float(input("Digite seu salário: "))
        if salario > 0:
            break
        else:
            print("O salário deve ser maior que zero.")


# Sexo: 'f' ou 'm'
while True:
    sexo = input("Digite seu sexo (f/m): ").lower()
    if sexo in ['f', 'm']:
        break
    else:
        print("Sexo deve ser 'f' para feminino ou 'm' para masculino.")

# Estado Civil: 's', 'c', 'v', 'd'
while True:
    estado_civil = input("Digite seu estado civil (s - solteiro, c - casado, v - viúvo, d - divorciado): ").lower()
    if estado_civil in ['s', 'c', 'v', 'd']:
        break
    else:
        print("Estado civil deve ser 's', 'c', 'v' ou 'd'.")