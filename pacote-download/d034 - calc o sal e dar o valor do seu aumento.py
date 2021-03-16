''' 034 Escreva um prigrama que pergunte o salário de um funcionário e calcule o valor do seu aumento
para salário superiores a R$ 1.250, calcule um aumento de 10%
para inferiores ou iguais, o aumento é de 15%'''

sal = float(input('Digite seu salário: R$ '))

if sal > 1250:
    print(f'Seu aumento é de R$ {sal + (sal * 10/100):.2f}')
else:
    print(f'Seu salário é dev R$ {sal + (sal *15/100):.2f}')