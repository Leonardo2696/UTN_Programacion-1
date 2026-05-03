# 1) Dado el siguiente código, hacer una lista con los distintos errores que contiene y detallar qué
# tipo de error es cada uno.
errores = ['TypeError','ZeroDivisionError','IndexError']

# 2) Utilizando el código del ejercicio 1, arreglar los errores para que la ejecución del programa
# sea correcta sin necesidad de usar excepciones
a = 10
b = input("Introduce un número: ")
#------ Se agrega un bucle y una condicion para que siempre sea un numero entero mayor a 0-----
while not b.isdigit() or int(b) == 0:
    print('El numero ingresado no es valido')
    b = input("Introduce un número: ")
result = a / int(b)
print(f"Resultado: {result}")
numbers = [1, 2, 3]
# print(numbers[5]) ---- Codigo original
print(numbers[2]) # --- pongo un numero que si esta donde del rango del indice
