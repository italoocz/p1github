# # 16. Faça um programa que calcule as raízes de uma equação do segundo grau, na forma ax2 + bx + c. 
# # O programa deverá pedir os valores de a, b e c e fazer as consistências, 
# # informando ao usuário nas seguintes situações:
# a. Se o usuário informar o valor de A igual a zero, a equação não é do segundo grau 
# e o programa não deve fazer
# pedir os demais valores, sendo encerrado;
# b. Se o delta calculado for negativo, a equação não possui raizes reais. Informe ao usuário 
# e encerre o programa;
# c. Se o delta calculado for igual a zero a equação possui apenas uma raiz real; informe-a ao 
# usuário;
# d. Se o delta for positivo, a equação possui duas raiz reais; informe-as ao usuário;

a = int(input('Digite o valor da a: '))
b = int(input('Digite o valor da b: '))
c = int(input('Digite o valor da c: '))

delta = b ** b - 4 * a * c

if a == 0:
    print('A equação nao é do segundo grau, programa encerrado.')
elif delta < 0:
    print('A equação é negativa e nao possui raiz real, programa encerrado.')
elif delta == 0:
    print('A equação possiu apenas uma raiz real')
elif delta > 0:
    print('A equação possiu duas raizes reais.')