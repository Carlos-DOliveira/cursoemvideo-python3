lista = []
cont = 0
while True:

    n = int(input('Digite um valor: '))

    if n not in lista:
        lista.append(n)
        cont += 1
    else:
        print('Valor duplicado! Tente novamente')
    while True:
        resp = str(input('Quer continuar? [S/N]')).strip().lower()[0]
        if resp in 'sn':
            break
        print('Não entendi. Tente novamente')
    if resp == 'n':
        print('Finalizando')
        break

print('-=-' * 30)
print(f'Você digitou {len(lista)} valores')
lista.sort(reverse=True)
print(f'Os valores em ordem decrescente são {lista}')
if 5 in lista:
    print(f'O valor cinco foi encontrado')
else:
    print(f'O valor cinco não foi encontrado')