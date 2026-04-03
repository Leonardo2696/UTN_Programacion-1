# ejercicio 5
'''
Crear una lista con los nombres de 8 estudiantes presentes en clase.
● Preguntar al usuario si quiere agregar un nuevo estudiante o eliminar uno existente.
● Mostrar la lista final actualizada.
'''
alumnos = ['Juan','Gabriel','Lucia','Angel','Yamila','Martin','Kevin','Jorge']
while True:
    print('Seleccione una opcion: ')
    print('1.Agregar un alumno      2.Quitar un alumno')
    eleccion = input()
    print()
    while not eleccion.isdigit():
        print('Error: tiene que ser un numero')
        print('Seleccione una opcion: ')
        print('1.Agregar un alumno      2.Quitar un alumno')
        eleccion = input()
        print()
    if int(eleccion) == 1:
        print('Ingrese el nombre del alumno: ')
        alumno = input().capitalize().strip()
        while not alumno.isalpha():
            print('Error: tiene que ser un nombre')
            print('Ingrese el nombre del alumno: ')
            alumno = input().capitalize().strip()
        alumnos.append(alumno)
        print()
    elif int(eleccion) == 2:
        print('Cual alumno quiere sacar de la lista')
        for i in range(len(alumnos)):
            print(f'{i+1}. {alumnos[i]}')
        eleccion = input()
        while not eleccion.isdigit():
            print('Error: tiene que ser un numero')
            print('Cual alumno quiere sacar de la lista')
            for i in range(len(alumnos)):
                print(f'{i+1}. {alumnos[i]}')
            eleccion = input()
        alumnos.remove(alumnos[int(eleccion)-1])
        print()
    print('Lista de alumnos: ')
    for i in range(len(alumnos)):
        print(f'{i+1}. {alumnos[i]}')
