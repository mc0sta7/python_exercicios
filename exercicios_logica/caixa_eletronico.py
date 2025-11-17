# Caixa eletrônico

dinheiro_para_sacar = int(input('Valor do saque: '))
cedulas = [100, 50, 20, 10, 5, 2, 1]

while dinheiro_para_sacar != 0:

    maior_cedula = 0

    for i in cedulas:

        if i > maior_cedula:
            maior_cedula = i

    quantidade_de_cedulas = dinheiro_para_sacar // maior_cedula

    cedulas_lista = []
    quantidade_de_cedulas_lista = []

    cedulas_lista.append(maior_cedula)
    quantidade_de_cedulas_lista.append(quantidade_de_cedulas)

    cedulas_e_quantidades = dict(zip(cedulas_lista, quantidade_de_cedulas_lista))
    print(cedulas_e_quantidades)

    cedulas.remove(maior_cedula)

    dinheiro_para_sacar -= (maior_cedula * quantidade_de_cedulas)