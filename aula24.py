'''
Operadores lógicos in (entre) e not in (não entre)
Strings são iteráveis - índices
 0 1 2 3 4
 H I A G O
-5-4-3-2-1
'''

nome = 'Hiago'
print(nome[2])#Me retorna o valor na iteração [2] = a
print(nome[-2])#Retorna o valor [-2] = g
print('a' in nome)#"'a' está em (nome) ? = True"
print('8' in nome)#"'8' está em (nome) ? = False"
print('ago' not in nome)#"'ago' não está em (nome) ? = False (ago está em (nome))"

nome2 = input('Digite seu nome: ')
encontrar = input('O que quer encontrar ? ')

if encontrar in nome2:
    print(f'{encontrar} está em {nome2}')
else:
    print(f'{encontrar} não está em {nome2}')
print('Até logo!')