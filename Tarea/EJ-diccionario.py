# 1. Creación Simple: Crea un diccionario llamado mascota con las claves: nombre, especie y edad. Imprime solo el nombre.
mascota = {
    'nombre':'Eulalia',
    'especie':'Canina',
    'edad': 13
}
print(mascota['nombre'])
# 2. Actualización de Datos: Dado el diccionario anterior, cambia la edad de la mascota a un valor diferente y añade una nueva clave llamada raza.
mascota['edad'] = 12
mascota['raza']='Pichichu'
print(mascota)
print()
# 3. El Traductor: Crea un pequeño diccionario "Español-Inglés" con 5 palabras. Pide al usuario que ingrese una palabra en español e imprime su traducción.
# español_ingles = {'Hola':'Hello','Perro':'Dog','Auto':'Car','Gato':'Cat','Comida':'Food'}
# palabra = input('Ingrese la palabra a traducir: ').capitalize().strip()
# print(f'La palabra == {palabra}, se traduce como == {español_ingles[palabra]}')
print()
# 4. Limpieza de Registro: Crea un diccionario que represente un auto. Elimina la clave color usando la sentencia del e imprime el diccionario resultante.
auto = {
    'marca':'Ford',
    'color':'Rojo',
    'modelo':'Ranger'
}
del(auto['color'])
print(auto)
print()
# Nivel Intermedio: Iteración y Métodos
# 5. Listado de Inventario: Crea un diccionario de productos donde la clave sea el nombre y el valor el precio. Usa un bucle for con .items() para imprimir: "El producto [clave] cuesta $[valor]".
productos = {'pan':'200',
             'papa':'230',
             'lechuga':'232'
             ,'leche':'90'
             }
for c,v in productos.items():
    print(f'El producto {c} cuesta ${v}')
print()
# 6. Solo Etiquetas: Usando el diccionario del ejercicio anterior, imprime únicamente la lista de los nombres de los productos utilizando el método .keys().
print('Los productos que estan en el carro son: ')
for etiqueta in productos.keys():
    print(etiqueta)
print()
# 7. Suma de Valores: Crea un diccionario con los gastos del mes (ej: {"luz": 5000, "internet": 3000}). Calcula el total de gastos sumando todos los .values().
gastos = {
    'internet':123,
    'gas':324,
    'luz':949,
    'agua':194
}
gastos_totales = gastos.values()
for servicions, monto in gastos.items():
    print(f'Servicio : {servicions}--- Valor : {monto}')
total = 0
for i in gastos_totales:
    total += int(i)
print(f'total a pagar : {total}')
print()
# 8. Verificación de Claves: Escribe un programa que consulte si la clave puesto existe en un diccionario de empleado. Si no existe, agrégala con el valor "Pasante".
datos = {'Clave': ''}
if datos['Clave'] != 'Pasante':
    datos['Clave'] = 'Pasante'


# Nivel Avanzado: Estructuras Complejas y Lógica
# 9. Diccionario de Listas: Crea un diccionario donde las claves sean nombres de estudiantes y los valores sean listas de sus notas (como las que hiciste en tu archivo Ejercicio.py). Calcula el promedio de un estudiante específico.
alumnos = {
    'Leonardo' : [1,2,4],
    'Angel' : [9,4,5],
    'Yami' : [5,6,7],
    'Eli' : [10,9,8]
}
notas = alumnos.values()

for n,x in alumnos.items():
    promedio = 0
    for i in x:
        promedio += i
    print(f'El promedio de {n} es {promedio/len(x)}')

# 10. Contador de Caracteres: Pide al usuario una frase. Crea un diccionario que cuente cuántas veces aparece cada letra en esa frase (la letra será la clave y la cantidad el valor).
print('Ingrese un frese: ')
frase = input('>>').lower().strip()
while not frase.isalpha():
    print('Error, tiene que ser una "string"')
    print('Ingrese un frese: ')
    frase = input('>>').lower().strip()
mayor = 0
for letra in frase:
    if frase.count(letra) > mayor:
        mayor_sale = letra
        mayor = frase.count(letra)
    letras_valor = dict()
    letras_valor[mayor_sale] = mayor
for d,n in letras_valor.items():
    if n == 1:
        print(f'La palabra "{frase.capitalize()}", no se repite ninguna letra')
    else:
        print(f'La letra "{d.upper()}" es la que mas se repite con un total de : {n}')

# 11. El Filtro de Precios: Dado un diccionario de productos y precios, crea un nuevo diccionario que contenga solo aquellos productos cuyo precio sea mayor a 1000 (similar a tu función filtrar_aprobados pero para diccionarios).
productos = {
    'Pan':1234,
    'Leche':232,
    'Agua':9434,
    'Azucar':93
}
mas_caros = dict()

for pro,pre in productos.items():
    if pre > 1000:
        mas_caros.update({pro:pre})
print(mas_caros)
