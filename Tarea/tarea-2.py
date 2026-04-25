# ventas = []

# from def_2 import *


# def cargar_venta():
#     print("\n--- Cargar nueva venta ---")

#     cliente = input("Nombre del cliente: ").strip()
#     if not cliente:
#         print("⚠ El nombre no puede estar vacío.")
#         return

#     productos_input = input("Productos comprados (separados por coma): ").strip()
#     if not productos_input:
#         print("⚠ Debe ingresar al menos un producto.")
#         return
#     productos = [p.strip() for p in productos_input.split(",") if p.strip()]
#     try:
#         total = float(input("Total de la compra ($): "))
#         if total < 0:
#             print("⚠ El total no puede ser negativo.")
#             return
#     except ValueError:
#         print("⚠ Total inválido. Ingrese un número.")
#         return

#     venta = (cliente, productos, total)  # tupla
#     ventas.append(venta)                 # lista
#     print(f"✓ Venta registrada para {cliente}.")
# def procesar_ventas(ventas):
#     clientes_unicos = set() # set
#     gastos_por_cliente = {} # diccionario
#     for cliente, productos, total in ventas:
#         clientes_unicos.add(cliente)
#         if cliente in gastos_por_cliente:
#             gastos_por_cliente[cliente] += total
#         else:
#             gastos_por_cliente[cliente] = total
#     return clientes_unicos, gastos_por_cliente
# def mostrar_resumen(ventas, clientes_unicos, gastos):
#     print("\nClientes únicos:")
#     print(clientes_unicos)
#     print("\nGastos por cliente:")
#     for cliente, total in gastos.items():
#         print(cliente, "->", total)
#     # cliente que más gastó
#     max_cliente = max(gastos, key=gastos.get)
#     print("\nCliente que más gastó:", max_cliente)
#     print("\nVentas mayores a 5000:")
#     for venta in ventas:
#         if venta[2] > 5000: # condicional
#             print(venta)
#     # Programa principal
#     ventas = cargar_ventas()
#     if len(ventas) > 0: # condicional
#         clientes, gastos = procesar_ventas(ventas)
#         mostrar_resumen(ventas, clientes, gastos)
#     else:
#         print("No se ingresaron ventas")
# def ver_cliente_unicos():
#     if not ventas:
#         print("No hay ventas cargadas")
#         return
#     clientes_unicos,_ = procesar_ventas()
#     print(f"clientes unicos ({len(clientes_unicos)}):")
#     for cliente in clientes_unicos:
#         print(f"- {cliente}")

# while True:
#     mostrar_menu()
#     eleccion = input('Ingrese una opcion del menu: ')
#     validar_opcion(eleccion)
#     match int(eleccion):
#         case 1:
#             lista_ventas = cargar_venta()
#             print(ventas)
#         case 2:
#             procesar_ventas(ventas)
#         case 3:
#             mostrar_resumen()
#         case 4:
#             pass
#         case 5:
#             pass
#         case 6:
#             pass
#         case 7:
#             pass
#         case 0:
#             print('Saliendo del programa')
#             break


ventas = []

def mostrar_menu():
    print("="*20)
    print("SISTEMA DE VENTAS")
    print("="*20)
    print("1. Cargar ventas")
    print("2. Motrar clientes unicos")
    print("3. Ver gastos por cliente")
    print("4. Ver cliente que mas gasto")
    print("5. Ver ventas mayores a $5000")
    print("6. ver resumen completo")
    print("0. salir")
    print("="*20)

def validar_opcion(menu):
    n = menu
    while not n.isdigit():
        mostrar_menu()
        n = input('Ingrese una opcion del menu: ')
    return n

def cargar_venta():
    print("\n--- Cargar nueva venta ---")

    cliente = input("Nombre del cliente: ").strip()
    if not cliente:
        print(" El nombre no puede estar vacío.")
        return

    productos_input = input("Productos comprados (separados por coma): ").strip()
    if not productos_input:
        print("Debe ingresar al menos un producto.")
        return
    productos = [p.strip() for p in productos_input.split(",")]
    try:
        total = float(input("Total de la compra ($): "))
        if total < 0:
            print(" El total no puede ser negativo.")
            return
    except ValueError:
        print("Total inválido. Ingrese un número.")
        return

    venta = (cliente, productos, total)  # tupla
    ventas.append(venta)                 # lista
    print(f"✓ Venta registrada para {cliente}.")

def procesar_ventas():
    clientes_unicos = set()       # set
    gastos_por_cliente = {}       # diccionario

    for cliente, productos, total in ventas:
        clientes_unicos.add(cliente)
        if cliente in gastos_por_cliente:
            gastos_por_cliente[cliente] += total
        else:
            gastos_por_cliente[cliente] = total
    return clientes_unicos, gastos_por_cliente

def ver_cliente_unicos():
    if not ventas:
        print("No hay ventas cargadas")
        return
    clientes_unicos,_ = procesar_ventas()
    print(f"clientes unicos ({len(clientes_unicos)}):")
    for cliente in clientes_unicos:
        print(f"- {cliente}")

def ver_gastos_clientes():
    if not ventas:
        print("No hay ventas cargadas")
        return
def cliente_gasto_mas (carro):
    print(carro[0])
    pass
while True:
    mostrar_menu()
    eleccion = input('Ingrese una opcion del menu: ').strip()
    match validar_opcion(eleccion):
        case 1:
            cargar_venta()
        case 2:
            ver_cliente_unicos()
        case 3:
            ver_gastos_clientes()
        case 4: # cliente que mas gasto
            cliente_gasto_mas(ventas)
            pass
        case 5:
            pass
        case 6:
            pass
        case 7:
            pass
        case 0:
            print('Saliendo del programa')
            break