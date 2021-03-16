'''lista = []
print(len(lista))
for n in range(0, 5):
    valor = int(input('Digite um valor: '))
    if len(lista) <= 2 or max(lista) < valor:
        print(f'O valor {valor} foi adicionado na posição {len(lista) + 1}')
        lista.append(valor)
    else:
        for c, numero in enumerate(lista):
            if numero < lista[c]:
                lista.append(valor)
                print(f'Valor adicionado na posição {c}')
print(lista'''

a, b, c = 5, 3.2, "Hello"

print (a)
print (b)
print (c)