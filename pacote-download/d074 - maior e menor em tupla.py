''' 074 Crie um programa que vai gerar cinco npumeros aleatórios e colocar em um tupla.
Depois disso, mostre a listagem de números gerados e também indique o menor e o maior valor que estão na tupla'''

from random import randint

tupla = (randint(1,20), randint(1,20), randint(1,20), randint(1,20), randint(1,20))
for n in tupla:
    print(n, end=' - ')
print(f'\nO maior valor sorteado foi {max(tupla)}')   # pega o maior dentro da tupla
print(f'O menor valor soretado foi: {min(tupla)}')    # pego o menor dentro da tupla