import random

'''FIFA'''

# Formação de pares com jogadores e times

# Parte 1
condicao_de_parada = 'pare'
repeticao = str()

while True:

    jogadores = []
    times = []
    jogador_aleatorio = str()
    time_aleatorio = str()

    print('  ---Jogadores---  ' \
    '   Condição de parada: Digite: PARE   ')

    while jogador_aleatorio != condicao_de_parada:

            jogador_aleatorio = str(input(f'Nome do {len(jogadores) + 1}º jogador: ')).strip().lower()
            if jogador_aleatorio == condicao_de_parada:
                   break
            jogadores.append(jogador_aleatorio)
    print(f'---Teremos {len(jogadores)} jogadores---')

    print(f'Recomendamos a escolha de {len(jogadores)} times')    
    print('  ---Times---  ' \
    '   Para encerrar o Digite: PARE   ')

    while time_aleatorio != condicao_de_parada:

            time_aleatorio = str(input(f'Nome do {len(times) + 1}º time: ')).strip().lower()
            if time_aleatorio == condicao_de_parada:
                   break
            times.append(time_aleatorio)
    print(f'Teremos {len(jogadores)} jogadores')

    if not jogadores or not times:
        print('É necessário pelo menos 1 jogador e 1 time')

    random.shuffle(jogadores)
    random.shuffle(times)

    final = dict(zip(jogadores, times))
    print('  ---Resposta---  ')
    print(dict(final))

    if len(jogadores) != len(times):
          print('A quantidade de times e de jogadores não é a mesma.')

    print('CASO ESPECIAL. Sobrou time ou jogador?')
    excecao = str(input('Deseja sortear times extras? Digite [S/N]: ')).strip().lower()
    
    if excecao == 'S':

        # Parte 2 é uma exceção 
                print('  ---Times Extras---  ' \
                '   Condição de parada: Digite: PARE   ')

                times_acrescentados = []
                times_diferentes = str()

                while times_diferentes != condicao_de_parada:
               
                        times_diferentes = str(input('Times acrescentados: ')).strip().lower()
                        if times_diferentes == condicao_de_parada:
                         break
                        times_acrescentados.append(times_diferentes)

                random.shuffle(times_acrescentados)
                random.shuffle(jogadores)

                final = dict(zip(times_acrescentados, jogadores))
                print(final)
                print('Tenha um bom jogo! :)')

    sorteio_do_zero = str(input('Você deseja realizar um novo sorteio? Tudo do ZERO? ')).strip().lower()

    if sorteio_do_zero == 'N':
           print('Programa encerrado! Tenha um bom jogo :)')
           break