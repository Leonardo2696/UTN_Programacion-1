#1. Mostrar el promedio de cada estudiante  
#2. Mostrar el estudiante con mejor promedio  
#3. Mostrar los estudiantes aprobados (promedio >= 6)  
#4. Crear una lista de tuplas con este formato: 
#Y ordenarla por promedio de mayor a menor.

estudiantes = { 
    "Luis": [6, 7, 5], 
    "Marta": [10, 9, 9],
    "Ana": [7, 8, 9]
} 
alumno = ''
mejor_promedio = 0
for nombre, notas in estudiantes.items():
    promedio = 0
    for i in range(len(notas)):
        promedio += notas[i]
    print(f'{nombre} tiene promedio de: {promedio/len(notas):.01f}')
    if (promedio) > mejor_promedio:
        alumno = nombre
        mejor_promedio = promedio
        total = mejor_promedio/len(notas)
    if (promedio/len(notas)) >= 6:
        aprobados = list(alumno)
print(f'El mejor promedio es: {total:.01f}, que lo tiene: {alumno}')
print(aprobados)