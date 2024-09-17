'''
Introdução ao try/except
try - tentar executar o código
except - ocorreu algum erro ao tentar executar o código
'''

# numero = input('Vou dobrar o número que digitar: ')

# numero_float = float(numero) #coerção de str para float.

# print(f'O dobro de {numero} é {numero_float * 2}.') #Dobrando um valor

numero_str = input(
    'Vou dobrar o número que digitar: '
)

try:
    print('STR:', numero_str)
    numero_float = float(numero_str)
    print('FLOAT:', numero_float)
    print(f'O dobro de {numero_str} é {numero_float * 2}.')
except:
    print('Isso não é um número.')

# if numero_str.isdigit(): #"variavel + . " mostra algumas funções disponíveis
#             #isdigit mostra apenas se foi digitado números
#     numero_float = float(numero_str)
#     print(f'O dobro de {numero_str} é {numero_float * 2}.')
# else:
#     print('Isso não é um número.')
