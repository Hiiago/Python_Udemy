"""
Fatiamento de strings
012345678
Olá Mundo
-987654321
Fatiamento [inicio:fim:passo][::]
Obs.: a função len retorna a qtd
de caracteres da str
"""
print('fatiamento:\n')
variavel = 'Olá mundo'
print(variavel[4:])
print(variavel[:4])
print(variavel[-8:-2])
print(variavel[-8:])
print(variavel[:-8])
print(variavel[0:5:1])
print(variavel[::-1])#0 a 9 de um em um

print('\nlen:\n')

print(len(variavel))
print(len(variavel[3:]))

