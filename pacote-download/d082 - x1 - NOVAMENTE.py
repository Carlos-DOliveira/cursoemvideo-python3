''' 082 Crie um programa que vai ler vários números e colocar em uma lista.
Depois disso, crie duas listas extras que vão conter apenas os valores pares e os valores ímpares digitados, respectivamente.
Ao final, mostre o conteúdo das três listas geradas
No primeiro loop monte a primeria lista, dps monte as outras'''

lista = []
lpares = []
limpares = []

while True:
   lista.append(int(input('Digite um número: ')))

   while True:
       resp = str(input('Quer continuar? [S/N]')).strip().lower()[0]
       if resp in 'sn':
           break
       print('Não entendi. Tente novamente')
   if resp == 'n':
       print('Finalizando')
       break
print(lista)

lista.sort()
for n in lista:
    if n % 2 == 0:
        lpares.append(n)
    else:
        limpares.append(n)


print(lpares)
print(limpares)
