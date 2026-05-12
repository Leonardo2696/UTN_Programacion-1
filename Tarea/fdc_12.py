import csv
def mostrar_menu():
    print('''
================ MENU =====================
1. Registrar estudiante
2. Mostrar estudiantes
3. Guardar archivo
4. Estadisticas
5. Salir''')

def cargar_archivo():
    lista = dict()
    try:
        with open('asistencia.csv','r',encoding='utf-8') as archivo:
            lector = csv.DictReader(archivo)
            for fila in lector:
                lista.update({
                    'nombre':fila['nombre'],
                    'edad':int(fila['edad']),
                    'presente':fila['presente']
                })
    except PermissionError:
        print('No tiene permiso de uso')
    except FileNotFoundError:
        print('Error, el archivo no existe')

def agregar_estudiante(lista):
    try:
        nombre = input('Ingrese el nombre del estudainte: ').lower()
        edad = int(input('Ingrese la edad del estudiande: '))
        presente = input('Ingrese si / no para asistencia: ').lower()

        nvo_estudiante = {
            'nombre' : nombre,
            'edad': edad,
            'presente': presente
        }

        lista.update(nvo_estudiante)
    except ValueError:
        print('Debe ingresar un numero entero')
    return lista

def mostrar_estudiante(lista):
    for est in lista:
        print(f'Nombre: {est['nombre']}')
        print(f'Edad: {est['edad']}')
        print(f'Presente: {est['presente']}')
        print()

def guardar_archivo(lista):
    try:
        with open('asistencia.csv','w',newline='',encoding='utf-8') as archivo:
            writer = csv.DictWriter(archivo, fieldnames=['nombre','edad','presente'])
            writer.writeheader
            writer.writerow(lista)
    except FileExistsError:
        print('El archivo no existe')
    except PermissionError:
        print('El archivo esta ocupado con otro programa')

def estadisticas(lista):
    print(f'Total de alumnos: {len(lista)}')
    presente = 0
    suma_edad = 0
    for est in lista:
        suma_edad += est['edad']

        if(est['presente']) == 'si':
            presente += 1
    try: 
        print(f'El total de estudiantes presentes es: {presente}')
        print(f'El total de estudiantes ausentes es: {presente - len(lista)}')
        print(f'Promedio de edad de las lista es: {(suma_edad / len(lista))}:.2f')
    except ZeroDivisionError:
        print('No se puede dividir por 0')