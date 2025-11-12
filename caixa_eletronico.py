# Caixa eletrônico

dinheiro_do_banco = [200, 100, 50, 20, 10, 5, 2, 1, 0.50, 0.25, 0.10, 0.5, 0.1]
dinheiro_do_banco.reverse()

dinheiro_para_sacar = float(input('R$: '))
valor = 0
notas = []

for i in dinheiro_do_banco:
    
    if valor != dinheiro_para_sacar:
        if i > dinheiro_para_sacar:
            break
        valor += i
        notas.append(i)
