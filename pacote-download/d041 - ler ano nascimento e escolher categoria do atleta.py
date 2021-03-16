''' 041 A confederação Nacional de Natação precisa de um programa que leia o ano de nascimento de um atleta e mostre sua categoria, de
acordo com a idade:
até 9 anos: MIRIM
até 14 anos: INFANTIL
até 19 anos: JUNIOR
até 20 anos: SÊNIOR
acimo: MASTER'''

from datetime import date

anonasc = int(input('Digite seu ano de nascimento: '))
anoatual = date.today().year
idade = anoatual - anonasc
print(f'Sua idade é {idade}')
if idade < 9:
    print('Categoria : MIRIM')
elif 9 <= idade < 14:
    print('Categoria INFANTIL')
elif 14 <= idade < 19:
    print('Categoria JUNIOR')
elif 19 <= idade < 20:
    print('Categoria SÊNIOR')
else:
    print('Categoria MASTER')
