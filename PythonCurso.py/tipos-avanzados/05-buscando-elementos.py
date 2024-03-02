mascotas = ['Perro', 'Snoopy', 'Tobby', 'Gordo', 'Turko', 'Pulga']

print(mascotas.index('Pulga'))  # me da el indice
# pero si quierpo saber cuantas 'Pulga' hay...
# UTILIZARE .count('metodo')
print(mascotas.count('Pulga'))
print(mascotas[4])
if 'Perro' in mascotas:
    print(mascotas.index('Perro'))
