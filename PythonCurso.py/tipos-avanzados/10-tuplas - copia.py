numeros = (1, 2, 3, 4) + (5, 6, 7, 8, 9)
print(numeros)
# LAS TUPLAS NO SE PUEDEN
# MODIFICAR--> (parentesis) <--OJO!
# SE PUEDEN CREAR OTRAS TUPLAS A RAIZ DE ELLAS
# O TRANSFOR EN LISTAS
# SE PUEDEN ITERAR

tuplaHija = tuple([1, 2])
print(tuplaHija)
tuplaNieta = numeros[2:5]
print(tuplaNieta)
# desempaquetar la TUPLA
n1, n2, *otros = numeros
print(n1, n2, otros)
# y devuelve los elementos y una lista


listaNumeros = list(numeros)
listaNumeros[0] = 'Chanchito Feliz'
print(listaNumeros)

# iterar la tupla
for n in numeros:
    print(n)
