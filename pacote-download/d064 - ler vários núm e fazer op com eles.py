''' 064 Crie um programa que leia vários números interios pelo teclado. o progama só vai parar quando digitear o valor 999,
que é a condição de parada. No final, mostre quantos números foram digitados e qual foi a soma entre eles (desconsiderando o flag'''


#n =0
#cont = 0
#soma = 0
n = cont = soma = 0    # forma te atribuir o valor 0 a várias variáveis

while n != 999:
    n = int(input('Digite um número [999 para parar]: '))
    if n != 999:
        cont += 1
        soma += n

print(f'A quantidade digitada foi {cont} e a soma entre ele é {soma}')