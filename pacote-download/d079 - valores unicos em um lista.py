''' 079 Crie um progama onde o usuário possa digitar vários valores numéricos e cadastre-os em uma lista. caso
o número já exista laá dentro, ele não será adicionado. No final, serão exibidos todos os valores únicos digitados, em ordem
crescente'''

lista = []

while True:
    n = int(input('Digite um valor: '))
    if n not in lista:
        lista.append(n)
        print('Valor adicionado com sucesso')
    else:
        print('Valor duplicado. Não vou adicionar')

    while True:
        resp = str(input('Quer continuar [S/N]')).strip().lower()[0]
        if resp in 'sn':
            break
        else:
            print('Não entendi.', end=' ')
    if resp == 'n':
        break
lista.sort()
print(f'lista organizada {lista}')