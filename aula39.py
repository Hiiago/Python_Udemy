"""
Iterando str com while
"""
#      01234567891011

nome = 'Hiago Soares'
tamanho_nome = len(nome)
print(nome)
print(tamanho_nome)

indice = 0

while indice < len(nome):
    print(f'{nome[indice]}', end='*')
    indice += 1

