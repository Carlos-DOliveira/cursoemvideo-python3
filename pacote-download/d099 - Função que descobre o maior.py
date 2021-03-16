''' 099 Faça um programa que tenha uma função chamada maior(), que receba vários parâmetros com valores interios.
Seu programa tem que analisar todos os valores e dizer qual deles é o maior.'''

from time import sleep

def maior(* num):
    print('\nAnalisando valores passados...')
    for valor in num:
        print(valor, end=' ')
        sleep(.3)

    m = max(num)
    print(f'\n Foram informados {len(num)} valores')
    print(f'O maior valor é {m}')


maior(2, 9, 4, 5, 7, 1)
maior(4, 7, 0)
maior(1, 2)
maior(6)
# maior()   - esse aqui não está dando certo, ao invés de max, teria que fazer na mão