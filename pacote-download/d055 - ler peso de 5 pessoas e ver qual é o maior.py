''' 055 Faça um programa que leia o peso de cinco pessoas. No final, mostre qual foi o maior e o menor peso lidos'''


maior = 0
menor = 220
for c in range(0, 5):
    peso = float(input(f'Qual o peso da pessoa {c+1} Kg: '))
    if peso > maior:
        maior = peso
    elif peso < menor:
        menor = peso

print(f'O maior peso é {maior:.2f} Kg e o menor é {menor:.2f} Kg')