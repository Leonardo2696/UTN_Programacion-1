usuario_correcto = 'alumno'
clave_correcta = 'python123'
intentos = 3
while intentos >= 1:
    ingreso_usuario = input('Ingrese su usuario: ')
    ingreso_clave = input('Ingrese la clave: ')
    if usuario_correcto != ingreso_usuario or clave_correcta != ingreso_clave:
        intentos -= 1
        print('Incorrecto')
        print(f'Intentos disponibles: {intentos}')
        print('El usuario o la clave es incorrecta')
        print('')
        if intentos == 0:
            print('Cuenta bloqueada')
            print('')
            break
    else :
        print('')
        print(f'Bienvenido "{usuario_correcto}"')
        while True:
            print('Seleccione una opcion: ')
            print('1).Estado    2).Cambiar clave    3).Mensaje    4).Salir')
            opcion = input()
            print('')
            while not opcion.isdigit():
                print('Error: tiene que ser un numero')
                print('1).Estado    2).Cambiar clave    3).Mensaje    4).Salir')
                opcion = input()
                print('')
            match int(opcion):
                case 1: 
                    print('Estado del alumno:')
                    print('Inscripto')
                    print('')
                case 2: 
                    print('La nueva clave debe tener minimo 6 caracteres')
                    nueva_clave = input('Ingrese nueva clave: ')
                    if len(nueva_clave) < 6:
                        print('Tiene que tener minimo 6 caracteres')
                        print('')
                    elif len(nueva_clave) >= 6:
                        confirme_clave = input('Confirme la nueva clave: ')
                        if nueva_clave != confirme_clave:
                            print('Las claves no coinciden')
                            print('')
                        elif nueva_clave == confirme_clave:
                            print('Clave cambiada')
                            print('')
                case 3:
                    print('No te rindas ante un bug; cada error es una leccion y un paso mas hacia una mejor version de tu software')
                case 4:
                    break
                case _:
                    print('Error: no es una opcion valida')      
                    print('')              
        break
