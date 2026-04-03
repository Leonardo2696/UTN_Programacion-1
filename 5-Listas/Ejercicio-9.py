# ejercicio 9
'''
Representar un tablero de Ta-Te-Ti como una lista de listas (3x3).
● Inicializarlo con guiones "-" representando casillas vacías.
● Permitir que dos jugadores ingresen posiciones (fila, columna) para colocar "X" o "O".
● Mostrar el tablero después de cada jugada.
'''
lineas = [[],[],[]]
r = 0
for i in range (len(lineas)):
    for j in range (len(lineas)):
        lineas[i].insert(j,'-')
        print(lineas[i][j],end=' ')
    print()

while r < 9 :
    print('-------------------')
    jugada_valida = False
    while not jugada_valida:
        if r % 2 == 0:
            print('Estas jugando con X')
            lx = int(input('Ingrese la linea (0-2): '))
            cx = int(input('Ingrese la clumna (0-2): '))
            jugador = 'X'
            if 0 <= lx < 3 and 0 <= cx < 3 and lineas[lx][cx] == '-':
                lineas[lx][cx] = 'X'
                jugada_valida = True
            else :
                print('Posicion invalida, vuelva a intentar: ')
                print()
        else :
            print('Estas jugando con O')
            lo = int(input('Ingrese la linea (0-2): '))
            co = int(input('Ingrese la clumna (0-2): '))
            jugador = 'O'
            if 0 <= lo < 3 and 0 <= co < 3 and lineas[lo][co] == '-':
                lineas[lo][co] = 'O'
                jugada_valida = True
            else :
                print('Posicion invalida, vuelva a intentar: ')
                print()
    for q in range(len(lineas)):
        for f in range(len(lineas)):
            print(lineas[q][f],end=' ')
        print()
    ganador = None
    if r >= 2:
        if lineas[0][0] == lineas[0][1] == lineas[0][2] or \
        lineas[1][0] == lineas[1][1]== lineas[1][2] or \
        lineas[2][0] == lineas[2][1] == lineas[2][2] or \
        lineas[0][0] == lineas[1][0] == lineas[2][0] or\
        lineas[0][1] == lineas[1][1] == lineas[2][1] or\
        lineas[0][2] == lineas[1][2] == lineas[2][2] or \
        lineas[0][0] == lineas[1][1] == lineas[2][2] or \
        lineas[0][2] == lineas[1][1] == lineas[2][0] :
            ganador = jugador
            print()
            print(f'GANO EL JUGADOR {ganador}')
            break
    r += 1
print('Fin del juego o empate')