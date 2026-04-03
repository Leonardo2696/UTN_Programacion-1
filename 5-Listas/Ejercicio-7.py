# ejercicio 7
'''
Crear una matriz (lista anidada) de 7x2 con las temperaturas mínimas y máximas de
una semana.
● Calcular el promedio de las mínimas y el de las máximas.
● Mostrar en qué día se registró la mayor amplitud térmica.
'''
import random
dias = ['Lunes','Martes','Miercoles','Jueves','Viernes','Sabado','Domingo']
temperaturas = [[],[]]
for i in range(len(dias)):
    temp_mañana = random.randint(0,40)
    temp_tarde = random.randint(0,40)
    if temp_mañana < temp_tarde:
        temperaturas[0].append(temp_mañana)
        temperaturas[1].append(temp_tarde)
    else:
        temperaturas[1].append(temp_mañana)
        temperaturas[0].append(temp_tarde)
print(temperaturas)
mayor_registro = 0
for t in range(len(dias)):
    print('           ',dias[t],end=' ')
print()
for j in range(2):
    if j == 0:
        print('temp min',end='')
    else:
        print('temp max',end='')
    for x in range(len(dias)):
        if j == 0:
            print('     ',temperaturas[j][x],'°',end='          ')
        else:
            print('     ',temperaturas[j][x],'°',end='          ')
            if mayor_registro < temperaturas[j][x]:
                mayor_registro = temperaturas[j][x]
                dia = dias[x]
    print()
print(f'El dia con mayor temperatura fue {dia}, con: {mayor_registro}°')
