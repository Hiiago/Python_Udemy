#Exercício

name = input('Digite seu nome: ')
age = input('Digite sua idade: ')

#if name and idade: <- também funciona.
if not name or not age:
    print('Desculpe, você deixou campos vazios.')
else:
    print(f'Nome: {name}.\n'
        f'Invertido: {name[::-1]}')
    if ' ' in name:
        print(f'Espaços: Sim!')
    else:
        print('Espaços: Não!')
    print(f'Qtd. Letras: {len(name)}\n'
        f'Primeira letra: {(name[0])}\n'
        f'Última letra: {(name[-1])}')
