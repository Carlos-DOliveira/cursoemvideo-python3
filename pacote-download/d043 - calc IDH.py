''' 043 Desenvolva um programa que leia o peso e a altura de uma pessoa, calcule seu IMC e mostre seu status, de acordo com a tabela abaixo:
abaixo de 18.5: abaixo do peso
entre 18.5 e 25: peso dial
de 25 até 30: sobrepeso
de 30 até 40: obesidade
acima de 40: obesidade mórbida'''

peso = float(input('Digite seu peso em kg: '))
altura = float(input('Digite sua altura em metros: '))

imc = peso / (altura * altura)
print(f'Seu IMC é de {imc:.2f}')
if imc < 18.5:
    print('Você está abaixo do peso.')
elif 18.5 <= imc < 25:
    print('Peso ideal')
elif 25 <= imc < 30:
    print('Sobrepeso')
elif 30 <= imc < 40:
    print('Obesidade.')
else:
    print('Obesidade mórbida.')