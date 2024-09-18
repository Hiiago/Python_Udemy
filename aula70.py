"""
Retorno de valores das funções (return)
"""
# variavel = print('gut  ')
# print(variavel)

# def soma(x, y):
#     return x + y
def soma(x, y):
    if x > 10:
        return 10, 20
    return x + y

soma1 = soma(2, 2)
soma2 = soma(3, 3)
print(soma1 + soma2)
print(soma(11, 55))