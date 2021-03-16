''' 018 Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo'''


import math
ang = float(input('Digite o angulo: '))
sen = math.sin(math.radians(ang))
cos = math.cos(math.radians(ang))
tan = math.tan(math.radians(ang))
print(f'O angulo é {ang}, o seno é {sen:.2f}, o cosseno é {cos:.2f} e a tangente é {tan:.2f}')
