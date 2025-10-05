"""
import math
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
"""
num = int(input("Digite um número inteiro: "))
fatorial = 1

for i in range(1, num + 1):
    fatorial = fatorial * i

print(f"O fatorial de {num} é {fatorial}")