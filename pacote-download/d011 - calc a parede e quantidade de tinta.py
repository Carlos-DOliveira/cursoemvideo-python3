''' 011 Faça um programa que leia a çargura e a alrura de um parade em metros, calcule a sua áre e a quantidade de tinta necessária
para pintá-la, sabendo que cada litro de tinta, pinta uma área de 2mq'''

h = float(input('Qual é a altura: '))
l = float(input('Qual é a largura: '))
a = h * l
print(f'Sua área de parede é {a}m². Você vai precisar de {a/2:.2f} litros de tinta')