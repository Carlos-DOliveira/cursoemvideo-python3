''' 019 Um professor quer sortear um dos seus quatro alunos para apagar o quadro. Faça um programa que ajude ele, lendo o nome deles e
escrevendo o nome escolhido'''


import random

escolhido = random.randint(1, 4)
print(f'O professor escolheu o número {escolhido}')

# mais complexo

n1 = input('Digite um nome: ')
n2 = input('Digite o segundo nome: ')
n3 = input('Digite o terceiro nome: ')
n4 = input('Digite o quarto nome: ')
lista = [n1, n2, n3, n4]
escolhi = random.choice(lista)
print(f'O professor escolheu o número {escolhi}')
