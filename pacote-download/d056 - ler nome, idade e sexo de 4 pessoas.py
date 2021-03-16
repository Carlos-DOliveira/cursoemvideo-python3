''' 056 Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas, No final do programa, mostre:
a média de idade do grupo
qual é o nome do homem mais velho
quantas mulheres te menos de 20 anos'''


idadetotal = 0
idademaisvelho = 0
nomemaisvelho =''
menorvinte = 0
for c in range(1, 5):
    print(f'---- {c}ª pessoa -----')
    n = str(input('Nome:'))
    i = int(input('Idade: '))
    s = str(input('Sexo [M/F]: ')).strip().upper()

    idadetotal += i

    if s == 'M' and idademaisvelho < i:
        idademaisvelho = i
        nomemaisvelho = n

    if s == 'F' and i < 20:
        menorvinte += 1

print(f'A idade média é {idadetotal/4:.1f}')
print(f'O homem mais velho tem {idademaisvelho} e seu nome é: {nomemaisvelho}')
print(f'Ao todo são {menorvinte} mulheres com menos de 20 anos')
