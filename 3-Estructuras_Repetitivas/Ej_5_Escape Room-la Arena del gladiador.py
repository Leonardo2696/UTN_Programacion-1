vida_gladiador = 100
vida_enemigo = 100
pocion_vida = 3
daño_ataque_pesado = 15
daño_ataque_enemigo = 12
turno_gladiador = True

print('Ingrese su nombre: ')
gladiador = input()
print('')
while not gladiador.isalpha():
    print('Error: Solo se permiten letras')
    print('Ingrese su nombre: ')
    gladiador = input()
    print('')

while True:
    print(f'Vida de {gladiador}: {vida_gladiador}')
    print(f'Vida de enemigo: {vida_enemigo}')
    print(f'Pociones restantes: {pocion_vida}')
    print('')
    print('MENU')
    print('1. Ataque Pesado')
    print('2. Rafaga Veloz')
    print('3. Curar')
    op_menu = input()
    print('')
    while not op_menu.isdigit() or int(op_menu) == 0 or int(op_menu) > 3:
        print('Error: tiene que ser una opcion del menu')
        print(f'Vida de {gladiador}: {vida_gladiador}')
        print(f'Vida de enemigo: {vida_enemigo}')
        print(f'Pociones restantes: {pocion_vida}')
        print('')
        print('MENU')
        print('1. Ataque Pesado')
        print('2. Rafaga Veloz')
        print('3. Curar')
        op_menu = input()
        print('')
    match int(op_menu):
        case 1:
            if vida_enemigo < 20:
                print('Golpe critico')
                daño_total = float(daño_ataque_pesado * 1.5)
                vida_enemigo -= daño_total
                print(f'¡Atacaste al enemigo por {daño_total} puntos de daño!')
                print('')
            else:
                vida_enemigo -= daño_ataque_pesado
                print(f'¡Atacaste al enemigo por {daño_ataque_pesado} puntos de daño!')
                print('')
                print('Turno del enemigo')
                print('¡El enemigo te ataco por 12 puntos de daño!')
                vida_gladiador -= daño_ataque_enemigo
                print('')
        case 2:
            for i in range (3):
                vida_enemigo -= 5
                print(f'Golpe conectado, daño =',5 * (i+1) )
            print('')
            print('Turno del enemigo')
            print('¡El enemigo te ataco por 12 puntos de daño!')
            vida_gladiador -= daño_ataque_enemigo
            print('')
        case 3:
            if pocion_vida > 0:
                vida_gladiador += 30
                pocion_vida -= 1
            elif pocion_vida == 0:
                print('¡No quedan mas pociones!')
                print('Turno del enemigo')
                print('¡El enemigo te ataco por 12 puntos de daño!')
                vida_gladiador -= daño_ataque_enemigo
                print('')
    if vida_gladiador <= 0 or vida_enemigo <= 0:
        if vida_gladiador > 0:
            print(f'¡VICTORIA! {gladiador} ha ganado la batalla')
            print('')
            break
        elif vida_gladiador <= 0:
            print('DERROTA. Has caido en combate')
            print('')
            break