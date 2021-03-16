velocidade = float(input('Qual a velocidade do carro em km/h: '))

if velocidade >= 80:
    multa = (velocidade - 80) * 7
    print(f'Você foi multado em R$ {multa:.2f} reais')
else:
    print('Velocidade permitida')
