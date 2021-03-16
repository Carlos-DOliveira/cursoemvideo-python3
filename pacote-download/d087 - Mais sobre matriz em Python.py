''' 087 Aprimore o desafio anterior, mostrando no final:
a soma de todos os valroes pares digitados
a soma dos balroes da terceira coluna
o maior valor ad segunda linha'''
matrix = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
maiorvalor = somasegunda = pares = 0

for l in range(0, 3):
    for c in range(0, 3):
        matrix[l][c] = int(input(f'Digite um valor [{l}, {c}]: '))

print('-=-' * 30)

for l in range(0, 3):
    for c in range(0, 3):
        print(f'[ {matrix[l][c]:^5} ]', end=' ')
        if matrix[l][c] % 2 == 0:
            pares += matrix[l][c]
        # if matrix[l][2] > 0:                  aqui da errado pq sempre ele acaba somanando os valores 3x, criar um for separado
            #somasegunda += matrix[l][2]
        if maiorvalor < matrix[1][c]:            # aqui acaba dando certo pq o valor do maior não muda, mas se somasse ele mudaria
            maiorvalor = matrix[1][c]
    print()

for l in range(0, 3):
    somasegunda += matrix[l][2]


print('-=-' * 30)

print(f'A soma dos valores pares é {pares}')
print(f'A soma dos valores da terceira coluna é {somasegunda}')
print(f'O maior valor da segunda linha é {maiorvalor}')