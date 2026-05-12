def mostrar_menu():
    print('''
================ MENU =====================
1. Agregar libro 
2. Mostrar libros 
3. Buscar libro 
4. Modificar libro 
5. Eliminar libro 
6. Estadísticas 
7. Guardar archivo 
8. Cargar archivo 
9. Salir''')
    
class ErrorNoEstring(Exception):
    pass
def no_es_string(dato):
    dato_str = str(dato).strip()
    if not dato_str:
        raise ErrorNoEstring("El campo no puede estar vacío")