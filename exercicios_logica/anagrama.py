p = 'amore'

palavra = p.lower()

alfabeto = 'abcdefghijklmnopqrstuvwxyz'

letra = []

for verificador_de_letra in palavra:
    if verificador_de_letra in alfabeto:
        letra.append(verificador_de_letra)

from collections import Counter

letras_e_quantidades = dict(Counter(letra))
quantidades_de_letras = letras_e_quantidades.values()

def fatorial(numeros):

    lista_numeros = []
    fatorial = 0

    for contagem in range(numeros,0,-1):
        lista_numeros.append(contagem)
    
    for verificador in lista_numeros:

        if fatorial <= verificador:
            fatorial = verificador 

        elif fatorial >= verificador:
            fatorial = fatorial * verificador

    return fatorial

fatorial_de_cada_numero_da_lisa = map(fatorial, quantidades_de_letras)

lista_com_valores_inteiros = []

for transformador in fatorial_de_cada_numero_da_lisa:
    transformador = int(transformador)
    lista_com_valores_inteiros.append(transformador)

multiplicacao_final = 0

for n in lista_com_valores_inteiros:
    if multiplicacao_final < n:
        multiplicacao_final = n
    elif multiplicacao_final >= n:
        multiplicacao_final = multiplicacao_final * n

fatorial_da_quantidade_de_itens = fatorial(len(letra))

final_de_tudo = fatorial_da_quantidade_de_itens / multiplicacao_final
print(final_de_tudo)