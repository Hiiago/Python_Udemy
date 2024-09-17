# Desempacotamento em chamadas
# de métodos e funções
print('-' * 30)
string = 7,4,6,8,2,4,8,9,0
lista = ['Maria', 'Helena', 1,2,3,4, 'Eduarda']
tupla = 'Python', 'é', 'legal'

print(*string)
print(*lista)
print(*tupla)

print('-' * 30)
salas = [
    # 0........1
    ['Maria', 'Helena', ],#0
    # 0
    ['Elaine'],#1
    # 0.......1.......2..........3
    ['Luiz', 'João', 'Eduarda', (0, 10, 20, 30, 40)], #2
]

print(*salas, sep='\n')