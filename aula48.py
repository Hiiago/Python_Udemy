"""
Listas em Python
Tipo list - Mutável
Suporta vários valores de qualquer tipo
Conhecimentos reutilizáveis - índices e fatiamento
Métodos úteis: append, insert, pop, del, clear, extend, +
Create, Read, Update, Delete
Criar,  ler,  alterar, apagar = lista[i] (CRUD)
"""

"""lista = [0]

for i in lista:
    mais = input("Algo: ")
    lista.append(mais)
    if mais == 'stop':
        lista.pop(0)
        lista.pop()
        break
print(lista)"""

"""lista = [0,1,2,3]
lista.append('Hiago')
nome = lista.pop()
del lista[-1]
lista.clear()
lista.insert(0, 8)
print(lista, nome)
"""


lista_a = ['Hiago', 'Eli', 1, True, 1.2]
lista_b = lista_a.copy()

lista_a[0] = 'Qualquer coisa'
print(lista_a)
print(lista_b)
