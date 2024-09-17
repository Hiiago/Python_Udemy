"""
iterável = str, range, etc (__iter__)
iterador = quem sabe entregar um valor por vez
next = me entregue o proximo valor
iter = me entregue seu iterador
"""

#texto = 'Hiago'.__iter__()
#print(texto)

# texto = iter('Hiago')

# print(next(texto))
# print(next(texto))
# print(next(texto))
# print(next(texto))
# print(next(texto))

texto = 'Hiago' #Iterável
# iterator = iter(texto) #Iterator

# while True:
#     try:
#         letra = next(iterator)
#         print(letra)
#     except StopIteration:
#         break

for letra in texto:
    print(letra)
