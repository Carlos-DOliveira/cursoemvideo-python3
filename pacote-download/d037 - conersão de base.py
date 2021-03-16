''' 037 Escreva um programa que leia um número inteiro qualquer e peça para o usuário escolher qual será a base de conversão
1 - binário
2 - octal
3 - hexadecimal'''

num = int(input('Digite um número: '))
conversao = int(input('''Escolha a base que quer converter: 
[ 1 ] binário, 
[ 2 ] octal, 
[ 3 ] hexadecimal'''))
print('Qual a opção? ')

if conversao == 1:
    print(bin(num)[2:])
elif conversao ==2:
    print(oct(num)[2:])
else:
    print(hex(num)[2:])
