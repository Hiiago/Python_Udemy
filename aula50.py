'''
ex. exiba os indices da lista:

'''
#minha solução
lista = ['Hiago', 'Eli', 'Dinheiros']
cont = -1
for nome in lista:
    cont += 1
    print(cont, nome)

print('*'*30)
#Na aula
lista2 = ['abacate', 'avocato', 'musgao']
lista2.append('seilamano')

indices = range(len(lista2))

for indice in indices:
    print(indice, lista2[indice])