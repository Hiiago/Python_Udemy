#Exercícios com funções


# def multiplicador(*args):
#     total = 1
#     for numero in args:
#         print(f'{total} * {numero}')
#         total *= numero
#         print(f'{total = }')
#         print('-' * 10)
#     return total
# multiplicador(1,2,3,4,5,6,7,8)


# def multiplicador(*args):
#     total = 1
#     for numero in args:
#         total *= numero
#     return total
# variavel = multiplicador(1,2,3,4,5,6,7,8)
# print(f'Total = {variavel}')

# print(1*2*3*4*5*6*7*8)

import random
from random import randint

#numero_aleatorio = randint(0, 100)
# numeros = input('Quer um número ? [S]im | [Não]: ')

# if numeros == 'n':
#     print('Ok, fim do programa')

# else:
#     print(numero_aleatorio)
#     if numero_aleatorio % 2 == 0:
#         print('par')
#     else:
#         print('impar')
# #print(numeros)

def par_impar(*args):
    for num in args:
        if num % 2 == 0:
            print(f'{num} é par')
        else:
            print(f'{num} é impar')
par_impar(randint(0,100))

#Na aula
def par_impar(numero):
    logica = numero % 2 == 0
    if logica:
        return f'{numero} é par'
    return f'{numero} é impar'
print(par_impar(randint(0, 100)))