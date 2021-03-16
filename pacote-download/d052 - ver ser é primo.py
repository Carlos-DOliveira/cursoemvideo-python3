''' 052 Faça um programa que leia um número intiero e dia se ele é ou não um número primo'''

n = int(input('Digite um número: '))
quant = 0
for c in range(1, n+1):
    if n % c == 0:
        print(f'\033[32m {c} \033[m', end=' - ')
        quant += 1
    else:
        print(f'\033[31m {c} \033[m', end=' - ')
print('Acabou')
print(' ')
if quant == 2:
    print('É um número primo')
else:
    print(f'Não é um número primo, pois ele é divisível por {quant} números')