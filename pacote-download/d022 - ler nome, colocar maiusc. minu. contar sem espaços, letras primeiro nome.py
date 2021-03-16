''' 022 Crie um programa qeu leia o nome completo de uma pessoa e mostre:
- O nome com todas as letras maiúsculas e minúsculas
- Quantas letras ao todo, sem considerar os espaços
- Quantas letras tem o primeiro nome '''


nome = input('Digite seu nome completo: ').strip()

print('Nome em maíuscula: ',nome.upper())
print('Nome em minúscula: ',nome.lower())
print('Tamanho total com espaços: ',len(nome))
dividido = nome.split()
print('Quantidade de grupo de caracteres: ',len(dividido[:]))
print('Quantidade de caracteres do primeiro nome: ',len(dividido[0]))

# nesse for calculei o total de grupos de letras na lista dividido e coloquei no total, meu range foi de 0 até esse total
# dps verifiquei o número de cada grupo e fui somando

total = int(len(dividido))
n = 0
valor = 0
for n in range(0,total):
    valor = valor + int(len(dividido[n]))
    n = n + 1
print('Quantidade de caracteres do nome: ',valor)

# outra maneira a do prof

print(f'Seu nome tem ao todo {len(nome) - nome.count(" ")} letras')    # aqui diminiu o número de espaços
print(f'Seu primeiro nome tem {nome.find(" ")} letras')       # aqui acho o primeiro nome, achando o primerio espaço
print(f'Seu primeiro nome é {dividido[0]} e ele tem {len(dividido[0])} letras')  # essa forma que usei
