# exercicio de calculadora
# para aprender a fazer a calculadora
""" Calculadora com while"""

number_1 = 0
number_2 = 0

while True:
    number_1 = input('Digite o primeiro número: ')
    number_2 = input('Digite o segundo número: ')
    operador = input('Digite o operador que deseja (+-*/): ')
    
    numeros_validos = None

    try:
        number_1 = float(number_1)
        number_2 = float(number_2)
        numeros_validos = True
    except:
        numeros_validos = None

    if numeros_validos is None:
        print('Um ou ambos os números digitados são inválidos.')
        continue

    operadores_permitidos = '+-*/'

    if operador not in operadores_permitidos:
        print('operador inválido.')
        continue

    if len(operador) > 1:
        print('Digite apenas um operador.')
        continue
    
    print('Realizando a conta. Confira o resultado abaixo: ')
    if operador == '+':
        print(f'{number_1} + {number_2} =',number_1 + number_2)
    elif operador == '-':
        print(f'{number_1} - {number_2} =',number_1 - number_2)
    elif operador == '*':
        print(f'{number_1} * {number_2} =',number_1 * number_2)
    elif operador == '/':
        print(f'{number_1} / {number_2} =',number_1 / number_2)
    else:
        print('Nunca deve chegar aqui')

    sair = input('Quer sair? [s]im: ').lower().startswith('s')
    
    if sair is True:
        break
    print('continuando...')

print('Saindo')
