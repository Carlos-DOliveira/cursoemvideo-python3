''' 091 Crie um programa onde 4 jogadores joguem um dado e tenham resultados aleatórios. Guarde esses resultados em um dicionário
. No final, colocque esse dicionário em ordem, sabendo que o vencedor tirou o maior número no dado'''

from random import randint
from time import sleep
from operator import itemgetter

jogo = {'jogador1': randint(1, 6),
        'jogador2': randint(1, 6),
        'jogador3': randint(1, 6),
        'jogador4': randint(1, 6)}

print()
print(jogo)   # aqui podemos ver a lista

ranking = list()
print('Valores sorteados: ')

print()

for k, v in jogo.items():
    print(f' {k} tirou {v} no dado.')
    sleep(.5)

ranking = sorted(jogo.items(), key=itemgetter(1), reverse=True)  # aqui está usando o sorted, ele é temporário, então tem que jogar
# em uma variável, depois jogo.items, que são os dois do dicionário, depois esse itemgetter(1) se fosse 0 ia pegar a key, não o value
# e no final usa o reverse=True pq ler a lista ao contrário.

print()
print(ranking)  # aqui podemos ver que são tuplas dentro de dicionários, então na hora de mostrar na tela, é com o enumerate e não com
# copy

print()
for i, v in enumerate(ranking):
    print(f'O {i+1} lugar foi o {v[0]} com {v[1]} ')
