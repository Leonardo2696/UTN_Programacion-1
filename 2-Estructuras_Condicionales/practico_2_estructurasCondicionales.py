#1
edad = int(input("Ingrese su edad: "))

if edad >= 18:
    print("Es mayor de edad")

#2
nota = int(input("Ingrese su nota: "))
if nota >= 6:
    print ("Aprobado")
else:
    print("Desaprobado")

#3 
num = int(input("Ingrese un numero par: "))
if num % 2 == 0:
    print("Has ingresado un numero par")
else :
    print("Por favor, ingrese un numero par")

#4) 
edad = int(input("Ingrese su edad: "))
if edad < 12 :
    print("El usuario/a es un Niño/a")
elif edad >= 12 and edad < 18 :
    print("El usuario/a es Adolescente")
elif edad >= 18 and edad < 30:
    print ("El usuario/a es Adulto/a joven")
elif edad >= 30 :
    print ("El usuario/a es Adulto/a")

#5) 
userPass = input("Ingrese una contraseña con caracteres entre 8 y 14")
if len(userPass) >= 8 and len(userPass) <= 14:
    print("Ha ingresado una contraseña correcta")
else :
    print("Por favor, ingrese una contraseña de entre 8 y 14 caracteres")

#6
from statistics import mode,median,mean
import random 
numero_aleatorios = [random.randint(1,100)for i in range (50)]
print(numero_aleatorios)
print("la media aritmética es:")
print(mean(numero_aleatorios))
media = mean(numero_aleatorios)

print("la mediana mediana es:")
print(median(numero_aleatorios))
mediana = median(numero_aleatorios)

print("la moda única es:")
print(mode(numero_aleatorios))
moda = mode(numero_aleatorios)

if media > mediana and mediana > moda:
    print("es sesgo positivo")
elif media < mediana and mediana < moda:
    print("es sesgo negativo")
elif media == mediana and media == moda:
    print("sin sesgo")

#7)

frase = input("ingrese una frase: ")

if frase[-1] == "a" or frase[-1] == "e" or frase[-1] == "i" or  frase[-1] == "o" or frase[-1] == "u":
    print(frase + "!")
else :
    print(frase)

#8) 
nombre = input("ingrese su nombre: ")
print("elija un nunero dependiendo la acción que quiera realizar:")
print("#1. si quiere convertir el nombre a mayúsculas")
print("#2. si quiere convertir el nombre a minúsculas")
print("#3. si quiere solo la primera letra mayuscula")
num = int(input("Numero: "))
if num == 1 :
    print (nombre.upper())
elif num == 2 :
    print (nombre.lower())
elif num == 3 :
    print (nombre.title())

#9)

escala = float(input("Ingrese la magnitud del terremoto :"))

if escala < 3 :
    print ("Muy leve")
elif escala >= 3 and escala < 4:
    print ("Leve")
elif escala >= 4 and escala < 5:
    print ("Moderado")
elif escala >= 5 and escala < 6:
    print ("Fuerte")
elif escala >= 6 and escala < 7:
    print("Muy fuerte")
elif escala >= 7:
    print("Extremo")


#10)
print("Ingrese de que hemisferio es, Norte(N) o Sur(S)")
hemisferio = input("N/S: ")

print("Ingrese que mes se encuentra: ")
print(' "Enero" "Febrero" "Marzo" "Abril" "Mayo" "Junio" "Julio" "Agosto" "Septiembre" "Octubre" "Noviembre" "Diciembre"')
mes = input("Mes: ").title()

dia = int(input("Ingrese el dia: "))
if hemisferio.upper() == "N":
    match mes :
        case "Diciembre": 
            if dia > 20 and dia <= 31:
                print("Invierno")
            elif dia >= 1 and dia <= 20:
                print('Otoño')
        case "Enero":
            print("Invierno ")
        case "Febrero":
            print("Invierno")
        case "Marzo":
            if dia < 21:
                print("Invierno")
            elif dia >= 21 and dia <=31:
                print("Primavera")
        case "Abril":
            print("Primavera")
        case 'Mayo':
            print('Primavera')
        case 'Junio':
            if dia < 21:
                print ('Primavera')
            elif dia >= 21 and dia <= 31:
                print ('Verano')
        case 'Julio':
            print ('Verano')
        case 'Agosto':
            print('Verano')
        case 'Septiembre':
            if dia < 21:
                print ('Verano')
            elif dia >= 21 and dia <= 31:
                print ('Otoño')
        case 'Octubre':
            print ('Otoño')
        case 'Noviembre':
            print('Otoño')

if hemisferio.upper() == "S":
    match mes :
        case "Diciembre": 
            if dia > 20 and dia <= 31:
                print("Verano")
            elif dia >= 1 and dia <= 20:
                print('Primavera')
        case "Enero":
            print("Verano ")
        case "Febrero":
            print("Verano")
        case "Marzo":
            if dia < 21:
                print("Verano")
            elif dia >= 21 and dia <=31:
                print("Otoño")
        case "Abril":
            print ("Otoño")
        case 'Mayo':
            print("Otoño")
        case 'Junio':
            if dia < 21:
                print ("Otoño")
            elif dia >= 21 and dia <= 31:
                print ('Invierno')
        case 'Julio':
            print ('Invierno')
        case 'Agosto':
            print('Invierno')
        case 'Septiembre':
            if dia < 21:
                print ('Invierno')
            elif dia >= 21 and dia <= 31:
                print ('Primavera')
        case 'Octubre':
            print ('Primavera')
        case 'Noviembre':
            print('Primavera')