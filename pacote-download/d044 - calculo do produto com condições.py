''' 044 Elabore um programa que calcule o valor a ser pago por um produto , considerando o seu proço normal e condição de pagamento
à vista dinheiro/cheque: 10 % de desconto
à vista no cartão: 5% de desconto
em até 2x no cartâo: precço normal
em 3x ou mais : 20 % de juros'''

valor = float(input('Digite o valor do produto: R$ '))

opcao = int(input('''Digite a opção de pagamento: 
[0] - à vista, 
[1] - à vista no cartão, 
[2] - 2x no cartão, 
[3] - 3x ou mais vezes: '''))

if opcao == 0:
    print(f'O valor à vista será: R$ {valor - (valor * 10/100):.2f}')
elif opcao == 1:
    print(f'O valor à vista no cartão será: R$ {valor - (valor * 5 / 100):.2f}')
elif opcao == 2:
    print(f'O valor à vista será: R$ {valor:.2f}')
else:
    print(f'O valor final: R$ {valor + (valor * 20 / 100):.2f}')
