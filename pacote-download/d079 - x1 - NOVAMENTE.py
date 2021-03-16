lista = []
while True:
    n = int(input('Digite um valor: '))
    if n not in lista:
        lista.append(n)
        print('valor adicionado com sucesso...')
    else:
        print('Valor duplicado! Não vou adicionar...')

    while True:
        resp = str(input('Deseja continuar? [S/N]')).strip().lower()[0]
        if resp in 'sn':
            break
        print('Não entendi.')
    if resp == 'n':
        print('FINALIZANDO')
        break

lista.sort()
print(f'A lista digitada foi {lista}')