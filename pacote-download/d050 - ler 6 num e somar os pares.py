''' 050 Desenvolva um programa que elia seis números interios e msotre a soma apenas daqueles que forem pares. Se o valor
 digitado for ímpar, desconsidere-o'''

soma = 0
for c in range(1, 7):
    n = int(input(f'Digite {c} valor: '))
    if n % 2 == 0:
        soma += n
        print(f'Somei o {n}')
print(f'Total da soma {soma}')