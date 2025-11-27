# Filtro de pessoas
pessoas_maiores_de_dade = apenas_homens = mulheres_com_menos_de_20_anos = 0
while True:

    idade = int(input('IDADE: '))

    sexo = str()
    while sexo != 'M' and sexo != 'F':
        sexo = str(input('SEXO [M/F]: ')).strip().upper()[0]
    
    if idade >= 18:
        pessoas_maiores_de_dade += 1

    if sexo == 'M':
        apenas_homens += 1
    
    if sexo == 'F':
        if idade < 20:
            mulheres_com_menos_de_20_anos += 1

    resposta = str()
    while resposta != 'S' and resposta != 'N':
        resposta = str(input('Quer continuar? [S/N]: ')).strip().upper()[0]

    if resposta == 'N':
        break

print(f'{pessoas_maiores_de_dade} são maiores de idade')
print(f'Temos o total de {apenas_homens} homen(s)')
print(f'Temos o total de {mulheres_com_menos_de_20_anos} mulheres com menos de 20 anos')


# Filtro de produtos
total_de_gastos = produto_que_custa_mais_de_100 = int()
produtos = list()
nomes_dos_produtos = list()
produto_mais_barato = 0

while True:

    nome_do_produto = str(input('Nome do produto: ')).strip().capitalize()
    preco_do_produto = float(input('Preço do produto: '))
    
    total_de_gastos += preco_do_produto

    if preco_do_produto > 100:
        produto_que_custa_mais_de_100 += 1
    
    produtos.append(preco_do_produto)
    nomes_dos_produtos.append(nome_do_produto)

    possivel_parada = str()
    while possivel_parada != 'S' and possivel_parada != 'N':
        possivel_parada = str(input('Deseja continuar? [S/N]: ')).strip().upper()[0]

    if possivel_parada == 'N':
        break

print(f'O total de gastos foi de {total_de_gastos:.2f}R$')
print(f'O total de produtos que custam mais de 100R$ é de {produto_que_custa_mais_de_100}')

for i in produtos:
    if produto_mais_barato == 0:
        produto_mais_barato = i
    if i < produto_mais_barato:
        produto_mais_barato = i

if produto_mais_barato in produtos:
    indice_produto_mais_barato = produtos.index(produto_mais_barato)

nome_do_produto_mais_barato = nomes_dos_produtos[indice_produto_mais_barato]

print(f'O produto mais barato é: {nome_do_produto_mais_barato}')