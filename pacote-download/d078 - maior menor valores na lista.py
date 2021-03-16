''' 076 Faça um programa que leia 5 balores numéricos e guarde-os em uma lista
No final, mostre ula foi o maior e o menor valore digitado
e as suas respectivas posições na lista'''

lista = list()
lista2 = []  # outra forma de criar um lista
for n in range(0, 5):
    lista.append(int(input(f'Digite o {n + 1} valor da lista: ')))

print(f'Você digitou os valores  {lista}')
print(f'O maior valor digitado foi o {max(lista)} na posição', end=' ')

maximo = max(lista)
minimo = min(lista)
for c, n1 in enumerate(lista):
    if n1 == maximo:
        print(f'{(c + 1)}...', end=' ')    # aqui tive que colocar mais um parenteses
print()
print(f'O maior valor digitado foi o {min(lista)} na posição', end=' ')
for c, n1 in enumerate(lista):
    if n1 == minimo:
        print(f'{(c + 1)}...', end=' ')
print()
# o professor usou o braço para faze o maior menor:
print('-=-' * 30)
mai = men = 0
for c in range(0, 5):
    lista2.append(int(input(f'Digite o {c + 1} valor da lista: ')))
    if c == 0:
        mai = men = lista2[c]
    else:
        if lista2[c] > mai:
            mai = lista2[c]
        if lista2[c] < men:
            men = lista2[c]
print(mai)
print(men)