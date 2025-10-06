def fatorial(numero):

    numeros = []
    numero_fatorial = 0

    for contagem in range(numero,0,-1):
        numeros.append(contagem)

    for contador in numeros:
        if numero_fatorial <= contador:
            numero_fatorial = contador
        elif numero_fatorial >= contador:
            numero_fatorial = numero_fatorial * contador
    return numero_fatorial

while True:
    try:
        numero_qualquer = int(input('Nº: '))
        print(fatorial(numero_qualquer))
    except ValueError:
        print('Digite apenas números!')