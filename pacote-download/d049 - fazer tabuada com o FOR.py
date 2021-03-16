''' 049 Refaça o DESAFIO 009, mostrando a tabuada de um número que o usuário escolher, só que agora utilizando o laço for'''

n = int(input('Digite um número: '))
for c in range(0, 11):
    print(f' {n:2} X {c:2} = {c * n:2}')
