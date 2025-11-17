# Caixa eletrônico

cedulas = [100, 50, 20, 10, 5, 2, 1]

valor_da_conta = int(5.000)
dinheiro_para_sacar = int(170)
maior_cedula = 0
maiores_cedulas = dict()
dinheiro = int()

for i in cedulas:

    if i > maior_cedula:
        maior_cedula = i

quantidade_de_cedulas_float = dinheiro_para_sacar / maior_cedula
quantidade_de_cedulas_inteiro = int(quantidade_de_cedulas_float)

subtracao = dinheiro_para_sacar - maior_cedula

print(subtracao)