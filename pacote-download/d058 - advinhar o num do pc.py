''' 058 Melhore o DESAFIO 028 onde o computador vai pensar em um número entre 0 e 10. Só que agora o jogador vai tentar adivinhar até
acertar, mostradno no final quantos palpites foram necessários para vencer'''

import random
num = int(input('Tente adinvinhar o número de 0 a 10, que o computador pensou: '))
pc = random.randint(1, 10)
cont = 0
while num != pc:
    cont += 1
    if num < pc:
       print('Um pouco MAIS...')
    else:
        print('Um pouco MENOS...')
    num = int(input('Um pouco menos. Tente novamente: '))

print(f'\nParabéns você acertou, com {cont} tentativas e o PC escoheu o {pc}')


# DO PROFESSOR

from random import randint
computador = randint(0, 10)
print('Sou seu computador... Ababei de pensar em um número entre 0 e 10.')
print('Será que você consegue adivinhar qual foi? ')
acertou = False
palpites = 0
while not acertou:
    jogador = int(input('Qual é o seu palpite? '))
    palpites += 1
    if jogador == computador:
        acertou = True
    else:
        if jogador < computador:
            print('Mais... tente mais uma vez')
        else:
            print('Menos... Tente mais uma vez')
print(f'Acertou com {palpites} tentativas')