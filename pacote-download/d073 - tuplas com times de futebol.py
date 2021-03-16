''' 073 Crie uma tupla preenchida com os 20 primeiros colocados da tabela do compeonato brasileiro, no ordem de colocação.
 Depois mostre:
 Apenas os 5 primeiros colocados.
 Os últimos 4 colocados da tabela
 uma lista com os times em ordem alfabética
 em que posição na tabela está o time do flamengo '''

ordemcapeonato = 'São Paulo', 'Internacional', 'Atlético-MG', 'Flamengo', 'Grêmio', \
                 'Palmeiras', 'Fluminense', 'Corinthians', 'Santos', 'Ceará', 'Athletico-PR', \
                 'Atlético-GO', 'Bragantino', 'Sport', 'Vasco', 'Fortaleza', 'Bahia', \
                 'Goiás', 'Botafogo', 'Coritiba'

print(ordemcapeonato)
print('-=-=-' * 43)
print('Os 5 primeiros são: ', ordemcapeonato[:5])
print('-=-=-' * 43)
print('Os 4 últimos colocados são:', ordemcapeonato[-4:])
print('-=-=-' * 43)
print(f'A orde alfabética é {sorted(ordemcapeonato)}')
print('-=-=-' * 43)
print(f'O Flamengo está na {ordemcapeonato.index("Flamengo") +1 } posião da tabela, lembrando que a lista começa do 0')