'''ERREI NOVAMENTE

lista = []
for c in range(0, 5):
    n = int(input('Digite um valor:'))
    if c == 0 or n >= lista[len(lista)]:
        print('valor adicionado ao final da lista')
        lista.append(n)
    else:
        for c, l in enumerate(lista):
            if n <= lista[c]:
                print(f'valor adicionado na posição {c+1}')

print(lista)
lista.sort()
print(lista)'''