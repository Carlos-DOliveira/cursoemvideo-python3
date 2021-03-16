''' Escreva um programa que leia a velocidade de um carro. Se ele ultrapassar 80 km/h, mostre uma mensagem dizendo que ele foi multado. A multa vai custar R$ 7,00 por cada Km acima do limite.'''

velocidade = float(input('Qual a velocidade do carro em km/h: '))

if velocidade >= 80:
    multa = (velocidade - 80) * 7
    print(f'Você foi multado em R$ {multa:.2f} reais')
else:
    print('Velocidade permitida')
