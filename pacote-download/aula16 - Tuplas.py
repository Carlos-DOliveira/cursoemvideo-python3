lanche = ('Hambúrguer', 'Suco', 'Pizza', 'Pudim', 'Batata Frita')
lanche1 = 'Hambúrguer', 'Suco', 'Pizza', 'Pudim', 'Batata Frita'    # no PYTHON novo não precisa de parenteses

print(lanche)
print(lanche1)
print(lanche[1])
print(lanche[3])
print(lanche[-2])
print(lanche[1:3])    # aqui estou fazendo um fatiamento. Lembrando que no fatiamento não pega o último elemento
print(lanche[2:])
print(lanche[:2])
print(lanche[-2:])
print(lanche[-3:])

#lanche[1] = 'Refrigerante'    # VAI DAR ERRO - TUPLAS SÃO IMUTÁVEIS
print('')

# Três formas de usar o FOR

for comida in lanche:
    print(f'Eu vou comer {comida}')    #    aqui ele não mostra a posição
print('Comi pra caramba!')
print('')

for cont in range(0, len(lanche)):
    print(f'Vou comer {lanche[cont]}, na posição', end=' ')
    print(cont)
print('')

for pos, comida in enumerate(lanche):
    print(f'Eu vou comer {comida} na posição {pos}')

# comandos
print('')

print(sorted(lanche))   # printa em ordem alfabética, da para notar que ele colocou em [], ele transformou em lista
print(lanche)     # aqui da para ver que ele não mudou a tupla, só organizou de forma temporária

# casos
print('')

a = (2, 5, 4)
b = (5, 8, 1, 2)
c = a + b
d = b + a

print(c)
print(d)
print(len(c))
print(d.count((5)))   # contando quantas vezes aparece o 5
print(d.count((4)))
print(d.count((9)))

print('')

print(d.index(8))     # mostra que posição está o 8
print(d.index(4))
print(d.index(2))    # pega a primeira ocorrência
print(d.index(2, 4))  # pega o dois a partir da 4ª ocorrência
print(d.index(5))
print(d.index(5, 1))

print('')

pessoa = ('Carlos', 35, 'M', 81.56)   # tuplas podem receber vários tipos primitivos
print(pessoa)

del(pessoa)  # apaga a tupla