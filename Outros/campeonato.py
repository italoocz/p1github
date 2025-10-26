# 2 times vão se enfrentar em um campeonato melhor de 3
# pegue os valores e faça a soma deles

print('Qual o placar da primeira partida?')

verde1p = int(input("DIgite quantos pontos o time verde fez na 1 partida:"))
azul_1p = int(input("DIgite quantos pontos o time azul fez na 1 partida:"))

print('Qual o placar da segunda partida?')

verde2p = int(input("DIgite quantos pontos o time verde fez na 2 partida:"))
azul_2p = int(input("DIgite quantos pontos o time azul fez na 2 partida:"))

print('Qual o placar da terceira partida?')

verde3p = int(input("DIgite quantos pontos o time verde fez na 3 partida:"))
azul_3p = int(input("DIgite quantos pontos o time azul fez na 3 partida:"))

verde1p = verde1p + verde2p + verde3p
azul_1p = azul_1p + azul_2p + azul_3p

print(f'O time verde ficou com {verde1p} pontos')
print(f'O time azul ficou com {azul_1p} pontos')

if verde1p > azul_1p:
    print('O time verde é o vencedor')

if azul_1p > verde1p:
    print('O time azul é o vencedor')

if azul_1p == verde1p:
    print('Os times empataram.')