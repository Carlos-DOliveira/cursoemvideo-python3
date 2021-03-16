''' 084 Faça um programa que leia nome e peso de várias pessoas, guardando tudo em uma lista. No final, mostre:
Quantas pessoas foram cadastradas
uma listagem com as pessos mais pesadas
uma listagem com as pessaos mais leves'''

dados = []
cadastro = []
totalpessoas = maiorpeso = 0
menorpeso = 999

while True:
    dados.append(str(input('Nome: ')))
    dados.append(float(input('Peso: ')))
    cadastro.append(dados[:])     # aqui estou criando uma cópia
    dados.clear()

    totalpessoas += 1

    while True:
        resp = str(input('Quer continuar? [S/N]')).strip().lower()[0]
        if resp in 'sn':
            break
        print('Não entendi.', end=' ')
    if resp == 'n':
        break

print(f'Ao todo, você cadastrou {totalpessoas} pessoas')
print(f'Ao todo, você cadastrou {len(cadastro)} pessoas')

for c, p in enumerate(cadastro):
    if cadastro[c][1] > maiorpeso:
        maiorpeso = cadastro[c][1]
    if cadastro[c][1] < menorpeso:
        menorpeso = cadastro[c][1]



print(f'O maior peso foi {maiorpeso}Kg. Peso de ', end=' ')
for c, p in enumerate(cadastro):
    if cadastro[c][1] == maiorpeso:
        print(f'{cadastro[c][0]}', end=' ')
print()
print(f'O menor peso foi {menorpeso} Kg. Peso de', end=' ')
for c, p in enumerate(cadastro):
    if cadastro[c][1] == menorpeso:
        print(f'{cadastro[c][0]}', end=' ')
