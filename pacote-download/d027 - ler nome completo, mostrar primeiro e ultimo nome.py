''' 027 Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro e o último nome separadamente.'''

nome = str(input('Digite seu nome completo: ')).strip()

separado = nome.split()
quantidadeN = int(len(separado)) - 1
#print(quantidadeN)
print(f'Olá: {separado[0]}')
print(f'Seu último nome é : {separado[quantidadeN]}')

print(f'Seu último nome é: {separado[len(separado)-1]}')
