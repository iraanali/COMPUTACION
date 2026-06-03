texto = "Python es Genial"
texto.upper()  # "PYTHON ES GENIAL"
texto.lower()  # "python es genial"
texto.capitalize()  # "Python es genial"
texto.title()  # "Python Es Genial"

texto = "   Hola   "
texto.strip()   # "Hola"
texto.lstrip()  # "Hola   "
texto.rstrip()  # "   Hola"

# Eliminar caracteres específicos
"...Python...".strip(".")  # "Python"

frase = "Me gusta programar en Java"
nueva_frase = frase.replace("Java", "Python")  # "Me gusta programar en Python"

# Reemplazar múltiples valores
frase = "1, 2, 3, 4"
frase.replace(",", ";").replace(" ", "")  # "1;2;3;4"

# Contar ocurrencias
"banana".count("a")  # 3

# Verificar inicio/fin
"Hola mundo".startswith("Hola")  # True
"Hola mundo".endswith("mundo")    # True

# Dividir y unir cadenas
"uno,dos,tres".split(",")  # ['uno', 'dos', 'tres']
" ".join(["Hola", "mundo", "!"])  # "Hola mundo !"

# Verificar si es numérico o alfabético
"123".isdigit()  # True
"abc".isalpha()  # True
"abc123".isalnum()  # True