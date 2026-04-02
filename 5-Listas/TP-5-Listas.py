# import random
# # ejercicio 1
# notas_alumnos = []
# promedio = 0
# for x in range (10):
#     notas_alumnos.append(random.randint(1,100))
# for i in range(len(notas_alumnos)):
#     promedio += notas_alumnos[i]
# print('Nota de los alumnos: ')
# print(notas_alumnos)
# print()
# print(f'El promedio de todas las notas fue de : {promedio/(i+1)}')
# notas_alumnos.sort()
# print(f'La nota mas alta fue {notas_alumnos[i]}')
# print(f'La nota mas baja fue {notas_alumnos[0]}')

# ejercicio 2
'''
Pedir al usuario que cargue 5 productos en una lista.
● Mostrar la lista ordenada alfabéticamente. Investigue el uso del método sorted().
● Preguntar al usuario qué producto desea eliminar y actualizar la lista.

'''
lista_productos = []
while len(lista_productos)<4:
    print('--------LISTA DE COMPRAS--------')
    print('1.Agregar        2.Quitar        3.Mostrar lista ordenada        4.Salir')
    eleccion = input('Elija una opcion: ')
    while not eleccion.isdigit():
        print('Error: tiene que ser un numero')
        print('--------LISTA DE COMPRAS--------')
        print('1.Agregar        2.Quitar        3.Salir')
        eleccion = input('Elija una opcion: ')
    match int(eleccion):
        case 1:
            print('Escriba que quiere agregar a la lista de compras')
            producto = input()
            while not producto.isalpha():
                print('Error: tiene que ser solo letras')
                print('Escriba que quiere agregar a la lista de compras')
                producto = input()
            lista_productos.append(producto.capitalize())
        case 2:
            if len(lista_productos)>0:
                print('Elija que prducto quiere sacar: ')
                for i in range(len(lista_productos)):
                    print(f'{i+1}.{lista_productos[i]}')
                quitar = input()
                while not quitar.isdigit() or (int(quitar)<=0) or (int(quitar)>=(len(lista_productos)+1)):
                    print('Error: tiene que ser algo de la lista')
                    print('Elija que prducto quiere sacar: ')
                    for i in range(len(lista_productos)):
                        print(f'{i+1}.{lista_productos[i]}')
                    quitar = input()
                quitar_lista = int(quitar)
                lista_productos.remove(lista_productos[quitar_lista-1])
            else:
                print('No hay productos que sacar')
        case 3:
            lista_ordenada = sorted(lista_productos)
            print(lista_ordenada)
        case 4:
            break
        case _:
            break
print('La lista final quedo lista: ')
print(lista_productos)
# ejercicio 3
'''
Generar una lista con 15 números enteros al azar entre 1 y 100.
● Crear una lista con los pares y otra con los impares.
● Mostrar cuántos números tiene cada lista.

'''
# ejercicio 4
'''
Dada una lista con valores repetidos:
● Crear una nueva lista sin elementos repetidos.
● Mostrar el resultado
'''
# ejercicio 5
'''
Crear una lista con los nombres de 8 estudiantes presentes en clase.
● Preguntar al usuario si quiere agregar un nuevo estudiante o eliminar uno existente.
● Mostrar la lista final actualizada.

'''
# ejercicio 6
'''
Dada una lista con 7 números, rotar todos los elementos una posición hacia la derecha
(el último pasa a ser el primero).
'''
# ejercicio 7
'''
Crear una matriz (lista anidada) de 7x2 con las temperaturas mínimas y máximas de
una semana.
● Calcular el promedio de las mínimas y el de las máximas.
● Mostrar en qué día se registró la mayor amplitud térmica.

'''
# ejercicio 8
'''
Crear una matriz con las notas de 5 estudiantes en 3 materias.
● Mostrar el promedio de cada estudiante.
● Mostrar el promedio de cada materia
'''
# ejercicio 9
'''
Representar un tablero de Ta-Te-Ti como una lista de listas (3x3).
● Inicializarlo con guiones "-" representando casillas vacías.
● Permitir que dos jugadores ingresen posiciones (fila, columna) para colocar "X" o "O".
● Mostrar el tablero después de cada jugada.

'''
# ejercicio 10
'''
Una tienda registra las ventas de 4 productos durante 7 días, en una matriz de 4x7.
● Mostrar el total vendido por cada producto.
● Mostrar el día con mayores ventas totales.
● Indicar cuál fue el producto más vendido en la semana.

'''
# ejercicio 11
'''
Crear una lista con los nombres de 10 estudiantes.
● Solicitar al usuario que ingrese un nombre a buscar.
● Indicar si el nombre se encuentra en la lista.
● Mostrar la posición en la que aparece.
● Si no se encuentra, informar que no está en la lista
'''
# ejercicio 12
'''
Pedir al usuario que ingrese 8 números enteros y almacenarlos en una lista.
● Mostrar la lista original.
● Mostrar la lista ordenada de menor a mayor.
● Mostrar la lista ordenada de mayor a menor.
● Investigar el uso de sorted() y del parámetro reverse.

'''
# ejercicio 13
'''
Dada la siguiente lista de puntajes de un videojuego:
puntajes = [450, 1200, 875, 990, 300, 1500, 640]
● Mostrar el puntaje más alto y el más bajo.
● Mostrar la lista ordenada de mayor a menor (ranking).
● Indicar en qué posición del ranking se encuentra el puntaje 990.
'''