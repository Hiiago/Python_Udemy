'''
Operadores lógicos
ºand (e) | or (ou) | not (não)
ºand - Todas as condições precisam ser verdadeiras.
ºSe qualquer valor for considerado falso,
a expressão inteira será avaliada naquele valor
ºSão considerados falsy (que você já viu):
0 | 0.0 | '' | False
ºTambém existe o tipo None que é usado para
representar um não valor.
'''

entrada = input('[E]ntrar [S]air: ')
senha_digitada = input('Senha: ')

senha_permitida = '123456'

# Para mostrar esse print,
# precisa-se que todas as condições sejam True
if entrada == 'E' and senha_digitada == senha_permitida:
    print('Entrar')
else:
    print('Sair')

print(True and True) #Retorna True
print(True and False)#Retorna False
print(False and False)#Retorna False
print(False and True)#Retorna False
