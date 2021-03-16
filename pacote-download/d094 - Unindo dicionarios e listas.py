''' 094 Crie um programa que leia nome, sexo e idade de várias pessoas, guardando os dados de cada pessoa em um dicionário e todas os dicionários em uma lista.
No final, mostre:
quantas pessoas foram cadastradas
a médias de idade do grupo
uma lisat com todas as mulheres
um lista com todas as pessoas com idade acima da média'''

pessoa = {}
grupo = []
idadetot = 0
while True:
    pessoa['nome'] = str(input('Nome: '))

    while True:
        pessoa['sexo'] = str(input('Sexo: [M/F]')).strip().upper()[0]
        if pessoa['sexo'] in 'MF':
            break
        print('Sexo inválido')

    pessoa['idade'] = int(input('Idade: '))

    grupo.append(pessoa.copy())         # não esquecer do copy

    while True:
        resp = str(input('Quer continuar: [S/N]')).strip().lower()[0]
        if resp in 'sn':
            break
        print('Não entendi.')
    if resp == 'n':
        break

print('-=-' * 30)
print(f'A) O grupo tem {len(grupo)} pessoas')

for c in range(0, len(grupo)):
    idadetot += grupo[c]['idade']

mediaidade = idadetot/len(grupo)
print(f'B) a média de idade é de {mediaidade:.2f} anos')

print('C) As mulhers cadastradas são/é ', end=' ')
for c in range(0, len(grupo)):
    if grupo[c]['sexo'] == 'f':
        print(grupo[c]['nome'], end=' ')

print()
print('D) Lista das pessas que estão acima da média: ', end='')
for c in range(0, len(grupo)):
    if grupo[c]['idade'] > mediaidade:
        print()
        for k, v in grupo[c].items():
            print(f'{k} = {v};', end=' ')

print()
print('<< ENCERRADO >>')
