
# 1 Creación de Tuplas: Crea una tupla llamada punto que represente una coordenada en un plano con los valores 10 y 20.
punto = (10,20)
print(punto)

#2 Acceso por Índice: Dada la tupla frutas = ("manzana", "banana", "cereza"), imprime únicamente el segundo elemento ("banana") usando su índice.
frutas = ('manzana','banana','cereza')
print(frutas[1])

#3 Inmutabilidad: Intenta cambiar el primer elemento de la tupla coordenada = (10, 20) a 15. ¿Qué sucede y por qué?.
# # Las tuplas son inmutables, no se pueden modificar y devolveria un error intetar hacerlo

#4 Eliminar Duplicados: Tienes la lista numeros = [1, 2, 2, 3, 4, 4, 5]. Utiliza una estructura de Python para obtener una colección que contenga solo valores únicos.
numero = [1,2,2,3,4,4,5]
print(f'Lista; {numero}')
n_sin_repetir = set(numero)
print(f'Nueva lista: {n_sin_repetir}')


#5 Verificación de Pertenencia: Crea un set con los colores "rojo", "verde" y "azul". Verifica si el color "amarillo" está dentro del set e imprime el resultado booleano.

colores = {'rojo','verde','azul'}
if 'amarillo' in colores:
    print(f'El color "amarillo" SI esta en el set')
else:
    print(f'El color "amarillo" NO esta en el set')

#6 Desempaquetado: Tienes la tupla auto = ("Peugeot", "208", 2024). Asigna sus valores a tres variables llamadas marca, modelo y anio en una sola línea.
auto = ('Peugeot', '208', 2024)
marca, modelo, anio = auto
print(f'El auto {marca}, modelo {modelo}, salio el {anio}')

#7 Contar y Localizar: Dada la tupla valores = (10, 5, 10, 3, 10, 8), usa los métodos de tuplas para:
#   .Contar cuántas veces aparece el número 10.
#   .Encontrar la posición (índice) de la primera aparición del número 3.
valores = (10, 5, 10, 3, 10, 8)
print(f'El numero "10" aparece un total de {valores.count(10)} veces')
print(f'La primera aparicion del numero "3" es en el indice {valores.index(3)}')

#8 Unión de Conjuntos: Tienes dos conjuntos: estudiantes_python = {"Ana", "Luis", "Pedro"} y estudiantes_java = {"Luis", "Marta", "Hugo"}. Crea un nuevo conjunto que contenga a todos los estudiantes de ambos lenguajes sin repeticiones.
estudiantes_python = {"Ana", "Luis", "Pedro"}
estudiantes_java = {"Luis", "Marta", "Hugo"}
todos_los_estudiantes = (estudiantes_java | estudiantes_python)
print(todos_los_estudiantes)

#9  Intersección: Usando los conjuntos del ejercicio anterior, encuentra únicamente a los estudiantes que están cursando ambos lenguajes al mismo tiempo.
estudiantes_en_dos_cursos = (estudiantes_python & estudiantes_java)
print(estudiantes_en_dos_cursos)
# 10 Conversión: Crea una lista de tus 3 películas favoritas. Conviértela a una tupla para "proteger" los datos y luego verifica su tipo con la función type().
pelis = ['Matrix', 'Halo', 'Blade']
pelis = tuple(pelis)
print(type(pelis))

#11 Diferencia de Conjuntos: Tienes un set con todos los alumnos_inscriptos y otro con los alumnos_que_asistieron. Obtén un set de los alumnos que faltaron a clase utilizando la operación de diferencia.\
alumnos_inscriptos = {'Leo','Juan','Javi','Yami','Angel','Eli'}
alumnos_que_asistieron = {'Leo','Yami','Angel'}
alumnos_que_faltaron = (alumnos_inscriptos ^ alumnos_que_asistieron)
print(alumnos_que_faltaron)

#12 Tuplas Anidadas: Crea una tupla llamada biblioteca que contenga dos tuplas internas. Cada tupla interna debe tener el (nombre_del_libro, autor). Accede e imprime el nombre del autor del segundo libro.
biblioteca = (('Metro','Dmitry'),('El señor del anillo','J.R.R Tolkien'),('La llamada de Cthulu','H.P. Lovecraft'))
print(biblioteca[1][1])

#13 Gestión Dinámica de Sets: Crea un set vacío llamado invitados. Agrega a "Juan", "Maria" y "Pedro" usando un solo método. Luego, elimina a "Juan" de forma segura (que no de error si ya no está).
invitados = set()
invitados.update(["Juan", "Maria", "Pedro"])
invitados.discard("Juan")

#14 Diferencia Simétrica: Tienes dos grupos de trabajo. El Grupo A = {1, 2, 3, 4} y el Grupo B = {3, 4, 5, 6}. Encuentra los elementos que están en un grupo o en el otro, pero no en ambos.
grupo_a ={1, 2, 3, 4}
grupo_b = {3, 4, 5, 6}
print(grupo_a ^ grupo_b)

#15 Análisis de Datos: Tienes una tupla de registros: datos = (("ID1", 25), ("ID2", 30), ("ID3", 25)). Convierte esta estructura en una lista para poder agregar un nuevo registro ("ID4", 40) y luego vuelve a convertirla en tupla.
datos = (("ID1", 25), ("ID2", 30), ("ID3", 25))
lista_datos = list(datos)
lista_datos.append(('ID4', 40))
datos = tuple(lista_datos)
print(datos)