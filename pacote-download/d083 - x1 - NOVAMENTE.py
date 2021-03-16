
'''expressao = str(input('Digite a expressão: '))
lista = []

for c in expressao:
    if c == ')' and len(lista) == 0:
        lista.append(c)
        break

    if c == '(':
        lista.append(c)
    elif c == ')':
        lista.append(c)
        lista.pop()

print(len(lista))

if len(lista) > 0:
    print('A expressão está errada.')
else:
    print('Expressão correta')'''

# programming languages list
languages = ['Python', 'Java', 'C++', 'French', 'C']

# remove and return the 4th item
return_value = languages.pop(3)

print('Return Value:', return_value)

# Updated List
print('Updated List:', languages)

dois = languages.pop()
print(dois)
print(languages)