''' 054 Crie um programa que leia o ano de nascimento de 7 pessoas. No final mostres quantas pessoas ainda não atingiram a maioridade
e quantas já são maiores'''

import datetime
count = 0
for c in range(0, 7):
    data = int(input(f'Ano nascimento da pessoa {c + 1}:'))
    idade = datetime.date.today().year - data
    if idade >= 18:
        count += 1

print(f'\nAo todo tivemos {count} pessoas maiores de idade e {7 - count} menores de idade')
