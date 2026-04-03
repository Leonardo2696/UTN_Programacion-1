# ejercicio 4
'''
Dada una lista con valores repetidos:
● Crear una nueva lista sin elementos repetidos.
● Mostrar el resultado.
'''
datos = [1,3,5,3,7,1,9,5,3]
numeros_que_no_repiten = []
for i in range(len(datos)):
    cont= 0
    for j in range(len(datos)):
        if datos[i] == datos[j]:
            cont += 1
    if cont == 1:
        numeros_que_no_repiten.append(datos[i])
print(f'Lista de datos: {datos}')
print(f'Lista de los que no se repiten: {numeros_que_no_repiten}')
