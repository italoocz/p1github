# # # for <variavel> in ()

# # x = 1
# # while x <=5:
# #     print(x)
# #     x += 1

# # for x in (10,9,8,7,6,5,4,3,2,1):
# #     print(x)

# x = tuple(range(1000))
# print(x)

# for x in range(10):
#     print('Loop executando 10x')

# n = int(input('Digite um numero: '))

# for x in range(n):
#     print(x + 1)

notas = int(input('Digite quantas notas você quer calcular: '))
soma = 0
for n in range(notas):
    nota = float(input('Digite a nota: '))
    soma += nota

print(f'A média é {soma/notas}')