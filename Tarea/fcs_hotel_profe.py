
def mostrar_menu():
    print('\n1. Agregar habitación')
    print('2. Mostrar todas')
    print('3. Consultar habitación')
    print('4. Cambiar estado')
    print('5. Listar por estado')
    print('6. Salir')

def pedir_numero_habitacion():
    while True:
        try:
            numero = int(input('Ingrese número de habitación: '))
            if numero < 100 or numero > 999:
                print('El número debe tener exactamente 3 dígitos.')
                continue
            return numero
        except ValueError:
            print('Ingrese un número válido.')

def pedir_estado():
    while True:
        try:
            estado = int(input('Ingrese estado (0=libre, 1=ocupada): '))
            if estado not in (0, 1):
                print('El estado debe ser 0 o 1.')
                continue
            return estado
        except ValueError:
            print('Ingrese un número válido.')

def buscar_habitacion(habitaciones, numero):
    for hab in habitaciones:
        if hab['numero'] == numero:
            return hab
    return None

def agregar_habitacion(habitaciones):
    numero = pedir_numero_habitacion()
    if buscar_habitacion(habitaciones, numero):
        print('La habitación ya existe.')
        return
    estado = pedir_estado()
    habitaciones.append({'numero': numero, 'estado': estado})
    print('Habitación agregada.')

def mostrar_habitaciones(habitaciones):
    if not habitaciones:
        print('No hay habitaciones registradas.')
        return
    for hab in habitaciones:
        estado = 'Libre' if hab['estado'] == 0 else 'Ocupada'
        print(f'Habitación {hab["numero"]}: {estado}')

def consultar_habitacion(habitaciones):
    numero = pedir_numero_habitacion()
    hab = buscar_habitacion(habitaciones, numero)
    if hab:
        estado = 'Libre' if hab['estado'] == 0 else 'Ocupada'
        print(f'Habitación {numero}: {estado}')
    else:
        print('La habitación no existe.')

def cambiar_estado(habitaciones):
    numero = pedir_numero_habitacion()
    hab = buscar_habitacion(habitaciones, numero)
    if not hab:
        print('La habitación no existe.')
        return
    estado = pedir_estado()
    hab['estado'] = estado
    print('Estado actualizado.')

def listar_por_estado(habitaciones):
    estado = pedir_estado()
    filtradas = [h for h in habitaciones if h['estado'] == estado]
    if not filtradas:
        print('No hay habitaciones con ese estado.')
        return
    for hab in filtradas:
        texto = 'Libre' if hab['estado'] == 0 else 'Ocupada'
        print(f'Habitación {hab["numero"]}: {texto}')