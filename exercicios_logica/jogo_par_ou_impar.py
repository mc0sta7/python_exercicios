import random

# par ou ímpar
# impor random
condicao = bool()

while condicao != False:

    par_ou_impar = str(input('Par ou ímpar? ')).strip().lower().replace('í', 'i')
    numero_do_jogador = int(input('Digite um número para o jogo: '))

    numeros_do_computador = [x for x in range(0,11)]
    numero_do_computadorcomputador = random.choice(numeros_do_computador)

    soma = numero_do_jogador + numero_do_computadorcomputador

    if par_ou_impar == 'par':
        if soma % 2 == 0:
            print(f'Você venceu! {soma} é par!')
            condicao = True
        else:
            print(f'Você perdeu! {soma} é ímpar! Tente de novo!')
            condicao = False

    if par_ou_impar == 'impar':
        if soma % 2 != 0:
            print(f'Você venceu! {soma} é ímpar!')
            condicao = True
        else:
            print(f'Você perdeu! {soma} é par! Tente de novo!')
            condicao = False