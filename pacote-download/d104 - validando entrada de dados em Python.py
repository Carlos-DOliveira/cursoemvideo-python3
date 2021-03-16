''' 104 Crie um programa que tenha a função leiaInt(), que vai funcionar de froma semelhante à função input() do Python, só que fazendo a validação para aceitar
apenas um valor numérico.
ex:     n=leiaInt('Digite um n')'''

def leiaInt(msg):
    num = input(msg)
    if num.isnumeric():
        return num
    else:
        while True:
            print('\033[31m ERRO! Digite um número inteiro válido. \033[m')
            num = input(msg)
            if num.isnumeric():
                return num
                break


n = leiaInt('Digite um número inteiro: ')
print(f'Você acabou de digitar o número: {n}')