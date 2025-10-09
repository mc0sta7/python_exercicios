p = 'arara'

palavra = p.lower()

alfabeto = 'abcdefghijklmnopqrstuvwxyz'

letra = []

for verificador_de_letra in palavra:
    if verificador_de_letra in alfabeto:
        letra.append(verificador_de_letra)

for contagem1 in len(letra):
    letra_atual = [letra[0]]

'''    
    subsequencias = []  # vai guardar todas as subsequências encontradas
    
    for i in range(len(lista)):
        atual = [lista[i]]

        for j in range(i + 1, len(lista)):
            if lista[j] > atual[-1]:
                atual.append(lista[j])
                
        subsequencias.append(atual)'''