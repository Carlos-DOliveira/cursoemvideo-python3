''' 040 Crie um programa que leia duas notas de um alino e calcule sua média, mostrando uma mesngem no final, de acordo com a média atingida
média abaixo de 5 - reprovado
média entre 5 e 6.9 - recuperação
média 7 ou sup - aprovado'''

n1 = float(input('Digite a primeira nota:'))
n2 = float(input('Digite a segunda nota: '))

media = (n1 + n2)/2

if media < 5:
    print(f'Você foi REPROVADO, com a nota {media:.2f}')
elif 5 <= media <= 6.9:
    print((f'Você está de RECUPERAÇÃO, com a média {media:.2f}'))
else:
    print(f'Parabéns, você está APROVADO!!! Média {media:.2f}')