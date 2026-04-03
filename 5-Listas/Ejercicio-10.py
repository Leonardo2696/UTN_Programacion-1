# ejercicio 10
'''
Una tienda registra las ventas de 4 productos durante 7 días, en una matriz de 4x7.
● Mostrar el total vendido por cada producto.
● Mostrar el día con mayores ventas totales.
● Indicar cuál fue el producto más vendido en la semana.

'''
dias = ['Lunes','Martes','Miercoles','Jueves','Viernes','Sabado','Domingo']
productos = [['Agujas '],['Suero  '],['Gasa   '],['Guantes']]
for i in range (len(dias)):
    print('            ',dias[i],end=' ')
print()
producto = 0
for j in range(len(productos)):
    total = 0
    print(productos[j][0],end=':....... ')
    for q in range(len(dias)):
        productos[j].insert(len(productos[0]),random.randint(0,10))
        total += productos[j][q+1]
        print(end=f'{productos[j][q+1]} ..................')
    if total > producto:
        producto = total
        prodMasVendido = productos[j][0]
    print(f'ventas totales:{total}')
semanal = 0
for s in range (len(dias)):
    totalS = 0
    for S in range (len(productos)):
        totalS+= productos[S][s+1]
    if totalS > semanal :
        semanal = totalS
        dia = dias[s]
print(f'Dia con mayor ventas totales fue: {dia}')
print(f'El producto mas vendido en la semana fue: {prodMasVendido}')