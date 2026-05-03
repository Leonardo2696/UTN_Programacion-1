def verificar_str(texto):
    text = texto
    while not text.replace(' ','').isalpha():
        print('El texto no valido')
        text = input('Ingrese el nombre ').strip().capitalize()
    return text

def verificar_int(numero):
    num_int = numero
    while not num_int.isdigit():
        print('No es un numero valido')
        num_int = input('Ingrese un numero: ')
    return int(num_int)

def dato_en_list(dato,dicc,mensaje):
    while dato in dicc:
        if type(dato) == str:
            print('Error. El dato ingresado ya existe: ')
            dato = verificar_str(input(mensaje).capitalize().strip())
            print()
        elif type(dato) == int:
            print('Error. El dato ingresado ya existe: ')
            dato = validar_N(input(mensaje).capitalize().strip())
            print()
    return dato

def cont_bucle(mensaje):
    print(f'{mensaje} (N--salir / S--continuar)')
    s_n = verificar_str(input('>>').upper().strip())
    while s_n != 'N' and s_n != 'S':
        print(f'"{s_n}" No es parte de la opcion')
        print(f'{mensaje} (N--salir / S--continuar)')
        s_n = verificar_str(input('>>').upper().strip())
    if s_n == 'N':
        print('Saliendo')
        return False
    elif s_n == 'S':
        return True

def menu(msj):
    print('='*8,'MENU','='*8)
    print(msj)
    print()
def caso_1(diccionario):
    nombre_prod = verificar_str(input('Ingrese el nombre del producto: ').capitalize().strip())
    cant_prod = verificar_int(input(f'Ingrese la cantidad de {nombre_prod}: ').strip())
    diccionario.update({nombre_prod:cant_prod})
    print()
def caso_2(diccionario):
    print('='*5,'STOCK','='*5)
    for k,v in diccionario.items():
        print(f'{k} --- {v}')
    print()
def caso_3(diccionario):
    prod = verificar_str(input('Ingrese el nombre del producto: ').capitalize().strip())
    if prod in diccionario:
        cant = verificar_int(input(f'Cuantas unidades quere ingresar para {prod}: ').strip())
        diccionario[prod] += cant
    else:
        print(f'"{prod}"- No se ha encontrado en lista. Se agregara como nuevo')
        cant = verificar_int(input(f'Cuantas unidades quere ingresar para {prod}: ').strip())
        diccionario.update({prod:cant})
    print()
def verificar_dia_semana(dia):
    if dia == 'Lunes':
        return False
    elif dia == 'Martes':
        return False
    elif dia == 'Miercoles':
        return False
    elif dia == 'Jueves':
        return False
    elif dia == 'Viernes':
        return False
    elif dia == 'Sabado':
        return False
    elif dia == 'Domingo':
        return False
    else:
        return True

def horas_minutos(h,m):
    while h > 23:
        print('El dia solo tiene 24 horas, ingrese un horario valido: ')
        h = verificar_int(input('Ingrese la hora (24hr) del evento: ').strip())
    while m > 59:
        print('Ingrese un numero entro 0 y 59')
        m = verificar_int(input('Ingrese los minutos (59) del horario: '))
    print()
    return (f'{h}:{m}')

def capital_repetida(cap,diccionario):
    return cap in diccionario.values()