import random
# ejercicio 1
notas_alumnos = []
promedio = 0
for x in range (10):
    notas_alumnos.append(random.randint(1,100))
for i in range(len(notas_alumnos)):
    promedio += notas_alumnos[i]
print('Nota de los alumnos: ')
print(notas_alumnos)
print()
print(f'El promedio de todas las notas fue de : {promedio/(i+1)}')
notas_alumnos.sort()
print(f'La nota mas alta fue {notas_alumnos[i]}')
print(f'La nota mas baja fue {notas_alumnos[0]}')

