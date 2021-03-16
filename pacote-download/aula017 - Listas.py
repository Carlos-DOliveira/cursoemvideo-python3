num = (2, 5, 9, 1)
#num[2] = 3   # aqui da erro pq tupla é imutável
print(num)

num = [2, 5, 9, 1]
num[2] = 3   # aqui muda pq é uma lista
print(num)

print('')
#num[4] = 7   # aqui da erro novamente, pq não é assim que adiciona valores
num.append(7)  # assim add valores no final da lista
print(num)
num.insert(2, 0)  # aqui adiciono o elemento 0 na posição 2
print(num)
num.pop()   # tira o último elemento da lista
print(num)
num.pop(2)  # retira o elemento da posição 2, neste caso é o zero
print(num)

print('')
num.sort()
print(num)
num.sort(reverse=True)
print(num)

print(f'Essa lista tem {len(num)} elementos')

print('')
num.insert(2, 2)   # inserimos mais um dois na lista, agora tem 2 dois
num.insert(0, 2)    # agora na posição zero inserimos um 2
print(num)
num.remove(2)    # ele vai retirar somente o primeiro elemento da lista
print(num)

#num.remove(4)  # assim da erro, pq o elemento não está na lista
if 4 in num:
    num.remove(4)   # ressolvo assim, colocando um if
else:
    print('não achei o número 4')

if 5 in num:
    num.remove(5)   # ressolvo assim, colocando um if
    print('consegui remover o valor 5')
else:
    print('não achei o número 5')

print(num)

print('')
valores = []
valores.append(5)
valores.append(9)
valores.append(4)
print(valores)

for v in valores:
    print(f'{v}...', end=' ')
print('')
for c, v in enumerate(valores):   # com enumerate pega tanto a chave, quanto o valor
    print(f'{v}... na posição {c}')


print('')
numeros = list()      # crio um variável lista
for cont in range(0, 1):
    numeros.append(int(input('Digite um valor: ')))   # para receber valores na lista
print(numeros)

print('')
a = [3, 4, 1, 3, 5]
b = a
print(f'Lista A: {a}')    # uma lista fica igual a outra, OBS elas estão linkadas, mesmo que mude depois somente uma, vai mudar as duas
print(f'Lista B: {b}')


print('')
a = [3, 4, 1, 3, 5]
b = a
b[2] = 8
print(f'Lista A: {a}')    # aqui da para notar que A e B estão linkadas
print(f'Lista B: {b}')

print('')
a = [3, 4, 1, 3, 5]
b = a[:]      # aqui eu criei um cópia de A em B, não linkei elas
b[2] = 8
print(f'Lista A: {a}')    # note que agora somente uma mudou
print(f'Lista B: {b}')
