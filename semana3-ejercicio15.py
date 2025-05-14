def invertir_texto(texto):
    """Invierte un texto"""
    return texto[::-1]

# Entrada de usuario
texto = input("Ingresa un texto: ")

# Procesamiento y salida
print("Texto invertido:", invertir_texto(texto))