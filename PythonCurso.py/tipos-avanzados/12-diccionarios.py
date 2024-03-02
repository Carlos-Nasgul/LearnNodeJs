# son una coleccion de datos {llave:valor}

puntos = {'x': 25, 'y': 50}

print(puntos['x'])  # Esto imprime el valor hay que llamar al string
print(puntos['y'])  # Esto imprime el valor hay que llamar al string
puntos['z'] = 75  # Añado otro dato al diccionario
print(puntos)
if 'h' in puntos:
    print('h OK', puntos['h'])


print(puntos.get('x'))  # obtener y añadir valor por defecto
# si solo busco h me imprime None pero si añado valor por defecto....
print(puntos.get('h', 100))
# del puntos['x'] #PARA BORRAR
# del (puntos['y'])
print(puntos)

########################
for llaves in puntos:
    print(llaves, puntos[llaves])

for valor in puntos.items():
    print(valor)
for llaves, valor in puntos.items():
    print(llaves, valor)
# USO REAL DE DICCIONARIOS EN PYTHON, con identificador U_N_I_C_O

usuarios = [
    {'id': 1, 'nombre': 'Chanchito'},
    {'id': 2, 'nombre': 'Feliz'},
    {'id': 3, 'nombre': 'Carlitos'},
    {'id': 4, 'nombre': 'Paco'}

]
print(usuarios)
for usuario in usuarios:
    print(usuario['nombre'])
