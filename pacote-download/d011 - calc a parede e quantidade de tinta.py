''' 011 Faça um programa que leia a largura e a alrura de um parade em metros, calcule a sua área e a quantidade de tinta necessária para pintá-la, sabendo que cada litro de tinta, pinta uma área de 2 metros quadrados'''

h = float(input('Qual é a altura: '))
l = float(input('Qual é a largura: '))
a = h * l
print(f'Sua área de parede é {a}m². Você vai precisar de {a/2:.2f} litros de tinta')