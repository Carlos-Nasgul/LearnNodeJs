def retornofuncion(a, b):  # ESTA SUMA...
    resultado = a + b
    return resultado  # <-- cambiado por print(resultado), pongo return


# ...LA REUTILIZO AQUI AÑADIENDO VARIABLES NUEVAS Y ASIGNANDO la def de arriba
c = retornofuncion(2, 3)
d = retornofuncion(c, 100)

print(c)
print(d)
