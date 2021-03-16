'''Faça um programa que jogue par ou ímpar com o computador. O jogo só será interropido qudno o jogador perder,
mostrado o total de vitórias consecutivas que ele conquistrou no final do jogo'''
from time import sleep
from random import randint
count = 0

while True:
    e = str(input('Escolha [P] para para ou [I] para ímpar. ')).strip().upper()
    n = int(input('Escolha seu número de 1 a 10: '))
    pc = randint(1, 10)

    print('3')
    sleep(1)
    print('2')
    sleep(1)
    print('1')

    if e == 'P':
        if (n + pc) % 2 == 0:
            print(f'Parbéns você ganhou!!! Você escolheu {n} e o pc {pc}')
            print('Você está com sorte, tente mais uma vez')
        else:
            print(f'Deu ímpar. O computador ganhou, ele escolheu {pc} e você escolheu {n}')
            break
    if e == 'I':
        if (n + pc) % 2 == 0:
            print(f'Deu par. O computador ganhou, ele escolheu {pc} e você escolheu {n}')
            break
        else:
            print(f'Parbéns você ganhou!!! Você escolheu {n} e o pc {pc}')
            print('Você está com sorte, tente mais uma vez')
    count += 1
print(f'Você ganhou {count} vezes')