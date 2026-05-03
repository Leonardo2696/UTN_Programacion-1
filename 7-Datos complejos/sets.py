#crear conjunto
c = {1,2,3}
print(c) # {1,2,3}
'''============='''
c = {1,2,3,1,2,3}
print(c) #{1,2,3}
'''============='''
c = set() 
print(c) #set()
'''============='''
#convertimos una lista
l = [1,2,3,4,4,1]
c = set(l)
print(c) # {1,2,3,4}
#operaciones
c = set()

c.add('Pedro')
c.add('Juan')
c.add('Roberto')
c.add('Pedro')
print(c) #{'Roberto','Juan','Pedro'}
'''============='''
#eliminamos un elemento del conjunto
c.discard('Pedro') # remove
print(c) #{'Juan','Roberto'}
print(f'La cantidad de elemtnos son {len(c)}') # La cantidad son 2
'''============='''
#borramos todos los elementos del conjunto
c.clear()
print(c) # set()
'''============='''
#recorrer el conjunto
frutas = {'manzana','banana','pera','banana'}
for f in frutas:
    print(f)
    #pera
    #manzana
    #banana
'''============='''
#verifica si un elemento existe en el conjunto
frutas = {'manzana','banana','pera','banana'}

if 'mazana' in frutas:
    print('existe el elemento en el confunto') # si 'manzana', lo imprime
else:
    print('no existe ele elmento en el conjunto') # si no esta en fruta, imprime esto
'''============='''
# operacion de conjunto
a = {1,2,3,4}
b = {3,4,5,6}

print(a | b) # union // {1, 2, 3, 4, 5, 6}
print(a & b) # interseccion  // {3, 4}
print(a - b) # diferencia // {1, 2}
print(a ^ b) # difetencia simetrica // {1, 2, 5, 6}

# '''============='''

# subconjunto y superconjuunto 
a = {1,2,3}
b = {1,2,3,4}

print(a.issubset(b)) # True
print(b.issuperset(a)) # True