"""
args - Argumentos não nomeados
* - *args (empacotamento e desempacotamento)
"""

# Lembre-te de desempacotamento
# x, y, *resto = 1, 2, 3, 4,
# print(x, y, resto)

#*ARGS PARTE 1
# def soma(*args):
#     total = 0
#     for numero in args:
#         print(f'Soma= {total} + {numero}')
#         total += numero
#         print(f'Total = {total}',)
#     print(total)
# soma(1, 2, 3, 4, 5, 6)

#*ARGS PARTE 2
def soma(*args):
    total = 0
    for numero in args:
        total += numero
    return total

soma_1_2_3 = soma(1, 2, 3)
print(soma_1_2_3)
#Somei 1 + 2 + 3 com o *args empacotamento não nomeado

soma_4_5_6_7 = soma(4, 5, 6, 7)
print(soma_4_5_6_7)

#Função para isso:
print(sum((4, 5, 6, 7)))