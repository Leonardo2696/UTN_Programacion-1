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

# 4)
# contactos = dict()
# for i in range(2):
#     nombre = verificar_str(input('Ingrese un nombre: ').capitalize().strip())
#     nombre = dato_en_list(nombre,contactos,'Ingrese un nombre valido: ')
#     numero = verificar_int(input('Ingrese el numero telefonico: ').strip())
#     print()
#     numero = dato_en_list(numero,contactos.values(),'Ingrese un numero valido: ')
#     contactos.update({nombre:numero})
# print()
# while True:
#     print('='*5,'Directorio','='*5)
#     nom_a_buscar = verificar_str(input('Ingrese el nombre a buscar: ').capitalize().strip())
#     print()
#     if nom_a_buscar in contactos:
#         print(f'Usuario: {nom_a_buscar} ---> Contacto: {contactos[nom_a_buscar]}')
#     else:
#         print('No se encontro el usuario en el Directorio.')
#     print('Buscar otro nombre? (N--salir / S--continuar)')
#     s_n = verificar_str(input('>>').upper().strip())
#     while s_n != 'N' and s_n != 'S':
#         print(f'"{s_n}"No es parte de la opcion')
#         print('Buscar otro nombre? (N--salir / S--continuar)')
#         s_n = verificar_str(input('>>').upper().strip())
#     if s_n == 'N':
#         print('Saliendo')
#         break
#     elif s_n == 'S':
#         continue

# 5)
# frase = input('Ingrese una frase: ')
# palabras = list(frase.split())
# recuento = {}
# for p in palabras:
#     mas_repite = palabras.count(p)
#     palabla_mas_repetirda = p
#     recuento.update({palabla_mas_repetirda:mas_repite})
# palabras_unicas = set(palabras)
# print(f'Palabras unicas: {palabras_unicas}')
# print(f'Recuento: {recuento}')

# 6) Permití ingresar los nombres de 3 alumnos, y para cada uno una tupla de 3 notas. Luego, 
# mostrá el promedio de cada alumno.  
alumnos = dict()
for i in range(3):
    alumno = verificar_str(input('Ingrese el nombre del alumno: ').capitalize().strip())
    alumno = dato_en_list(alumno,alumnos,'Ingrese el nombre del alumno: ')
    a = verificar_int(input(f'Ingrese las notas de {alumno}: '))
    b = verificar_int(input(f'Ingrese las notas de {alumno}: '))
    c = verificar_int(input(f'Ingrese las notas de {alumno}: '))
    notas = (a,b,c)
    alumnos.update({alumno : notas})
print(alumnos)
total = 0
for nota in alumnos.values():
    for n in nota:
        total += n
    print(f'{total}')