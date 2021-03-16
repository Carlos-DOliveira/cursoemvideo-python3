''' 082 Crie um programa que vai ler vários números e colocar em uma lista.
Depois disso, crie duas listas extras que vão conter apenas os valores pares e os valores ímpares digitados, respectivamente.
Ao final, mostre o conteúdo das três listas geradas
No primeiro loop monte a primeria lista, dps monte as outras'''



lpares = []
limpares = []           # aqui coloquei essas três listas na mesma linha, não deu certo
lista = []
while True:
    lista.append(int(input('Digite um valor: ')))
    resp = str(input('Quer continuar? [S/N]')).strip().lower()[0]
    if resp in 'Nn':
        break

for c in lista:
    if c % 2 == 0:
        lpares.append(c)
    else:
        limpares.append(c)

print(f'A lista completa é {lista}')
print(f'A lista de pares é {lpares}')
print(f'A lista de ímpares é {limpares}')