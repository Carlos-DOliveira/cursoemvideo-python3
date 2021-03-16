''' 035 Desenvolva um programa que leia o comprimento de três retas e diga ao usuário se elas podem ou não formar um triângulo'''

print('-=-' * 20)
print('Analisador de triângulos')
print('-=-' * 20)


l1 = int(input('Digite o primeiro lado: '))
l2 = int(input('Digite o segundo lado: '))
l3 = int(input('Digite o terceiro lado: '))
t = 0
if l1 < l2 + l3 and l2 < l1 + l3 and l3 < l1 + l2:
    print('Este é um triângulo')
else:
    print('Não formam um triângulo')
