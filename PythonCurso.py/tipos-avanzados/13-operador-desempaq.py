lista1 = [1, 2, 3, 4]
print(lista1)
print(*lista1)

lista2 = [5, 6, 7, 8]
print(lista2)

combinada = [*lista1, *lista2]
print(combinada)

# Tambien con Diccionarios

punto1 = {'x': 19}
punto2 = {'y': 15}
nuevoPunto = {**punto1, **punto2}
print(nuevoPunto)
