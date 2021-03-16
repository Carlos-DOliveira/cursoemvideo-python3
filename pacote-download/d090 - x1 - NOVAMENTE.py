aluno = {}

aluno['Nome'] = str(input('Nome: '))
aluno['Média'] = float(input(f'Média de {aluno["nome"]} : '))
if aluno['media'] > 7:
    aluno['Situação'] = 'Aprovado'
else:
    aluno['Situação'] = 'Reprovado'

print(aluno)
print()
for k, v in aluno.items():
    print(f' {k} é igual a {v}')