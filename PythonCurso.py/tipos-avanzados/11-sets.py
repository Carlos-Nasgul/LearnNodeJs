# set = grupo o conjunto
primerSet = {1,  2,  3, 4, 5, 6, 9, 10}
# primerSet.add() o .remove() para añadir elements
segundoSet = [3, 4, 5, 7, 8]
segundoSet = set(segundoSet)
print(primerSet)
print(segundoSet)
print(primerSet | segundoSet)  # :da un set Une y elimina las repeticiones
print(primerSet & segundoSet)  # interseccion: da unset de las coincidencias
# diferencia: muestra los no coincidentes del primerset respecto del segundo
print(primerSet - segundoSet)
# diferencia Simetrica, eliminara los duplicados y solo dara los 'unicos'
print(primerSet ^ segundoSet)

if 5 in segundoSet:
    print('Its OK')
