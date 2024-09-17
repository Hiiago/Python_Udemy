'''
split e join com list e str
split - divide uma string
join - une uma string
'''

frase = 'Olha só que, coisa interessante'
lista_palavras = frase.split() #quebra nos espaços
lista_palavras = frase.split(', ') #quebra na vírgula

#for i, frase in enumerate(lista_palavras):
#    print(lista_palavras[i].strip()) #strip corta espaços do começo e fim (use r e l no começo)
for i, frase in enumerate(lista_palavras):
    lista_palavras[i] = lista_palavras[i].strip()

print(lista_palavras)

frases_unidas = ' - '.join(lista_palavras)
print(frases_unidas)