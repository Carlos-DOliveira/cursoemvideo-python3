''' 088 Faça um programa que ajude um jogador da MEGA SENA a criar palpites. O programa vai perguntar quantos jogos serão gerados
e vai sortear 6 números entre 1 e 60 para cada jogo, cadastrado tudo em uma lista composta'''
from random import randint
from time import sleep
jogos = []
rodada = []
total = contador = 0

t = 'JOGO DA MEGA SENA'
print('-' * 40)
print(f'{t:^40}')
print('-' * 40)

n = int(input('Quantos jogos você quer que eu sorteie? '))

'''for q in range(0, n):
    jogada = [randint(1, 60), randint(1, 60), randint(1, 60), randint(1, 60), randint(1, 60), randint(1, 60)]   # aqui plotei depois um prob
    jogos.append(jogada[:])   # dessa manira ele pode repetir os números, então da errado
    jogada.clear()'''

while total <= n:
    contador = 0
    while True:
        num = randint(0, 60)
        if num not in rodada:
            rodada.append(num)
            contador += 1
        if contador >= 6:
            break
    jogos.append(rodada[:])
    rodada.clear()
    total += 1

for c in range(0, n):
    jogos[c].sort()

print(f'-=-=-=-=- < SORTEANDO {n} JOGOS > -=-=-=-=-')
for i in range(0, n):
    print(f'Jogo {i + 1}: {jogos[i]}')
    sleep(.5)

print(f'-=-=-=-=- <    BOA SORTE!     > -=-=-=-=-')

