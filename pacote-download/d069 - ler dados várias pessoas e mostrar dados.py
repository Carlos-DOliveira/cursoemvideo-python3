''' 069 Crie um programa que leia a idade e o sexo de várias pessoas. A cada pessoa cadastrada, o porgrama deverá perguntar se o usuário
quer ou não continuar. No final, mostre:
quantas pessoas tem mais de 18 anos
quantos homens foram cadastrados
quantas mulheres te menos de 20 anos'''
t = 'CADASTRE UM PESSOA'
jovens = totalhomem = totalidade = i = 0
resp = s = 'p'

while True:
    print('-=-' * 20)
    print(F'{t:^60}')
    print('-=-' * 20)
    i = int(input('Idade: '))
    while True:
        s = str(input('Sexo: [M/F] ')).strip().upper()[0]
        if s in 'MF':
            break
    if i >= 18:
        totalidade += 1
    if s == 'M':
        totalhomem += 1
    if s == 'F' and i < 20:
        jovens += 1
    resp = 'p'
    while resp not in 'SN':
        resp = str(input('Quer continuar: [S/N] ')).strip().upper()[0]

    if resp == 'N':
        break


print(f'''quantas pessoas tem mais de 18 anos - {totalidade}
quantos homens foram cadastrados - {totalhomem}
quantas mulheres te menos de 20 anos - {jovens}''')
