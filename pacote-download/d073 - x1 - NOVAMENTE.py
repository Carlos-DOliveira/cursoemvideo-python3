times = 'São Paulo', 'Internacional', 'Atlético-MG', 'Flamengo', 'Grêmio', \
                 'Palmeiras', 'Fluminense', 'Corinthians', 'Santos', 'Ceará', 'Athletico-PR', \
                 'Atlético-GO', 'Bragantino', 'Sport', 'Vasco', 'Fortaleza', 'Bahia', \
                 'Goiás', 'Botafogo', 'Coritiba'

print('Lista de times do Brasileirão',times)

print('-=-' * 50)
print(f'Os cinco primeiros colocados são: {times[:5]}')

print('-=-' * 50)
print(f'Os 4 últimos são {times[16:]}')

print('-=-' * 50)
print(f'Os times em ordem alfabética: {sorted(times)}')

print('-=-' * 50)
for c, t in enumerate(times):
    if t == 'Flamengo':
        print(f' O Flamengo está na {c + 1}')

# outra maneira que tinha esquecido

print(f'O Flamengo está na {times.index("Flamengo") + 1} posição do campeonato')
print('-=-' * 50)
