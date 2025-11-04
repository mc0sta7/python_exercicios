import random

'''FIFA'''

condicao_de_parada = 'pare'
repeticao = str()

while repeticao != 'N':

    jogadores = []
    times = []
    jogador_aleatorio = str()
    time_aleatorio = str()

    print('  ---Jogadores---  ' \
    '   Condição de parada: Digite: PARE   ')

    while jogador_aleatorio != condicao_de_parada:

            jogador_aleatorio = str(input('Nome do jogador: ')).lower()
            jogadores.append(jogador_aleatorio)

    print('  ---Times---  ' \
    '   Para encerrar o Digite: PARE   ')

    while time_aleatorio != condicao_de_parada:

            time_aleatorio = str(input('Nome do time: ')).lower()
            times.append(time_aleatorio)

    if 'pare' in times:
            times.remove('pare')
    if 'pare' in jogadores:
            jogadores.remove('pare')

    random.shuffle(jogadores)
    random.shuffle(times)

    final = dict(zip(jogadores, times))
    print('  ---Resposta---  ')
    print(dict(final))

    repeticao = str(input('Deseja repetir? S/N: ')).upper()