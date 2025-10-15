"""
>Input<
arara
30

>Output<
amore
120

Formula:
Total = 5! / (3! * 2!) = 120 / (6 * 2) = 120 / 12 = 10

# Porque usar função? Qual o impacto do uso das funções neste exercício?
# Qual a diferença dos tipos de dados em python? list, tuple, set, dict quando usar cada um?
# Oque pode ser melhorado nesta solução?
"""
def fatorial(numero):
    somatorio = 0
    for i in range(numero,0,-1):
        if somatorio == 0:
            somatorio = i
        else:
            somatorio *= i
    return somatorio

def retorna_letras_repetidas(palavra):
    letras_repetidas = {}

    for letra in palavra:
        if letra in letras_repetidas.keys():
            letras_repetidas[letra] += 1
        else:
            letras_repetidas[letra] = 1
    return letras_repetidas.values()

palavra = input("digite a palavra para calular o anagrama: ").lower()

if len(palavra) == len(set(palavra)):
    print(fatorial(len(palavra)))
else:
    letras = retorna_letras_repetidas(palavra)

    fatorial_das_letras_repetidas = 1

    for numero in letras:
        fatorial_das_letras_repetidas = fatorial_das_letras_repetidas * fatorial(numero)

    quantidade_de_letras = len(palavra)

    print(fatorial(quantidade_de_letras) / fatorial_das_letras_repetidas)
