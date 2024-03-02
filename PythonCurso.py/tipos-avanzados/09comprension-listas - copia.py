usuarios = [[5, 'Carlitos'], [1, 'Flori'], [32, 'Michel'], [2, 'Paco']]
# vamos a pasar de una lista de usuariols a un alista de nombrees

# nombres = []
# for usuario in usuarios:
# nombres.append(usuario[1])#si le paso [0] me dara el primer objeto, con [1]me da el 2ºobject


# nombres = [usuario[1] for usuario in usuarios]#-->·MANERA CORTA Y ELEGANTE·<--
# AHORA A FILTRAR LA LISTA nombrelista=  [expresion for item in items] + if usuario[0]>X
nombres = [usuario[1] for usuario in usuarios if usuario[0] > 4]
print(nombres)
