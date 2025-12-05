sequencia = str(input('Digite uma expressão: '))

parentese_aberto = '('
parentese_fechado = ')'
colchete_aberto = '['
colchete_fechado = ']'
chave_aberta = '{'
chave_fechada = '}'
pilha = 0
condicao_true_or_false = True

for i in sequencia:
    if i == parentese_aberto:
        pilha += 1
    if i == parentese_fechado:
        if pilha > 0:
            pilha -= 1
        else:
            condicao_true_or_false = False
            break
    
    if i == colchete_aberto:
        pilha += 1
    if i == colchete_fechado:
        if pilha > 0:
            pilha -= 1
        else:
            condicao_true_or_false = False
            break

    if i == chave_aberta:
        pilha += 1
    if i == chave_fechada:
        if pilha > 0:
            pilha -= 1
        else:   
            condicao_true_or_false = False
            break

if condicao_true_or_false == False:
    print('sequência inválida')
elif pilha != 0:
    print('sequência inválida')
else:
    print('Sequência válida')