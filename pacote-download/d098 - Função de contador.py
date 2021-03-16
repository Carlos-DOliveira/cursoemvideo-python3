''' 098 Faça um programa que tenha uma função chamada contador(), que receba três parâmetros: início, fim e passo e realiza a contagem.
Seu programa tem que realizar três contagens através da função criada:
a) de 1 até 10, de 1 em 1
b) de 10 até 0, de 2 em 2
c) uma contagem personalizada'''

from time import sleep

def contador():
    print('-=-' * 20)
    print('Contagem de 1 até 10 em 1 em 1:')
    for c in range(1, 11):
        print(c, end=' ')
    print('FIM')
    print('-=-' * 20)
    print('Contagem de 10 até 0 de 2 em 2:')
    d = 10
    while d >= 0:
        print(d, end=' ')
        d -= 2
    print('FIM')
    print('-=-' * 20)

def contador2():
    print('Agora é sua vez de presonalizar a contagem!')
    i = int(input('Início: '))
    f = int(input('Fim: '))
    p = int(input('Passo: '))
    print('-=-' * 20)
    print(f'Contagem de {i} até {f} em {p} em {p}')
    if p == 0:
        if i < f:
            while i <= f:
                print(i, end=' ')
                i += 1
                sleep(.3)
        else:
            while i >= f:
                print(i, end=' ')
                i -= 1
                sleep(.3)

    elif p < 0:
        if i < f:
            while i <= f:
                print(i, end=' ')
                i -= p
                sleep(.3)
        else:
            while i >= f:
                print(i, end=' ')
                i += p
                sleep(.3)

    elif i < f:
        while i <= f:
            print(i, end=' ')
            i += p
            sleep(.3)

    elif i > f:
        while i >= f:
            print(i, end=' ')
            i -= p
            sleep(.2)
    print('FIM!')

contador()
contador2()
