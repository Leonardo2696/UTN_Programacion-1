diccionario = {} # Es typo diccionario

diccionario = dict() # Lo convierte a diccionario

agenda = {
    'Jose':'34652',
    'Maria':'563245'
}
print(agenda['Jose']) # 34652

# Forma de agreagar datos al diccionario
agenda.update({'Rita':'1235412','Pedro':'09535'})
print(agenda) # {'Jose': '34652', 'Maria': '563245', 'Rita': '1235412', 'Pedro': '09535'}

agenda['Florencia'] = '894034'
print(agenda) # {'Jose': '34652', 'Maria': '563245', 'Rita': '1235412', 'Pedro': '09535', 'Florencia': '894034'}

# for i in range(2):
#     nombre = input('Ingrese un nombre')
#     telefono = input('Ingrese su numero')
#     agenda[nombre] = telefono
# print(agenda)

# Forma de ingresar a los valores (keys, valores)
claves = agenda.keys()
lista_claves = list(claves)
for claves in lista_claves:
    print(claves)
    # Jose
    # Maria
    # Rita
    # Pedro
    # Florencia

valores = agenda.values()
lista_valores = list(valores)
for valores in lista_valores:
    print(valores)
    # 34652
    # 563245
    # 1235412
    # 09535
    # 894034

# metodo items, podemos obtener la clave y el valor
pares = agenda.items()
lista_pares = list(pares)
for pares in lista_pares:
    print(pares)
    # ('Jose', '34652')
    # ('Maria', '563245')
    # ('Rita', '1235412')
    # ('Pedro', '09535')
    # ('Florencia', '894034')