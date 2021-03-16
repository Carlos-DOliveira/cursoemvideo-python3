''' 062 Melhore o DESAFIO 061, perguntando para o usuário se ele quer mostrar mais alguns termos. O programa ancerra quando
ele disser que qeur mostrar ) termos'''


n = int(input('Ditige o primeiro termo: '))
r = int(input('Digite a razão: '))
quantidade = int(input('Digite quantas vezes que contar: '))
pa = n
print(n, end=' -> ')
c = 1
contador = quantidade
cont = False
while not cont:
    while c <= quantidade:
        if c != quantidade:
            pa += r
            print(pa, end=' -> ')
            c += 1
        else:
            print('PAUSA')
            quantidade = int(input('Quantos mais que proceguir? '))
            contador += quantidade
            c = 0
        if quantidade == 0:
            cont = True
            break
print(f'Progressão finalizada com {contador} termos mostrados.')

# a do professor

primeiro = int(input('Primeiro termo: '))
razao = int(input('Razão da PA: '))
termo = primeiro
con = 1
total = 0
mais = 10
while mais != 0:
    total = total + mais
    while con <= total:
        print(f'{termo} -> ', end='')
        termo += razao
        con += 1
    print(('PAUSA'))
    mais = int(input('Quantos termos você qeur mostrar a mais? '))

print(f'Progressão finalizada com {total} termos mostrados.')