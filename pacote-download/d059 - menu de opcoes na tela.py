''' 059 Crie um programa que leia dois valores e mostre um emnu na tela:
[1] somar
[2] multiplicar
[3] maior
[4] novos números
[5] sair do programa
Seu programa devera´realizar a operção solicitada em cada caso'''

sair = False

while not sair:
    n1 = float(input('Digite o primeiro valor: '))
    n2 = float(input('Digite o primeiro valor: '))
    print('''Qual a opção você deseja?
    [1] somar
    [2] multiplicar
    [3] maior
    [4] novos números
    [5] sair do programa
    ''')
    o = int(input(': '))

    if o == 1:
        r = n1 + n2
        print(f'O resultado da soma de {n1} + {n2} é  {r}')
    elif o == 2:
        r = n1 * n2
        print(f'O resultado da multiplicação de {n1} x {n2} é {r}')
    elif o == 3:
        if n1 > n2:
            print(f'O número {n1} é maior que {n2}')
        elif n2 > n1:
            print(f'O número {n2} é maior que {n1}')
        else:
            print('Os dois números são iguais')
    elif o == 4:
        print('')
    elif o == 5:
        sair = True
    else:
        print('Não entendi digite os valores novamente')

    print('=-' * 20)
    print('Digite as opções novamente.')