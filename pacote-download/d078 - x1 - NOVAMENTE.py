lista = []

for n in range(0, 8):
    num = int(input(f'Digite o valor da posição {n}: '))
    lista.append(num)
print('-=-' * 30)
print(f'Você digitou os valores : {lista}')
print(f'O maior valor {max(lista)}', end=' ')
for c, n in enumerate(lista):
    if n == max(lista):
        print(c, end='... ')
print()
print(f'O menor valor {min(lista)}', end=' ')
for c, n in enumerate(lista):
    if n == min(lista):
        print(c, end='... ')