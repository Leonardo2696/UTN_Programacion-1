
## 1. Definí dos variables: `servidor_online <- TRUE` y `base_datos_ok <- FALSE`. [cite_start]Usá el operador `&` para verificar si el sistema está operativo[cite: 145].

# servidor_online <- TRUE
# base_datos_ok <- FALSE
# print(sistema_operativo <- servidor_online & base_datos_ok)

## 2. Creá un vector que represente los zócalos de memoria RAM de una notebook: `ram_slots <- c(TRUE, FALSE, TRUE, TRUE)`. [cite_start]Usá la función `any()` para comprobar si existe al menos un slot vacío (`FALSE`)[cite: 180].

# ram_slots <- c(TRUE,FALSE,TRUE,TRUE)
# slot_vacio <- !ram_slots
# print(any(slot_vacio))

## 3. Estás probando procesadores Ryzen. Tenés `temperaturas_ok <- c(TRUE, TRUE, TRUE, TRUE)`. [cite_start]Usá la función `all()` para verificar si todos pasaron la prueba[cite: 179].

# temperaturas_ok <- c(T,T,T,T)
# todo_ok <- all(temperaturas_ok)
# if(todo_ok){
#     print('Las temperaturas estas correctas')
# }else{
#     print('Algunos nucleos estas con temperaturas elevadas')
# }

## 4. Simulá una regla del ajedrez: `en_jaque <- TRUE` y `rey_movido <- FALSE`. [cite_start]Usá la disyunción (`|`) para determinar si el jugador debe moverse o bloquear el ataque[cite: 146].

# en_jaque <- TRUE
# rey_movido <- FALSE
# en_peligro <- en_jaque | rey_movido
# if (en_peligro){
#     bloquear_ataque <- TRUE
# }else{
#     bloquear_ataque <-FALSE
# }
# if(bloquear_ataque){
#     print('El ataque ha sido bloqueado')
# }

## 5. [cite_start]Traducí la equivalencia lógica del condicional (Si P entonces Q) a R usando `!p | q` con las variables `p <- TRUE` y `q <- FALSE`[cite: 148].

# p <- T
# q <- F
# condicional <- !p | q
# if(condicional){
#     print('El condicional es Verdadero')
# }else{
#     print('El condicional es Falso')
# }

## 6. [cite_start]Creá los vectores `p <- c(TRUE, TRUE, FALSE, FALSE)` y `q <- c(TRUE, FALSE, TRUE, FALSE)`[cite: 158, 164].

p <- c(T,T,F,F)
q <- c(T,F,T,F)

# # 7. [cite_start]Construí un `data.frame` llamado `tabla_verdad` uniendo los vectores `p` y `q` del ejercicio anterior[cite: 165].

#print('Aca se crea el data.frame')
tabla_verdad <- data.frame(p,q)


##8. [cite_start]Agregá una columna a `tabla_verdad` llamada `Conjunción` que calcule `p & q`[cite: 166].

# print('Aca se agrega Disyuncion(OR) a la tabla')
tabla_verdad$OR <- (p | q)
# print(tabla_verdad)

# print('Aca se agrega Conjuncion(AND)')
tabla_verdad$AND <- (p & q)
# # print(tabla_verdad)

#print('Aca se agrega Condicional(XOR)')
tabla_verdad$XOR <- (p != q)
# print(tabla_verdad)

##9. Milo quiere jugar a Roblox. La regla es: `tarea_lista <- FALSE`, `fin_de_semana <- TRUE`. Escribí la expresión lógica para saber si tiene permiso (`tarea_lista | fin_de_semana`).

# tarea_lista <- FALSE
# fin_de_semana <- TRUE
# if(tarea_lista | fin_de_semana){
#     tiene_permiso <- TRUE
# }else{
#     tiene_permiso <- FALSE
# }
# if(tiene_permiso){
#     print('Milo, puede jugar Roblox')
# }else{
#     print('Milo, no tiene permiso para jugar')
# }

## 10. Comprobá el estado de un componente en React: `is_loaded <- TRUE` y `has_error <- FALSE`. [cite_start]Validá que cargó y no tiene errores usando `&` y `!`[cite: 145, 147].

# is_loaded <- T
# has_error <- F

# if(is_loaded & !has_error){
#     print('El sistema cargó y no tiene errores')
# }else if(is_loaded & has_error){
#     print('El sistema cargó, pero tiene un error')
# }else if(!is_loaded){
#     print('El sistema no ha cargado')
# }

##11. Simulá una red Starlink: `conexion_activa <- c(rep(TRUE, 9), FALSE)`. [cite_start]Usá `any(!conexion_activa)` para detectar si algún nodo se cayó[cite: 180].

# conexion_activa <- c(rep(TRUE, 9), FALSE)
# if(any(!conexion_activa)){
#     print('Algun node se ha caido')
# }
# print(conexion_activa)

##12. Demostrá en un script si el resultado de evaluar `p | [cite_start]!p` en un vector de prueba devuelve siempre `TRUE` (Tautología)[cite: 186].

tabla_verdad$pnotp <- (p | !p)
# if(all(tabla_verdad$pnotp)){
#     print('Es una tautologia')
# }

##13. Evaluá una doble negación en R: definí `estado <- TRUE` e imprimí `!!estado` para ver si retorna el valor original.

# estado <- T
# print(!!estado)

##14. Un script de permisos de Firebase requiere: `usuario_logueado & (es_admin | dueño_documento)`. [cite_start]Asigná valores booleanos y evaluá la variable resultante[cite: 170, 173] 

# usuario_logueado <- T
# es_admin <- F
# dueño_documento <- T
# tiene_permisos <- usuario_logueado & (es_admin | dueño_documento)

# if(tiene_permisos){
#     print('Tiene persmisos')
# }else{
#     print('No tiene permisos')
# }

##15. [cite_start]Explicá en un comentario de tu script por qué `all(c(TRUE, TRUE, FALSE))` devuelve `FALSE`[cite: 181].
#all(c(TRUE, TRUE, FALSE)) # Este script da falso porque al usar la funcion all() con los datos que se le ingresen compara que todos sean TRUE, y asi devuelva TRUE, caso contrario si hay al menos 1 dato que sea FALSE, devuelve FALSE