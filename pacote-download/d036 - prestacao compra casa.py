''' 036 Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa. O programa vai perguntar
o valor da casa
salário do comprador
e em quantos anos vai quere pagar.
Calcule o valor da prestação mensal, sabendo que ela não pode excede 30% do salário ou então o empréstimo será negado'''

valorcasa = float(input('Digite o valor da casa: R$ '))
salario = float(input('Digite o salário: R$'))
anospagar = float(input('Quantos anos quer pagar? '))

salanual = salario * 12

if (valorcasa/anospagar) > (salanual * 30/100):
    print(f'A necessidade anual é de {valorcasa/anospagar:.2f}, da prestação R$ {(valorcasa/anospagar)/12} por mês e ultrapassa a 30% da sua renda anual que é de {salanual * 30/100:.2f}')
else:
    print(f'Parabéns você pode comprar a casa')
