'''
desempacotamento + tuplas
'''
"""nomes = ['Hiago', 'Eli', 'Corinthians']
nome1, nome2, nome3 = nomes
"""
_, nome, *resto = ['Hiago', 'Eli', 'Corinthians']
#Posso usar " _ " para indicar que a variavel
#foi criada mas não usarei ela.
print(nome, resto)