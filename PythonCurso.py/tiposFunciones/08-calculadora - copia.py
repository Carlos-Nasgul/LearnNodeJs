n1 = input('Ingrese primer número ')
n2 = input('Ingrese segundo número ')

n1 = int(n1)
n2 = int(n2)

# print(n1, n2) # si intento sumar
# hay que insertar int(), para que haga operac.

suma = n1 + n2
resta = n1 - n2
multi = n1 * n2
div = n1 / n2

mensaje = f"""
Para los números {n1} y {n2},
el resultado de la suma es {suma}
el resultado de la resta es {resta}
el resultado de la multiplicación es {multi}
el resultado de la division es {div}
"""
print(mensaje)
