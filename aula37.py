"""
while + continue
pulando alguma repetição
"""

# contador = 0

# while contador <= 10:
#     contador += 1
#     print(contador)

#     if contador == 4:
#         break
# print('Acabou')

contador = 0

while contador <= 100:
    contador += 1

    if contador == 6:
        print(f'Não vou mostrar o {contador}.')
        continue

    if contador >= 10 and contador <= 27:
        print(f'Não vou mostrar o {contador}.')
        continue

    print(contador)

    if contador == 40:
        break

print('Acabou')