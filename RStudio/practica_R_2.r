# #16. [cite_start]Evaluá el operador XOR (`xor()`) simulando dos jugadores que deben elegir caminos distintos en un juego[cite: 23, 26]
# jugador_1 <- T
# jugador_2 <- F
# caminos_distinto <- xor(jugador_1,jugador_2)
# if(caminos_distinto){
#     print('Cada uno elijio un camino distinto')
# }else{
#     print('Ambos se fueron por el mismo camino')
# }

# #17. [cite_start]Escribí una función propia en R llamada `nor_gate <- function(a, b)` que devuelva la lógica de una compuerta NOR universal[cite: 24, 26].
# # Definimos la función NOR (Not OR)
nor_gate <- function(a, b) {
    resultado <- !(a | b)
    return(resultado)
} 
# # Probamos la función
# a <- FALSE
# b <- FALSE
# print(paste("Resultado de la compuerta NOR:", nor_gate(a, b)))

#18. Probá tu `nor_gate` pasándole como argumentos `a = TRUE` y `b = FALSE`.

# a <- T
# b <- F
# print(paste('Se cambiaron los valores, (a<-T) y (b<-F)',nor_gate(a,b)))

#19. En un juego de minería, podés picar un mineral si: `pico_nivel_5 & capa_obsidiana`. Escribí esto como una expresión booleana simple.
# pico_nivel_5 <- T
# capa_obsidiana <- F
# se_puede_picar <- pico_nivel_5 & capa_obsidiana
# if(se_puede_picar){
#     print('Se puede picar este bloque')
# }else{
#     print('No se puede picar obsidiana sin pico nivel 5')
# }

#20. [cite_start]Creá un `data.frame` con 8 filas para las combinaciones de 3 variables lógicas: `A`, `B` y `C`[cite: 36].
A <- rep(c(0,1),each = 4)
B <- rep(c(0,1),each = 2 ,times = 2)
C <- rep(c(0,1),times = 4)
nueva_tabla <- data.frame(A,B,C)
#print(nueva_tabla)

#21. [cite_start]Agregá una columna `Salida` a ese dataframe definida por la regla `(A | B) & !C`[cite: 37].

nueva_tabla$Salida <- as.numeric((A|B)&!C)
# print(nueva_tabla)

#22. [cite_start]Usá funciones de R para filtrar y mostrar únicamente las filas del dataframe donde `Salida == TRUE`[cite: 38].

solo_true <- subset(nueva_tabla, Salida == 1)
indice <- which(nueva_tabla$Salida == 1)
# print('Las filas que niene solo 1 son: ')
# print(solo_true)
# print(indice)

#23. [cite_start]Observando las filas filtradas en el ejercicio 22, escribí en un comentario la expresión SOP (Suma de Productos) canónica (Ej. $m_2 + m_4$)[cite: 39].

# La exprecion SOP (Suma de Productos) canonica es: 
# F = m_2 + m_4 + m_6

#Por que?
#Fila 3 = A'BC' ----> m_2
#Fila 5 = AB'C' ----> m_4
#Fila 7 = ABC' -----> m_6

# print('La expresión canónica correcta es F = m_2 + m_4 + m_6')

#24. Vas a crear un sistema de disparo en un FPS. Las reglas son: `(gatillo & municion) & !seguro`. Definí las variables y probá la salida.

FPS <- data.frame(
    gatillo = c(T,T,T,T,F,F,F,F),
    municion = c (T,T,F,F,T,T,F,F),
    seguro = c(T,F,T,F,T,F,T,F)
)
FPS$accion <- ifelse((FPS$gatillo & FPS$municion) & !FPS$seguro,'!PUUUM',ifelse(FPS$gatillo & (!FPS$municion & !FPS$seguro), 'Sin municion, hay que recargar','No se uso el arma'))

print(FPS)