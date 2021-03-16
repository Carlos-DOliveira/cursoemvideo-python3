def titulo(msg):
    print('-' * 30)
    print(f'{msg:^30}')
    print('-' * 30)


titulo('Hello World')
titulo('CURSO')
titulo('OLÁ')

print()
print()
def soma(a, b):
    s = a - b
    print(f'A = {a}, B = {b}', end=' --> ')
    print(f'{a} - {b} = {s}')


soma(5, 4)
soma(8, 9)
soma(a=4, b=9)
soma(b=4, a=9)


print()
print()
# EMPACOTAR PARÂMETROS


def contador(* núm):
    print(núm)


    for valor in núm:
        print(f'{valor}', end=' ')
    print()
    print(f'Recebi os valores {núm} e são ao todo {len(núm)} números')
    print()


contador(2, 3, 7)
contador(4, 6, 7, 1, 6, 9)
contador(4, 7)

print()
def dobra(lst):
    pos = 0
    while pos < len(lst):
        lst[pos] *= 2
        pos += 1

valores = [6, 3, 9, 1, 0, 2]
dobra(valores)
print(valores)