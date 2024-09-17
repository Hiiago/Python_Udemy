'''
Operadores lógicos
ºand (e) | or (ou) | not (não)
ºor - Qualquer condição verdadeira,
avalia toda a expressão como verdadeira.
ºSe qualquer valor for considerado verdadeiro,
a expressão inteira será avaliada naquele valor
ºSão considerados falsy (que você já viu):
0 | 0.0 | '' | False
ºTambém existe o tipo None que é usado para
representar um não valor.
'''
entrada = input('[E]ntrar [S]air: ')
senha_digitada = input('Senha: ')

senha_permitida = '123456'

#Parênteces usados para avaliar a primeira condição querendo True
if (entrada == 'E' or entrada == 'e') and senha_digitada == senha_permitida:
    print('Entrar')
else:
    print('Sair')

senha = input('Senha: ') or 'Sem senha'
print(senha)

print(True or True)#True
print(True or False)#True
print(False or False)#False
print(False or True)#True