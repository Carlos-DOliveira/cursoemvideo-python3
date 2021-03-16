''' 045 Crie um programa que faça o computador jogar jokenpô com vocês'''

import random,time
lista = [1, 2, 3]
n = random.choice(lista)
if n == 1:
    pc = 'pedra'
elif n == 2:
    pc = 'tessoura'
else:
    pc = 'papel'

escolha = int(input('Escolha um número: 1 - pedra. 2 - tersosura. 3 - papel: '))

if escolha == 1:
    vc = 'pedra'
elif escolha == 2:
    vc = 'tessoura'
else:
    vc = 'papel'


time.sleep(1)
print('JO')
time.sleep(1)
print('KEN')
time.sleep(1)
print('PO')
print('')

print(f'compudaror: {pc} X {vc} : você')
print('')

if n == escolha:
    print('EMPATE')
elif n == 1 and escolha == 2:
    print(f'O Pc escolheu pedra, ele ganhou!!!')
elif n == 1 and escolha == 3:
    print(f'Você ganhou, papel ganha de pedra')
elif n == 2 and escolha == 1:
    print('Pedra ganha de tessoura, você ganhou.')
elif n == 2 and escolha == 3:
    print('O PC ganhou, tessou ganha de papel')
elif n == 3 and escolha == 1:
    print(' O PC escolheu papel, papel ganha de pedra. Parabéns!!')
else:
    print('Você escolheu tessoura e ela ganha de papel. Parabéns!!!')
