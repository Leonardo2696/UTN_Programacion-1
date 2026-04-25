def verificar_str(texto):
    text = texto
    while not text.isalpha():
        print('El texto no valido')
        text = input('Ingrese el nombre ').strip().capitalize()
    return text

def verificar_int(numero):
    num_int = numero
    while not num_int.isdigit():
        print('No es un numero valido')
        num_int = input('Ingrese un numero: ')
    return int(num_int)

def dato_en_list(dato,dicc,mensaje):
    while dato in dicc:
        if type(dato) == str:
            print('Error. El dato ingresado ya existe: ')
            dato = verificar_str(input(mensaje).capitalize().strip())
            print()
        elif type(dato) == int:
            print('Error. El dato ingresado ya existe: ')
            dato = validar_N(input(mensaje).capitalize().strip())
            print()
    return dato