# saludo = 'Bienvenido a la super calculadora'
# print(saludo)
# operacion = 'suma', 'resta', 'multi', 'div'

# n1 = input('Ingrese nº ')
# n2 = input('Operación  ')
# n3 = input('Segundo nº ')

# for suma in operacion:
# suma = n1 + n3
# print(f"{suma}")
# for resta in operacion:
# resta = n1 - n3
# print(f"{resta}")
# for multi in operacion:

# multi = n1 * n3
# print(f"{multi}")
# for div in operacion:
# div = n1 / n3
# print(f"{div}")


# operacion = " "
# while True:
# operacion.lower == "salir"
# break

# print(resultado)

# SOLUCION 2º31'
print('Bienvenido a la super \'calculator\'')
print('Para salir escriba: salir ')
print('Las operaciones son: suma, resta, multi y div.')

resultado = ""

while True:
    if not resultado:
        resultado = input('Ingrese un número: ')
        if resultado.lower() == 'salir':
            break

    resultado = int(resultado)
    operacion = input('Ingrese operacion: ')
    if operacion.lower() == 'salir':
        break
    n2 = input('Ingrese el segundo número: ')
    if n2.lower() == 'salir':
        break
    n2 = int(n2)

    if operacion.lower() == 'suma':
        resultado += n2
    elif operacion.lower() == 'resta':
        resultado -= n2
    elif operacion.lower() == 'multi':
        resultado *= n2
    elif operacion.lower() == 'div':
        resultado /= n2
    else:
        print('Error no definido')
        break

    print(f"el resultado es: {resultado}")
