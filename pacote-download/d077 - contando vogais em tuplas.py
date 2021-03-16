''' 077 Crie um programa que tenha um tupla com várias palavras (não usar acentos).
Depois disso, você deve mostrar, para cada palavra, quais são as suas vogais'''

palavras = ('aprender', 'programar', 'liguagem', 'python', 'curso', 'gratis', 'estudar',
            'praticar', 'trabalhar', 'mercado', 'programador', 'futuro')

for c in palavras:
    print(f' Na palavra {c.upper()} temos as vogais ', end='')
    quant = len(c)
    for l in range(0, quant):
        if c[l] == 'a':
            print('a', end=' ')
        if c[l] == 'e':
            print('e', end=' ')
        if c[l] == 'i':
            print('i', end=' ')
        if c[l] == 'o':
            print('o', end=' ')
        if c[l] == 'u':
            print('u', end=' ')
    print(' ')

# maneira do professor

print('-==-' * 20)
for p in palavras:
    print(f' Na palavra {p.upper():12} temos as vogais ', end='')
    for letra in p:
        if letra.lower() in 'aeiou':
            print(letra, end=' ')
    print('')