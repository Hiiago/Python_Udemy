'''
enumerate - enumera iteráveis (indices)'''
#   [(0, 'abacate'), (1, 'avocato'), (2, 'musgao'), (3, 'seilamano')]
lista = ['abacate', 'avocato', 'musgao']
lista.append('seilamano')

'''lista_enumerada = enumerate(lista)

for item in lista_enumerada:
    print(item)'''

'''for item in enumerate(lista):
    print(item)'''

'''lista_enumerada = list(enumerate(lista))
print(lista_enumerada)'''

'''for item in enumerate(lista):
    indice, nome = item
    print(indice, nome)'''

for indice, nome in enumerate(lista):
    print(indice, nome)

'''for tupla_enumerada in enumerate(lista):
    for valor in tupla_enumerada:
    print(valor)'''

for tupla_enumerada in enumerate(lista):
    print('FOR da tupla:')
    for valor in tupla_enumerada:
        print(f'\t{valor}')