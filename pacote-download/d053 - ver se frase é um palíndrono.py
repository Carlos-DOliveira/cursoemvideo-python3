''' 053 Crie um programa qeu leia um frase e diga se ela é um palíndromo, desconsideranod os espaços
Exp:

a sacada da casa
a torre da derrota
o lobo ama o bolo
anotaram a data da maratona'''

frase = str(input('Digite a frase para se verificar se é um palíndromo: ')).lower().strip()
conj = frase.split()
frase = ''.join(conj)

tamanho = len(frase) -1
num = 0

for c in range(0, tamanho):
    # if len(frase) % 2 == 0:  - tinha colocado esse detalhe para calcular as frase impares e pares, mas no final não faz dif
    if frase[c] == frase[tamanho - c]:
        num += 1

if tamanho == num:
    print('Está frase é um palíndromo')
else:
    print('Está frase não é um palíndromo')

## a do professor

fras = str(input('Digite uma frase: ')).strip().upper()
palavras = fras.split()
junto = ''.join(palavras)
inverso = ''
for letra in range(len(junto) - 1, -1, -1):   # usando o for
    inverso += junto[letra]
print(junto, inverso)

# mais uma maneira

fra = str(input('Digite uma frase: ')).strip().upper()
palavra = fras.split()
junt = ''.join(palavras)
invers = junt[::-1]       # da para jogar direto, sem o for
print(junto, inverso)


