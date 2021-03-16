''' 057 Faça um programa que leia o sexo de uma pessoa, mas só aceite os valores 'M' ou F. Caso esteja errado, peça a digitação novamente
até ter um valor correto'''

resp = str(input('Informa seu sexo: [M/F]: ')).strip().upper()[0]
while resp not in ('mfMF'):
    resp = str(input('Dados inválidos. Por favor, informe qual o seu sexo? [M/F]')).strip().lower()[0]
print(f'Sexo {resp} resgistrado com sucesso')