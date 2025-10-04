numeros_primos = []
numeros_nao_primos = []

for contador in range(10,21):
    if contador % 2 != 0:
        numeros_primos.append(contador)
    else:
        numeros_nao_primos.append(contador)
print(numeros_primos)
print(numeros_nao_primos)