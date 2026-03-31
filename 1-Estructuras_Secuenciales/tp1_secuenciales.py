# ejercicio 1
print('Hola Mundo!')

# ejercicio 2
nombre = input('Ingrese su nombre: ')
print(f'Hola {nombre}!')

# ejercicio 3
nombre = input('Ingrese su nombre: ')
apellido = input('Ingrese su apellido: ')
residencia = input('Ingrese pais donde vive: ')
edad = int(input('Ingrese su edad: '))
print(f'Soy {nombre} {apellido}, tengo {edad} años y vivo en {residencia}')

# ejercicio 4
radio = int(input('Ingrese el radio del circulo'))
pi = 3.14
perimetro = (2*pi)*radio
area = pi * (radio * radio)
print(f'El area del circulo es: {area}')
print(f'El perimetro de un circulo es: {perimetro}')

# ejercicio 5
segundos = int(input('Ingrese una cantidad de segundos: '))
horas = float(segundos / 3600)
print(f'En {segundos} seg. hay un total de {horas} hr.')

# ejercicio 6
numero = int(input('Ingrese un numero para hacer la tabla: '))
for i in range (1,11):
    print(f'{numero} x {i} = {numero * i}')

# ejercicio 7
numero_1 = int(input('Ingrese un numero mayor a 0: '))
numero_2 = int(input('Ingrese otro numero mayor a 0: '))
print(f'La suma de ambos numero es {numero_1 + numero_2}')
print(f'La resta de ambos numero es {numero_1 - numero_2}')
print(f'La multiplicacion de ambos numero es {numero_1 * numero_2}')
print(f'La division de ambos numero es {numero_1 / numero_2}')

# ejercicio 8
altura = float(input('Altura en m: '))
peso = float(input('Peso en kg: '))
imc = peso / (altura ** 2)
print(f'IMC: {imc}')

# ejercicio 9
grados_celcius = int(input('Ingrese los grados celcius a convertir: '))
temp_fahrenheit = 9/5 * grados_celcius + 32
print(f'Hay {temp_fahrenheit}')

# ejercicio 10
num_1 = int(input('Ingrese un numero: '))
num_2 = int(input('Ingrese otro numero: '))
num_3 = int(input('Ingrese otro numero: '))
promedio = float((num_1 + num_2 + num_3) / 3)
print(f'El promedio total es de : {promedio}')