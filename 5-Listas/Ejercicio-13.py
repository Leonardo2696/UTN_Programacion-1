# ejercicio 13
'''
Dada la siguiente lista de puntajes de un videojuego:
puntajes = [450, 1200, 875, 990, 300, 1500, 640]
● Mostrar el puntaje más alto y el más bajo.
● Mostrar la lista ordenada de mayor a menor (ranking).
● Indicar en qué posición del ranking se encuentra el puntaje 990.
'''
puntajes = [450, 1200, 875, 990, 300, 1500, 640]
print()
rank = sorted(puntajes)
rank.reverse()
print('===RANKING===')
for i in range(len(puntajes)):
    print(f'  {i+1}: {rank[i]}')
print(f'El puntaje "990" se encuentra en el puesto: {puntajes.index(990)}')
puntajes_ordenado = sorted(puntajes)
print(f'El puntaje mas alto es: {puntajes_ordenado[-1]}')
print(f'El puntaje mas bajo es: {puntajes_ordenado[0]}')