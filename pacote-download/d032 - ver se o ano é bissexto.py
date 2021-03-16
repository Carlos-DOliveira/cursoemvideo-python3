''' 032 Ler um ano qualquer e ver se ele é um ano bissexto'''

ano = int(input('Digite um ano: '))

u = ano // 1 % 10
d = ano // 10 % 10
dezena = u + (d * 10)

if dezena % 4 == 0:
    if (u == 0) and (d == 0):
        if ano % 400 == 0:
            print(f'O ano de {ano} é bissexto')
        else:
            print(f'Este ano não é bissexto')
    if (u != 0) and (d != 0):
        print(f'Este é um ano bissexto')
else:
    print('Não é um ano bissexto')

# a do professor

from datetime import date # importa data do sistema

anoo = int(input('Que ano quer analisar? Coloque 0 para analisar o ano atual: '))

if anoo == 0:
    anoo = date.today().year
if anoo % 4 == 0 and anoo % 100 != 0 or ano % 400 == 0:
    print(f'O ano {anoo} é BISSEXTO')
else:
    print('Este ano não é ')