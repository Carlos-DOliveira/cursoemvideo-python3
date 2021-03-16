''' 066 Crie um programa que leia vários números inteiros pelo teclado. O program só vai para quando o usuário digitar o valor 999,
que é a condição de parada. No final, mostre quantos números foram figitados e qual foi a soma entre eles(desconsiderando o flag)'''
soma = cont = 0

while True:
    n = int(input('Digite um número [999 para parar]: '))
    if n == 999:
        break
    cont += 1
    soma += n
print(f'Foi digitado {cont}  números e a soma entre eles foi {soma}')