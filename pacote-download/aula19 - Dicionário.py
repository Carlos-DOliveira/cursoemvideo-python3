pessoas = {'nome': 'Carlos', 'sexo': 'M', 'idade': 25}
print(pessoas)
#print(pessoas[0])   - assim ele da erro
print(pessoas['nome'])
print(pessoas['idade'])
print(f'O {pessoas["nome"]} tem {pessoas["idade"]} anos')  # lembrar que são aspas duplas

print()
print(pessoas.keys())
print(pessoas.values())
print(pessoas.items())   # na represenção gráfica, podemos ver que são 3 tuplas dentro de uma lista

print()
for k in pessoas.keys():
    print(k, end=' ')

print()
for v in pessoas.values():
    print(v, end=' ')

print()
for i in pessoas.items():
    print(i, end=' ')

print()
for k, v in pessoas.items():     # no dicionário não tem o enumarate, tem que usar o items
    print(f'{k} = {v}')

print()
del pessoas['sexo']
print(pessoas)

pessoas['nome'] = 'Leandro'
print(pessoas)

pessoas['peso'] = 80       # não preciso utilizar o append
print(pessoas)


print()
brasil = []
estado1 = {'uf': 'Rio de Janeiro', 'sigla': 'RJ'}
estado2 = {'uf': 'São Paulo', 'sigla': 'SP'}
brasil.append(estado1)
brasil.append(estado2)

print(brasil)
print(brasil[0])
print(brasil[1])
print(brasil[0]['uf'])
print(brasil[1]['sigla'])

print()
estado = dict()
brasilao = list()
for c in range(0, 3):
    estado['uf'] = str(input('Unidade Federativa: '))
    estado['sigla'] = str(input('Sigla do Estado: '))
    brasilao.append(estado.copy())   # no dicionário não usa [:], o método é o copy()
print(brasilao)

print()
for e in brasil:
    print(e)  # vai imprimir a lista de dicionários

print()
for e in brasil:
    for k, v in e.items():
        print(f'O campo {k} tem valor {v}')