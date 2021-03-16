''' 086 Crie um programa que crie uma matriz de dimensão 3x3 e preencha com valores lidos pelo teclado.
No final, cmostre a matreiz na tela, com a formatação correta'''

matriz = [[], [], []]

for c0 in range(0, 3):
    for c1 in range(0, 3):
        n = int(input(f'Digite um valore para [{c0}, {c1}]: '))
        matriz[c0].append(n)

for c0 in range(0, 3):
    for c1 in range(0, 3):
        print(f'[ {matriz[c0][c1]:^5} ]', end=' ')
    print()

# a do professor foi parecida

matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

for l in range(0, 3):
    for c in range(0, 3):
        matriz[l][c] = int(input(f'Digite um valore para [{l}, {c}]: '))

for l in range(0, 3):
    for c in range(0, 3):
        print(f'[ {matriz[l][c]:^5} ]', end=' ')
    print()