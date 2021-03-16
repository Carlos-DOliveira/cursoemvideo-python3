''' 089 Crie um programa que leia nome e duas notas de vários alunos e guarde tudo em uma lista composta. No final, mostre um boletim
contendo a média de cada um e permita que o usuário possa mostrar as notas de cada aluno individualmente'''

'''aluno = []
lista = []

while True:
    aluno.append(str(input('Nome: ')))
    aluno.append(float(input('Nota 1:')))
    aluno.append(float(input('Nota 2:')))
    lista.append(aluno[:])
    aluno.clear()

    resp = str(input('Quer continuar: [S/N]')).strip().lower()[0]
    if resp in 'n':
        break
print('-=-' * 30)
print('No.    Nome         Média')
print('-' * 30)
for n in range(0, len(lista)):
    print(f'{n}     {lista[n][0]:10}   {(lista[n][1]+lista[n][2])/2:.2f}')

print('-' * 30)

while aluno != 999:
    aluno = int(input('Mostrar notas de qual aluno? [999 interrompe]'))
    if aluno < len(lista):
        print(f'Notas de {lista[aluno][0]} são {lista[aluno][1]} e {lista[aluno][2]}')
    elif aluno == 999:
        print('Saindo. VOLTE SEMPRE!')
    else:
        print('Não temos esse aluno!')'''

# a do professor - achei interressante pq lista dentro de listas

ficha = list()

while True:
    nome = str(input('Nome: '))
    nota1 = float(input(('Nota1: ')))
    nota2 = float(input(('Nota2: ')))
    media = (nota1 + nota2) / 2
    ficha.append([nome, [nota1, nota2], media])   # note que tem 3 listas uma dentro da outra
    resp = str(input('Quer continar? [S/N]'))
    if resp in 'Nn':
        break

print('-=-' * 30)
print(f'{"No":<4}{"Nome":<10}{"Média":>8}')     # maneira que não conhecia
print('-' * 30)

for i, a in enumerate(ficha):
    print(f'{i:<4}{a[0]:<10}{a[2]:>8.1f}')       # criou um alinhemento com o cabeçalho
while True:
    print('-' * 30)
    opc = int(input('Mostrar notas de qual aluno? (999 interrompe): '))
    if opc == 999:
        print('FINALIZANDO...')
        break
    if opc <= len(ficha) - 1:
        print(f'Notas de {ficha[opc][0]} são {ficha[opc][1]}')
