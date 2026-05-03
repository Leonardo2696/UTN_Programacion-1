from def_tp7 import *
# 1)
precios_frutas = {'Banana': 1200, 'Ananá': 2500, 'Melón': 3000, 'Uva':1450}
precios_frutas.update({'Naranja': 1200,'Manzana': 1500,'Pera': 2300})

# 2)
precios_frutas['Banana'] = 1330
precios_frutas['Manzana'] = 1700
precios_frutas['Melón'] = 2800

# 3)
lista_frutas = list(precios_frutas)

# 4)
contactos = dict()
for i in range(2):
    nombre = verificar_str(input('Ingrese un nombre: ').capitalize().strip())
    nombre = dato_en_list(nombre,contactos,'Ingrese un nombre valido: ')
    numero = verificar_int(input('Ingrese el numero telefonico: ').strip())
    print()
    numero = dato_en_list(numero,contactos.values(),'Ingrese un numero valido: ')
    contactos.update({nombre:numero})
print()
while True:
    print('='*5,'Directorio','='*5)
    nom_a_buscar = verificar_str(input('Ingrese el nombre a buscar: ').capitalize().strip())
    print()
    if not cont_bucle('Buscar otro contacto ? '):
        break

# 5)
frase = input('Ingrese una frase: ')
palabras = list(frase.split())
recuento = {}
for p in palabras:
    mas_repite = palabras.count(p)
    palabla_mas_repetirda = p
    recuento.update({palabla_mas_repetirda:mas_repite})
palabras_unicas = set(palabras)
print(f'Palabras unicas: {palabras_unicas}')
print(f'Recuento: {recuento}')

# 6) 
alumnos = dict()
for i in range(3
):
    alumno = verificar_str(input('Ingrese el nombre del alumno: ').capitalize().strip())
    alumno = dato_en_list(alumno,alumnos,'Ingrese el nombre del alumno: ')
    a = verificar_int(input(f'Ingrese las notas de {alumno}: '))
    b = verificar_int(input(f'Ingrese las notas de {alumno}: '))
    c = verificar_int(input(f'Ingrese las notas de {alumno}: '))
    notas = (a,b,c)
    alumnos.update({alumno : notas})
print()
total = 0
for a,nota in alumnos.items():
    for n in nota:
        total += n
    print(f'Alumno: {a} ---> Promedio: {total/(len(nota))}')

# 7)
asistencias = []
while True:
    empleados = verificar_str(input('Ingrese el nombre del empleado: ').capitalize().strip())
    asistencias.append(empleados)
    if not cont_bucle('Ingresar otro empleado: '):
        break
print(f'Asistencias : {asistencias}')
nombres_solos = set(asistencias)
print(f'Nombres : {nombres_solos}')
asistio = dict()
for nombre in asistencias:
    aparece = asistencias.count(nombre)
    asistio.update({nombre : aparece})
for x,y in asistio.items():
    print(f'{x} asistio : {y}')

# 8) 
productos = dict()
while True:
    menu('''1. Agregar un producto
2. Consultar stock
3. Agregar unidades
Otro numero = (Salir)''')
    opcion = verificar_int(input('Ingrese una opcion: ').strip())
    print()
    match opcion:
        case 1:
            caso_1(productos)
        case 2:
            caso_2(productos)
        case 3:
            caso_3(productos)
        case _:
            print('Saliendo del menu')
            break

# 9) 
agenda = {
    ('Lunes','10:10'):'Clases',
    ('Martes','15:00'):'Jugar'
}
while True:
    menu('''
1. Ver dia y hora
2. Agregrar nuevo evento
3. Ver agenda completa
Otro --- Salir''')
    opcion = verificar_int(input('Ingrese una opcion del menu: ').strip())
    match opcion:
        case 1:
            if not agenda:
                print('La agenda esta vacia, ingrese en la opcion 2 del menu: ')
            else:
                dia_consulta = verificar_str(input('Ingrese el dia a consultar: ').capitalize().strip())
                horas = verificar_int(input('Ingrese la hora (24hr) del evento: ').strip())
                minutos = verificar_int(input('Ingrese los minutos (59) del horario: '))
                hora = horas_minutos(horas,minutos)
                for dia, hora_min in agenda.keys():
                    if dia_consulta == dia and hora == hora_min:
                        print(f'El dia "{dia}" a las {hora_min} -- tiene evento: "{agenda[dia,hora_min]}"')
        case 2:
            dia_nuevo = verificar_str(input('Ingrese un dia de la sema: ').capitalize().strip())
            while verificar_dia_semana(dia_nuevo):
                print('El dia ingresado no es valido: ')
                dia_nuevo = verificar_str(input('Ingrese un dia de la sema: ').capitalize().strip())
            horas = verificar_int(input('Ingrese la hora (24hr) del evento: ').strip())
            minutos = verificar_int(input('Ingrese los minutos (59) del horario: '))
            hora = (horas_minutos(horas,minutos))
            evento_nuevo = input('Ingrese el evento a agendar: ').capitalize().strip()
            verificar_str(evento_nuevo.replace(' ',''))
            agenda.update({(dia_nuevo,hora):evento_nuevo})
            print(evento_nuevo)
        case 3:
            for d_h , evento in agenda.items():
                print(f'{d_h} -- {evento}')
        case _:
            print('Saliendo')
            break

# 10)
original = {'Argentina':'Bueos Aires','Chile':'Santiago de Chile'}
invertido = dict()
while True:
    pais = input('Ingrese un pais: ').capitalize().strip()
    verificar_str(pais.replace(' ',''))
    while not dato_en_list(pais,original,'Existe'):
        break
    else:
        capital = input(f'Ingrese la capital de {pais}: ').capitalize().strip()
        verificar_str(capital.replace(' ',''))
        if capital in original:
            print('La capital ya fue ingresada ')
        else:
            original.update({pais:capital})
    if not cont_bucle('Agregar otro dato? '):
        break
print(f'Diccionario Original: {original}')
for p,c in original.items():
    pais = c
    capital = p
    invertido.update({pais:capital})
print(f'Diccionario Invertido: {invertido}')

original = {'Argentina': 'Buenos Aires', 'Chile': 'Santiago de Chile'}
invertido = dict()

while True:
    entrada_pais = input('Ingrese un país: ').strip().capitalize()
    pais = verificar_str(entrada_pais)
    pais = dato_en_list(pais, original, 'Ese país ya está registrado, ingrese otro: ')
    entrada_cap = input(f'Ingrese la capital de {pais}: ').strip().capitalize()
    capital = verificar_str(entrada_cap.title())
    while capital_repetida(capital, original):
        print(f'Error: La capital "{capital}" ya está asignada a otro país.')
        capital = input(f'Ingrese una capital diferente para {pais}: ').strip().capitalize()
        capital = verificar_str(capital)
    original[pais] = capital
    if not cont_bucle('¿Desea agregar otro dato?'):
        break
invertido = {capital: pais for pais, capital in original.items()}
print("\n" + "="*20)
print(f'Diccionario Original: {original}')
print(f'Diccionario Invertido: {invertido}')