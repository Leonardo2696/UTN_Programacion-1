'''1.Carga Inicial de Libros: 
2
3.
4.
5.
6.
7.
8.Salir: Finalizar el programa.'''
libros = []
ejemplares = []
while True:
    print('''
    ===== MENU =====
    1. Cargar Libros
    2. Cargar ejemplares
    3. Mostrar catalogo
    4. Buscar titulo
    5. Reporte de critico
    6. Adquirir nuevo titulo
    7. Prestamo / Devolucion
    8. Salir
    ''')
    opc_menu = input('>>')
    while not opc_menu.isdigit():
        print('Error: tiene que ser un numero')
        print('''
        ===== MENU =====
        1. Cargar Libros
        2. Cargar ejemplares
        3. Mostrar catalogo
        4. Buscar titulo
        5. Reporte de critico
        6. Adquirir nuevo titulo
        7. Prestamo / Devolucion
        8. Salir
        ''')
        opc_menu = input('>>')
    match int(opc_menu):
        case 1: #Solicitar al usuario la cantidad de títulos a ingresar. Validar que el nombre no esté vacío ni duplicado. Si el dato es erróneo, reintentar hasta completar la cantidad pedida
            print('Ingrese cuantos libros quiere ingresar')
            cant_libros = input('>>')
            while not cant_libros.isdigit():
                print('Error. Tiene que ser un numero valido')
                print('Ingrese cuantos libros quiere ingresar')
                cant_libros = input('>>')
            for i in range(int(cant_libros)):
                print('Ingrese el titulo del libro')
                nom_libro = input('>> ').strip().capitalize()
                while not nom_libro.replace(' ','').isalpha():
                    print('Error. Tiene que ser un nombre valido')
                    print('Ingrese el titulo del libro')
                    nom_libro = input('>> ').strip().capitalize()
                while nom_libro in libros:
                    print(f'El titulo {nom_libro}, ya esta en la biblioteca')
                    print('Ingrese el titulo del libro')
                    nom_libro = input('>> ').strip().capitalize()
                libros.append(nom_libro)
                ejemplares.append(0)
            for x in range(len(libros)):
                print(f'Se ha cargado el libro: {libros[x]}')
        case 2: #.Carga de Ejemplares: Para cada libro cargado en la opción 1, solicitar la cantidad de copias disponibles. Se debe mostrar el nombre del libro mientras se pide el número.
            if not libros:
                print('No se han cargados libro. Ingrese en la opcion 1 del menu')
            else:
                for i in range(len(libros)):
                    print(f'Ingrese la cantidad de ejemplares de {libros[i]}')
                    cant_ejemplares = input('>>')
                    while not cant_ejemplares.isdigit():
                        print('Error. Tiene que ser un numero valido')
                        print(f'Ingrese la cantidad de ejemplares de {libros[i]}')
                        cant_ejemplares = input('>>')
                    ejemplares[i] = int(cant_ejemplares)
        case 3:#Mostrar Catálogo: Listar todos los libros con sus respectivos ejemplares.
            if not libros:
                print('No se han cargados libro. Ingrese en la opcion 1 del menu')
            else:
                for i in range(len(libros)):
                    if ejemplares[i] == 0:
                        print(f'{libros[i]} <---> "Sin Stock"')
                    else:
                        print(f'{libros[i]} <---> {ejemplares[i]}')
        case 4:#Buscar Libro: El usuario ingresa un título y el sistema informa cuántos ejemplares hay. Si no existe, avisar al usuario.
            if not libros:
                print('No se han cargados libro. Ingrese en la opcion 1 del menu')
            else:
                print('Ingrese el tiulo a buscar: ')
                busqueda = input('>>').capitalize().strip()
                while not busqueda.replace(' ','').isalpha():
                    print('Error. Titulo invalido')
                    print('Ingrese el tiulo a buscar: ')
                    busqueda = input('>>').capitalize().strip()
                if busqueda in libros:
                    if ejemplares[libros.index(busqueda)] == 0:
                        print(f'{libros[i]} <---> "Sin Stock"')
                    else:
                        print(f'{busqueda} <---> {ejemplares[libros.index(busqueda)]}')
        case 5:#Reporte de Críticos: Listar solo los libros que tengan menos de 2 ejemplares (stock crítico).
            if not libros:
                print('No se han cargados libro. Ingrese en la opcion 1 del menu')
            else:
                for i in range(len(libros)):
                    if ejemplares[i] == 0:
                        print(f'{libros[i]} <---> "Sin Stock"')
                    elif ejemplares[i] > 0 and ejemplares[i] < 3:
                        print(f'{libros[i]} <---> "Stock Critico"')
        case 6:#Adquirir Nuevo Título: Permitir agregar un (1) solo libro nuevo al final de las listas con su stock inicial. Validar: nombre no vacío, no duplicado y stock no negativo. Si falla, volver al menú informando el error.
            nuevo_libro = input('Ingrese el titulo a ingresar: ').strip().capitalize()
            while not nuevo_libro.replace(' ','').isalpha():
                print('Error. Tiene que ser un nombre valido')
                nuevo_libro = input('Ingrese el titulo a ingresar: ').strip().capitalize()
            if nuevo_libro in libros:
                print('El titulo ya esta en la estanteria')
            else:
                cant_nuevo_ejemplar = input('Ingrese cantidad para el nuevo ejemplar: ')
                while not cant_nuevo_ejemplar.isdigit():
                    print('Error. Tiene que ser un numero valido')
                    cant_nuevo_ejemplar = input('Ingrese cantidad para el nuevo ejemplar: ')
                if cant_nuevo_ejemplar == 0:
                    print('No se puede cargar un libro con 0 ejemplares')
                else:
                    libros.append(nuevo_libro)
                    ejemplares.append(cant_nuevo_ejemplar)
        case 7:#Préstamo / Devolución: * Préstamo: Restar 1 unidad al stock (validar que haya al menos 1 disponible para prestar).Devolución: Sumar 1 unidad al stock por reingreso.
            if not libros:
                print('No se han cargados libro. Ingrese en la opcion 1 del menu')
            else:
                print('1.Prestamo           2.Devoluvion')
                eleccion = input('>>')
                while not eleccion.isdigit():
                    print('Error. tiene que ser un numero valido')
                    print('1.Prestamo           2.Devoluvion')
                    eleccion = input('>>')
                if int(eleccion) == 1:
                    prestamo = input('Ingrese el titulo a pedir: ').strip().capitalize()
                    while not prestamo.replace(' ','').isalpha():
                        print('Error. Tiene que ser un nombre valido')
                        prestamo = input('Ingrese el titulo a pedir: ').strip().capitalize()
                    if  prestamo in libros:
                        if ejemplares[libros.index(prestamo)] == 0:
                            print('No queda en Stock de este libro')
                        else:
                            ejemplares[libros.index(prestamo)] -= 1
                elif int(eleccion) == 2:
                    devolucion = input('Ingrese el titulo a devolver: ').strip().capitalize()
                    while not devolucion.replace(' ','').isalpha():
                        print('Error. Tiene que ser un nombre valido')
                        devolucion = input('Ingrese el titulo a devolver: ').strip().capitalize()
                    if  devolucion in libros:
                        ejemplares[libros.index(devolucion)] += 1
                    else:
                        print('El ejemplar que quiere ingresar no esta en el sistema')
                else:
                    print('El numero ingresado no es una opcion del menu')
        case 8:
            print('Saliendo del programa')
            break