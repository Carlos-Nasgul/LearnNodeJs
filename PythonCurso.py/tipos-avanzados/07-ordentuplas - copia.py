# ORDENAR LISTAS
numeros = [2, 9, 1, 35, 33, 10, 15, 26, 30]
letras = ['a', 'b', 'c', 'd', 'e', 'f']


numeros.sort(reverse=True)
letras.sort(reverse=False)
numerosordena2 = sorted(numeros)
print(numeros, letras, numerosordena2)


usuarios = [['Carlitos', 5], ['Flori', 1], ['Michel', 32], ['Paco', 2]]


def ordena(elemento):
    return elemento[1]


usuarios.sort(key=ordena)
print(usuarios)
