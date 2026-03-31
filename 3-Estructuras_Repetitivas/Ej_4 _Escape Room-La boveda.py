energia = 100
tiempo = 12
cerraduras_abiertas = 0
alarma = False
cerradura_forzada = 0
nombre_agente = input('Buenos dias agente, ingrese su nombre: ')
print('')
while not nombre_agente.isalpha():
    print('Error: Tiene que ser un nombre')
    nombre_agente = input('Buenos dias agente, ingrese su nombre: ')
    print('')
print(f'Bienvenido agente {nombre_agente.capitalize()}')
while True:
    codigo_parcial = ''
    print(f'Energia: {energia}')
    print(f'Tiempo: {tiempo}')
    print(f'Cerraduras abiertas: {cerraduras_abiertas}')
    print('')
    if cerraduras_abiertas == 3:
        print('Victoria')
        break
    if energia <= 0 or tiempo <= 0:
        print('Derrota')
        break
    if alarma and tiempo <= 3 and cerraduras_abiertas < 3:
        print('Sistema bloqueado')
        break
    print('Elija una opcion: ')
    print('1. Forzar cerradura')
    print('2. Hackear panel')
    print('3. Descanzar')
    eleccion = input()
    print('')
    while not eleccion.isdigit():
        print('Error: tiene que ser una opcion valida: ')
        print('1. Forzar cerradura')
        print('2. Hackear panel')
        print('3. Descanzar')
        eleccion = input()
        print('')
    match int(eleccion):
        case 1:
            cerradura_forzada += 1
            if cerradura_forzada >= 3:
                print('Cerradura bloqueada')
                alarma = True
                print('')
                continue
            if energia >= 20 and tiempo >= 2:
                energia -= 20
                tiempo -= 2
                if energia < 40:
                    print('Eliga un numero 1-3')
                    num = input()
                    print('')
                    while not num.isdigit() or int(num) == 0 or int(num) > 3:
                        print('Error: tiene que ser un numero de la opcion')
                        print('Eliga un numero 1-3')
                        num = input()
                        print('')
                    if int(num) != 3 and (not alarma):
                        print('Forzando cerradura')
                        cerraduras_abiertas += 1
                        print('Cerradura abierta')
                        print('')
                    else:
                        print('¡¡¡ALARMA ACTIVADA!!!')
                        alarma = True
                        print('')
                else:
                    print('Forzando cerradura')
                    cerraduras_abiertas += 1
                    print('Cerradura abierta')
                    print('')
        case 2:
            cerradura_forzada = 0
            if energia >= 10 and tiempo >= 3:
                energia -= 10
                tiempo -= 3
                for i in range (4):
                    print('Ingrese el codigo: ')
                    codigo = input()
                    while codigo == '':
                        print('No puede ser un campo vacio')
                        print('Ingrese el codigo: ')
                        codigo = input()
                    codigo_parcial += codigo
                    print(f'craking: {codigo_parcial}')
                    if len(codigo_parcial) >= 8:
                        print('Cerradura abierta')
                        cerraduras_abiertas += 1
                        print('')
                        break
        case 3:
            cerradura_forzada = 0
            if tiempo >= 1 and alarma:
                tiempo -= 1
                energia -= 10
            elif tiempo >= 1 and (not alarma):
                energia += 15
                tiempo -= 1
            if energia > 100:
                energia = 100
        case _:
            print('Eleccion no valida')
            print('')
            continue