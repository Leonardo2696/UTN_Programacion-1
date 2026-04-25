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
    return int(n)