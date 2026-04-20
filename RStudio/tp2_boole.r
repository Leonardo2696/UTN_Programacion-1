# 1. Generar sistemáticamente todas las combinaciones (2^4 = 16)
tabla <- expand.grid(D = 0:1, C = 0:1, B = 0:1, A = 0:1)
tabla <- tabla[, c("A", "B", "C", "D")]

# 2. Definir la función lógica F basada en las variables
# Ejemplo: F = (A AND B) OR (NOT C AND D)
# En R, los operadores lógicos son: & (AND), | (OR), ! (NOT)
tabla$F <- as.integer((tabla$A & tabla$B) | (!tabla$C & tabla$D))

# 3. Filtrar los Mintérminos (donde F es 1)
minterm_df <- tabla[tabla$F == 1, ]

# 4. Procesamiento de texto vectorizado
# Transformamos los 0s y 1s en su representación SOP
A_txt <- ifelse(minterm_df$A == 1, "A", "A'")
B_txt <- ifelse(minterm_df$B == 1, "B", "B'")
C_txt <- ifelse(minterm_df$C == 1, "C", "C'")
D_txt <- ifelse(minterm_df$D == 1, "D", "D'")

# 5. Construcción de la cadena final
terminos <- paste0("(", A_txt, B_txt, C_txt, D_txt, ")")
sop_final <- paste(terminos, collapse = " + ")

# --- Salida de resultados ---
print("Tabla de Verdad Completa:")
print(tabla)

cat("\nExpresión Canónica SOP para la función definida:\n")
cat("F =", sop_final, "\n")