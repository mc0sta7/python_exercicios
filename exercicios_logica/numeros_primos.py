'''Numeros primos entre 10 e 20'''
def numeros_primos_entre_10_e_20():  
    numeros_primos = []

    for contagem in range(10,21):
        if (contagem % 2 != 0 and contagem % 3 != 0 and contagem % 4 != 0 and contagem % 5 != 0 and contagem % 6 != 0 and
            contagem % 7 != 0 and contagem % 8 != 0 and contagem % 9 != 0):
            numeros_primos.append(contagem)

    return numeros_primos

def numero_primo(numero):
    
    if numero < 2:
        return 'Não é primo'
    
    elif numero == 2:
        return 'O número é primo'
    
    elif numero & 2 == 0:
        return 'O número não é primo'
    
    for numerais in range(3,int(numero**0.5)+1,2):
        if numero % numerais == 0:
            return 'O número é primo'
    else:
        return 'Não é primo'
    
print(numeros_primos_entre_10_e_20())

'''Teste para verificar numero primo aleatório'''
while True:
    try:
        numero = int(input('Nº: '))
        print(numero_primo(numero))
    except ValueError:
        print('Digite apenas números!')