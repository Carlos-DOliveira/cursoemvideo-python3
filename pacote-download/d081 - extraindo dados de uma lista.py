''' 081 Crie um programa que vai ler vários números e colocar em um lista. Depois, mostre:
quantos números foram digitados
a lista de valores, ordenada de forma decrescente
se o valor 5 foi digitado e está ou na lista'''

lista = []
cont = 0
while True:
    n = int(input('Digite um valor: '))
    if len(lista) == 0:
        lista.append(n)
    else:
        pos = 0
        lista.append(n)
    cont += 1


    while True:
        resp = str(input('Quer continuar? [S/N]')).strip().lower()[0]
        if resp in 'sn':
            break
        print('Não entendi. Digite novamente! ')
    if resp == 'n':
        break

print(f'Você digitou {cont} elementos')
lista.sort(reverse=True)
print(f'Os valores digitados em ordem decrescentes são {lista}')
if 5 in lista:
    print(f'O valor 5 faz parte dessa lista')
else:
    print('O valor 5 não faz parte dessa lista')