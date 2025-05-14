import random

def lanzar_dado():
    """Simula el lanzamiento de un dado de 6 caras"""
    return random.randint(1, 6)

# Entrada de usuario
input("Presiona Enter para lanzar el dado...")

# Lanzamiento y resultado
resultado = lanzar_dado()
print(f"El dado cayó en: {resultado}")