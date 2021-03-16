''' 023 Faça um programa que leia um número de 0 a 9999 e mostre na tela cada um dos dígitos separados.
Ex:
Digite um número:1834
unidade: 4 dezena: 3 centena: 8 milhar: 1'''

# errei, quando coloco 4 dígitos deu certo, mas se quando coloco com menos da erro

'''num = str(input('Ditigite um número até 9999: '))

print(f'Casas das milhar: {num[0]}')
print(f'Casa das centenas: {num[1]}')
print(f'Casa das dezenas: {num[2]}')
print(f'Casa das unidades: {num[3]}')'''


num = int(input('Informe um número de até 9999: '))
u = num // 1 % 10
d = num // 10 % 10
c = num // 100 % 10
m = num // 1000 % 10

print(f'Analisando o número {num}')
print(f'Unidade {u}')
print((f'Dezena: {d}'))
print(f'Centena: {c}')
print(f'Milhar: {m}')

'''
O cálculo:
divisão inteira primeiro
8653 // 1 == 8653   -> div por 10, o resto da div é 3
8653 // 10 == 865   -> div por 10, o resto da div é 5
8653 // 100 == 86   -> div por 10, o resto da div é 6
8653 // 1000 == 8   -> div por 10, o resto da div é 8

'''