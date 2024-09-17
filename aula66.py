"""
Argumentos nomeados e não nomeados em funções python
Argumento nomeado tem nome com sinal de igual
Argumento não nomeado recebe apenas o argumento (valor)
"""

# def soma(x, y):
#     #Definição
#     print(x + y)
# soma(1, 2)

def soma(x, y):
    #Definição
    print(f'{x=} y={y}', '|', 'x + y =', x + y)

soma(1, 2)
soma(x=1, y=2)
