''' 017 Faça um programa que leia o conprimento do cateto oposto e do cateto adjacente de um triângulo retângulo, calcule e mostre o compromento
da hipotenusa'''

import math
co = float(input('Comprimento do cateto oposto: '))
ca = float(input('Comprimento do cateto adjacente: '))
hi = (co ** 2 + ca ** 2) ** (1/2)
print(f'A hipotenusa é {hi:.2f}')

hi2 = math.hypot(co, ca)
print(f'Outra maneira: {hi2:.2f}')