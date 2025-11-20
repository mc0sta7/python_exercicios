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
            if jogador_aleatorio == condicao_de_parada:
                   break
            jogadores.append(jogador_aleatorio)

    print('  ---Times---  ' \
    '   Para encerrar o Digite: PARE   ')

    while time_aleatorio != condicao_de_parada:

            time_aleatorio = str(input('Nome do time: ')).lower()
            if time_aleatorio == condicao_de_parada:
                   break
            times.append(time_aleatorio)

    random.shuffle(jogadores)
    random.shuffle(times)

    final = dict(zip(jogadores, times))
    print('  ---Resposta---  ')
    print(dict(final))

    repeticao = str(input('Deseja repetir? S/N: ')).upper()

"""times_adicionados = []

for i in range(2):

   adcionar_times = str(input('Time a mais: '))
   times_adicionados.append(adcionar_times)

jogadores_a_mais = []

for i in range(2):
        jogadores_com_2_times = random.choice(jogadores)
        jogadores_a_mais.append(jogadores_com_2_times)

final = dict(zip(jogadores_a_mais, times_adicionados))

print(final)"""