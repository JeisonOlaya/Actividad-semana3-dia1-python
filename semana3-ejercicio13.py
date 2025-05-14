def fizzbuzz(n):
    """Implementa las reglas del juego FizzBuzz"""
    if n % 15 == 0:
        return "FizzBuzz"
    elif n % 3 == 0:
        return "Fizz"
    elif n % 5 == 0:
        return "Buzz"
    return str(n)

# Entrada de usuario
try:
    num = int(input("Ingresa un número: "))
    # Procesamiento y salida
    print(fizzbuzz(num))
except ValueError:
    print("Por favor ingresa un número válido.")