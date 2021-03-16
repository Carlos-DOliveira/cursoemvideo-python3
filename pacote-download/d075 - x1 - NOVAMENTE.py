tupla = ((int(input('Digite um número: '))),
         (int(input('Digite um número: '))),
         (int(input('Digite um número: '))),
         (int(input('Digite um número: '))),
         (int(input('Digite um número: '))),
         (int(input('Digite um número: '))),
         (int(input('Digite um número: '))),
         (int(input('Digite um número: '))))

print('-=-' * 30)
print(f'Você digitou os valores: {tupla}')

print('-=-' * 30)
print(f'O valor 9 foi digitado: {tupla.count(9)} vezes')

print('-=-' * 30)
if 3 in tupla:
    print(f'O valor 3 apareceu na posíção {tupla.index(3) + 1}')
else:
    print('Valor 3 não digitado')

print('-=-' * 30)
print('Os valores pares digitados foram: ', end=' ')
for n in tupla:
    if n % 2 == 0:
        print(n, end=' - ')

print()
print('-=-' * 30)


