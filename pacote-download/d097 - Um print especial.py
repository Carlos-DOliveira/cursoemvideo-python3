''' 097 Faça um programa que tenha uma função chamada escreva(), que receba um texto qualquer como parâmetro e mostre uma mensagem com tamanho adaptável
ex.
    escreva('Olá Mundo!')

saída:
    ~~~~~~~~~~~~
     Olá Mundo!
    ~~~~~~~~~~~~
'''


def escreva(msg):
    multi = len(msg) + 4
    print('~' * multi)
    print(f'  {msg}')   # aqui ele deu 2 espaços para centralizar
    print('~' * multi)

escreva('Carlos Henrique')
escreva('Curso de Python no YT')
escreva('Cev')