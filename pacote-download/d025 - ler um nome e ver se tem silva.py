''' 025 Crie um programa que leia o nome de uma pessoa e diga se ela tem SILVA no nome '''

nome = str(input('Digite um nome completo: ')).strip().lower()


tem = nome.find('silva')
print(tem)
if ( tem > 0):
    print('Nome Silva encontrado')
else:
    print('Nome não encontrado')

print(f'Seu nome tem Silva: {"silva" in nome.lower()}')