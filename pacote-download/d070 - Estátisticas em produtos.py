''' 070 Crie um programa que leia o nome e o preço de vários produtos. O programa deverá perguntar se o usuário vai continuar.
No final, mostre:
qual é o total gasto no compra
quantos produtos custam mais de 1000
qua é o nome do produto mais barato'''
t = 'LOJA SUPER BARATÃO'
altovalor = totalC = 0
maisbarato = 99999999
nomemaisbarato = ''
while True:
    print('-=-' * 20)
    print(f'{t:^60}')
    print('-=-' * 20)
    produto = str(input('Nome do Produto: '))
    preço = float(input('Preço: R$ '))
    resp = 'r'
    totalC += preço
    if preço > 1000:
        altovalor += 1
    if preço < maisbarato:
        maisbarato = preço
        nomemaisbarato = produto
    while resp not in 'SN':
        resp = str(input('Quer continuar: [S/N] ')).strip().upper()[0]
    if resp == 'N':
        break

print(f'''qual é o total gasto no compra - {totalC}
quantos produtos custam mais de 1000 - {altovalor}
qua é o nome do produto mais barato - {nomemaisbarato} que custa R${maisbarato}''')