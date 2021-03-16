''' 105 Faça um prgrama que tenha uma função notas() que pode receber várias notas de alunos e vai retornar um dicionário com as seguintes informações:
Quantidade de notas
a maior nota
a menor nota
a média da turma
a situação(opcional)
Adicione também as docstrings da função'''

def notas(*n, sit=False):
    nota = []
    info = {}
    nota.append(n)
    info = {'total': len(nota)}
    info = {'maior': max(nota)}
    info = {'menor': min(nota)}
    #tot = sum(nota)
    #tam = len(nota)

    #info = {'média': tot}
    if sit == True:
        if info['média'] > 7:
            info = {'situação': 'BOA'}
        elif info['média'] > 5:
            info = {'situação': 'MÉDIA'}
        else:
            info = {'situação': 'RUIM'}
    resp = info
    return resp



resp = notas(3.5, 3, 6.5, 2, 7, 4)
print(resp)