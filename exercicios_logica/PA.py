# 10 termos de uma Progressão Aritimétrica

primeiro_termo = int(input('Primeiro termo: '))
razao = int(input('Razão da PA: '))

pa = []
pa.append(primeiro_termo)

for i in range(9):
    i = primeiro_termo
    primeiro_termo += razao
    pa.append(primeiro_termo)

print('PA: ', end='')

for i in pa:
    print(f'{i} ->', end=' ')
print('Acabou')