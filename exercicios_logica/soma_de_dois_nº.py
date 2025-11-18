from array import array

'''nums[i] + nums[j] = target'''

# 1ª solução

numeros = array('i', [1,2,3,4,5,6,7,8])

target = 9
num = 0
subsequencias = []

for i in numeros:

    for num in numeros:

        possibbilidade = i + num

        if possibbilidade == target:
            subsequencias.append(f'{i} + {num}')

print(subsequencias, f'Existem {len(subsequencias)} somas para chegar ao número {target}')

# 2ª solução

numeros1 = array('i', [1, 2, 3, 4, 5, 6, 7, 8])
target1 = 9
nums_vistos = {} # {valor: indice}
pares_otimizados = []

# Iteramos apenas uma vez (enumerate fornece o índice 'i' e o valor 'num')
for i, num in enumerate(numeros1):
    complemento = target1 - num
    
    # Se o complemento necessário já foi visto e armazenado:
    if complemento in nums_vistos:
        indice_complemento = nums_vistos[complemento]
        
        # Encontrado! Este par é único e os índices são diferentes.
        pares_otimizados.append(f'Indices [{indice_complemento}, {i}] -> {complemento} + {num}')
        
    # Armazenamos o número atual para checagens futuras
    nums_vistos[num] = i

print("\n--- Solução Otimizada O(n) ---")
print(pares_otimizados)
print(f'Existem {len(pares_otimizados)} pares (únicos) para chegar ao número {target}')