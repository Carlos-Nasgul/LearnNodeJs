buscar = 13
for numero in range(15):
    print(numero)
    if numero == buscar:
        print('Encontrado', buscar)
        break
else:
    print('Número no encontrado...')
