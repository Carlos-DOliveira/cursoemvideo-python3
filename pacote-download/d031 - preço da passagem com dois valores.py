''' 031 Desenvolva um programaque pergunte a distânia de uma viagem em KM.
Calcule o preço da passagem, cobrando R$ 0,50 por Km para viagens de até 200 km e R$ 0,45 para viagens mais longas'''

dist = float(input('Digite quantos km é a viagem: '))

if dist <= 200:
    print(f'Sua viagem vai custar: R$ {dist * 0.5:.2f} reais, com o valor por km de 0,50')
else:
    print(f'Sua viagem irá custar: R$ {dist * 0.45:.2f} reais, com o valor por km de 0,45')