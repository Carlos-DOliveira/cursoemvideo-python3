''' 033 Faça um programa que leia três números e moste qual é o menor e qual é o maior entre eles'''

n1 = int(input('Digite o primeiro número: '))
n2 = int(input('Digite o segundo número: '))
n3 = int(input('Digite o terceiro número: '))

if (n1 > n2) and (n1 > n3):
    if n2 > n3:
        print(f'O maior é {n1}, o menor é {n3}')
    else:
        print(f'O maior é {n1} e o menor é {n2}')
if (n2 > n1) and (n2 > n3):
    if n1 > n3:
        print(f'O maior é {n2}, o menor é {n3}')
    else:
        print(f'O maior é {n2} e o menor é {n1}')
if (n3 > n1) and (n3 > n2):
    if n1 > n2:
        print(f'O maior é {n3}, o menor é {n2}')
    else:
        print(f'O maior é {n3} e o menor é {n1}')

# do professor


a = int(input('Digite o primeiro número: '))
b = int(input('Digite o segundo número: '))
c = int(input('Digite o terceiro número: '))
# verificando quem é menor
menor = a
if b < a and b < c:
    menor = b
if c < a and c < b:
    menor = c
# verificando quem é maior
maior = a
if b > a and b > c:
    maior = b
if c > a and c > b:
    maior = c
print(f'O maior é {maior} e o menor é {menor}')