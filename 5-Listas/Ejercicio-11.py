# ejercicio 11
'''
Crear una lista con los nombres de 10 estudiantes.
● Solicitar al usuario que ingrese un nombre a buscar.
● Indicar si el nombre se encuentra en la lista.
● Mostrar la posición en la que aparece.
● Si no se encuentra, informar que no está en la lista
'''
lista_estudiantes = ['Raul','Leonardo','Javier','Maria','Yamila','Kevin','Angel','Jorge','Marta','Axel']
while True:
    nombre_buscar = input('Ingrese el nombre del alumno: ').strip().capitalize()
    while not nombre_buscar.isalpha():
        print('Error')
        nombre_buscar = input('Ingrese el nombre del alumno: ').strip().capitalize()
    if nombre_buscar in lista_estudiantes:
        print(f'El alumno {nombre_buscar} se encuentra en la posicion {lista_estudiantes.index(nombre_buscar)}')
    else:
        print(f'El nombre ingresado no esta en la lista')