def factorial(n):
    """Calcula el factorial de un número"""
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)

# Entrada de usuario
try:
    num = int(input("Ingresa un número entero positivo: "))
    if num < 0:
        print("Por favor ingresa un número positivo.")
    else:
        # Procesamiento y salida
        print(f"El factorial de {num} es {factorial(num)}")
except ValueError:
    print("Por favor ingresa un número válido.")