numeros = '5 1 8 2 3 9 4 10 11 12'
numeros_juntos = numeros.replace(' ','')

numeros_1 = []

for num in numeros_juntos:
    num = int(num)
    numeros_1.append(num)

numeros_copia = numeros_1[:]

sequencia1 = []
numeral_1 = 0

for n in numeros_1[:]:
    if numeral_1 < n:
        numeral_1 = n
        sequencia1.append(numeral_1)
        numeros_1.remove(numeral_1)

numeros_2 = [number for number in numeros_copia if number not in sequencia1]

sequencia2 = []
numeral_2 = 0

for n in numeros_2:
    if numeral_2 < n:
        numeral_2 = n
        sequencia2.append(numeral_2)
        numeros_1.remove(numeral_2)

if len(sequencia1) > len(sequencia2):
    print(len(sequencia1))
else:
    print(len(sequencia2))
