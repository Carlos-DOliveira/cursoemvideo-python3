''' 083 Crie um programa onde o usuário digite uma expressão qualquer que use parênteses. Seu aplicativo deverá analisar se a expressão
passada está com os parênteses abertos e fechados na ordem correta'''

'''conte = contd = 0
lista = []
expressão = str(input('Digite um expressão: '))

for c in expressão:
    if c == '(':
        lista.append(c)
    if c == ')':
        lista.append(c)

while True:
    if lista[0] == ')':
        print('Sua expressão está errada')
        break
    else:
        for c in lista:
            if conte >= contd:
                if c == '(':
                    conte += 1
                elif c == ')':
                    contd += 1
        if contd == conte:
            print('A expressão está coreta!')
            break
        else:
            print('Sua expressão está errada')
            break
print(f'{conte} = ( e {contd} = )')
print(lista)'''


# a do professor

expr = str(input('Digite a expressão: '))
pilha = []
for simb in expr:
    if simb == '(':
        pilha.append('(')
    elif simb == ')':
        if len(pilha) > 0:
            pilha.pop()      # aqui ele tira O ÚLTIMO ELEMENTO, SEM ADICIONAR NADA, ELE TIROU O '('
        else:
            pilha.append(')')
            break
if len(pilha) == 0:
    print('Sua expressão está válida!')
else:
    print('Sua expressão está errada')


# ((a+b)*(a*c)-2)