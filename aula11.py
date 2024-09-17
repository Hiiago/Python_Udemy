'''
precedência dos valores:

1º (n + n) - parenteces
2º ** - potenciacao
3º * / // % - operadores
4º + - - subtração e adição
da esquerda para direita
'''
conta1 = 1 + 1 ** 5 + 5
conta2 = (1 + 1) ** (5 + 5)
#           1º   3º    2º
print(conta1)
print(conta2)
