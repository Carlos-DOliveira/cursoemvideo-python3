''' 048 Faça um programa que calcule a soma entre todos os números ímpares que são múltiplos de três e que se enocntram no intervalo
de 1 até 500'''
n1 = 0
q = 0
for c in range(1, 500, 2):
    n = c
    u = n // 1 % 10
    d = n // 10 % 10
    ce = n // 100 % 10
    if (u + d + ce) % 3 == 0:
        n1 += c
        q += 1
print(f'A soma dos números ímpares é : {n1} e a quantidade somada são {q}')
print('')
# forma do prof

soma = 0
cont = 0
for c in range(1, 501, 2):
    if c % 3 == 0:
        cont = cont + 1   # pode ser cont += 1
        soma = soma + c   # pode ser soma += c
print(f'A soma de todos os {cont} valores solicitados é {soma}')
