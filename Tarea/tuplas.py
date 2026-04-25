# creacion de la tupla
t = (1,2,3)
print(t) # (1,2,3)

# empaquetar crea una tupla

t = 1,2,3
print(t) # print(1,2,3)

# convertir una lista a tupla
l = [2,3,4]
t = tuple(l)
print(t) # (2,3,4)

# acceder a elementos
t = (1,2,3,4)
print(t[2]) # 3
print(t[:2]) # (1,2)

# recorrer una tupla
t = (1,2,3,4)

for e in t:
    print(e)
    # 1
    # 2 
    # 3
    # 4

# verifivar si un elemento esta en la tupla
t = (1,2,3,4)

if 2 in t:
    print('Esta en la tupla') # Si "2" esta en "t" = TRUE
else:
    print('No esta en la tupla') 

# dedempaquetar una tupla
t = (1,2,3)
a, b, c = t
print(f'el valor de a: {a}, b: {b} y c : {c}') # el valor de a: 1, b: 2 y c: 3

# usando el comodin
t = (1,2,3,4)
a, *t2 = t

print(f'el valor de a: {a}, t2: {t2}') # el valor de a: 1, t2: [2,3,4]

# operadores basicos
t = (1,2,2,3,3,4,2,2)
print(t)
print(f'cantidad de elementos : {len(t)}') # cantidad de elementos : 8
print(f'cantidad de veces que aparece 2: {t.count(2)}') # cantidad de veces que aparece 2: 4
print(f'el indice del elemento 3: {t.index(3)}') # el indice del elemto 3: 3

# concatenamos tuplas
t = (1,2,3) + (4,5,6)
print(t) # (1,2,3,4,5,6)

# repetir tupla
t = (1,2)*4
print(t) # (1,2,1,2,1,2,1,2)

# tupla de un solo elemento
t = (1,) #// t = (1)----- devuelve solo 1
print(t) # (1,)

# devolver varios elementos
def func():
    return 1,2,3

a,b,c = func()

print(f'a: {a}, b: {b}, c:{c}') # a:1,b:2,c:3