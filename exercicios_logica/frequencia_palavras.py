from collections import Counter

frutas = 'banana maçã banana uva uva banana maçã maçã maçã'
frutas1 = frutas.split()

quantidade_de_frutas = Counter(frutas1)
frutas2 = dict(quantidade_de_frutas)

frutas_em_ordem = sorted(frutas2.items(), key=lambda pares_defrutas: pares_defrutas[1],reverse=True)

for fruits, quantidades in frutas_em_ordem:
    print(f'{fruits}: {quantidades}')