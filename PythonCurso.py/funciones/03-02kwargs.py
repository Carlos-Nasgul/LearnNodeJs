# KeyWords arguments

def get_product(**datos):  # con doble asterico hago multiples argumentos pero obligatoriamt**
    # al [explicitar id] pues devuelve valor id soloamt
    print(datos["id"], datos['name'])
# si añado mas datos[] pues imprime esos


# TENGO QUE DAR NOMBRE AL LLAMADO DE LA FUNCION con id= no solo'id'
get_product(id='1',
            name='Carlos')  # lo que devuelve en Terminal
# se llama DICCIONARIO {'id' : 'id'}<--Diccionario
