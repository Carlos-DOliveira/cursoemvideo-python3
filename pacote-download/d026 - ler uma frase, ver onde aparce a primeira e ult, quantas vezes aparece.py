''' 026 Faça um programa que leia uma frase pelo teclado e mostre:
- quantas vezes aparece a letra A.
- em que posição ela aparece a primeira vez.
- em que posição ela aparece a última vez.'''

frase = str(input('Digite uma frase: ')).strip().lower()

quantidadeA = frase.count('a')
print(f'Quantidade de letras a: {quantidadeA}')

print(f'A primeira posição encontrada é: {frase.find("a") + 1}')
print(f'A primeira posição encontrada é: {frase.rfind("a") + 1}')
