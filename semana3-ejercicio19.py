import random
import string

def generar_contraseña(longitud=12):
    """Genera una contraseña aleatoria segura"""
    if longitud < 8:
        return "La contraseña debe tener al menos 8 caracteres"
    
    # Definir los conjuntos de caracteres
    mayusculas = string.ascii_uppercase
    minusculas = string.ascii_lowercase
    numeros = string.digits
    simbolos = "!@#$%^&*()_+-=[]{}|;:,.<>?"
    
    # Asegurar al menos un carácter de cada tipo
    contraseña = [
        random.choice(mayusculas),
        random.choice(minusculas),
        random.choice(numeros),
        random.choice(simbolos)
    ]
    
    # Completar el resto de la contraseña
    todos_caracteres = mayusculas + minusculas + numeros + simbolos
    contraseña.extend(random.choice(todos_caracteres) for _ in range(longitud - 4))
    
    # Mezclar los caracteres
    random.shuffle(contraseña)
    
    return ''.join(contraseña)

# Entrada de usuario
try:
    longitud = int(input("Longitud de la contraseña (mínimo 8): "))
    if longitud < 8:
        print("La longitud mínima es 8")
    else:
        # Generación y resultado
        nueva_contraseña = generar_contraseña(longitud)
        print(f"Tu nueva contraseña es: {nueva_contraseña}")
except ValueError:
    print("Por favor ingresa un número válido")