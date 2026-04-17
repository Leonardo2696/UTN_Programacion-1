def validar_numero(numero):
    n_a_int = numero
    while True :
        if not n_a_int.replace('.','').isdigit():
            print('El dato ingresado no es valido')
            n_a_int = input('Ingrese un numero : ')
        else :
            return float(n_a_int)

def validar_str(cadena,msj):
    str_validar = cadena
    while True:
        if not str_validar.isalpha():
            print('El dato ingresado no es valido')
            str_validar = input(msj)
        else:
            return str_validar.capitalize().strip()


'''
1. Crear una función llamada imprimir_hola_mundo que imprima por
pantalla el mensaje: “Hola Mundo!”. Llamar a esta función desde el
programa principal.
'''
def imprimir_hola_mundo():
    print('"Hola Mundo!"')

imprimir_hola_mundo()
'''
2. Crear una función llamada saludar_usuario(nombre) que reciba
como parámetro un nombre y devuelva un saludo personalizado.
Por ejemplo, si se llama con saludar_usuario("Marcos"), deberá devolver: “Hola Marcos!”. Llamar a esta función desde el programa
principal solicitando el nombre al usuario.
'''
def saludar_usuario(nombre):
    print(f'"Hola {nombre}!"')

usuario = saludar_usuario(validar_str(input('Ingrese su nombre: '),'Ingrese su nombre: '))

'''
3. Crear una función llamada informacion_personal(nombre, apellido,
edad, residencia) que reciba cuatro parámetros e imprima: “Soy
[nombre] [apellido], tengo [edad] años y vivo en [residencia]”. Pedir los datos al usuario y llamar a esta función con los valores ingresados.
'''
def informacion_personal(nombre, apellido, edad, residencia):
    print(f'"Soy {nombre} {apellido}, tengo {edad} años y vivo en {residencia}"')
nombre_usuario = validar_str(input('Ingrese su nombre  >> '), 'Ingrese su nombre  >> ')
apellido_usuario = validar_str(input('ingrese su apellido  >> '), 'Ingrese su apellido  >> ')
edad_usuario = validar_numero(input('Ingrese su edad  >> '))
residencia_usuario = validar_str(input('Ingrese su residencia  >> '), 'Ingrese su residencia  >> ')
informacion_personal(nombre_usuario, apellido_usuario, edad_usuario, residencia_usuario)

'''
4. Crear dos funciones: calcular_area_circulo(radio) que reciba el radio como parámetro y devuelva el área del círculo. calcular_perimetro_circulo(radio) que reciba el radio como parámetro y devuelva el perímetro del círculo. Solicitar el radio al usuario y llamar ambas funciones para mostrar los resultados.
'''
def calcular_area_circulo(radio):
    area = 3.1415 * (radio ** 2)
    return area
def calcular_perimetro_circulo(radio):
    perimetro = 2 * 3.1415 * radio
    return perimetro
print('Ingrese el Radio de un circulo: ')
radio = validar_numero(input('Ingrese el Radio >> '))
print(f'El Area de un circulo es {calcular_area_circulo(int(radio)):.2f}, y su Perimetro es {calcular_perimetro_circulo(int(radio)):.2f}')

'''
5. Crear una función llamada segundos_a_horas(segundos) que reciba
una cantidad de segundos como parámetro y devuelva la cantidad
de horas correspondientes. Solicitar al usuario los segundos y mostrar el resultado usando esta función.
'''
def segundos_a_horas(segundos):
    hora = segundos / 3600
    return hora
print('Ingrese la cantidad de segundos')
seg_ingresados = validar_numero(input('Ingrese la cantidad de segundos >> '))
print(f'La cantidad de horas es {segundos_a_horas(int(seg_ingresados)):.2f}')

'''
6. Crear una función llamada tabla_multiplicar(numero) que reciba un
número como parámetro y imprima la tabla de multiplicar de ese
número del 1 al 10. Pedir al usuario el número y llamar a la función.
'''
def tabla_multipicar(numero):
    print(f'Tabla de multiplicar de {numero}')
    for i in range(1,11):
        print(f'{numero} x {i} = {numero * i}')
print('Ingrese un numero para hacer la tabla')
numero_a_para_tabla = input('>> ')
tabla_multipicar(validar_numero(numero_a_para_tabla))
'''
7. Crear una función llamada operaciones_basicas(a, b) que reciba
dos números como parámetros y devuelva una tupla con el resultado de sumarlos, restarlos, multiplicarlos y dividirlos. Mostrar los resultados de forma clara.
'''
def opradores_basicos(a,b):
    sum = a + b
    res = a - b
    multi = a * b
    if b != 0:
        div = a / b 
    else:
        div = 'Imposible dividir por 0'
    return (sum,res,multi,div)

num_uno = validar_numero(input('Ingrese el primer numero >> '))
num_dos = validar_numero(input('Ingrese el segundo numero >> '))
tupla = opradores_basicos(num_uno, num_dos)
print(f'Suma ==== {tupla[0]}')
print(f'Resta === {tupla[1]}')
print(f'multiplicacion === {tupla[2]}')
print(f'divicion === {tupla[3]}')

'''
8. Crear una función llamada calcular_imc(peso, altura) que reciba el
peso en kilogramos y la altura en metros, y devuelva el índice de
masa corporal (IMC). Solicitar al usuario los datos y llamar a la función para mostrar el resultado con dos decimales.
'''
def calcular_imc(peso,altura):
    imc = peso / ((altura/100) * (altura/100))
    return imc

kilogramos = validar_numero(input('Ingrese su peso (kg): '))
metros = validar_numero(input('Ingrese su altura (metros): '))
print(f'Su IMC es de: {calcular_imc(kilogramos,metros):.2f}')

'''
9. Crear una función llamada celsius_a_fahrenheit(celsius) que reciba
una temperatura en grados Celsius y devuelva su equivalente en
Fahrenheit. Pedir al usuario la temperatura en Celsius y mostrar el
resultado usando la función.
'''
def celsius_a_fahrenheit(celsius):
    fahrenheit = celsius * (9/5) + 32
    print(f'De Celsius a Farenhait (F°) : {fahrenheit}')


grados = validar_numero(input('Ingrese la cantidad de grados (C°): '))
celsius_a_fahrenheit(grados)

'''
10.Crear una función llamada calcular_promedio(a, b, c) que reciba
tres números como parámetros y devuelva el promedio de ellos.
Solicitar los números al usuario y mostrar el resultado usando esta
función.
'''
def calcular_promedio(a, b, c):
    promedio = (a + b + c)/3
    print(f'El promedio de los numeros ingresado es : {promedio}')

numero_uno = validar_numero(input('Ingrese el primer valor: '))
numero_dos = validar_numero(input('Ingrese el segundo valor: '))
numero_tres = validar_numero(input('Ingrese el tercer valor: '))
calcular_promedio(numero_uno,numero_dos,numero_tres)