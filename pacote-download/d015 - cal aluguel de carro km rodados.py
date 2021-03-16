''' 015 Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado e a quantidade de diaz pelos quais
ele foi alugado. Calcule o preço a pagar, sabendo que o carro custa R$ 60 por dia e R$ 0,15 por Km rodado '''

d = int(input('Quantos dias foi alugado? '))
t = d * 60    # 60 reais o dia
km = float(input('Quantos km rodados? '))
kmt = km * 0.15
print(f'O valor total vai ser: {t + kmt}')
