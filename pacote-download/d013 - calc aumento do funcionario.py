''' 013 Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salãria, com 15% de aumento'''

sal = float(input('Digite o seu salário: R$  '))
print(f'O seu salário com aumento de 15% é {sal + (sal * 15)/100:.2f}')
