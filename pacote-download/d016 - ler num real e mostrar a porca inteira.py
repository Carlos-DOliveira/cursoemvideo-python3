''' 016 Crie um programa que leia um número Real qualquer pelo teclado e mostre na tela a sua porção inteira'''

import math
num = float(input('Digite um número real: '))
print(f'Sua parte inteira é {math.floor(num)}')


# da para fazer também usando a função trunq e também da sem usar função int(num)