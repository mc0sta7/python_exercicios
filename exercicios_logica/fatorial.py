numero = int(input('Nº: '))

numeros = []
fatorial = 0

for contagem in range(numero,0,-1):
    numeros.append(contagem)

for contador in numeros:
    if fatorial <= contador:
        fatorial = contador
    elif fatorial >= contador:
        fatorial = fatorial * contador

print(fatorial)