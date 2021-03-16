''' 080 Crie um programa onde o usuário possa digitar cinco valores numéricos e cadastre-os em uma lista, já a posição correta de inserção
(sem usar o sort()). No final, mostre a lista ordenada '''
lista = []

for c in range(0, 5):
    n = int(input('Digite um valor: '))
    if c == 0 or n > lista[-1]:    # esqueço de como referenciar esse lista[-1]
        lista.append(n)
        print('Adicionado ao final da lista')
    else:
        pos = 0
        while pos < len(lista):
            if n <= lista[pos]:
                lista.insert(pos, n)
                print(f'Adicionado na posião {pos} da lista')
                break
            pos += 1

print(f'Os valroes digitados em ordem foram: {lista}')
    #else:
        #for c in lista:
            #if n >