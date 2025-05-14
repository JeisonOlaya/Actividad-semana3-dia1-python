def es_palindromo(texto):
    """Determina si un texto es palíndromo"""
    texto = texto.lower().replace(" ", "").replace("á", "a").replace("é", "e").replace("í", "i").replace("ó", "o").replace("ú", "u")
    return texto == texto[::-1]

# Entrada de usuario
texto = input("Ingresa una palabra o frase: ")

# Procesamiento y salida
if es_palindromo(texto):
    print("¡Es un palíndromo!")
else:
    print("No es un palíndromo.")