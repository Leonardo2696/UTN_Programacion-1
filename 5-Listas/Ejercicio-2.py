# ejercicio 2
'''
Pedir al usuario que cargue 5 productos en una lista.
● Mostrar la lista ordenada alfabéticamente. Investigue el uso del método sorted().
● Preguntar al usuario qué producto desea eliminar y actualizar la lista.
'''
lista_productos = []
while True:
    print('--------LISTA DE COMPRAS--------')
    print('1.Agregar        2.Quitar        3.Mostrar lista ordenada        4.Salir')
    eleccion = input('Elija una opcion: ')
    print()
    while not eleccion.isdigit():
        print('Error: tiene que ser un numero')
        print('--------LISTA DE COMPRAS--------')
        print('1.Agregar        2.Quitar        3.Salir')
        eleccion = input('Elija una opcion: ')
        print()
    match int(eleccion):
        case 1:
            if len(lista_productos) < 5:
                print('Escriba que quiere agregar a la lista de compras')
                producto = input().capitalize().strip()
                while not producto.isalpha():
                    print('Error: tiene que ser solo letras')
                    print('Escriba que quiere agregar a la lista de compras')
                    producto = input().capitalize().strip()
                lista_productos.append(producto.capitalize())
                print()
            else:
                print('Lista llena')
                print()
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
                print()
            else:
                print('No hay productos que sacar')
                print()
        case 3:
            lista_ordenada = sorted(lista_productos)
            print(lista_ordenada)
            print()
        case 4:
            print('Adios')
            break
        case _:
            print('Eleccion no disponible')
