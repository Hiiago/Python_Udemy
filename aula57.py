"""
Lista de listas e seus índices
"""

salas = [
    # 0........1
    ['Maria', 'Helena', ],#0
    # 0
    ['Elaine'],#1
    # 0.......1.......2..........3
    ['Luiz', 'João', 'Eduarda', (0, 10, 20, 30, 40)], #2
]

# print(salas[1][0])
# print(salas[0][1])
# print(salas[2][2])
# print(salas[2][3][2])

cont_sala = 0
cont_aluno = 1

for sala in salas:
    print(f'A sala {cont_sala} é: {sala}')
    cont_sala += 1
    for aluno in sala:
        print(f'{cont_aluno}º aluno')
        cont_aluno += 1