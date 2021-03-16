''' 039 Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com sua idade:
se ele ainda vai se alistar ao serviço militar
se é a hora de se alistar
se já passou do tempo do alistamento
Seu programa também deverá mostrar o tempo que falta ou que passou do prazo'''
import datetime
nasc = int(input('Que ano você nasceu? '))
anoatual = datetime.date.today().year
idade = anoatual - nasc
print('Sua idade é: ',idade,' anos de idade')

if idade == 18:
    print('Hora de se alistar!')
elif idade > 18:
    print(f'Já passou do tempo do alistamento, já passou {idade - 18} anos')
else:
    print(f'Você ainda terá que se alistar, falta {18 - idade} anos')

