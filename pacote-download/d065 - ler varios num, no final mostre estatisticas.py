''' 065 Crie um programa que leia vários números inteiros pelo teclado. No final da execução, mostre a média entre todos os valroes e
qual foi o maior e o menor valores lidos. O programa dece perguntar ao usuário se ele quer ou não continuar a digitar valores'''

maior = cont = media = soma = 0
menor = 999999999999999
r = 's'
while r not in 'Nn':
    n = int(input('Digite um número: '))
    if cont == 0:
        maior = n
        menor = n        # tive que colocar esse if pq caso o valor fosse 1, ele só atribuia o maior que está na frente
    else:
        if n > maior:
            maior = n
        elif n < menor:
            menor = n
    media += n
    cont += 1
    r = str(input('Quer continuar: [S/N]')).strip().upper()[0]

print(f'\nVocê digitou {cont} números e a média foi {media/cont:.2f}')
print(f'O maior valor foi {maior} e o menor foi {menor}')
