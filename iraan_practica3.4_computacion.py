[2:49 p.m., 2/6/2026] Daisy: texto = "Python"

# Índices (comienzan en 0)
primer_caracter = texto[0]    # 'P'
segundo_caracter = texto[1]   # 'y'
ultimo_caracter = texto[-1]   # 'n' (negativos cuentan desde el final)

# Slicing (rebanadas)
# sintaxis: [inicio:fin:paso]
primeras_tres = texto[0:3]    # 'Pyt' (índice 3 no incluido)
ultimos_tres = texto[-3:]     # 'hon'  (desde el -3 hasta el final)
cada_segundo = texto[::2]     # 'Pto'  (cada segundo carácter)
reverso = texto[::-1]         # 'nohtyP' (invierte la cadena)

# Longitud de la cadena
longitud = len(texto)         # 6

texto = "Python"
texto[:3]  # 'Pyt' (igual que texto[0:3])
texto[3:]  # 'hon' (igual que texto[3:6])

def nombre_de_la_funcion(parametro1, parametro2):
    """
    Documentación de la función (opcional pero recomendado)
    Explica qué hace la función y qué parámetros espera
    """
    # Cuerpo de la función
    resultado = parametro1 + parametro2
    return resultado  # Opcional: devuelve un valor

def saludar(nombre):
    """
    Muestra un saludo personalizado
    
    Args:
        nombre (str): El nombre de la persona a saludar
        
    Returns:
        str: Un mensaje de saludo
    """
    mensaje = f"¡Hola, {nombre}! Bienvenido al curso de Python."
    return mensaje

# Llamando a la función
print(saludar("Ana"))  # Muestra: ¡Hola, Ana! Bienvenido al curso de Python.
[2:49 p.m., 2/6/2026] Daisy: print("¡Hola, Mundo!")
nombre= input("¿Cual es tu nombre?")
print(f"¡Bienvenido/a al curso de Python, {nombre}!")