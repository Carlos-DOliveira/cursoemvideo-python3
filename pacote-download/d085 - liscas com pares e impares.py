''' 085 Crie um programa onde o usuário possa digitar sete valores numériocos e cadastre-os um uma lista única que
 mantenha separados o s valores pares e ímpares. No fina , mostre os valores pares e ímpres em ordem crescente'''
pares = []
impares = []
números = []

for c in range(0, 7):
    n = int(input(f'Digite o {c+1}º valor: '))
    if n % 2 == 0:
        pares.append(n)
    else:
        impares.append(n)

números.append(pares)
números.append(impares)

print('-=-' * 30)
números[0].sort()
números[1].sort()
print(f'Os valores pares digitados foram: {números[0]}')
print(f'Os valores ímpares digitados foram: {números[1]}')


# a do professor:

núm =[[], []]
valor = 0
for c in range(1, 8):
    valor = int(input(f'Digite o {c} valor:'))
    if valor % 2 == 0:
        núm[0].append(valor)
    else:
        núm[1].append(valor)

print()
núm[0].sort()
núm[1].sort()
print(f'Os valores pares digitados foram: {núm[0]}')
print(f'Os valores ímpares digitados foram: {núm[1]}')