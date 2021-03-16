''' 060 Faça um programa que leia um número qualquer e mostre o seu factorial
Exp: 5! = 5 x 4 x 3 x 2 x 1 = 120'''

from math import factorial
n = int(input('Digite o número que você deseja fazer o fatorial: '))
fatorial = 1
for c in range(n, 0, -1):
    fatorial *= c
    if c == n:
        print(f'{n}! =', end=' ')
    if c > 1:
        print(f'{c} x',end=' ')
    else:
        print('1 =',end=' ')
print(fatorial)

# método usando a biblioteca

f = factorial(n)
print(f'O fatorial de {n} é {f}')

# com while


total = 1
print(f'{n}! = ', end='')
while n > 0:
    total *= n
    print(f'{n}', end='')
    if n > 1:
        print(' x ', end='')
    else:
        print(' = ', end='')
    n -= 1

print(total)


