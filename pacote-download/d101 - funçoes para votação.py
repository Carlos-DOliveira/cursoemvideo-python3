''' 101 Crei u mprograma que tenaha uma função chamada voto() que vai receber como parâmetro o ano de nascimento de uam pessoa, retornando um valore literal
indicando se uma pessoa tem voto NEGADO, OPCIONAL ou OBRIGATÓRIO nas eleições'''


def anovoto():
    from datetime import date
    anonascimento = int(input('Em que ano você nasceu? '))
    idade = date.today().year - anonascimento
    if idade >= 65 or 16 <= idade < 18:
        return (f'Com {idade} anos: VOTO OPCIONAL')
    if idade >= 18:
        return (f'com {idade} anos: VOTO OBRIGATÓRIO')
    else:
        return (f'com {idade} anos: VOTO NÃO É OBRIGATÓRIO')


resp = anovoto()
print(resp)
