''' 092 Crie um programa que leia nome, ano de nascimento e carteira de trabalho e cadastre-os (com idade) em um dicionário
 se por acaso o CTPS for digrente de zero, o ficionário receberá também o ano de contratação e o salário. Calcule e acrescente além da idade,
 com quantos anos a pessoa vai se aposentar'''
from datetime import date

pessoa = {}


pessoa['nome'] = str(input('Nome: '))

anonascimento = int(input('Ano de nascimento: '))
#anoatual = date.today().year
#pessoa['idade'] = anoatual - anonascimento
pessoa['idade'] = date.today().year - anonascimento

pessoa['CTPS'] = int(input('Carteira de trabalho (0 não tem): '))

if pessoa['CTPS'] == 0:
    print(pessoa)
else:
    pessoa['contratação'] = int(input('Ano da contratação: '))
    anoaposentadoria = pessoa['contratação'] + 35     # ano que vai se aposentar
    idadeaposentadoria = anoaposentadoria - anonascimento
    pessoa['salário'] = float(input('Salário: R$'))

    for k, v in pessoa.items():
        print(f'{k} tem o valor {v}')
    print(f'aposentadoria tem o valor {idadeaposentadoria}')