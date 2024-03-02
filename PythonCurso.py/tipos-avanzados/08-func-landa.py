usuarios = [['Carlitos', 5], ['Flori', 1], ['Michel', 32], ['Paco', 2]]


# def ordena(elemento):
#   return elemento[1]

# LAMBDA ES UNA FUN ANÓNIMA Y NO PODEMOS LLENAR EL CÓDIGO,
# LA USAREMOS UNA ÚNICA VEZ
# usuarios.sort(key=lambda parametros : valorRetorno)
usuarios.sort(key=lambda el: el[1])
print(usuarios)
