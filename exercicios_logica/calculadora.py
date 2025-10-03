def adicao(x, y):  #adição
  return x + y


def subtracao(x, y):  #subtração
  return x - y


def multiplicacao(x, y):  #multiplicação
  return x * y


def divisao(x, y):
  if x == 0 or y == 0:
    return ("Não existe divisão por zero!")  #divisão
  else:
    return x / y


def potencia(x, y):  #potência
  return x ** y

print('Escolha uma operação!')
print('Digite 1 para adição, 2 para subtração, 3 para multiplicação, 4 para divisão ou 5 para potência!')

while True:  #estrutura de repetição
  try:  #tratamento de erros
    while True:
     escolha = int(input("escolha sua opção: (1,2,3,4,5): "))
     if escolha in [1,2,3,4,5]:
       break
    x = float(input("Digite o primeiro número: "))
    y = float(input("Digite o segundo número: "))

    if escolha == 1:
      print(f'R: {adicao(x,y)}')

    elif escolha == 2:
      print(f'R: {subtracao(x,y)}')

    elif escolha == 3:
      print(f'R: {multiplicacao(x, y)}')

    elif escolha == 4:
      print(f'R: {divisao(x,y)}')

    elif escolha == 5:
      print(f'R: {potencia(x,y)}')

    print('Novamente!')
  except ValueError:
    print("Digite apenas números!")