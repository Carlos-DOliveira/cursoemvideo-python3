''' 095 Aprimore o DESAFIO 093 para que ele funcione com vários jogadores, incluindo um sistema de visualização de detalhes do aproveitametneo de cada jogador'''

jogador = dict()
partidas = list()
players = []

while True:
    jogador['nome'] = str(input('Nome do jogador: '))

    tot = int(input(f'Quantas partidas {jogador["nome"]} jogou? '))
    partidas.clear()
    for c in range(0, tot):
        partidas.append(int(input(f'    Quantos gols na partida {c}? ')))

    jogador['gols'] = partidas[:]   # NÃO ESQUECER O [:]

    jogador['total'] = sum(partidas)      # novo método

    players.append(jogador.copy())
    jogador.clear()

    while True:
        resp = str(input('Quer continuar: [S/N]')).strip().lower()[0]
        if resp in 'sn':
            break
        print('Não entendi.')
    if resp == 'n':
        break

print('-=-' * 30)

print(f'{"cod":4}{"nome":15}{"gols":21}{"total":5}')
print('-' * 50)
for c in range(0, len(players)):
    print(f'{c:>3} {players[c]["nome"]:15}{str(players[c]["gols"]):21}{players[c]["total"]:>5}')    # nesse consegui formatar dps que colocquei str, tranformando em string

while True:
    e = int(input('Mostrar dados de qual jogador: [999 - para parar]'))
    print()
    if e == 999:
        print('FINALIZANDO. VOLTE SEMPRE')
        break
    if e < len(players):
        print(f'-- LEVANTAMENTO DO JOGADOR: {players[e]["nome"]}')
        for c, v in enumerate(players[e]['gols']):
            print(f'No jogo {c} fez {v} gols')
    else:
        print('Não tem esse jogador. TENTE NOVAMENTE!')
    print()





