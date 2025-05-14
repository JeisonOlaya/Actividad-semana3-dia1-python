def suma_elementos_unicos(numeros):
    """Suma los elementos únicos de una lista"""
    return sum(set(numeros))

# Entrada de usuario
entrada = input("Ingresa números separados por espacios: ")
numeros = [int(num) for num in entrada.split()]

# Cálculo y resultado
suma = suma_elementos_unicos(numeros)
print(f"La suma de los elementos únicos es: {suma}")