#Condicionais - if/ elif/ else
#              se  ou se  se nao

entrada = input('Quer "entrar" ou "sair" ?\nR: ')

if entrada == 'entrar':
    print('Você entrou no sistema.')
elif entrada == 'sair':
    print('Você saiu do sistema.')
    print('Até logo!')
else:
    print('Você não digitou nem "entrar" nem "sair". ')
print('------------------')