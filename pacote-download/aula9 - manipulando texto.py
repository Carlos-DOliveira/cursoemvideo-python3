frase = 'Curso em Vídeo Python'
print(frase)
print(frase[3])    # pegou na o 3, lembrar que a conta começa com 0
print(frase[1:4])  # aqui foi de um a 4, a posição zero não entrou e lembrando que o 4 não entra
print(frase[1:15:2])  # do 1 até o 15 pulando de 2 em 2
print(frase[:15:2])   # pegou tudo até 15 puladno de 2 em 2
print(frase[1::3])    # do 1 até o final, puladno de 3 em 3
print(frase[8:])     # do 8 até o final

print(frase.count('o'))       # contei a quantidade de 'o' deu 3
print(frase.count('O'))       #  contei o número de 'O', deu 0 pq ele diferencia maiúscula de minúscula
print(frase.upper().count('O'))     # aqui eu joguei a frase para letra maiúscula e contei o número de 'O', agora deu 3

frasecomespaços = '     Curso em Vídeo Python      '
print(len(frase))   # aqui mostra o tamanho da frase que é 21
print(len(frasecomespaços))   # aqui vai contar todos os espaços, apesar da frase paracer a mesma, então vai 32
print(len(frasecomespaços.strip()))  # com o comando split, tira os espaços da frente e do final
print(frase.replace('Python','Android')) # aqui ele só vai fazer momentaneamente
frase = (frase.replace('Python','Android')) # agora estou substituindo a variável, ai muda a frase

print('Curso' in frase)   # a resposta vai ser TRUE
print(frase.find('Curso'))   # aqui vai passar a posição, que vai ser 0
print(frase.find('Vídeo'))   # aqui vai passar a posição, que vai ser 9
print(frase.find('vídeo'))   # aqui vai passar a posição, que vai ser -1, pq não existe na frase
print(frase.lower().find('vídeo'))   # aqui vai passar a posição, que vai ser 9, voltou a mostrar pq transformei a frase para minúsculo antes

print(frase.split())   # cria uma lista das palavras - ['Curso', 'em', 'Vídeo', 'Android']
dividido = frase.split()
print(dividido)
print(dividido[0])  # mostrar o primeiro elemento da lista
print(dividido[2][3])  # mostrar o a palavra da posição 3 que é vídeo e a letra da posição 4

print('''O artigo objetivou captar as representações sociais do medicamento genérico por usuários de medicamentos no intuito de que seus 
resultados possam ser utilizados no aprimoramento da política desse tipo de medicamento no Brasil. Utilizou-se a Teoria das Representações 
Sociais como suporte teórico-metodológico. A pesquisa foi realizada no período de abril de 2002 a fevereiro de 2003, na cidade do Natal/RN, 
com 116 usuários de medicamentos, abordados em farmácias e/ou drogarias.''') # para imprimir um testo genérico