def numeros_primos_entre_1_e_40():  

    numeros_primos = []

    for n in range(2,41):

        if n in (2, 3, 5, 7):
             print(n , 'é primo')
            
        elif (n % 2 != 0 and n % 3 != 0 and n % 4 != 0 and n % 5 != 0 and
                n % 6 != 0 and n % 7 != 0 and n % 8 != 0 and n % 9 != 0 and n % 10 != 0):
             numeros_primos.append(n)
    return numeros_primos
        
print(numeros_primos_entre_1_e_40())

def numero_primo(numero):
    
     if numero < 2:
         return 'Não é primo'
     
     if numero >= 2:
        for i in range(2, int(numero ** 0.5) + 1):

            if numero % i == 0:

                return 'Não é primo'
            
        return 'É primo'

while True:
     try:
         
         numero = int(input('Nº: '))
         print(numero_primo(numero))

     except ValueError:
         print('Digite apenas números!')


### SOBRECARGA DE OPERADORES
# https://realpython.com/operator-function-overloading/

## funções recursivas https://www.dio.me/articles/funcoes-recursivas-em-python-o-que-sao-e-como-funcionam
# number = int(input("Digite um número: "))
# def factorial_rec(number: int) -> int:
#     if number == 1:
#         return 1
#     return number * factorial_rec(number - 1)

# print(factorial_rec(number))