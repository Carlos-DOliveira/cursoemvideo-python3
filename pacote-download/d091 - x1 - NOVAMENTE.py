from random import randint
from time import sleep
from operator import itemgetter

jogadores = {'Jogador1': randint(1, 26),
             'Jogador2': randint(1, 26),
             'Jogador3': randint(1, 26),
             'Jogador4': randint(1, 26),
             'Jogador5': randint(1, 26),
             'Jogador6': randint(1, 26)}
print('VALORES SORETADOS')

for k, v in jogadores.items():
    print(f'   O {k} tirou {v}')
    sleep(.4)

ranking = sorted(jogadores.items(), key=itemgetter(1), reverse=True)

print(ranking)

for i, v in enumerate(ranking):
    print(f' O {i+1}º lugar é o {v[0]} com {v[1]}')