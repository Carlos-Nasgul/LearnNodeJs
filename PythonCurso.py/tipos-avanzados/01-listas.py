numeros = [1, 2, 3]
letras = ['a', 'b', 'c']
palabras = ['hola', 'maña', 'colega']
nombrePropios = ['Carlos', 'Flori']
booleans = [True, False, False, True]
matriz = [[0, 1], ['x', 'y']]
ceros = [0] * 5
alfaNumerico = letras + numeros
rango = list(range(1, 11))
chars = list('Hola Mundo')


print(numeros)
print(letras)
print(palabras)
print(nombrePropios)
print(booleans)
print(matriz)
print(ceros)
print(rango)
print(chars)


# MANIPULANDO LISTAS

mascotas = ['Gordo', 'bobby', 'Linda', 'Toby']
print(mascotas[0])  # Imprime el indice de la lista [0]=numero 1 del index
mascotas[1] = 'Snoopy'
mascotas[3] = 'Turko'
print(mascotas)
print(mascotas[2:4])
print(mascotas[-1])
print(mascotas[::2])  # para saltar así da los index pares, OSEA IMPARES
print(mascotas[2::5])

numeros = list(range(21))
print('IMPARES', numeros[1::2])  # impares del rango 21
print('PARES', numeros[0::2])  # pares del rango 21


# DESEMPAQUE DE LAS LISTAS
