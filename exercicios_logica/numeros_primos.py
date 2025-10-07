'''Numeros primos entre 10 e 20'''
# def numeros_primos_entre_10_e_20():  
#     numeros_primos = []

#     for contagem in range(10,21):
#         if (contagem % 2 != 0 and contagem % 3 != 0 and contagem % 4 != 0 and contagem % 5 != 0 and contagem % 6 != 0 and
#             contagem % 7 != 0 and contagem % 8 != 0 and contagem % 9 != 0):
#             numeros_primos.append(contagem)

#     return numeros_primos

# def numero_primo(numero):
    
#     if numero < 2:
#         return 'Não é primo'
    
#     elif numero == 2:
#         return 'O número é primo'
    
#     elif numero & 2 == 0:
#         return 'O número não é primo'
    
#     for numerais in range(3,int(numero**0.5)+1,2):
#         if numero % numerais == 0:
#             return 'O número é primo'
#     else:
#         return 'Não é primo'

# while True:
#     try:
#         numero = int(input('Nº: '))
#         print(numero_primo(numero))
#     except ValueError:
#         print('Digite apenas números!')
# for n in range(2,101):
#     if n in (2, 3, 5, 7):
#         print(n , 'é primo')
#     elif (n % 2 != 0 and n % 3 != 0 and n % 4 != 0 and n % 5 != 0 and
#         n % 6 != 0 and n % 7 != 0 and n % 8 != 0 and n % 9 != 0 and n % 10 != 0):
#         print(n, 'é primo')


# ### Fatorial de um número
# n = int(input())
# f = 1
# for i in range(1, n+1):
#     f *= i
# print(f) 

### SOBRECARGA DE OPERADORES
# https://realpython.com/operator-function-overloading/

## funções recursivas https://www.dio.me/articles/funcoes-recursivas-em-python-o-que-sao-e-como-funcionam
# number = int(input("Digite um número: "))
# def factorial_rec(number: int) -> int:
#     if number == 1:
#         return 1
#     return number * factorial_rec(number - 1)

# print(factorial_rec(number))

def eh_primo(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True

a = int(input())
b = int(input())
for num in range(a, b+1):
    if eh_primo(num):
        print(num)
