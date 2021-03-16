
teste = list()
teste.append('Carlos')
teste.append(35)
galera = list()
galera.append(teste)    # estou jogando a lista teste dentro de outra lista galera,OBS linkando elas
print(galera)            # JÁ QUE ESTÁ LINKADO, SE EU MUDAR UMA, MUDA A OUTRA

teste[0] = 'Maria'
teste[1] = 22
print(galera)      # Mesmo modigifando o teste a galera modifica também, já que teste está dentro de galera, ele modificou pq está linkado
galera.append(teste)   # aqui adiciono teste novamente
print(galera)

print()
teste1 = list()
teste1.append('Carlos')
teste1.append(35)
galera1 = list()
galera1.append(teste1[:])    # agora estou fazendo uma cópia, AGORA NÃO MUDA A OUTRA SE TIVER MUDANÇA
print(galera1)

teste1[0] = 'Maria'
teste1[1] = 22
print(galera1)      # Mesmo modigifando o teste a galera modifica também, já que teste está dentro de galera, ele modificou pq está linkado
galera1.append(teste1[:])   # aqui adiciono teste1 novamente, agora estão diferentes
print(galera1)

print()
galera2 = [['João', 19], ['Ana', 33], ['Carlos', 43], ['Maria', 50]]   # 4 estruturas compostas dentro de outra estrutura
print(galera2[0])
print(galera2[0][0])
print(galera2[2][1])

print()
for p in galera2:
    print(p[0])
for p in galera2:
    print(f'A idade {p[1]} anos é de {p[0]}')

print()
galera4 = list()
dado = []
for c in range(0, 3):
    dado.append(str(input('Nome: ')))
    dado.append(int(input('Idade: ')))
    galera4.append(dado[:])      # NÃO PODE ESQUECER O [:], PQ SE NÃO ELE VAI CRIAR LISTAS VAZIAS
    dado.clear()             # Limpa lista de dados

print(galera4)
totmai = totmenor = 0
for p in galera4:
    if p[1] >= 21:
        print(f'{p[0]} é maior de idade')
        totmai += 1
    else:
        print(f'{p[0]} é menor de idade')
        totmenor += 1
print(f'temos {totmai} maiores e {totmenor} menores')