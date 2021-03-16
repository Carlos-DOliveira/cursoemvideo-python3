lista = ('Lápis', 1.75, 'Borracha', 2, 'Caderno', 15.9, 'Estojo', 25, 'Transferidor', 4.20,
         'Compasso', 9.99, 'Mochila', 120.32, 'Canetas', 22.30, 'Livro', 34.9)

print('-' * 50)
print(f'{"LISTAGEM DE PREÇOS":^50}')
print('-' * 50)

for cont, c in enumerate(lista):
    if cont % 2 == 0:
        print(f'{c:.<40} R$', end=' ')
    else:
        print(f'{c:>6.2f}')

print('-' * 50)
