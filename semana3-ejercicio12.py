
def eliminar_duplicados(lista):
    """Elimina elementos duplicados manteniendo el orden"""
    return list(dict.fromkeys(lista))

# Entrada de usuario
entrada = input("Ingresa elementos separados por espacios: ")
elementos = entrada.split()

# Procesamiento y salida
sin_duplicados = eliminar_duplicados(elementos)
print("Lista sin duplicados:", " ".join(sin_duplicados))