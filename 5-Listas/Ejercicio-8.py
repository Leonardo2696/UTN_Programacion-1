# ejercicio 8
'''
Crear una matriz con las notas de 5 estudiantes en 3 materias.
● Mostrar el promedio de cada estudiante.
● Mostrar el promedio de cada materia.
'''
import random
datos = [['Lengua','Matematicas','Ingles'],
        ['alumno1','alumno2','alumno3','alumno4','alumno5'],
        []
        ]
promMateria = []
for m in range(len(datos)):
    print('          ',datos[0][m],end=' ')
print()
lengua =0
matematicas = 0
ingles = 0
for a in range(len(datos[1])):
    print(datos[1][a],end='        ')
    punt=0
    for p in range(0,3):
        datos[2].insert(p,random.randint(0,100))
        punt += datos[2][p]
        print('',datos[2][p],end='               ')
        if p == 0 :
            lengua += datos[2][p]
        elif p == 1:
            matematicas += datos[2][p]
        elif p == 2 :
            ingles += datos[2][p]
    print('Promedio:',round(punt/len(datos[0]),2))
    if a == 4 :
        promMateria.insert(0,lengua)
        promMateria.insert(1,matematicas)
        promMateria.insert(2,ingles)
        print('Pomedio: ',end=' ')
        for prom in range (len(promMateria)):
            print('    ',promMateria[prom]/len(datos[1]),end='          ')
