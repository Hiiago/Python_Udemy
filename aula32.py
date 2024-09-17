"""
1.
condições:
usuario digitar um numero inteiro
mostrar se é par ou impar
se não for inteiro, mostrar o erro.
"""

inteiro = input('Número inteiro: ')

try:
    numero_int = int(inteiro)
    par = numero_int % 2 == 0
    impar = numero_int % 2 != 0
    print(f'Par: ', par)
    print(f'Ímpar: {impar}')
except:
    print(f'"{inteiro}": não é um número inteiro.')


"""
2.
Perguntar a hora
exibir saudação apropriada
"""

hora = int(input('Tem hora pra me dar ? '))

horas = [00, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11,
        12, 13, 14, 15, 16, 17,
        18, 19, 20, 21, 22, 23
]

if hora in horas[0:12]:
    print(f'Bom dia! são {hora:.2f}h')
elif hora in horas[12:18]:
    print(f'Boa tarde! são {hora:.2f}h')
elif hora in horas[18:24]:
    print(f'Boa noite! são {hora:.2f}h')
else:
    print(f'{hora} não está correto.')

"""
3.
pedir o nome do usuário
verificar se é curto, normal ou grande
"""

nome = input('Nome: ')

if len(nome) > 1:
    if len(nome) <= 4:
        print('Seu nome é curto demais.')
    elif len(nome) >= 7:
        print('Seu nome é muito grande.')
    else:
        print('Seu nome é normal.')
else:
    print('Digite algo com mais de uma letra.')
