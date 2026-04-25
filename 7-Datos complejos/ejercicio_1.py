from def_tp7 import *
# 1)
precios_frutas = {'Banana': 1200, 'Ananá': 2500, 'Melón': 3000, 'Uva':1450}
precios_frutas.update({'Naranja': 1200,'Manzana': 1500,'Pera': 2300})

# 2)
precios_frutas['Banana'] = 1330
precios_frutas['Manzana'] = 1700
precios_frutas['Melón'] = 2800

# 3)
lista_frutas = list(precios_frutas)

# 4) Escribí un programa que permita almacenar y consultar números telefónicos.  
# • Permití al usuario cargar 5 contactos con su nombre como clave y número como valor.  
# • Luego, pedí un nombre y mostrale el número asociado, si existe.
contactos = dict()
for i in range(3):
    nombre = verificar_str(input('Ingrese un nombre: ').capitalize().strip())
    if nombre in contactos:
        nombre = dato_en_list(nombre,contactos,'Ingrese un nombre valido: ')
    numero = validar_N(input('Ingrese el numero telefonico: ').strip())
    print()
    numero = dato_en_list(numero,contactos.values(),'Ingrese un numero valido: ')
    # while numero in contactos.values():
    #     print('Ese numero ya existe con un contacto')
    #     numero = validar_N(input('Ingrese el numero telefonico: ').strip())
    #     print()
    contactos.update({nombre:numero})
print()
print(contactos)
