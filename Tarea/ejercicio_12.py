from fdc_12 import *
estudiantes = cargar_archivo()
while True:
    mostrar_menu()

    opcion = input('Ingrese una opcion: ')

    match opcion:
        case '1':
            estudiantes = agregar_estudiante(estudiantes)
        case '2':
            mostrar_estudiante(estudiantes)
        case '3':
            estudiantes = guardar_archivo(estudiantes)
        case '4':
            estadisticas(estudiantes)
        case '5':
            print('Saliendo')
            break
        case _:
            print('No es valido la eleccion')