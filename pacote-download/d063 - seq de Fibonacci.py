''' 063 Escreva um programa que leia um número inteiro qualquer e mostre na tela os n primeiros elementos de uma sequência de Fibonacci'''

titulo = 'Sequência de Fibonacci'
print('-=-' * 30)
print(f'{titulo:^90}')
print('-=-' * 30)

quantidade = int(input('Quantidade da Sequência de Fibonacci: '))

c = 3  # começei no 3 pq colocquei valores fora do while
n = 0
n1 = 1
seq = 0
print('~' * 90)
print(n,' -> ', end='')
print(n1,' -> ', end='')
while c <= quantidade:
    seq = n + n1
    print(seq,' -> ', end='')
    n = n1
    n1 = seq
    c += 1
print('FIM')
print('~' * 90)