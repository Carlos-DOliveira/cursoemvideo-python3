nome = input('Digite seu nome: ')
print(f'Olá {nome}')
print(f'Olá {nome:20} !')
print(f'Olá {nome:>20} !')
print(f'Olá {nome:<20} !')
print(f'Olá {nome:^20} !')
print(f'Olá {nome:=^20} !')

n1 = int(input('Um valor: '))
n2 = int(input('Digite outro valor: '))
print(f'A soma vale {n1 + n2}')
diminu = n1 - n2
m = n1 * n2
di = n1 // n2
d = n1 / n2
e = n1 ** n2
print(f'a diminuição é {diminu}, \n a multiplicação é {m}, \n a divisão inteira é {di}, a divisão é {d:.3f}', end=' ')
print(f'a exponeciação é {e}')
