
# Código não funcional

numeros = '5 1 8 2 3 9 4'
numeros_juntos = numeros.split()

numeros_1 = []

for num in numeros_juntos:
    num = int(num)
    numeros_1.append(num)

def subsequencia(lista_numeros):
    
    if len(lista_numeros) == 0:
        return 'A lista está vazia'
    
    while True:

        sequencia1 = []
        numeral_1 = 0

        for n in lista_numeros:
            if numeral_1 < n:
                numeral_1 = n
                sequencia1.append(numeral_1)

        if len(lista_numeros) == 0:
            return f'A maior subsequência é: {len(sequencia1)}! E não há mais itens na lista'
            break

        else: 
            numeros_2 = [num for num in lista_numeros if num not in sequencia1]

            sequencia2 = []
            numeral_2 = 0

            for n in numeros_2:
                if numeral_2 < n:
                    numeral_2 = n
                    sequencia2.append(numeral_2)

            if len(sequencia1) > len(sequencia2):
                return f'A maior subsquência é: {len(sequencia1)}'
            else:
                return f'A maior subsequência é: {len(sequencia2)}'

print(subsequencia(numeros_1))

# Código funcional

numeros_2 = '5 1 8 2 3 9 4'
numeros_juntos2 = numeros_2.split()
numeros_3 = [int(num) for num in numeros_juntos2]

def maior_subsequencia_crescente(lista):
    if not lista:
        return 'A lista está vazia'
    
    subsequencias = []  # vai guardar todas as subsequências encontradas
    
    for i in range(len(lista)):
        atual = [lista[i]]

        for j in range(i + 1, len(lista)):
            if lista[j] > atual[-1]:
                atual.append(lista[j])
                
        subsequencias.append(atual)
    
    # encontra a maior
    maior = max(subsequencias, key=len)
    return f'A maior subsequência crescente é: {maior}, com tamanho {len(maior)}'

print(maior_subsequencia_crescente(numeros_3))