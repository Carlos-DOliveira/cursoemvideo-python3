palavras = ('aprender', 'programar', 'liguagem', 'python', 'curso', 'gratis', 'estudar',
            'praticar', 'trabalhar', 'mercado', 'programador', 'futuro')

for c, p in enumerate(palavras):
    print(f'Na {c+1:2}ª palavra: {p.upper():.<12} temos',end=' ')
    for l in p:
        if l in 'aeiou':
            print(l, end=' ')
    print()