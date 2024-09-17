"""
Interpolação básica de strings
s - string
d e i - int
f - float
x e X - Hexadecimal (ABCDEF0123456789)
"""

nome = 'Hiago'
preco = 1000.923546
variavel = '%s, o preço é: R$%.2f' % (nome, preco)#(parenteses) = apenas com mais de um valor
print(variavel)
print('O hexadecimal de %d é %04x' % (1500, 1500))#X maiúsculo para converter o nmr para maiusculo. etc...