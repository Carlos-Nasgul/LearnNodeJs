# agrengando elem a una list y eliminando
mascotas = ['Wolfgang',
            'Pelusa',
            'Pulga',
            'Pulga',
            'Gordo',
            'Turko',
            'Lassie'
            ]

mascotas.insert(1, 'Snoopy')  # .insert inserta en el indice
# indicado el elemento que quieras incluir
mascotas.append('Rambo')  # lo añade añ final de la lista


mascotas.remove('Pulga')  # elimina el elemnto
mascotas.pop()  # elimina el ultimo siu le añado un indice
del mascotas[2]
mascotas.clear()
print(mascotas)
