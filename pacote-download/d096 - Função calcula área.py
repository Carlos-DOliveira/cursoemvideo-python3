''' 096 Faça uma programa qeu tenha uma função chamada área(), que receba as dimensões de um terreno retangular( largura e comprimento ) e mostre a área do terreno'''

def controleterrenos(a, b):
    print()
    print('Controle terrenos')
    print('-' *30)
    print(f'A área de terreno {a}x{b} é de {a * b}m²')


l = float(input('LARGURA (m): '))
c = float(input('COMPRIMENTO: '))
controleterrenos(l, c)