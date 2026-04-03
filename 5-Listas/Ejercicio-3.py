# ejercicio 3
'''
Generar una lista con 15 números enteros al azar entre 1 y 100.
● Crear una lista con los pares y otra con los impares.
● Mostrar cuántos números tiene cada lista.
'''
import random
lista_de_numeros = []
lista_de_pares = []
lista_de_impares = []
for num in range(15):
    lista_de_numeros.append(random.randint(1,100))
    if lista_de_numeros[num] % 2 == 0:
        lista_de_pares.append(lista_de_numeros[num])
    else:
        lista_de_impares.append(lista_de_numeros[num])
print(f'Total de numeros: {len(lista_de_numeros)}')
print(f'Lista de numeros: {lista_de_numeros}')
print()
print(f'Lista de pares: {lista_de_pares}')
print(f'Total de numeros pares: {len(lista_de_pares)}')
print()
print(f'Lista de impares: {lista_de_impares}')
print(f'Total de numeros impares: {len(lista_de_impares)}')
