print('\33[31m Olá mundo!')
print('\33[31;43m Olá mundo!')       # coloquei o fundo amarelo com o 43
print('\33[1;31;43m Olá mundo!')     # em negrito
print('\33[1;31;43m Olá mundo!\033[m')  # aqui corto no final a cor para não ir na linha inteira
print('\33[4;30;45m Olá mundo!\033[m')  # aqui coloquei o underline e mudei as cores
print('\33[37m Olá mundo!\033[m')      # esse aqui é o pradrão
print('\33[7;30m Olá mundo!\33[m')     # aqui estou invertendo
print('\33[30m Olá mundo!\33[m')

a = 3
b = 4
nome = 'Carlos'
print(f'Os valores são {a} e {b} !!!')
print(f'Os valores são \033[32m {a} \033[m e \033[31m{b} \033[m !!!')
print('Os valores são {}{}{} !!!'.format('\033[4;34m', nome, '\033[m'))

# uma forma mais avançada

nome = 'Carlos'
cores = {'limpa':'\033[m',
         'azul':'\033[34m',
         'amarelo':'\033[m33',
         'pretoebranco':'\033[7;30m'}

print(f'Olá! Muito prazer em te conhecer, {cores["azul"]}{nome}{cores["limpa"]}')