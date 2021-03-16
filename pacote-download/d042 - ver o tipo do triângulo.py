''' 042 Refaça o desafio 035 dos triângulo, acrescentadno o recurso de mostrar que tipo de triângulo será formado:
Equilátero - todos os lados iguais
Isósceles - dois lados iguais
Escaleno - todos os lados diferentes'''

l1 = float(input('Digite o primeiro lado: '))
l2 = float(input('Digite o segundo lado: '))
l3 = float(input('Digite o terceiro lado: '))

if l1 < l2 + l3 and l2 < l1 + l3 and l3 < l1 + l2:
    if l1 == l2 and l2 == l3:
        print('É um triângulo equilátero')
    elif l1 == l2 or l2 == l3 or l1 == l3:
        print('É um triângulo isósceles')
    else:
        print('É um triângulo escaleno')
else:
    print('Não é um triângulo!!!')
