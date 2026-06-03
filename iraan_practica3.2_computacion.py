# Variables para los ejemplos
nombre = "Ana"
edad = 25

# Formateo básico
saludo = f"Hola, me llamo {nombre} y tengo {edad} años"

# Expresiones dentro de f-strings
precio = 19.99
cantidad = 3
total = f"Total: {precio * cantidad:.2f}€"  # Formato de 2 decimales

# Llamadas a funciones
f"En mayúsculas: {nombre.upper()}"  # Resultado: "En mayúsculas: ANA"

# Alineación de texto
f"{nombre:>10}"  # Alineado a la derecha en 10 caracteres
f"{nombre:^10}"  # Centrado en 10 caracteres
f"{nombre:<10}"  # Alineado a la izquierda en 10 caracteres