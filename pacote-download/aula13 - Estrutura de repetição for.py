for c in range(0, 5):
    print('oi')        # vai colocar do a até 4 não conta o último

print('\nsegundo exemplo')
for c in range(0, 5):
    print(c)    # aqui vai do 0 até o 4

print('\nterceiro exp')
for c in range(1, 5):
    print(c)    # aqui vai do 1 até o 4

print('\nquarto exemplo')
for c in range(6, 0, -1):
    print(c)    # aqui vai do 6 até o 0

print('\nquinto exemplo')
for c in range(0, 7, 2):
    print(c)

print('\nsexto exemplo')
n = int(input('Digite um número até quanto devo contar: '))
for c in range(0, n+1):
    print(c)

print('\nsétimo exemplo')
ini = int(input('Início: '))
fim = int(input('Fim: '))
passo = int(input('Passo: '))
for c in range(ini, fim, passo):
    print(c)

print('\noitável exemplo')
s = 0
for c in range(0, 4):
   n = int(input('Digite um valor: '))
   s += n
print(f'O somatório de todos os valores foi {s}')