'''
Operador lógico "not"
Usado para inverter expressões
not True = False
not False = True
'''

senha = input('senha: ')

# if senha == '123456':
#     print('entrou')
# else:
#     print('senha incorreta')

#Se não tiver senha: print
if not senha:
    print('senha incorreta')

print(not True)#False
print(not False)#True