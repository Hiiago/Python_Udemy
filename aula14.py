#continuação .format()

a = 'a'
b = 'b'
c = 1.1

string = 'a = {nome1}\nb = {nome2}\nc = {nome3:.2f}'
formato = string.format(
    nome1=a, nome2=b , nome3=c
)
print(formato)