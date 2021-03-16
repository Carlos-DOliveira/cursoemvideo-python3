''' 102 Crie um programa que tenah uma função fatorial() que receba dois parâmetros: o primeiro que indique o número a calcular e o outro chamado show,
que será um valor lógico(opcional) indicando se será mostrado ou não na tela o processo de cálculo do fatorial'''

def fatorial(a=0, show=False):
    """-> Calcula o Fatorial de um número.
    :param n: O número a ser calculado.
    :param show: (opcional). Mostrar ou não a conta.
    :return: O valor do Fatorial de um número n"""

    fato = 1
    for c in range(a, 0, -1):
        fato *= c
        if show == True:
            if c > 1:
                print(c, end=' x ')
            else:
                print(c, end=' = ')
    return fato

# Programa principal
print(fatorial(5))
print(fatorial(5, show=True))
print(fatorial(6, show=False))
help(fatorial)


