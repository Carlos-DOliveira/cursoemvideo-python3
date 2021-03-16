''' 061 Refaça o DESAFIO 051, lendo o primeiro termo e a razão de uma PA, mostrando os 10 primeiros termos da progressão usando
a estrutura while'''

n1 = int(input('Ditige o primeiro termo: '))
r = int(input('Digite a razão:'))
c = 1
pa = n1
print(n1, end=', ')
while c < 10:
    pa += r
    print(pa, end=', ')
    c += 1

