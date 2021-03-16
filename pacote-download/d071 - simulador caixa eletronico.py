''' 071 Crie um programa que simule o funcionamento de um caixa eletrônico. No início, pergunte ao usuário qual será o valor a ser savado
(número inteiro) e o programa vai informar quantas cédulas de cada valor serão entregues
OBS. Considere que o vaixa possui cédulas de R$ 50, 20, 10 e 1'''
t = 'BANCO DO CARLOS'
print('===' * 20)
print(f'{t:^60}')
print('===' * 20)


while True:
    valor = int(input('Digite um valor: R$ '))
    qcinquenta = valor // 50
    resto50 = valor % 50
    qvinte = resto50 // 20
    resto20 = resto50 % 20
    qdez = resto20 // 10
    resto10 = resto20 % 10
    qum = resto10 // 1
    break

print(f'''Será sacado: 
{qcinquenta:4} notas de R$ 50,00. 
{qvinte:4} notas de R$ 20,00. 
{qdez:4} notas de R$ 10,00. 
{qum:4} notas de R$ 1,00''')
print('===' * 20)
print('Volte sempre!!! Tenha um bom dia')