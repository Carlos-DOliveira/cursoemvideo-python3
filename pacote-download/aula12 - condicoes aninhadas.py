nome = str(input('Qual é o seu nome? ')).strip().lower()

if nome == 'carlos':
    print('Que nome bonito')
elif nome == 'predro' or nome == 'maria' or nome == 'paulo':
    print('Seu nome é bem comum no Brasil.')
elif nome in 'ana cláudia jéssica julinana':
    print('Belo nome feminino')
else:
    print('Seu nome é normal')

print(f'Tenha um bom dia, {nome.title()}')