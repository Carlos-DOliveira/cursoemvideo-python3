''' 075 Desenvolva um programa que leia quatro valores pelo teclado e guarde-os em um tupla. No final, mostre:
quantas vezes apareceu o valor 9
em que posição foi digitado o primeiro valor 3
quais foram os números pares '''

tupla = (int(input('Digite o primeiro valor: ')),
 int(input('Digite segundo valor: ')),
 int(input('Digite terceiro valor: ')),
 int(input('Digite quarto valor: ')))     # forma de criar um tupla, lembrar que a tupla é imutável

print(tupla)

contpares = cont9 = 0

for n in tupla:
    print(n)
    if n == 9:
        cont9 += 1
    if n % 2 == 0:
        contpares += 1
print(f'O valor 9 apareceu {cont9} vezes')
print(f'O valor 9 foi digitado {tupla.count(9)}') # forama direta de contar dentro da tupla
if 3 in tupla:
    print(f'O número 3 apareceu na {tupla.index(3) + 1} posição')    # retira o erro caso não seja digitado o 3
else:
    print('O valor 3 não foi digitado!')

print(f'Os valores pares digitados foram {contpares}')
