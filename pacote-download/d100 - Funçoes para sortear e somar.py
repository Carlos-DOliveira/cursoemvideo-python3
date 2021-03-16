''' 100 Faça um programa que tenha um lista chamada números e duas funções chamadas sorteia() e somaPar(). A primeira função vai sortear 5 números
 e vai colocá- lós dentro da lista e a segunda função vai mostrar a soma entre todos os valores PARES sorteados pela função anterior'''

from random import randint
from time import sleep

def sorteando():
    print('Sorteando 5 valroes da lista: ', end=' ')
    for c in range(0, 5):
        n = randint(0, 10)
        print(n, end=' ')
        sleep(.4)
        lista.append(n)
    print('PRONTO!')

def somando(lst):
    soma = 0
    for c in lst:
        if c % 2 == 0:
            soma += c
    print(f'Somando os valroes pares de {lst}, temos {soma}')
    lista.clear()


lista = []

sorteando()
somando(lista)
print('-=-' * 20)
sorteando()
somando(lista)
print('-=-' * 20)
sorteando()
somando(lista)

