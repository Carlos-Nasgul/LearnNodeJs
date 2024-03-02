# def saludo(nombre):
# print('Hola Cazalla!')
# print(f"Bienvenido {nombre}")


# saludo('Carlos')


# def saludo(nombre, apellido):
# print('Hola Cazalla!')
# print(f"Bienvenido {nombre} {apellido}")


# saludo('Carlos', 'García')
# saludo('Pepe', 'Python')

def saludo(nombre, apellido='Python'):
    print('Hola Cazalla!')
    print(f"Bienvenido {nombre} {apellido}")


saludo('Carlos', 'García')
saludo('Py')  # por defecto tomara de argumento el parametro de arriba
