''' 012 Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto'''


valor = float(input('Digite o valor do protudo: R$ '))
print(f'O Valor do produto com 5% de desconto é {valor - (valor * 5)/100:.2f}')