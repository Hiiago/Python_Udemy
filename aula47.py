"""MINHA TENTATIVA
senha = 'agua'

cont = 0
certo = ''

print('__JOGUINHO DA FORCA__')

while certo != 'agua':
    usuario = input('Liquido: ')
    cont += 1
    for i in usuario:
        if len(usuario) == 1 and usuario in senha:
            certo += usuario
            print(f'\033[32m{usuario}\033[0m')
        elif usuario not in senha:
            print('\033[31m****\033[0m')

print(f'Tentativas: \033[35m{cont}\033[0m\n'
    f'Palavra: \033[34m{certo}\033[0m')
"""
palavra_secreta = 'perfume'
letras_acertadas = ''
numero_tentativas = 0

while True:
    letra_digitada = input('Digite uma letra: ')
    numero_tentativas += 1

    if len(letra_digitada) > 1:
        print('Digite apenas uma letra.')
        continue

    if letra_digitada in palavra_secreta:
        letras_acertadas += letra_digitada

    palavra_formada = ''
    for letra_secreta in palavra_secreta:
        if letra_secreta in letras_acertadas:
            palavra_formada += letra_secreta
        else:
            palavra_formada += '*'

    print('Palavra formada:', palavra_formada)

    if palavra_formada == palavra_secreta:
        print('VOCÊ GANHOU !')
        print('A palavra era: ', palavra_secreta)
        print('Tentativas: ', numero_tentativas)
        letras_acertadas = ''
        numero_tentativas = 0
