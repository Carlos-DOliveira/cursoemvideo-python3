''' 076 Crie um programa que tenah um tupla única com nomes de profutos e seus respectivos preços, na sequência.
No final, mostre uma listagem de preços, organizando os dados em forma tabular.'''

lista = ('Lápis', 1.75, 'Borracha', 2, 'Caderno', 15.9, 'Estojo', 25, 'Transferidor', 4.20,
         'Compasso', 9.99, 'Mochila', 120.32, 'Canetas', 22.30, 'Livro', 34.9)

t = 'LISTAGEM DE PREÇOS'
print('-' * 33)
print(f'{t:^30}')
print('-' * 33)

for pos, n in enumerate(lista):   # usando o enumerate
    if pos % 2 == 0:
        print(f'{n:.<22}R$', end=' ')
    else:
        print(f'{n:>6.2f}')     # com formatação de duas casas decimais e com 6 casa alinhadas a direita
print('-' * 33)
