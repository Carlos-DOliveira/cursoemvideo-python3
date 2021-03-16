''' 051 Desenvolva um programa que leia o primeiro termo e a razão de uma PA, No final, mostre os 10 primeiros termos
 dessa progressão'''

f = '10 TERMOS DE UMA PA'
print('=' * 40)
print(f'{f:^40}')
print('=' * 40)

n1 = int(input('Digite o primeiro termo: '))
r = int(input('Digite a razão: '))

for c in range(0, 10):
    print(n1, end=' -> ')
    n1 += r

print('Acabou!')