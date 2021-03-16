''' 093 Crie um programa que gerencie o aproveitamento de um jogador de futebol. O programa vai ler o nome do jogador e quantas partidas ele jogou.
Depois vai ler a quantidade de gols feitos em cada partida. No final , tudo isso será guardado em um dicionário, incluindo o total de gols feitos durente o
campeonato'''

'''jogador = {}
gols = []
tot = 0
jogador['nome'] = str(input('Digite o nome do jogador: '))
np = int(input(f'Digite a quantidade de partidas que o {jogador["nome"]} jogou? '))
for p in range(0, np):
    gols.append(int(input(f'    Quantos gols na partida {p}: ')))
for n in gols:
    tot += n

jogador['gols'] = gols[:]   # NÃO ESQUECER O [:], NESSE NÃO DEU PROBLEMA, MAS SE ENTRAR EM LOOP VAI DAR
jogador['total'] = tot

print('-=-' * 30)
print(jogador)

print('-=-' * 30)
for k, v in jogador.items():
    print(f'O campo {k} tem o valor {v}')

print('-=-' * 30)
print(f'O jogador {jogador["nome"]} jogou {np} partidas')
for c, v in enumerate(gols):
    print(f'    => Na partida {c}, fez {v} gols.')
print(f'Foi um total de {jogador["total"]}')'''


# a do professor

jogador = dict()
partidas = list()
jogador['nome'] = str(input('Nome do jogador: '))
tot = int(input(f'Quantas partidas {jogador["nome"]} jogou? '))
for c in range(0, tot):
    partidas.append(int(input(f'    Quantos gols na partida {c}? ')))
jogador['gols'] = partidas[:]   # NÃO ESQUECER O [:]
jogador['total'] = sum(partidas)      # novo método

print('-=-' * 30)
print(jogador)
print('-=-' * 30)
for k, v in jogador.items():
    print(f'O campo {k} tem o valor {v}')
print('-=-' * 30)
print(f' O jogador {jogador["nome"]} jogou {len(jogador["gols"])} partidas')
for i, v in enumerate(jogador["gols"]):
    print(f'    => Na partida {i}, fez {v} gols.')
print(f'Foi um total de {jogador["total"]} gols.')