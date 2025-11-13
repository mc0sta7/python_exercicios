# Caixa eletrônico

cedulas = [100, 50, 20, 10, 5, 2, 1]

valor_da_conta = float(5.000)
dinheiro_para_sacar = float(170)
maior_cedula = 0
maiores_cedulas = []
valor = float()

while valor != dinheiro_para_sacar:

    for i in cedulas:
        if i > maior_cedula:
            maior_cedula = i

    quantidade_de_notas = float()

    if dinheiro_para_sacar % maior_cedula == 0:
        dinheiro_para_sacar / maior_cedula = quantidade_de_notas
    else:
        dinheiro_para_sacar / maior_cedula = quantidade_de_notas
    
    cedulas_e_quantidades = zip(dict(maior_cedula, quantidade_de_notas))