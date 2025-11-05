# Solução com for loop
fatorial_com_for = 1
numero_fatorial_com_for = int(input('Fatorial: '))

for i in range(numero_fatorial_com_for, 0, -1):
    fatorial_com_for *= i

print(fatorial_com_for)

# Solução com While loop
numeros_para_fatorial = []
numero_para_fatorial = int(input('Fatorial: '))
c = numero_para_fatorial
fatorial = 1

print(f'Calculando {c}! = ', end=' ')
while c > 0:
    print(f'{c}', end=' ')
    print(' x ' if c > 1 else ' = ', end=' ')
    fatorial *= c
    c -= 1 
print(f'{fatorial}', end=' ')

# Solução diferente
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