
operador = input('Ingrese su nombre: ')
print('')
Lunes = 4
turno_1_Lunes = 'Juan'
turno_2_Lunes = 'Miguel'
turno_3_Lunes = 'Marta'
turno_4_Lunes = ''
Martes = 3
turno_1_Martes = 'Luisa'
turno_2_Martes = ''
turno_3_Martes = ''
while not operador.isalpha():
    print('Tiene que ser letras.')
    operador = input('Ingrese su nombre: ')
    print('')
while True:
    if operador.isalpha():
        print('---- MENU ----')
        print('Seleccione una opcion: ')
        print('1.Reservar turno    2.Cancelar turno   3.Ver turnero del dia    4.Ver resumen general    5.Cerrar sistema')
        opcion_menu = input()
        print('')
        while not opcion_menu.isdigit():
            print('Error: tiene que ser un numero del menu: ')
            print('1.Reservar turno    2.Cancelar turno   3.Ver turnero del dia    4.Resumen general    5.Cerrar sistema')
            opcion_menu = input()
            print('')
        match int(opcion_menu):
            case 1: #Resevar turno (por nombre)
                print('Ingrese que dia quiere reservar: ')
                print('1__Lunes       2___Martes')
                dias = input()
                while not dias.isdigit():
                    print('Error: tiene que ser una opcion valida: ')
                    print('1__Lunes       2___Martes')
                    dias = input()
                match int(dias):
                    case 1 : #__Lunes
                        paciente = input('Ingrese el nombre del paciente: ')
                        while not paciente.isalpha():
                            print('Ingrese solo el nombre con letras: ')
                            paciente = input('Ingrese el nombre del paciente: ')
                            if paciente.isalpha():
                                continue
                        if paciente.capitalize() == turno_1_Lunes.capitalize():
                            print(f'Este paciente {paciente.capitalize()} ya tiene turno')
                            continue
                        elif paciente.capitalize() != turno_1_Lunes.capitalize() and turno_1_Lunes == '':
                            print('Turno asignado al puesto 1')
                            turno_1_Lunes = paciente.capitalize()
                            continue
                        if paciente.capitalize() == turno_2_Lunes:
                            print(f'Este paciente {paciente.capitalize()} ya tiene turno')
                            continue
                        elif paciente.capitalize() != turno_2_Lunes.capitalize() and turno_2_Lunes == '':
                            print('Turno asignado al puesto 2')
                            turno_2_Lunes = paciente.capitalize()
                            continue
                        if paciente.capitalize() == turno_3_Lunes:
                            print(f'Este paciente {paciente.capitalize()} ya tiene turno')
                            continue
                        elif paciente.capitalize() != turno_3_Lunes.capitalize() and turno_3_Lunes == '':
                            print('Turno asignado al puesto 3')
                            turno_3_Lunes = paciente.capitalize()
                            continue
                        if paciente.capitalize() == turno_4_Lunes:
                            print(f'Este paciente {paciente.capitalize()} ya tiene turno')
                            continue
                        elif paciente.capitalize() != turno_4_Lunes and turno_4_Lunes == '':
                            print('Turno asignado al puesto 4')
                            turno_4_Lunes = paciente.capitalize()
                    case 2:#__Martes
                        paciente = input('Ingrese el nombre del paciente: ')
                        while not paciente.isalpha():
                            print('Ingrese solo el nombre con letras: ')
                            paciente = input('Ingrese el nombre del paciente: ')
                            continue
                        if paciente.capitalize() == turno_1_Martes.capitalize():
                            print(f'Este paciente {paciente.capitalize()} ya tiene turno')
                            continue
                        elif paciente.capitalize() != turno_1_Martes.capitalize() and turno_1_Martes == '':
                            print('Turno asignado al puesto 1')
                            turno_1_Martes = paciente.capitalize()
                            continue
                        if paciente.capitalize() == turno_2_Martes:
                            print(f'Este paciente {paciente.capitalize()} ya tiene turno')
                            continue
                        elif paciente.capitalize() != turno_2_Martes.capitalize() and turno_2_Martes == '':
                            print('Turno asignado al puesto 2')
                            turno_2_Martes = paciente.capitalize()
                            continue
                        if paciente.capitalize() == turno_3_Martes:
                            print(f'Este paciente {paciente.capitalize()} ya tiene turno')
                            continue
                        elif paciente.capitalize() != turno_3_Martes.capitalize() and turno_3_Martes == '':
                            print('Turno asignado al puesto 3')
                            turno_3_Martes = paciente.capitalize()
                            continue
                    case _:
                        print('Opcion no valida')
                        continue
            case 2: #Cancelar turno(por nombre)
                print('Ingrese que dia quiere cancelar un turno: ')
                print('1__Lunes       2___Martes')
                dias = input()
                while not dias.isdigit():
                    print('Error: tiene que ser una opcion valida: ')
                    print('1__Lunes       2___Martes')
                    dias = input()
                    print('')
                match int(dias):
                    case 1: #Cancelar turnos Lunes
                        print('Ingrese el nombre del paciente a cancelar turno: ')
                        paciente_cancelar = input()
                        while not paciente_cancelar.isalpha():
                            print('Error: tiene que ser un nombre: ')
                            print('Ingrese el nombre del paciente a cacelar turno: ')
                            paciente_cancelar = input()
                            print('')
                        if paciente_cancelar.capitalize() == turno_1_Lunes:
                            print(f'Turno de {paciente_cancelar} a sido cancelado')
                            turno_1_Lunes = ''
                            print('')
                        if paciente_cancelar.capitalize() == turno_2_Lunes:
                            print(f'Turno de {paciente_cancelar} a sido cancelado')
                            turno_2_Lunes = ''
                            print('')
                        if paciente_cancelar.capitalize() == turno_3_Lunes:
                            print(f'Turno de {paciente_cancelar} a sido cancelado')
                            turno_3_Lunes = ''
                            print('')
                        if paciente_cancelar.capitalize() == turno_4_Lunes:
                            print(f'Turno de {paciente_cancelar} a sido cancelado')
                            turno_4_Lunes = ''
                            print('')
                        else:
                            print('El paciente no coincide')
                            print('')
                    case 2: #Cancelar turnos Martes
                        print('Ingrese el nombre del paciente a cancelar turno: ')
                        paciente_cancelar = input()
                        while not paciente_cancelar.isalpha():
                            print('Error: tiene que ser un nombre: ')
                            print('Ingrese el nombre del paciente a cacelar turno: ')
                            paciente_cancelar = input()
                            print('')
                        if paciente_cancelar.capitalize() == turno_1_Martes:
                            print(f'Turno de {paciente_cancelar} a sido cancelado')
                            turno_1_Martes = ''
                            print('')
                        if paciente_cancelar.capitalize() == turno_2_Martes:
                            print(f'Turno de {paciente_cancelar} a sido cancelado')
                            turno_2_Martes = ''
                            print('')
                        if paciente_cancelar.capitalize() == turno_3_Martes:
                            print(f'Turno de {paciente_cancelar} a sido cancelado')
                            turno_3_Martes = ''
                            print('')
                        else:
                            print('El paciente no coincide')
                            print('')
                    case _:
                        print('Opcion no encontrada')
            case 3: #Ver agenda del dia seleccionado
                print('Que dias quiere ver la agenda: ')
                print('1__Lunes       2___Martes')
                agenda_dia = input()
                print('')
                while not agenda_dia.isdigit():
                    print('Error: tiene que ser un dia valido')
                    print('Que dias quiere ver la agenda: ')
                    print('1__Lunes       2___Martes')
                    agenda_dia = input()
                    print('')
                match int(agenda_dia):
                    case 1:
                        print('Turnero dia Lunes: ')
                        if turno_1_Lunes.isalpha():
                            print(f'Turno 1--- {turno_1_Lunes}')
                        else:
                            print('Turno 1--- "Libre"')
                        if turno_2_Lunes.isalpha():
                            print(f'Turno 2--- {turno_2_Lunes}')
                        else:
                            print('Turno 2--- "Libre"')
                        if turno_3_Lunes.isalpha():
                            print(f'Turno 3--- {turno_3_Lunes}')
                        else:
                            print('Turno 3--- "Libre"')
                        if turno_4_Lunes.isalpha():
                            print(f'Turno 4--- {turno_4_Lunes}')
                        else:
                            print('Turno 4--- "Libre"')
                    case 2:
                        print('Turnero dia Martes: ')
                        if turno_1_Martes.isalpha():
                            print(f'Turno 1--- {turno_1_Martes}')
                        else:
                            print('Turno 1--- "Libre"')
                        if turno_2_Martes.isalpha():
                            print(f'Turno 2--- {turno_2_Martes}')
                        else:
                            print('Turno 2--- "Libre"')
                        if turno_3_Martes.isalpha():
                            print(f'Turno 3--- {turno_3_Martes}')
                        else:
                            print('Turno 3--- "Libre"')
                    case _:
                        print('Opcion no encontrada')
            case 4: #Resumen general
                #Condicionon del turnero Lunes
                Ocupado_Lunes = 0
                Ocupado_Martes = 0
                Libre_Lunes = 0
                Libre_Martes = 0
                if turno_1_Lunes.isalpha():
                    tl_1 = 'O'
                    Ocupado_Lunes += 1
                else:
                    tl_1 = 'L'
                    Libre_Lunes += 1
                if turno_2_Lunes.isalpha():
                    tl_2 = 'O'
                    Ocupado_Lunes += 1
                else:
                    tl_2 = 'L'
                    Libre_Lunes += 1
                if turno_3_Lunes.isalpha():
                    tl_3 = 'O'
                    Ocupado_Lunes += 1
                else:
                    tl_3 = 'L'
                    Libre_Lunes += 1
                if turno_4_Lunes.isalpha():
                    tl_4 = 'O'
                    Ocupado_Lunes += 1
                else:
                    tl_4 = 'L'
                    Libre_Lunes += 1
                #Condiciones del tunero Martes
                if turno_1_Martes.isalpha():
                    tm_1 = 'O'
                    Ocupado_Martes += 1
                else:
                    tm_1 = 'L'
                    Libre_Martes += 1
                if turno_2_Martes.isalpha():
                    tm_2 = 'O'
                    Ocupado_Martes += 1
                else:
                    tm_2 = 'L'
                    Libre_Martes += 1
                if turno_3_Martes.isalpha():
                    tm_3 = 'O'
                    Ocupado_Martes += 1
                else:
                    tm_3 = 'L'
                    Libre_Martes += 1
                print('')
                print('     Lunes       Martes')
                print(f'T-1     {tl_1}         {tm_1}')
                print(f'T-2     {tl_2}         {tm_2}')
                print(f'T-3     {tl_3}         {tm_3}')
                print(f'T-4     {tl_4}         X')
                print('')
                if Ocupado_Lunes > Ocupado_Martes:
                    print(f'El dia Lunes tiene mas turnos ocupados con total de: {Ocupado_Lunes}')
                    print(f'Y tiene libre: {Libre_Lunes} turnos libres')
                    print('')
                elif Ocupado_Lunes < Ocupado_Martes:
                    print(f'El dia Martes tiene mas turnos ocupados con un total de: {Ocupado_Martes}')
                    print(f'Y teine libre: {Libre_Martes} turnos libres')
                    print('')
                else:
                    print('Los turnos estan empatados con turnos')
                    print('')
            case 5:
                break
            case _:
                print('Opcion invalida')
                print('')