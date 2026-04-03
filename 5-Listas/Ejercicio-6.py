# ejercicio 6
'''
Dada una lista con 7 números, rotar todos los elementos una posición hacia la derecha
(el último pasa a ser el primero).

'''
lista = [1,2,3,4,5,6,7]
lista.insert(0, lista.pop())
print(lista)

