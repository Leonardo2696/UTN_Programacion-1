# ejercicio 12
'''
Pedir al usuario que ingrese 8 números enteros y almacenarlos en una lista.
● Mostrar la lista original.
● Mostrar la lista ordenada de menor a mayor.
● Mostrar la lista ordenada de mayor a menor.
● Investigar el uso de sorted() y del parámetro reverse.
'''
lista_numeros = []
for i in range(9):
    print('Ingrese un numero entero:')
    numero = input().strip()
    while not numero.isdigit():
        print('Error: tiene que ser un numero entero')
        numero = input().strip()
print(f'La lsita originar es: \n {lista_numeros}')
print()
lista_menor_mayor = sorted(lista_numeros)
print(f'La lsita ordenada de menor a mayor: \n {lista_menor_mayor}')
print()
lista_menor_mayor.reverse()
print(f'La lsita ordenada de mayor a menor: \n {lista_menor_mayor}')
