def contar_vocales(texto):
    """Cuenta las vocales en un texto"""
    vocales = "aeiouáéíóúAEIOUÁÉÍÓÚ"
    return sum(1 for letra in texto if letra in vocales)

# Entrada de usuario
texto = input("Ingresa un texto: ")

# Procesamiento y salida
print(f"El texto contiene {contar_vocales(texto)} vocales")