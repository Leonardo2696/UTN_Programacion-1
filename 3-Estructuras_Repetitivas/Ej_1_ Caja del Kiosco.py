
nombre_cliente = input('Ingrese su nombre: ')
while not nombre_cliente.isalpha():
    print('Error: tiene que ser letras')
    nombre_cliente = input()
    print('')
print(f'Hola {nombre_cliente}')
print('')
cantidad_productos = input('Cantidad de articulos ingresados: ')
while not cantidad_productos.isdigit() or (int(cantidad_productos) <= 0):
    print('Tiene que ser un numero positivo mayor a 0')
    cantidad_productos = input('Cuantos productos quiere ingresar: ')
    print('')

total_sin_descuento = 0
total_con_descuento = 0
ahorro = 0
for i in range (int(cantidad_productos)):
    precio = input(f'Ingrese el precio del producto {i + 1}: ')
    while not precio.isdigit() or int(precio) <= 0:
        print('Tiene que ser un numero entero: ')
        precio = input(f'Ingrese el precio del preducto {i + 1}: ')
        print('')
    descuento = input(f'El producto {i + 1} tiene descuento: S/N ').upper()
    print('')
    while not descuento.isalpha() or (descuento != 'S') and (descuento != 'N'):
        print('Tiene que ser una opcion valida: S/N ')
        descuento = input(f'El producto {i + 1} tiene descuento: S/N ')
        print('')
    if descuento == 'N':
        total_sin_descuento += int(precio)
    elif descuento == 'S':
        total_sin_descuento += int(precio)
        ahorro += (float(precio) * 0.1)
    total_con_descuento = (float(total_sin_descuento - ahorro))
    print(f'Producto {i + 1} - Precio: {precio} - Descuento (S/N): {descuento}')
    print('')
print(f'Total sin descuentos: ${total_sin_descuento}')
print(f'Total con descuentos: ${total_con_descuento:.2f}')
print(f'Ahorrado: ${ahorro}')
print(f'Promedio por producto: ${total_con_descuento / int(cantidad_productos):.2f}')