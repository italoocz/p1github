
valor = int(input("Digite o valor do saque (mínimo R$10 e máximo R$600): "))

    # Cálculo usando operador módulo

n100 = valor // 100
resto = valor % 100

n50 = resto // 50
resto = resto % 50

n10 = resto // 10
resto = resto % 10

n5 = resto // 5
resto = resto % 5

n1 = resto  # o que sobra já são notas de 1

print(f"Saque de R${valor} realizado com as seguintes notas:")
if n100 > 0: print(f"{n100} nota(s) de R$100")
if n50 > 0: print(f"{n50} nota(s) de R$50")
if n10 > 0: print(f"{n10} nota(s) de R$10")
if n5 > 0: print(f"{n5} nota(s) de R$5")
if n1 > 0: print(f"{n1} nota(s) de R$1")

        